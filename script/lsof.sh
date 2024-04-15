#!/bin/bash
# @Author: JogFeelingVI
# @Date:   2024-04-15 10:22:39
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-04-15 10:30:50
lsof -i tcp:8080 -sTCP:LISTEN | awk '{print $2, $6}' | tail -n +2
