def bin_addition_count(n, m):
    binary_n = bin(n)[2:]
    binary_m = bin(m)[2:]

    max_len = max(len(binary_n), len(binary_m))
    binary_n = binary_n.zfill(max_len)
    binary_m = binary_m.zfill(max_len)

    sum_result = [int(bit_n) + int(bit_m) for bit_n, bit_m in zip(binary_n, binary_m) if int(bit_n) + int(bit_m) == 1]

    return len(sum_result)

# Get input from the user
n = int(input("Enter the first integer: "))
m = int(input("Enter the second integer: "))

result = bin_addition_count(n, m)
print("Number of differing bits:", result)
