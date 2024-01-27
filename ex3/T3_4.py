def find_indices_with_sum(nums, target_sum):
    indices = set()
    seen = set()

    for i, x in enumerate(nums):
        complement = target_sum - int(x)
        complement_str = str(complement)

        if complement_str in seen:
            indices.add((i, nums.index(complement_str)))
        seen.add(x)

    return sorted(indices)

if __name__ == "__main__":
    input_str = input().strip()
    target = int(input())

    nums = input_str.split(' ')
    indices = find_indices_with_sum(nums, target)

    if not indices:
        print('Not Found!')
    else:
        for i, j in indices:
            print(i + j)
