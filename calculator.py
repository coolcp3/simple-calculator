# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# 示例使用
if __name__ == "__main__":
    print("加法：", add(10, 5))
    print("减法：", subtract(10, 5))
    print("乘法：", multiply(10, 5))
    print("除法：", divide(10, 5))