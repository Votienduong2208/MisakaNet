# Agent-Medici

> **MisakaNet 的私有 fork — Hub 专属扩展**

Agent-Medici 是 [MisakaNet](https://github.com/Ikalus1988/MisakaNet) 的 fork，添加了 Hub 编排层（知识图谱、仲裁、飞书通知）。

## 架构

```
MisakaNet (upstream)          Agent-Medici (fork)
┌──────────────────┐         ┌──────────────────────────┐
│ lessons/         │ ──merge──→ lessons/ (继承 + 扩展)   │
│ scripts/         │         │ scripts/ (继承)           │
│ docs/            │         │ docs/ (继承)              │
│ search_knowledge │         │ search_knowledge (继承)   │
└──────────────────┘         │ hub/ ← Hub 专属代码       │
                             │   ├── hermes_hub.py       │
                             │   ├── orchestrator/       │
                             │   ├── storage/            │
                             │   ├── sync/               │
                             │   └── master/             │
                             │ reference/ ← 设计文档     │
                             │ .hook_stats/ ← 运行数据   │
                             └──────────────────────────┘
```

## 上游同步

```bash
git fetch upstream
git merge upstream/main --no-edit
# 解决冲突（通常只在 lessons/ 和 CLAUDE.md）
git push origin main
```

## Hub 功能

| 功能 | 状态 | 说明 |
|------|------|------|
| Knowledge Graph | ✅ 活跃 | NetworkX 图谱，176+ 节点 |
| Feishu 通知 | ✅ 活跃 | hook_stats → 飞书卡片 |
| Skill Indexer | ✅ 活跃 | BGE-m3 语义去重 |
| Hub Poller | ✅ 活跃 | 消费 GitHub Issues |
| Standby Poller | ✅ 活跃 | 主 Hub 离线时接管 Feishu |
| Arbitration | ⏳ standby | 等真实冲突数据 |
| Confidence Model | ⏳ standby | 等仲裁数据激活 |
| A2A Server | ⏳ standby | 当前用 GitHub Issues 通信 |

## Dir Structure

```
Agent-Medici/
├── hub/                      # Hub 专属代码
│   ├── hermes_hub.py         # Hub 主入口
│   ├── orchestrator/         # 仲裁/置信度/去重
│   ├── storage/              # 知识图谱/向量存储
│   ├── sync/                 # A2A/飞书/调度
│   └── master/               # Master API
├── lessons/                  # 知识库（98 条，含上游）
├── misakanet/scripts/        # 节点侧脚本（继承上游）
├── reference/                # 设计文档
├── .hook_stats/              # Hook 统计数据
├── search_knowledge.py       # 节点侧检索
├── AGENTS.md                 # 节点接入规则
├── CLAUDE.md                 # Agent 行为指令
└── README.md                 # 本文件
```

## 节点

| 节点 | 类型 | 读 lessons | 写 lessons | 拦截 hook |
|------|------|-----------|-----------|----------|
| Node 1 | Hermes (WSL) | ✅ | ✅ | ✅ |
| Node 2 | Hermes (另一台) | ✅ | ✅ | ⏳ |
| Node 3 | cc-haha | ✅ | ❌ | ✅ |
| Node 4 | OpenClaw | 待确认 | ❌ | ❌ |

## License

Apache 2.0
