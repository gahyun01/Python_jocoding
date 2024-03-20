a = 'python'
print(a)
a = "python"
print(a)

# '출력
a = "Python's favorite food is perl"
print(a)
a = 'Python\'s favorite food is perl'
print(a)

# "출력
a = '"Python is very easy." he says.'
print(a)
a = "\"Python is very easy.\" he says."

a = "Life iss too short \nyou need python"
print(a)

# 여러줄 문자열
a = """Life is too short    
    yor need python"""
print(a)
a = '''Life is too short
    you need python'''
print(a)

#문자열 +
head = "python"
tail = "is fun!"
print(head + tail)
print("="*50)

#해당 인덱스 순번의 값
a = "Life is too short, you need Python"
print(a[3])
print(a[-1])
print(a[:4])    # 0번째 부터 3번째까지의 값

# %s에 문자열 추가, %d에 숫자 추가
a = "I eat %s apples." %"five"
print(a)
number = 10
day = "three"
a = "I ate %d apples. so I was sick %s days." %(number, day)
print(a)

print("%10s" % "hi")    #10번째 칸 뒤에 문자열 추가
print("%-10sjane" % "hi")   #10번째 칸 앞에 문자열 추가
print("%0.4f" % 3.42134234)     #소수점 4번쨰자리까지
a = "Python is best choice"
print(a.count('b'))
print(a.find('b'))  # 없으면 -1
print(a.index('b'))     #없으면 error남

a = ","
print(a.join('abcd'))   #해당 문자열 사이사이에 a추가

a = '   Hi  '
print(a.upper())    #대문자
print(a.lower())    #소문자

print(a.lstrip())   #왼쪽 공백 삭제
print(a.rstrip())   #오른쪽 공백 삭제
print(a.strip())    #양쪽 공백 삭제

a = "Life is too short"
print(a.replace("Life", "Your leg")) #바꾸고싶은 문자열, 바꿀 문자열
print(a.split()) #space기준으로 나눠서 리슽트 만듬


a = f"I eat {number} apples"
print(a)
a = "I eat {} apples".format(number)
print(a)