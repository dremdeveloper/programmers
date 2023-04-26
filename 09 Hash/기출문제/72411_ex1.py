from itertools import combinations

sample_menu = "ABC"
for it in combinations(sample_menu,2):
    print(it) 

#아래와 같이 출력됨
#('A', 'B')
#('A', 'C')
#('B', 'C')

sample_num = [1,2,3,4]
for it in combinations(sample_num,3):
    print(it) 
    
#아래와 같이 출력됨
#(1, 2, 3)
#(1, 2, 4)
#(1, 3, 4)
#(2, 3, 4)
