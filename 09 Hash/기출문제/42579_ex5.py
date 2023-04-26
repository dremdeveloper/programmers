list1 = [1, 2, 3]
tuple1 = (4, 5, 6)
set1 = {7, 8, 9}
list1.extend(tuple1) # [1, 2, 3, 4, 5, 6]


list1.extend(set1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
