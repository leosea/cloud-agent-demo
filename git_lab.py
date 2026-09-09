"""Git 学习实验脚本。"""

LESSON = "conflict side B: changed on learn/conflict-side-b"
REMOTE = "https://github.com/leosea/cloud-agent-demo"
BRANCH_RULE = "do not commit directly on main"


def current_lesson() -> str:
    """返回当前练习步骤说明。"""
    return LESSON


def repo_remote() -> str:
    """返回这个练习仓库对应的 GitHub 地址。"""
    return REMOTE


def branch_rule() -> str:
    """返回日常开发时应遵守的分支规则。"""
    return BRANCH_RULE


def main() -> None:
    print("Git Lab")
    print(current_lesson())
    print(repo_remote())
    print(branch_rule())


if __name__ == "__main__":
    main()
