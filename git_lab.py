"""Git 学习实验脚本。"""

LESSON = "working-tree -> staging -> commit -> push -> pull request"
REMOTE = "https://github.com/leosea/cloud-agent-demo"


def current_lesson() -> str:
    """返回当前练习步骤说明。"""
    return LESSON


def repo_remote() -> str:
    """返回这个练习仓库对应的 GitHub 地址。"""
    return REMOTE


def main() -> None:
    print("Git Lab")
    print(current_lesson())
    print(repo_remote())


if __name__ == "__main__":
    main()
