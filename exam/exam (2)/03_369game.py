'''
    1ë¶??„° 100ê¹Œì?? ?ˆ˜ë¥? ë°˜ë³µ?•˜?—¬ ì¶œë ¥?•˜ë©´ì„œ,
    ?ˆ˜ê°? 3 ?˜?Š” 6 ?˜?Š” 9 ?¸ ê²½ìš° ê·? ê°œìˆ˜ë§Œí¼ ë³?(*)?„ ì¶œë ¥?•˜?Š” ?”„ë¡œê·¸?¨?„ ?™„?„±?•˜?‹œ?˜¤.
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
    
    