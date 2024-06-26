#!/bin/bash
# @Author: JogFeelingVI
# @Date:   2024-04-15 12:40:31
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-04-16 21:42:50

# 判断操作系统类型
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS系统
    ipconfig getifaddr en0 # 获取en0接口的IP地址
else
    # 其他系统 (Linux)
    ip -4 address show | grep "noprefixroute" | grep -v "127.0.0.1" | awk '{print $2}' | cut -d "/" -f1 | tail -n 4
fi
