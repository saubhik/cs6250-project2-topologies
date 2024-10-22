# Ben Black, bblack45, Summer 2020
# My topo test case 2

# 5 nodes x 5 nodes square, with numbers and links scattered
# 1 --- 2 --- 4 --- 6 --- 9
# |                 |     |
# 3    16 -- 13 -- 12 -- 10
# |     |     |     |     |
# 5    15 -- 14    24    11
# |     |           |     |
# 7 -- 21 -- 18 -- 23    19
# |     |           |     |
# 8 -- 20 -- 22 -- 25 -- 17

# Solution
# 1 --- 2 --- 4 --- 6 --- 9
# |                 |     |
# 3    16 -- 13 -- 12    10
# |           |     |     |
# 5    15    14    24    11
# |     |                 |
# 7 -- 21 -- 18 -- 23    19
# |                       |
# 8 -- 20 -- 22 -- 25    17

topo = { 1 : [2, 3],
         2 : [1, 4],
         3 : [1, 5],
         4 : [2, 6],
         5 : [3, 7],
         6 : [4, 9, 12],
         7 : [5, 8, 21],
         8 : [7, 20],
         9 : [6, 10],
         10: [9, 11, 12],
         11: [10, 19],
         12: [6, 10, 13, 24],
         13: [12, 14, 16],
         14: [13, 15],
         15: [14, 16, 21],
         16: [13, 15],
         17: [19, 25],
         18: [21, 23],
         19: [11, 17],
         20: [8, 21, 22],
         21: [7, 15, 18, 20],
         22: [20, 25],
         23: [18, 24, 25],
         24: [12, 23],
         25: [17, 22, 23] }
