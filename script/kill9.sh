#!/bin/bash
# @Author: JogFeelingVI
# @Date:   2024-04-15 09:16:01
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-04-15 09:29:31
kill -9 $(lsof -ti tcp:8080)
echo "ok"
