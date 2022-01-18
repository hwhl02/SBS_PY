# 튜플 컬렉션
# : () 기호로 여러 개의 변경할 수 없는 자료를 저장하는 컬렉션
t1 = (10, 12.45, 'hello')
t2 = (20, 22.45, 'bye')
t3 = t1+t2

print('t1 : ',t1)
print('t2 : ',t2)
print('t3 : ',t3)

#튜플 언덱싱
t4 = (1,2,3)
print('t4[0] : ', t4[0])
print('t4[1] : ', t4[1])
print('t4[2] : ', t4[2])

#튜플 슬라이싱
t5 = ('월','화','수','목','금','토','일')
print ( 't5[0:5] : ', t5[0:5])
print ( 't5[5:7] : ', t5[5:7])

#주의
# : 튜플을 정의할 때, 요소를 하나만 저장하는 경우
# 기호를 같이 작성해야 튜플로 인식된다

#,을 입력하지 않으면 tuple로 인식되지 않는다.
t6 = (10)
print(type(t6))

t7(10,)
print(type(t7))

