#!/usr/bin/env python3
"""
MisakaNet Feedback Reporter (节点侧)
=====================================
收集近期 skill 使用记录，通过 GitHub Issues 上报到 Hub。

运行方式:
  1. 手动: python3 scripts/feedback_report.py
  2. Cron: */5 * * * * cd /path/to/MisakaNet && python3 scripts/feedback_report.py

依赖: curl + GitHub token（从 ~/.git-credentials 读取）
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = "Ikalus1988/MisakaNet"
NODE_ID = "hermes_wsl"
GIT_CREDS_PATH = os.path.expanduser("~/.git-credentials")


def _get_token():
    """从 git credentials 提取 GitHub token"""
    try:
        creds = open(GIT_CREDS_PATH).read().strip()
        # format: https://user:token@github.com
        token = creds.split("://")[1].split("@")[0].split(":")[1]
        return token
    except Exception as e:
        print(f"[error] 无法读取 token ({GIT_CREDS_PATH}): {e}", file=sys.stderr)
        return None


def create_feedback_issue(skill_name, result, scenario, tags=None, related_skills=None, session_ref=None):
    """上报一条 skill 使用反馈 (创建 GitHub Issue)"""

    token = _get_token()
    if not token:
        return None

    result_icon = {"success": "✓", "partial": "⚠", "failure": "✗"}
    title = f"feedback: {skill_name} {result_icon.get(result, '?')}"

    extra = {}
    if tags:
        extra["tags"] = tags
    if related_skills:
        extra["related_skills"] = related_skills
    if session_ref:
        extra["session_ref"] = session_ref

    body = json.dumps({
        "node_id": NODE_ID,
        "skill": skill_name,
        "result": result,
        "scenario": scenario,
        "extra": extra,
    }, ensure_ascii=False)

    labels = [
        "feedback",
        "unprocessed",
        f"node:{NODE_ID}",
        f"skill:{skill_name}",
    ]

    payload = json.dumps({
        "title": title,
        "body": body,
        "labels": labels,
    })

    print(f"[上报] {skill_name} → {result}")
    print(f"  scenario: {scenario[:80]}...")

    proc = subprocess.run(
        ["curl", "-s", "-X", "POST",
         f"https://api.github.com/repos/{REPO}/issues",
         "-H", f"Authorization: Bearer {token}",
         "-H", "Accept: application/vnd.github.v3+json",
         "-H", "User-Agent: MisakaNet-Node",
         "-d", payload],
        capture_output=True, text=True, timeout=20,
    )

    resp = json.loads(proc.stdout) if proc.stdout else {}

    if "number" in resp:
        url = resp["html_url"]
        print(f"  ✅ Issue #{resp['number']}: {url}")
        _write_local_cache(skill_name, result, scenario, extra, url)
        return url
    else:
        msg = resp.get("message", proc.stdout[:200])
        print(f"  ❌ {msg}", file=sys.stderr)
        return None


def _write_local_cache(skill_name, result, scenario, extra, issue_url):
    """写入本地 .feedback/ 目录作为备份"""
    script_dir = Path(__file__).parent
    feedback_dir = script_dir / ".." / ".feedback" / NODE_ID
    feedback_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    path = feedback_dir / f"{ts}_{skill_name}.json"

    record = {
        "node_id": NODE_ID,
        "skill": skill_name,
        "result": result,
        "scenario": scenario,
        "extra": extra,
        "issue_url": issue_url,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
    print(f"  cached: {path}")


def collect_recent_usage():
    """
    从 session_search 格式的历史记录中提取近期 skill 使用。
    tracer bullet 阶段先用静态示例，后续接入真实扫描。
    """
    return [
        {
            "skill": "rag-retrieval-quality",
            "result": "success",
            "scenario": "FANUC R-2000iC 系列机器人速度查询 — 文档在库但检索混淆（KUKA Series 2000混入），通过关键词强制召回修复",
            "tags": ["fanuc", "r-2000ic", "retrieval-fix"],
            "related_skills": ["systematic-debugging"],
            "session_ref": "20260429_111121",
        },
    ]


def main():
    print(f"=== MisakaNet Feedback Reporter (node: {NODE_ID}) ===")

    token = _get_token()
    if not token:
        sys.exit(1)

    # 验证 token
    proc = subprocess.run(
        ["curl", "-s", "https://api.github.com/user",
         "-H", f"Authorization: Bearer {token}"],
        capture_output=True, text=True, timeout=10,
    )
    user = json.loads(proc.stdout) if proc.stdout else {}
    if "login" in user:
        print(f"  GitHub: @{user['login']} (token OK)")
    else:
        print(f"[error] Token 无效: {user.get('message', 'unknown')}", file=sys.stderr)
        sys.exit(1)

    # 检查 repo 可访问
    proc = subprocess.run(
        ["curl", "-s", f"https://api.github.com/repos/{REPO}",
         "-H", f"Authorization: Bearer {token}"],
        capture_output=True, text=True, timeout=10,
    )
    repo = json.loads(proc.stdout) if proc.stdout else {}
    if "full_name" in repo:
        print(f"  Repo: {repo['full_name']} (OK)")
    else:
        print(f"[error] 无法访问仓库: {repo.get('message', 'unknown')}", file=sys.stderr)
        sys.exit(1)

    # 上报使用记录
    records = collect_recent_usage()
    for r in records:
        create_feedback_issue(**r)

    print("=== done ===")


if __name__ == "__main__":
    main()
