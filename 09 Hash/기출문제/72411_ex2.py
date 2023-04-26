from itertools import combinations
from collections import Counter
str1 = "abc"
str2 = "cba"
menu = []

menu += combinations(str1,2)
menu += combinations(str2,2)

counter = Counter(menu)

for c in counter.items():
    print(c)
    
    
#아래와 같이 출력됨
#(('a', 'b'), 1)
#(('a', 'c'), 1)
#(('b', 'c'), 1)
#(('c', 'b'), 1)
#(('c', 'a'), 1)
#(('b', 'a'), 1)

</>

정렬이 수행되면, 아래와 같이 원하는대로 나오는 것을 알 수 있습니다.
<Code>
from itertools import combinations
from collections import Counter
str1 = "abc"
str2 = "cba"
menu = []

menu += combinations(sorted(str1),2)
menu += combinations(sorted(str2),2)

counter = Counter(menu)

for c in counter.items():
    print(c)
    
    
#아래와 같이 출력됨
#(('a', 'b'), 2)
#(('a', 'c'), 2)
#(('b', 'c'), 2)
