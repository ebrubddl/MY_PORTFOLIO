import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
a=len(names)
will_pay=random.randint(0,a-1) 
person = names[will_pay]
print(person)
