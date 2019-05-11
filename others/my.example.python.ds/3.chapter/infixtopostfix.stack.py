#!/usr/bin/env python
'''
Create an empty stack called opstack for keeping operators. 
Create an empty list for output.
Convert the input infix string to a list by using the string method split.
Scan the token list from left to right.

If the token is an operand, append it to the end of the output list.
If the token is a left parenthesis, push it on the opstack.
If the token is a right parenthesis, 
  pop the opstack until the corresponding left parenthesis is removed. 
  Append each operator to the end of the output list.
If the token is an operator, *, /, +, or -, push it on the opstack. 
  However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
When the input expression has been completely processed, check the opstack
  . Any operators still on the stack can be removed and appended to the end of the output list.

'''
from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        elif token in "+-*/":
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)
        else:
          raise ValueError ('Unrecognized token ' + token + "!")

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2): 
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    else: 
      raise RuntimeError ('Unrecognized token ' + token + "!")

        
def   printInfixToPostfix(s):
  print( infixToPostfix (s) )

def infixEvaluation(s): 
  """
    3.3 Implement a direct infix evaluator that combines the functionality of infix-to-postfix conversion and 
    the postfix evaluation algorithm. Your evaluator should process infix tokens from left to right and 
    use two stacks, one for operators and one for operands, to perform the evaluation.
  """
  t = infixToPostfix( s )
  print ( "%s = %d" %(s, postfixEval(t)) )


def main ():
  printInfixToPostfix("A * B + C * D")                          #
  printInfixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )")  #
  printInfixToPostfix("( A + B ) * ( C + D )")                  # 'A B + C D + *'
  printInfixToPostfix("( A + B ) * C")                          # 'A B + C *'
  printInfixToPostfix("A + B * C")                              # 'A B C * +'
  print(postfixEval('7 8 + 3 2 + /'))                           #

if __name__ == "__main__":
  infixEvaluation    ( "( 7 & 8 ) / ( 3 + 2 )")                           # 
  #main()
