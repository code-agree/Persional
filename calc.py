def calculate(input: str) -> int:
    # 合法值
    typeext = ['+', '-', '*', '/', '(', ')']
    error_num = 0
    for i in range(len(input)):
        num_single = input[i]
        if not num_single.isdigit() and num_single not in typeext:
            error_num += 1
    if error_num != 0:
        return "ERROR"
    elif error_num == 0:
        def helper(input: list) -> int:
            stack = []
            sign = '+'
            num = 0
            while len(input) > 0:
                c = input.pop(0)
                c = str(c)
                if c.isdigit():
                    num = 10 * num + int(c)
                if c == '(':
                    num = helper(input)
                if (not c.isdigit() and c != ' ') or len(input) == 0:
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
            sum_res = sum(stack)
            if sum_res >= 2**31 - 1 or sum_res <= - 2**31 - 1:
                print("OVERFLOW")
            else:
                return sum(stack)
    # 需要把字符串转成列表方便操作
    return helper(list(input))


res = "(4+3)*5+9-7"
print(calculate(res))


# 计算器，向下取整