'''
   ���� ��ȯ
   : ���̽㿡���� �ϳ��� ��ȯ���� ó���� �� �ְ�,
     ���� ���� ��ȯ���� ó���� �� �ִ�.
     
    def �Լ��� (�Ű�����):
        ���๮
        ���๮
        return(��1), (��2), (��3),...
        
'''

def calculate(*args):
    result1 = sum(args)
    result2 = sum(args)/len(args)
    result3 = max(args)
    result4 = min(args)
    return result1, result2, result3, result4
#��ȯ������ Ʃ�÷� �����Ͽ� ��ȯ�Ѵ�

a,b,c,d = calculate(1,2,3,4,5)
result = calculate(1,2,3,4,5)

print('a : {}',format(a))
print('b : {}',format(b))
print('c : {}',format(c))
print('d : {}',format(d))

print('result : {}'.format(result))
    
    