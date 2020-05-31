# Topology with a tail:
#    submitted by Lindsey Bates
# 5 --- 4 --- 1
# |     |     |
# |     |     |
# 3 --- 2 --- 7 --- 6

topo = { 1 : [4, 7],
         2 : [3, 4, 7],
         3 : [2, 5],
         4 : [1, 2, 5],
         5 : [3, 4],
         6 : [7],
	 7 : [1, 2, 6]}