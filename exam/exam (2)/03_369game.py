'''
    1λΆ??° 100κΉμ?? ?λ₯? λ°λ³΅??¬ μΆλ ₯?λ©΄μ,
    ?κ°? 3 ?? 6 ?? 9 ?Έ κ²½μ° κ·? κ°μλ§νΌ λ³?(*)? μΆλ ₯?? ?λ‘κ·Έ?¨? ??±???€.
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
    
    