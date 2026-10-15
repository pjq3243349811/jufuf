#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""饮食记录：记热量＋蛋白质/碳水/脂肪，数据存在同目录的 diet_log.csv 里。"""

import csv
import os
from datetime import date

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diet_log.csv")
FIELDS = ["日期", "餐次", "食物", "热量(kcal)", "蛋白质(g)", "碳水(g)", "脂肪(g)"]
NUTRIENTS = ["热量(kcal)", "蛋白质(g)", "碳水(g)", "脂肪(g)"]


def ensure_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="", encoding="utf-8-sig") as f:
            csv.writer(f).writerow(FIELDS)


def ask_number(prompt):
    raw = input(prompt).strip()
    if not raw:
        return 0.0
    try:
        return float(raw)
    except ValueError:
        print("  没看懂，按 0 记。")
        return 0.0


def add():
    ensure_file()
    meal = input("餐次（早餐/午餐/晚餐/加餐，直接回车=加餐）：").strip() or "加餐"
    food = input("吃了什么：").strip() or "未命名"
    kcal = ask_number("热量(kcal)：")
    protein = ask_number("蛋白质(g)：")
    carbs = ask_number("碳水(g)：")
    fat = ask_number("脂肪(g)：")
    with open(FILE, "a", newline="", encoding="utf-8-sig") as f:
        csv.writer(f).writerow([str(date.today()), meal, food, kcal, protein, carbs, fat])
    print("已记录 ✓")


def today():
    ensure_file()
    day = str(date.today())
    with open(FILE, encoding="utf-8-sig") as f:
        rows = [r for r in csv.DictReader(f) if r["日期"] == day]
    if not rows:
        print("今天还没有记录，先去吃点好的再来记！")
        return
    totals = {k: 0.0 for k in NUTRIENTS}
    for r in rows:
        print(f"{r['餐次']} {r['食物']}: "
              f"{r['热量(kcal)']}kcal 蛋白质{r['蛋白质(g)']}g "
              f"碳水{r['碳水(g)']}g 脂肪{r['脂肪(g)']}g")
        for k in NUTRIENTS:
            try:
                totals[k] += float(r[k])
            except (ValueError, TypeError):
                pass
    print(f"—— 今日合计：{totals['热量(kcal)']:.0f}kcal "
          f"蛋白质{totals['蛋白质(g)']:.1f}g "
          f"碳水{totals['碳水(g)']:.1f}g "
          f"脂肪{totals['脂肪(g)']:.1f}g")


def main():
    print("=== 饮食记录 ===")
    choice = input("1. 记一笔  2. 看今天合计（直接回车=1）：").strip() or "1"
    if choice == "2":
        today()
    else:
        add()


if __name__ == "__main__":
    main()
