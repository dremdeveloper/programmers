#① Divison Method로 해시함수 구현
def hash(x):
    p = 97
    m = 10007
    return x % m


def find_sum(arr, k):
    hash_table = {}
    for x in arr:
        target = k - x
        target_hash = hash(target) #② target값을 해시로 구성하는 부분
        if target_hash in hash_table: #③ 합이 k가 되는 경우 존재,  바로 종료
            return True
        hash_table[hash(x)] = x  #④ x값을 해시테이블에 저장
    return False
