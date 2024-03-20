a=[]
print(a)

a=[1,2,3,4,5]
print(a[0]+a[2])
print(a[-1])    # 리스트의 마지막값 출력

print(a[0:2])
print(a[:2])
print(a[2:])

a=[1,2,3]
b=[4,5,6]
print(a+b)
print(a*3)  #리스트 반복

#해당 인덱스값 변경
a[2]=4
print(a)
a[1:2]=['a','b','c']
print(a)

#리스트 요소 삭제
a[1:3]=[]
print(a)
del a[1]
print(a)
a=[1,2,3,1,2,3]
a.remove(3)     #맨 처음 나오는 해당값 제거
print(a)

#리스트에 요소 추가
a=[1,2,3]
a.append(4)
print(a)
a.append([5,6])
print(a)
a.extend([4,5])
print(a)
a.insert(3,5)   #3번째 인덱스에 값추가
print(a)

#리스트 정렬
a=[1,4,3,2]
a.sort()
print(a)
a=['a', 'c', 'b']
a.sort()
print(a)

#리스트 뒤집기 (해당 리스트 역순)
a=[1,4,3,2]
a.reverse()
print(a)

#위치 반환 (해당값 없으면 error뜸)
print(a.index(3))

#리스트요소끄집어내기
print(a.pop()) #마지막 인덱스 값
print(a)
print(a.pop(1)) #해당 인덱스 값
print(a)

#해당값 개수
print(a.count(4))