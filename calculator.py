# calculator.py
import math
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

def power(a, b):
    """计算 a 的 b 次方"""
    return a ** b

def sqrt(a):
    """计算 a 的平方根"""
    if a < 0:
        raise ValueError("不能对负数开平方根")
    return math.sqrt(a)

# 示例使用
if __name__ == "__main__":
    print("加法：", add(10, 5))
    print("减法：", subtract(10, 5))
    print("乘法：", multiply(10, 5))
    print("除法：", divide(10, 5))
    print("乘方：", power(2, 3))
    print("平方根：", sqrt(16)) 
