# Description: 딕셔너리 자료형

dic = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
print(type(dic))
print(dic)

# 하나의 키에 하나의 값만 대응
a = {1: 'hi'}
print(a)

# value에 리스트도 넣을 수 있음
a = {'a': [1, 2, 3]}
print(a)

# 딕셔너리에 새로운 값 추가
a = {1: 'a'}
a[2] = 'b'
print(a)
a[3] = [1, 2, 3]    #value에 리스트 추가
# a[0] = 'c'  # key값을 중복시켜value값 수정
print(a)

# 딕셔너리 요소 삭제
del a[1]    # key값이 1인 요소 삭제 ( ,로 여러개 삭제 가능 ) 
print(a)

# 딕셔너리에서 key를 사용해 value얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey']) # 없는 key값을 입력하면 error

dic = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
print(dic['name'])  # 실전에서 많이 사용됨

# 주의사항
# key는 무조건 하나만 존재해야함
#key가 변할 수 없는 값이어야함 (리스트는 변할 수 있어서 key로 사용 불가능)

# 딕셔너리 key 리스트 만들기
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys()) #key값만 리스트로 반환 ( dict_keys 객체로 반환 )
print(a.items()) #key, value값을 튜플로 묶어서 반환

# key, value 쌍 모두 지우기
a.clear()   # 모든 key, value값 삭제
print(a)    # 빈 딕셔너리 출력

# key로 value얻기
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get('name'))    # a['name']과 같은 결과 출력
# 없는 key값을 입력하면 error가 안나고, None 출력
print(a.get('nokey', "값이 없습니다."))  # 없는 key값을 입력하면 뒤에 있는 문장 출력

# 해당 key가 딕셔너리 안에 있는지 조사하기
print('name' in a)  # True
print('email' in a) # False