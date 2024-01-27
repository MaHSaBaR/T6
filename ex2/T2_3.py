def convert_to_base(decimal_num, base):
    result = ''
    while decimal_num != 0:
        remainder = decimal_num % base
        decimal_num = int((decimal_num - remainder) / base)
        result += str(remainder)
    result = result[::-1]
    return result

def calculate_numerator_sum():
    total_sum = 0
    while True:
        inputs = list(map(int, input().split()))
        if inputs == [-1, -1]:
            break
        num, base = inputs
        if base > 9 or base < 2:
            print('Invalid base!')
        else:
            base_result = convert_to_base(numerator(num), base)
            total_sum += int(base_result)

    return total_sum

def numerator(n):
    a = 0
    for i in range(1, n+1):
        if n % i == 0:
            a += i
    return a

if __name__ == "__main__":
    result = calculate_numerator_sum()
    print(result)
