#!/usr/bin/env python3
"""Entry point for the news-image-20261126 bounty.

Stdlib only (the grader's Python 3.13 slim image has no Pillow).
Copies the pre-rendered entry.png next to this file to the output
directory, so the program is deterministic: two runs write identical
bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
