# 注释行
# - xxx as R|B 从这些待选列表中删除这些数字
# - 17 24 25 34 as R
- 13 2 3 6 11 7 12 15 as B
# 必须包含 + 23 as R 只针对 R
# + 13 15 18 26 29 as R
# bit1 需要出现的数字 +|- 1 2 3 4 5 6 7 @bit[1-7]
# 同一个位置可以指定多条规则 结果将是它们综合结果
# 8 10 11 12
+ 1 @bit1
+ 25 27 24 23 @vit6
+ 2 13 15 11 @bit2
+ 23 26 25 @bit5
+ 14 16 18 19 9 21 22 3 @bit3
+ 22 20 17 19 23 18 21 16 24 @bit4



