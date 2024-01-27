def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

def binomial_coefficient(n, k):
    return int(factorial(n) / (factorial(n - k) * factorial(k)))

def generate_pascal_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [str(binomial_coefficient(i, j)) for j in range(i + 1)]
        triangle.append(' '.join(row))
    return triangle

def main():
    n = int(input("Enter the number of rows for Pascal's Triangle: "))
    pascal_triangle = generate_pascal_triangle(n)

    for row in pascal_triangle:
        print(row)

if __name__ == "__main__":
    main()
