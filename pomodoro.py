#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""番茄钟：25分钟专注 + 5分钟休息，4轮后长休息15分钟。纯标准库，双击就能跑。"""

import time

FOCUS_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
ROUNDS_BEFORE_LONG = 4


def countdown(total_seconds, label):
    """倒计时显示，结束时响一声。"""
    remaining = total_seconds
    while remaining > 0:
        m, s = divmod(remaining, 60)
        print(f"\r{label} 剩余 {m:02d}:{s:02d}  ", end="", flush=True)
        time.sleep(1)
        remaining -= 1
    print(f"\r{label} 时间到！{' ' * 20}")
    print("\a", end="", flush=True)  # 蜂鸣


def main():
    print("=== 番茄钟 ===")
    print(f"规则：专注{FOCUS_MIN}分钟 → 休息{SHORT_BREAK_MIN}分钟，"
          f"满{ROUNDS_BEFORE_LONG}轮后长休息{LONG_BREAK_MIN}分钟。")
    try:
        raw = input(f"要来几轮？直接回车默认{ROUNDS_BEFORE_LONG}轮：").strip()
        rounds = int(raw) if raw else ROUNDS_BEFORE_LONG
        rounds = max(1, rounds)
    except ValueError:
        rounds = ROUNDS_BEFORE_LONG

    for i in range(1, rounds + 1):
        print(f"\n第 {i}/{rounds} 轮：开始专注，手机放一边！")
        countdown(FOCUS_MIN * 60, "专注中")
        if i == rounds:
            break
        if i % ROUNDS_BEFORE_LONG == 0:
            print("长休息：起来走走、喝水、看看远处。")
            countdown(LONG_BREAK_MIN * 60, "长休息")
        else:
            print("短休息：起来走走、喝水、看看远处。")
            countdown(SHORT_BREAK_MIN * 60, "短休息")

    print("\n全部完成，辛苦了，好好放松一下吧！")


if __name__ == "__main__":
    main()
