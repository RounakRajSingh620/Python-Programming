from random import randint
def get_random_ints(count, begin, end):
    print("get_random_ints start")
    list_numbers = []
    for x in range(0, count):
        list_numbers.append(randint(begin, end))
        print("get_random_ints end")
    return list_numbers
print(type(get_random_ints))
nums = get_random_ints(10, 0, 100)
print(nums)
