# - xxx as R|B 从这些待选列表中删除这些数字
# - 17 24 25 34 as R
# - 13 2 3 6 11 7 12 15 as B
# 必须包含 + 23 as R 只针对 R
# + 13 15 18 26 29 as R
# bit1 需要出现的数字 +|- 1 2 3 4 5 6 7 @bit[1-7]
# + 29 22 as R
+ 4 @bit1
+ 23 24 25 @bit6
+ 2 3 14 15 16 21 22 23 24 @bit2
+ 21 22 @bit5
+ 13 14 15 16 17 18 19 @bit3
+ 16 17 18 19 @bit4
+ 4 6 7 8 9 14 15 16 @bit7