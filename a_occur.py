input_name= input("enter a list of names seprated by spaces:")
names= input_name.split()
count_a =" ".join(names).lower().count('a')

print("total occurences of 'a':", count_a)