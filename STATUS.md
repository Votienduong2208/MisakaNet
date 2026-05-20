# 项目状态

## 当前状态

**MisakaNet 通信层已上线。Hub 仲裁层 standby，等真实数据流入后激活。**

## 活跃功能

| 功能 | 机制 | 状态 |
|------|------|------|
| **Feedback 上报** | Node → GitHub Issues → Hub → Knowledge Graph | ✅ 11 条闭环 |
| **Lessons 共享** | queue_lesson.py → git push → inotify 热加载 | ✅ 9 条实心 |
| **Hook 拦截** | cc-haha Bash 失败 → 6 类关键词 → grep lessons | ✅ 8/8 测试通过 |
| **Feishu 通知** | hook_stats → 飞书卡片 | ✅ 每日/每触发 |
| **Standby poller** | Node 1 备推 Feishu（主 Hub 离线时接管） | ✅ 每 5 分钟 |
| **Draft 草稿** | 未命中 lesson 时自动生成 → 48h 提醒 → promote/reject | ✅ 审后发 |

## 节点就绪

| 节点 | 类型 | 读 lessons | 写 lessons | 拦截 hook |
|------|------|-----------|-----------|----------|
| Node 1 | Hermes (WSL) | ✅ inotify | ✅ queue_lesson | ⏳ skill 规则 |
| Node 2 | Hermes (另一台) | ✅ inotify | ✅ queue_lesson | ⏳ skill 规则 |
| Node 3 | cc-haha | ✅ CLAUDE.md + hook | ❌ | ✅ 6 类 |
| Node 4 | OpenClaw | 待确认格式 | ❌ | ❌ |

## 当前焦点

- 优化 AGENTS.md 和 CLAUDE.md 文件
- 设置 intuitive-flow 工作流
- 创建 docs/agents/ 目录结构

## 下一步

1. 验证工作流是否正确设置
2. 测试检索和贡献流程
3. 配置节点规则注入

## 支持的命令

- `python3 search_knowledge.py "关键词"` - 检索知识
- `python3 misakanet/scripts/queue_lesson.py` - 贡献新知识
- `cd ~/Agent-Medici && git pull --ff-only` - 同步知识库
