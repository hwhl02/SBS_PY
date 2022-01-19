name = input('이름을 입력해주세요 : ')
age = input('나이를 입력해주세요 : ')

#기본출력
print('이름 : ', name)
print('나이 : ', age)

#형식 문자열 - format
print('이름 : {}' .format(name))
print('나이 : {}' .format(age))

#{}안에 띄어쓰기 하면 안된다
#format앞에는,가 아니라 .이다

#f-strings
print(f'이름 : {name}')
print(f'나이 : {age}')