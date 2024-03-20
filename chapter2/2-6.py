# Description: 집합 자료형

s1 = set([1,2,3])
print(s1)
print(type(s1))     # <class 'set'>
s1 = set("hello")
print(s1)   # 순서가 없고 랜덤으로 출력, 중복을 허용하지 않음

# 집합은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없음
li = list(s1)    # 리스트로 변환
print(li[0])    # 리스트로 변환 후 인덱싱 가능
t1 = tuple(s1)  # 튜플로 변환
print(t1[0])    # 튜플로 변환 후 인덱싱 가능

# 집합 자료형 활용하는 방법
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)  # 출력: {1, 2, 3}
print(s1.difference(s2))
print(s2 - s1)  # 출력: {8, 9, 7}

# 집합 자료형 관련 함수
s1 = set([1,2,3])
s1.add(4)   # 값 1개 추가
print(s1)   # 출력: {1, 2, 3, 4}

s1.update([5,6,7])  # 값 여러개 추가
# s1.add([8,9])   # 리스트 추가 불가능

s1.remove(2)    # 값( value ) 제거 ( 없으면 error )
print(s1)

# 보통 리스트 자료형에서 중복된 값을 제거하기 위해 사용
a = [1,2,3,4,3,2,1]
a = set(a)  # 중복된 값 제거
a = list(a) # 리스트로 변환
print(a)