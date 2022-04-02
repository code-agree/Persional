def calculate(s: str) -> int:
    def helper(s: list) -> int:
        stack = []
        sign = '+'
        num = 0
        while len(s) > 0:
            c = s.pop(0)
            c = str(c)
            if c.isdigit():
                num = 10 * num + int(c)
            if c == '(':
                num = helper(s)
            if (not c.isdigit() and c != ' ') or len(s) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    # python 除法向 0 取整的写法
                    stack[-1] = int(stack[-1] / float(num))
                num = 0
                sign = c
            if c == ')':
                break
        return sum(stack)
    # 需要把字符串转成列表方便操作
    return helper(list(s))




# res = 3*(4-5/5)-6
res = "3*(6-3)-3/1"
# res = [3*(4-5/5)-6]
print(calculate(res))