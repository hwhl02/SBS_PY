''''''
#3. len() �Լ�
#: �Լ��� ���޵� ��ü�� ����(����)�� ��ȯ�ϴ� �Լ�
#ex) li = [1,2,3,4]
#len(li) --> 4

#4. sorted() �Լ�
#: �ݺ������� ��ü�� ������������ ������ ��� ��ȯ�ϴ� �Լ�
#ex) li=[10,3,9,2,5]
#sorted(li) --> [2,3,5,9,10]

#5. zip()�Լ�
# : ���� ���� �ݺ������� ��ü���� Ʃ�÷� ��� ��ȯ�ϴ� �Լ�
# ex) names = ['c���','���̽�','JAVA']
#     scores = [100,90,80]
#     zip (names ,scores)
# --> ('c���',100),
# --> ('���̽�',90),
# --> ('JAVA',80),

#c���, ���̽�, java
#0,1,2
#enumerate(prog)

prog=['c���','���̽�','java']
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
    
li = ['��','ȭ','��','��','��','��','��']
print(li)
print('li�� ����� ���� : {}'.format(len(li)))

scores=[100,90,65,80,70]
print(scores)
print(sorted(scores))

names = ['s1','s2','s3','s4','s5']

for student in zip(names, scores):
    print(student)
