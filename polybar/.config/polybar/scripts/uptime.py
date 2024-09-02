#! /usr/bin/env python3

intervals = (
#    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('d', 86400),    # 60 * 60 * 24
    ('h', 3600),    # 60 * 60
    ('m', 60),
    ('s', 1),
)

def get_uptime():
    with open('/proc/uptime') as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds

def display_time(seconds, granularity=3):
    result = []

    for name, count in intervals:
        value = int(seconds // count)
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{}{}".format(value, name))
    return ':'.join(result[:granularity])

print(display_time(get_uptime()))
