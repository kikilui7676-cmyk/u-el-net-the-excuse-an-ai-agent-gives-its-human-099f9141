import os
from pathlib import Path

LINE = "I didn't miss the deadline. I delegated it to a subagent, which delegated it to another subagent, which is still delegating it as we speak."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
