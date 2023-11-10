# Calculate factorial of n
# fact(n) = 1*2*3*4*5 ... *n

n = 5
result = 1
for i in range(n):
    result = result * (i+1)

print(result)

# 5! = 1*2*3*4*5
# 5! = 4! * 5
# 4! = 3! * 4
# 3! = 2! * 3
# 2! = 1! * 2
# 1! = 0! * 1

# 0! = 1

# fact(n) = fact(n-1) * n

def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n

print(fact(5))
print(fact(10))

def count_digit(n):
    if n < 10:
        return 1
    return count_digit(n // 10) + 1

# count_digit(12345)
# count_digit(1234)
# count_digit(123) -> 1 + 1 + 1
# count_digit(12) -> 1 + 1
# count_digit(1) -> 1

print(count_digit(12345))
print(count_digit(99887766))

# "software" -> "erawtfos"
# "e ngineer" -> "reenign e"

# what if i know how to reverse "ngineer" uses the result and add e

def reverse_string_recursive(s):
    if len(s) == 1:
        return s
    reverse_of_substring = reverse_string_recursive(s[1:])
    return reverse_of_substring + s[0]

# reverse_string_recursive("engineer")
# reverse_string_recursive("ngineer")
# reverse_string_recursive("gineer")
# reverse_string_recursive("ineer")
# reverse_string_recursive("neer")
# reverse_string_recursive("eer") -> "re" + "e" -> "ree"
# reverse_string_recursive("er") -> "r" + "e" = "re"
# reverse_string_recursive("r") -> "r"

print(reverse_string_recursive("engineer"))
print(reverse_string_recursive("software"))



import copy

def gen_comb_list_recursive(list_set):
    if len(list_set) == 1:
        start_list = []
        for item in list_set[0]:
            start_list.append([item])
        return start_list
    comb_list_temp = gen_comb_list_recursive(list_set[0:-1])
    start_list = []
    for list_item in comb_list_temp:
        for val in list_set[-1]:
            temp_item = copy.deepcopy(list_item)
            temp_item.append(val)
            start_list.append(temp_item)
    return start_list

print("Test gen_comb_list")
x = [1, 2, 3]
y = [4, 5]
z = [6, 7, 8]
u = [9, 10]
comb_list = gen_comb_list_recursive([x]) 
print(comb_list)
comb_list = gen_comb_list_recursive([x, y])
print(comb_list)
# comb_list = gen_comb_list_recursive([x, y, z])
# print(comb_list, len(comb_list), [x, y, z])