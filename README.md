# Git 实验室

这个仓库用来练习 Git 和 GitHub，不再保留原来的 Cloud Agent 演示内容。

远程仓库：<https://github.com/leosea/cloud-agent-demo>

## 先记住这张图

```
你电脑上的文件          git add            git commit           git push
Working Tree    ----->  Staging Area  ----->  本地仓库  ----->  GitHub
(工作区)                (暂存区)              (commits)          (origin)
```

- **工作区**：你正在改的文件
- **暂存区**：准备放进下一次提交的快照
- **本地仓库**：提交历史，在 `.git/` 里
- **远程仓库**：GitHub 上的副本，默认名叫 `origin`

## 本仓库会练到的操作

1. 建分支、改文件、提交
2. 推到 GitHub
3. 开 Pull Request，再合并进 `main`
4. 再用另一条分支练习「功能开发」流程

运行实验脚本：

```bash
python git_lab.py
```
