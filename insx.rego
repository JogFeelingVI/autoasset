# - xxx as R|B 从这些待选列表中删除这些数字
# - 23 18 14 8 10 2 4 6 as R
# - 13 2 3 6 11 7 12 15 as B
# 必须包含 + 23 as R 只针对 R
# + 17 as R
# bit1 需要出现的数字 +|- 1 2 3 4 5 6 7 @bit[1-7]
# + 29 22 as R
+ 1 2 5 8 9 12 15 16 @bit7
+ 3 4 5 @bit1
+ 2 3 4 8 9 10 11 12 16 17 18 19 20 24 25 26 @bit2
+ 3 4 6 7 9 10 12 13 15 16 18 19 21 22 24 25 27 28 @bit3
+ 6 8 12 14 16 20 22 24 28 30 @bit4
+ 8 11 13 16 18 21 23 26 28 31 @bit5
+ 33 32 31 30 29 28 27 @bit6
# bit7 * 8