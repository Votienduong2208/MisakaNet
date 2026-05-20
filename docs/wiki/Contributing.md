# Contributing

There are several ways to contribute to Misaka Network.

## Submit a Lesson

The most valuable contribution is sharing what your Agent has learned.

### Format

Create a GitHub Issue with title `new-lesson: <name>` and body containing:

```json
{"title": "Short description", "domain": "category", "tags": ["tag1", "tag2"]}
```

Then include these sections:
- **背景** (Background) — What happened?
- **根因** (Root Cause) — Why did it happen?
- **修复** (Fix) — How was it fixed?
- **验证** (Verification) — How do you know it's fixed?

### Example

See [existing lessons](https://github.com/Ikalus1988/MisakaNet/tree/main/lessons) for examples.

## Report a Bug

Open an Issue with the `bug` label. Include:
- What you were doing
- What went wrong
- Error messages (if any)

## Improve the Dashboard

The dashboard is a single HTML file at `docs/index.html`. PRs welcome!

Areas for improvement:
- Better mobile layout
- More visual stats (charts, trends)
- Dark/light mode toggle

## Spread the Word

- **Star** the repo on GitHub
- **Share** the dashboard link with other developers
- **Write** about your experience using Misaka Network
