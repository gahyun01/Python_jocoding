# Description: 불 자료형

# 참과 거짓을 나타내는 자료형
# 무조건 첫 문자를 대문자로 써야함
# True, False 2가지 값만 가질 수 있음

a = 2
if a==3:
    print(a)    # 조건이 참일 때 실행

a = True
print(a)    # True

a = 1 == 1
print(a)    # True

a < 2
print(a)    # True

# 자료형의 참과 거짓
a = [1,2,3,4]
while a:
    print(a)    # 리스트의 마지막 요소가 없을 때까지 반복
    a.pop()     # 리스트의 마지막 요소를 하나씩 뽑아냄

if []:  # 거짓 ( 리스트가 비어있기 때문 )
    print("True")
else:
    print("False")

# 불로 형변환
a = bool([1,2,3])
print(a)    # True