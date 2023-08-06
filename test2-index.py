
#แบบที่ 1

def find_max_index(arr):
    max_value = float('-inf')
    max_index = -1

    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i

    return max_index

my_array =  [1,2,1,3,5,6,4]
max_index = find_max_index(my_array)

if max_index != -1:
    print(f"Index ของค่ามากที่สุดคือ {max_index}")
else:
    print("ไม่พบค่าในรายการ")



#แบบที่ 2

# my_array =  [1,2,1,3,5,6,4]

# max_value = None
# max_index = None

# for i in range(len(my_array)):
#     if max_value is None or my_array[i] > max_value:
#         max_value = my_array[i]
#         max_index = i

# if max_index is not None:
#     print(f"Index ของค่ามากที่สุดคือ {max_index}")
# else:
#     print("ไม่พบค่าในรายการ")









