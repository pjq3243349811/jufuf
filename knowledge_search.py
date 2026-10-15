#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""知识点速查：在 study 备考资料里按关键词秒找知识点。
第一次运行会自动从 GitHub 下载备考资料，之后离线也能用。"""

import os
import urllib.parse
import urllib.request

BASE = "https://raw.githubusercontent.com/pjq3243349811/jufuf/main/study"
NOTES = [
    "国考行测常识速记.md",
    "低压电工理论要点.md",
    "无人机理论要点.md",
    "备考计划表.md",
]


def study_dir():
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "study")
    os.makedirs(d, exist_ok=True)
    return d


def ensure_notes(d):
    missing = [n for n in NOTES if not os.path.exists(os.path.join(d, n))]
    if not missing:
        return
    print("正在下载备考资料…")
    for n in missing:
        url = BASE + "/" + urllib.parse.quote(n)
        try:
            urllib.request.urlretrieve(url, os.path.join(d, n))
            print("  " + n + " 下载好了")
        except Exception:
            print("  " + n + " 下载失败，手动下载：" + BASE + "/" + n)


def search(keyword, d):
    results = []
    for n in NOTES:
        path = os.path.join(d, n)
        if not os.path.exists(path):
            continue
        heading = ""
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if line.startswith("#"):
                    heading = line.lstrip("#").strip()
                if keyword in line:
                    results.append((n, heading, line.strip()))
    return results


def main():
    print("=== 知识点速查 ===")
    print("输入关键词，秒找备考资料里的相关知识点。输入 q 退出。")
    d = study_dir()
    ensure_notes(d)
    while True:
        kw = input("\n搜什么：").strip()
        if kw.lower() == "q":
            print("下次见！")
            break
        if not kw:
            continue
        hits = search(kw, d)
        if not hits:
            print("没找到「" + kw + "」，换个词试试。")
            continue
        print("找到 " + str(len(hits)) + " 条：")
        for fname, heading, line in hits[:20]:
            tag = "【" + fname.replace(".md", "") + "】"
            sec = "（" + heading + "）" if heading else ""
            print(tag + sec + "\n  " + line)
        if len(hits) > 20:
            print("…还有 " + str(len(hits) - 20) + " 条，只显示前 20 条。")


if __name__ == "__main__":
    main()
