#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""倒计时：重要日子还剩几天，一眼看清。"""

from datetime import datetime

EVENTS = [
    ("国考报名截止", "2026-10-24 18:00"),
    ("国考笔试", "2026-11-29 09:00"),
    ("国开春季报名建议完成", "2027-02-28 00:00"),
]


def show(name, dt_str):
    try:
        target = datetime.strptime(dt_str.strip(), "%Y-%m-%d %H:%M")
    except ValueError:
        print(f"{name}：日期格式不对，跳过。")
        return
    delta = target - datetime.now()
    if delta.total_seconds() <= 0:
        print(f"{name}（{dt_str}）：已过")
        return
    days = delta.days
    hours, rem = divmod(delta.seconds, 3600)
    minutes = rem // 60
    print(f"{name}（{dt_str}）：还剩 {days} 天 {hours} 小时 {minutes} 分钟")


def main():
    print("=== 倒计时 ===")
    for name, dt_str in EVENTS:
        show(name, dt_str)
    custom = input("\n要加自己的倒计时吗？格式：名字,YYYY-MM-DD HH:MM（直接回车跳过）：").strip()
    if custom and "," in custom:
        name, dt_str = custom.split(",", 1)
        show(name.strip(), dt_str)


if __name__ == "__main__":
    main()
