"""
grid_size = [2,2]

def rec_path(grid_size):
	
	# base case, no moves left
	if grid_size == [0,0]: return 1
	# recursive calls
	paths = 0 
	# moves left 
	if grid_size[0] > 0:
		paths += rec_path([grid_size[0]-1,grid_size[1]])
		print("left", paths)
	# moves down
	if grid_size[1] > 0:
		paths += rec_path([grid_size[0],grid_size[1]-1])
		print("down", paths)
	print(grid_size)
	return paths



result = rec_path(grid_size)

print(result)
"""


def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j] + L[j - 1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]


n = route_num(20)
print(n)
