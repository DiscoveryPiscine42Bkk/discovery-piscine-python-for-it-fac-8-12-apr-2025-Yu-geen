ori_arr = [3, 5, 1, 8, 8, 2,11, 11]
print(ori_arr)

new_arr = [i + 2 for i in ori_arr if i > 5]
new_arr = set(new_arr)
print(new_arr)