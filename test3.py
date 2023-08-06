def count_trailing_zeros(num):
    count = 0
    while num % 10 == 0:
        count += 1
        num //= 10
    return count

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("กรุณาใส่ตัวเลขที่ต้องการหา factorial: "))
fact = factorial(num)
trailing_zeros = count_trailing_zeros(fact)

print(f"{num}! = {fact} มีเลข 0 ต่อท้าย {trailing_zeros} ตัว")
