'''
    1�??�� 100까�?? ?���? 반복?��?�� 출력?��면서,
    ?���? 3 ?��?�� 6 ?��?�� 9 ?�� 경우 �? 개수만큼 �?(*)?�� 출력?��?�� ?��로그?��?�� ?��?��?��?��?��.
'''

for i in range(1,101):
    ten = int( i / 10 )
    one = int( i % 10 )
    ten369 = ( ten == 3 or ten == 6 or ten == 9 )
    one369 = ( one == 3 or one == 6 or one == 9 )
    if ten369 and one369:
        print("**")
    elif ten369 or one369:
        print("*")
    else:
        print(i)
    
    