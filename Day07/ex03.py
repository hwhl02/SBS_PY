''''''
#3. len() 함수
#: 함수의 전달된 객체으 길이(개수)를 반환하는 함수
#ex) li = [1,2,3,4]
#len(li) --> 4

#4. sorted() 함수
#: 반복가능한 객체를 오름차순으로 정렬한 결과 반환하는 함수
#ex) li=[10,3,9,2,5]
#sorted(li) --> [2,3,5,9,10]

#5. zip()함수
# : 여러 개의 반복가능한 객체들을 튜플로 묶어서 반환하는 함수
# ex) names = ['c언어','파이썬','JAVA']
#     scores = [100,90,80]
#     zip (names ,scores)
# --> ('c언어',100),
# --> ('파이썬',90),
# --> ('JAVA',80),

#c언어, 파이썬, java
#0,1,2
#enumerate(prog)

prog=['c언어','파이썬','java']
for item in enumerate(prog):
    print(item)
    
#range(10) : 0 1 2 3 4 5 6 7 8 9
for i in range(10) : 
    print(i, end=' ')

print()

#range(1,11) : 1 2 3 4 5 6 7 8 9 10
for i in range(1,11):
    print(i,end=' ')

print()

#range(2,21 2) : 2 4 6 8 10 12 14 16 18 20
for i in range(2,21,2):
    print(i,end=' ')
    
li = ['월','화','수','목','금','토','일']
print(li)
print('li의 요소의 개수 : {}'.format(len(li)))

scores=[100,90,65,80,70]
print(scores)
print(sorted(scores))

names = ['s1','s2','s3','s4','s5']

for student in zip(names, scores):
    print(student)
