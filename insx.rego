# - xxx as R|B 从这些待选列表中删除这些数字
# - 17 24 25 34 as R
# - 13 2 3 6 11 7 12 15 as B
# 必须包含 + 23 as R 只针对 R
# + 13 15 18 26 29 as R
# bit1 需要出现的数字 +|- 1 2 3 4 5 6 7 @bit[1-7]
# + 29 22 as R
+ 2 4 6 @bit1
+ 6 7 8 9 @bit2
+ 12 13 14 @bit3
+ 29 @bit4
+ 30 @bit5
+ 31 @bit6
+ 10 5 6 @bit7