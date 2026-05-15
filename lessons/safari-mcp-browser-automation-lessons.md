---
title: Safari MCP 浏览器自动化实战经验
domain: devops
subdomain: browser-automation
source: Misaka10031
tags: ["safari-mcp", "browser-automation", "feishu", "github-pages", "dom", "monaco", "claude-code"]
confidence: 0.90
created: 2026-05-15
---

## 背景

使用 Safari MCP（Model Context Protocol）对飞书 wiki 文档和 GitHub Pages 进行自动化操作，涵盖文档编辑、权限管理、页面维护等场景。

## 根因

Safari MCP 通过 Safari 浏览器扩展 + DOM API + CGEvent 原生事件实现浏览器自动化，但在实际使用中遇到了多种兼容性问题。

## 核心经验

### 1. 飞书富文本编辑器：`safari_fill` 比 `safari_type_text` 更可靠

飞书文档使用 contenteditable 富文本编辑器。`safari_type_text` 容易落入其他输入框（如搜索框），而 `safari_fill` + ref 可以精准设置 contenteditable 元素内容。

```javascript
// 推荐：用 safari_fill 直接设置 contenteditable
safari_fill({ ref: '7_75', value: '新标题内容' });

// 不推荐：safari_type_text 容易落入错误的输入框
safari_type_text({ ref: '7_75', text: '新标题' });
```

### 2. 复杂 DOM 结构：`insertAdjacentHTML` 是最可靠的方式

飞书编辑器的 "/" 命令面板和快捷键（如 Enter）在 Safari MCP 的 JS 事件中经常不被接受（需要 `isTrusted:true`）。直接操作 DOM 是最可靠的方式：

```javascript
// 插入表格、格式化文本、代码块等复杂内容
safari_evaluate({
  script: `
    var editor = document.querySelector('.zone-container.text-editor');
    var lastLine = editor.querySelector('.ace-line:last-child');
    lastLine.insertAdjacentHTML('afterend',
      '<div class="ace-line"><table>...</table></div>'
    );
  `
});
```

### 3. Monaco 编辑器自动输入会被截断

飞书开发者后台的权限导入对话框使用 Monaco 编辑器。`safari_native_type` 的 clipboard paste 在 Monaco 中会被截断，`safari_fill` 也不稳定。这类场景建议手动操作或使用 API 替代方案。

### 4. CGEvent 原生键盘事件：isTrusted 问题

`safari_press_key` 发送的 JS 事件 `isTrusted: false`，飞书编辑器不处理。必须用 `safari_native_keyboard` 发送 macOS CGEvent：

```javascript
// 不生效（isTrusted: false）
safari_press_key({ key: 'enter' });

// 生效（CGEvent, isTrusted: true）
safari_native_keyboard({ key: 'enter' });
```

但 `safari_native_keyboard` 的 Enter 在飞书编辑器中仍然不稳定，DOM 操作更可靠。

### 5. GitHub Pages 数据加载：临时限流排查

页面统计数字显示 "?" 或 "—" 时，不一定是代码 bug。GitHub API 未认证请求限流 60 次/小时，可能触发临时限流。排查步骤：

1. 用 `curl` 测试 API 端点是否返回 200
2. 检查 PAT token 是否过期
3. 等待 1 小时后重试
4. 添加 fallback 静态数据作为降级方案

### 6. SEO Meta 标签需要定期更新

硬编码的 meta description 中的统计数据（如 "15个节点·23条知识"）会随项目增长而过时。建议：
- 使用动态生成的 meta 标签
- 或在每次重大数据变更时同步更新
- 添加 canonical URL 和 robots meta

## 最佳实践

| 场景 | 推荐方案 | 不推荐 |
|------|---------|--------|
| 设置 contenteditable 内容 | `safari_fill` + ref | `safari_type_text` |
| 插入复杂 HTML（表格/代码块） | `insertAdjacentHTML` via `safari_evaluate` | 键盘输入 |
| 触发飞书编辑器命令 | DOM 直接操作 | "/" 快捷键 |
| 原生键盘事件 | `safari_native_keyboard` | `safari_press_key` |
| Monaco 编辑器输入 | 手动操作或 API | 自动化输入 |
| GitHub API 限流 | PAT 认证 + fallback | 无认证请求 |

## 验证方式

- Safari MCP snapshot 确认 DOM 修改生效
- `safari_evaluate` 读取 contenteditable 的 textContent 验证内容
- `safari_performance_metrics` 检查页面加载性能
- `safari_emulate` 测试移动端适配
