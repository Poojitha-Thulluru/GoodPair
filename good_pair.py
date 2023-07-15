def is_good_pair_exists(num_array, target_value):
    for index in range(len(num_array) - 1):
        for element in range(index + 1, len(num_array)):
            if num_array[index] + num_array[element] == target_value:
                return 1
    return 0


try:
    nums_array = list(map(int, input("Enter Integers separated by space : ").split()))
    value = int(input("Enter an Integer : "))
    print(is_good_pair_exists(nums_array, value))
except ValueError:
    print("Invalid input. Please enter only integers")
