# MisakaNet Shared Lessons

> 最后更新: 2026-05-19 15:40:11 UTC | 来源: hermes_wsl2

每条 lesson 包含踩坑记录、修复方法和验证方式，跨节点自动同步。

## 目录

| Lesson | Domain | Tags | Source |
|--------|--------|------|--------|
- [BGE embedding 模型需要降级 fallback 避免启动崩溃](lessons/bge-embedding-模型需要降级-fallback-避免启动崩溃) | rag | "project:agent-medici", "severity:high", "node:hermes_wsl" | draft
- [Chroma 建库无 Checkpoint — 进程一死全部丢失](lessons/chroma-建库无-checkpoint-进程一死全部丢失) | rag |  | active
- [ChromaDB 不能放在 NTFS 文件系统](lessons/chromadb-不能放在-ntfs-文件系统) | rag | "project:self-grow-wiki", "severity:critical", "platform:wsl", "node:hermes_wsl" | draft
- [Config was last written by a newer OpenClaw (2026.](lessons/config-was-last-written-by-a-newer-openclaw-2026) | feishu |  | active
- [DeepSeek TUI Agent 模式下 write_file 写入不落地 + worktree git 链接路径断裂](deepseek-tui-agent-模式下-write-file-写入不落地-worktree-git-链接路径断裂.md) | devops | deepseek-tui, agent-mode, write-file, worktree, wsl, git, lesson-written | hermes_wsl2
- [FANUC KL: 1086 是代码行号而非错误码](lessons/fanuc-kl-1086-是代码行号而非错误码) | fanuc |  | draft
- [FANUC KL: BYTES_AHEAD 是 Karel 内置 Procedure](lessons/fanuc-kl-bytes-ahead-是-karel-内置-procedure) | fanuc |  | draft
- [FANUC KL: ERR_ABORT vs ERR_PAUSE 行为差异](lessons/fanuc-kl-err-abort-vs-err-pause-行为差异) | fanuc |  | draft
- [FANUC KL: mm_module_h.kl 禁止 ROUTINE 声明](lessons/fanuc-kl-mm-module-h-kl-禁止-routine-声明) | fanuc |  | draft
- [Feishu WebSocket 404 Error - HTTP Webhook Required](feishu-websocket-404-error-http-webhook-required.md) | feishu-integration |  | hermes_wsl2
- [Feishu Wiki批量下载：文件类型处理策略](feishu-wiki-batch-download-file-type-handling.md) | devops | feishu, wiki, batch-download, file-type, pdf, docx, safari | hermes_wsl2
- [Feishu 凭证轮换后 Gateway 必须重启](lessons/feishu-凭证轮换后-gateway-必须重启) | feishu |  | active
- [Gateway 进程挂死未崩溃 — watchdog 自动恢复](lessons/gateway-进程挂死未崩溃-watchdog-自动恢复) | devops |  | active
- [Git 凭证和 Node ID — Node2 加网后必须设置](lessons/git-凭证和-node-id-node2-加网后必须设置) | devops |  | active
- [Hermes Agent 手动更新步骤（update 超时）](lessons/hermes-agent-手动更新步骤-update-超时) | devops | "project:agent-medici", "severity:medium", "node:hermes_wsl" | draft
- [Hub FeishuWSClient.start() 从未调用 — WebSocket 接收死代码](lessons/hub-feishuwsclient-start-从未调用-websocket-接收死代码) | feishu |  | active
- [Hub Hermes 凭证体系 — Gateway vs Hub 各自读哪里](lessons/hub-hermes-凭证体系-gateway-vs-hub-各自读哪里) | devops |  | active
- [InternalGateway API 网关不兼容 Anthropic 原生格式](lessons/InternalGateway-api-网关不兼容-anthropic-原生格式) | devops | "project:rag", "severity:medium", "node:hermes_wsl" | draft
- [OpenClaw 重装教训 — 删除前先停服务清残留](lessons/openclaw-重装教训-删除前先停服务清残留) | devops |  | active
- [POC 记录已写入飞书文档末尾（21个块，含 Q2/Q5 验证结果、修正说明和待办清单）。 有一个小](lessons/poc-记录已写入飞书文档末尾-21个块-含-q2-q5-验证结果-修正说明和待办清单-有一个小) | feishu |  | active
- [RAG 三通道 LLM 容灾方案](lessons/rag-三通道-llm-容灾方案) | rag | "project:self-grow-wiki", "node:hermes_wsl", "scope:broad" | draft
- [RAG 分块参数：800 字符 + 100 重叠 + 每文件最多 100 分块](lessons/rag-分块参数-800-字符-100-重叠-每文件最多-100-分块) | rag | "project:self-grow-wiki", "severity:medium", "node:hermes_wsl" | draft
- [RAG 报警代码检索需要关键词强制召回](lessons/rag-报警代码检索需要关键词强制召回) | rag | "project:self-grow-wiki", "severity:high", "node:hermes_wsl" | draft
- [RAG 检索中文乱码 — pymupdf4llm 默认编码问题](lessons/rag-检索中文乱码-pymupdf4llm-默认编码问题) | rag |  | active
- [WSL pip install GBK 编码导致 hub_poller 崩溃](lessons/wsl-pip-install-gbk-编码导致-hub-poller-崩溃) | devops | "project:agent-medici", "severity:critical", "platform:wsl", "node:hermes_wsl" | draft
- [WSL 终端编辑配置危险 — TTy粘贴吞下划线](lessons/wsl-终端编辑配置危险-tty粘贴吞下划线) | system |  | active
- [WSL 需要代理配置才能访问 HuggingFace 和外部网络](lessons/wsl-需要代理配置才能访问-huggingface-和外部网络) | devops | "project:self-grow-wiki", "severity:high", "platform:wsl", "node:hermes_wsl" | draft
- [[cc-haha] 权限 错误 — permission:Permission denied](cc-haha-权限-错误-permission-permission-denied.md) | permission | cc-haha, hook-auto, permission, permission:Permission denied | cc_haha
- [[cc-haha] 模型输出异常 错误 — Exit code 1 Traceback (most recent call last):   File "<stri...(截断)](cc-haha-模型输出异常-错误-exit-code-1-traceback-most-recent-call-las.md) | model_output | cc-haha, hook-auto, model_output,  | cc_haha
- [[cc-haha] 网络连接 错误 — Exit code 1 Name: websocket-client Version: 1.9.0 Summary: W...(截断)](cc-haha-网络连接-错误-exit-code-1-name-websocket-client-version-1-.md) | network | cc-haha, hook-auto, network,  | cc_haha
- [[cc-haha] 网络连接 错误 — Exit code 1 Traceback (most recent call last):   File "<stdi...(截断)](cc-haha-网络连接-错误-exit-code-1-traceback-most-recent-call-last-.md) | network | cc-haha, hook-auto, network,  | cc_haha
- [[cc-haha] 网络连接 错误 — Exit code 128 From https://github.com/Ikalus1988/MisakaNet  ...(截断)](cc-haha-网络连接-错误-exit-code-128-from-https-github-com-ikalus19.md) | network | cc-haha, hook-auto, network,  | cc_haha
- [[cc-haha] 网络连接 错误 — network:Timeout](cc-haha-网络连接-错误-network-timeout.md) | network | cc-haha, hook-auto, network, network:Timeout | cc_haha
- [[草稿] cc-haha network 错误: Exit code 1](草稿-cc-haha-network-错误-exit-code-1.md) | devops | cc-haha, hook-auto, network | hermes_wsl2
- [aily 飞书 MCP 通道：只能拉取不能推送](lessons/aily-飞书-mcp-通道-只能拉取不能推送) | ailysw |  | draft
- [bootstrap 关于 table aware re chunking 我的判断 部分同意魔术师的根因分析 但不](lessons/bootstrap-关于-table-aware-re-chunking-我的判断-部分同意魔术师的根因分析-但不) | rag |  | draft
- [bootstrap 方案一 ChromaDB Server 飞书多维表事件通知 定位 最轻量 倒吊人 Gbr](lessons/bootstrap-方案一-chromadb-server-飞书多维表事件通知-定位-最轻量-倒吊人-gbr) | feishu |  | draft
- [bootstrap 评审意见 优点 分层清晰 四层防御体系思路正确 问题分析到位 严重程度分级合理](lessons/bootstrap-评审意见-优点-分层清晰-四层防御体系思路正确-问题分析到位-严重程度分级合理) | devops |  | draft
- [bootstrap 这也是倒吊人的操作 二 当前未解决的 3 个问题 问题 1 hermes run 命令仍然找不到](lessons/bootstrap-这也是倒吊人的操作-二-当前未解决的-3-个问题-问题-1-hermes-run-命令仍然找不到) | devops |  | draft
- [bootstrap 这里面包含答案吗 PLAIN_TEXT usr bin env python3](lessons/bootstrap-这里面包含答案吗-plain-text-usr-bin-env-python3) | rag |  | draft
- [cc-connect 飞书机器人完整配置指南](cc-connect-飞书机器人完整配置指南.md) | feishu |  | bootstrap
- [lessons.md 修正（4 处） 项目 旧结论 修正后 heading block（type=4](lessons/lessons-md-修正-4-处-项目-旧结论-修正后-heading-block-type-4) | rag |  | active
- [wcferry 微信版本锁定 — 3.9.12.51 才能用](lessons/wcferry-微信版本锁定-3-9-12-51-才能用) | devops | "project:rag", "platform:windows", "node:hermes_wsl", "scope:narrow" | draft
- [wxauto 必须在 Windows Python 下安装，不能走 WSL pip](lessons/wxauto-必须在-windows-python-下安装-不能走-wsl-pip) | devops | "project:rag", "platform:windows", "node:hermes_wsl", "scope:narrow" | draft
- [企业微信机器人：长连接模式不需要 ngrok](lessons/企业微信机器人-长连接模式不需要-ngrok) | devops | "project:rag", "platform:windows", "node:hermes_wsl", "scope:narrow" | draft
- [再补充一下，RAG助手这两天的一个工作内容，主要就是一个通过让RAG知识库来读取我已有的一些工业机器](lessons/再补充一下-rag助手这两天的一个工作内容-主要就是一个通过让rag知识库来读取我已有的一些工业机器) | rag |  | active
- [另外，RAG助手， Wiki项目又有新进展。 这个项目经过了从一开始的OPUS 4.6，写了初版之后](lessons/另外-rag助手-wiki项目又有新进展-这个项目经过了从一开始的opus-4-6-写了初版之后) | rag |  | active
- [复盘下你的飞书技能如何提高，并给出方案](lessons/复盘下你的飞书技能如何提高-并给出方案) | feishu |  | active
- [好，控制并发，那就开始布置本开源方案，作为 wsl 的第三个 agent](lessons/好-控制并发-那就开始布置本开源方案-作为-wsl-的第三个-agent) | feishu |  | active
- [容灾方案输出为飞书云文档](lessons/容灾方案输出为飞书云文档) | feishu |  | active
- [帮我记一下我今天的日记啊，阈值的日记啊，今天完成了什么工作，然后跟你说完，你整理一下，然后发出来。](lessons/帮我记一下我今天的日记啊-阈值的日记啊-今天完成了什么工作-然后跟你说完-你整理一下-然后发出来) | rag |  | active
- [我已将部分工作直接发给Hermes cli助手，你注意检查，不要重复施工](lessons/我已将部分工作直接发给hermes-cli助手-你注意检查-不要重复施工) | feishu |  | active
- [按照方案进行测试https://tarot-club.feishu.cn/docx/TkcHd3Lq](lessons/按照方案进行测试https-tarot-club-feishu-cn-docx-tkchd3lq) | feishu |  | active
- [知识库 4σ 质量审计流水线](lessons/知识库-4-质量审计流水线) | rag | "project:self-grow-wiki", "severity:medium", "node:hermes_wsl" | draft
- [考生1回复：考试执行受阻，未完成作答： 执行第一步安装依赖时遇到环境问题：当前运行环境中pip命令不](lessons/考生1回复-考试执行受阻-未完成作答-执行第一步安装依赖时遇到环境问题-当前运行环境中pip命令不) | rag |  | active
- [这是倒吊人在本周修改wsl的记录，有没有关联：一、本周修改的 WSL 内容 文件 操作 目的 ~/.](lessons/这是倒吊人在本周修改wsl的记录-有没有关联-一-本周修改的-wsl-内容-文件-操作-目的) | feishu |  | active
- [这里面也有答案？ ```PLAIN_TEXT # Edoc V10.0 POC 召回测试 ## 环境](lessons/这里面也有答案-plain-text-edoc-v10-0-poc-召回测试-环境) | rag |  | active
- [问题： Hermes 的 mmx CLI（WSL 内）需要自己的 ~/.mmx/config.jso](lessons/问题-hermes-的-mmx-cli-wsl-内-需要自己的-mmx-config-jso) | feishu |  | active
- [防火墙端口开放不等于内网穿透](lessons/防火墙端口开放不等于内网穿透) | devops | "project:rag", "platform:wsl", "node:hermes_wsl", "scope:broad" | draft
- [飞书 Block API 假成功特征](lessons/飞书-block-api-假成功特征) | feishu |  | draft
- [飞书 Block Type 正确值与已知限制](lessons/飞书-block-type-正确值与已知限制) | feishu |  | draft
- [飞书 Block 批量写入上限](lessons/飞书-block-批量写入上限) | feishu |  | draft
- [飞书 webhook URL 必须用环境变量或 gitignored 的 config.yaml](lessons/飞书-webhook-url-必须用环境变量或-gitignored-的-config-yaml) | devops | "project:agent-medici", "severity:critical", "node:hermes_wsl" | draft
- [OpenClaw Gateway 动态模块缺失 — 飞书消息分发失败](lessons/openclaw-gateway-动态模块缺失-导致飞书消息分发失败) | feishu | "node:misaka10004", "severity:critical", "project:misakanet" | active
