"""Git 学习实验脚本。"""

LESSON = "working-tree -> staging -> commit -> push -> pull request"


def current_lesson() -> str:
    """返回当前练习步骤说明。"""
    return LESSON


def main() -> None:
    print("Git Lab")
    print(current_lesson())


if __name__ == "__main__":
    main()
