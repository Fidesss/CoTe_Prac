def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return False
                break
    else:
        if stack:
            return False
        else:
            return True