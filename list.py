numbers = list(map(int, input("enter integers separated by spaces: ").split()))
positive_numbers =[]
for num in numbers:
 if num >0:
   positive_numbers.append(num)
print("original list:", numbers)
print("positive numbers:",positive_numbers)