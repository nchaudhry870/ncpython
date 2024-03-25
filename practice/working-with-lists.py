numbers = list(range(1,6))
print(numbers)
print(range(1,9))

multiples_of_three = []
for value in range(1,11):
    multiples_of_three.append(value*3)

print(multiples_of_three)

print(list(range(1,11)))

multiples_of_three_through_list_comprehension = [value*3 for value in range(1,13)]

print(multiples_of_three_through_list_comprehension)

#practice min, max, sum
print(max(multiples_of_three_through_list_comprehension))

#program to sum first 100 numbers

nums = list(range(1,101))
print(sum(nums))