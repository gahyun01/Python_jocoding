# Description: 튜플 자료형

t1=()
t2=(1,)
t3=1,2,3
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

#인덱싱
print(t3[0])

#슬라이싱
print(t3[1:])

#더하기
print(t1+t3)

#반복(*)
print(t3*3)