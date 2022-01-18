S = "안녕하세요"

#문자열 선택 연산자 : [index]
#인덱싱
#indx는 0부터 시작하는 순서번호
print(S[0])
print(S[1])
print(S[2])
print(S[3])
print(S[4])
#안녕하세요 : index (0~4)

#슬라이싱
#[시작 index : 끝 index+1]
print(S[0:2]) #안녕
print(S[2:]) #하세요
print(S[:2]) #안녕

#문자열의 길이 - len
print("문자열의 길이 : "+str(len(S)))
#문자열 + 숫자 : 숫자를 문자열로 변환해서 출력해준다.