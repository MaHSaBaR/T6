def calculate_sum():
    numbers = []
    num = 0
    while num != 'end':
        numbers.append(int(num))
        num = input()
    return sum(numbers)

def calculate_average():
    numbers = []
    num = 0
    while num != 'end':
        numbers.append(int(num))
        num = input()
    return round(sum(numbers) / (len(numbers) - 1), 2)

def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calculate_gcd_multiple():
    num = input()
    result = int(num)
    while num != 'end':
        result = calculate_gcd(result, int(num))
        num = input()
    return result

def calculate_lcd():
    numbers = []
    num = input()
    while num != 'end':
        numbers.append(int(num))
        num = input()
    i = 1
    while True:
        if all(i % n == 0 for n in numbers):
            print(i)
            break
        i += 1

def find_max():
    numbers = []
    num = input()
    while num != 'end':
        numbers.append(int(num))
        num = input()
    return max(numbers)

def find_min():
    numbers = []
    num = input()
    while num != 'end':
        numbers.append(int(num))
        num = input()
    return min(numbers)

def main():
    command = input()
    if command == 'sum':
        print(calculate_sum())
    elif command == 'average':
        print(calculate_average())
    elif command == 'gcd':
        print(calculate_gcd_multiple())
    elif command == 'lcd':
        calculate_lcd()
    elif command == 'min':
        print(find_min())
    elif command == 'max':
        print(find_max())
    else:
        print('Invalid command')

if __name__ == "__main__":
    main()
