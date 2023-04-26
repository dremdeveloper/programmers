price = {}

price["apple"] = 300
price["banana"] = 500
price["melon"] = 2000

#정렬대상 : price.items, 정렬기준 : 키(x[0]), 내림차순  [('melon', 2000), ('banana', 500), ('apple', 300)] 
print(sorted(price.items(), key = lambda x: x[0], reverse = True))

#정렬대상 : price.items, 정렬기준 : 값(x[1]), 내림차순  [('apple', 300), ('banana', 500), ('melon', 2000)]
print(sorted(price.items(), key = lambda x: x[0], reverse = False))# 

#정렬대상 : price.keys, 정렬기준 : 키(x[0]), 내림차순  ['apple', 'banana', 'melon']
print(sorted(price.keys(), key = lambda x: x[0], reverse = False))

#정렬대상 : price.keys, 정렬기준 : 값(x[1]), 내림차순  ['banana', 'melon', 'apple']
print(sorted(price.keys(), key = lambda x: x[1], reverse = False))# ['banana', 'melon', 'apple']
