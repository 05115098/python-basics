def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            raise ValueError("除数不能为 0。")
        return a / b
    else:
        raise ValueError("不支持这个运算符。")


if __name__ == "__main__":
    print("简单计算器")

    try:
        first_number = float(input("请输入第一个数字："))
        operator = input("请选择运算（+、-、*、/）：")
        second_number = float(input("请输入第二个数字："))

        result = calculate(first_number, second_number, operator)
        print("计算结果：", result)
    except ValueError as error:
        print("错误：", error)
