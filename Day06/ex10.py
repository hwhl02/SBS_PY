
# 짝수의 합계

a=1
while a <= 20:
    
    # 홀수인 경우
    if(a%2 ==1):
        continue
    
    sum += a
    a = a+1
    
print('1~20 사이의 짝수의 합계 : {}'.format(sum))