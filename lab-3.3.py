Op = set(['+', '-', '', '/', '(', ')', '^'])
number = {'+':1, '-':1, '':2, '/':2, '^':3} 

def FiFo(expression): 
    product = [] 
    output = '' 
    for CRTer in expression:
        if CRTer not in Op: 
            output+= CRTer
        elif CRTer=='(': 
            product.append('(')
        elif CRTer==')':
            while product and product[-1]!= '(':
                output+=product.pop()
            product.pop()
        else: 
            while product and product[-1]!='(' and number[CRTer]<=number[product[-1]]:
                output+=product.pop()
            product.append(CRTer)
    while product:
        output+=product.pop()
    return output

expression = input('Enter infix expression ')
print("infix :",expression)
print("postfix :",FiFo(expression))