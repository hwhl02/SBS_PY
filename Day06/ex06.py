
# 리스트 내포 
# : 리스트 내부에 for문을 사용하여
#   리스트 요소를 효율적으로 저장하는 방식

# 문법
# 리스트 = [표현삭 for 변수 in [컬렉션]

# [1,2,3,4,5] --> [2,4,6,8,10]
# 2배씩 값을 변경

a = [1,2,3,4,5]
li= [ n*2 for n in a]
print('li : ', li)

