logo='''
 _____________________
|  _________________  |
| |             0.0 |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(logo)
def sum(a,b):
	return a+b
def subtraction(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	return a/b

operations={
	"+":sum,
	"-":subtraction,
	"*":multiply,
	"/":divide
}
##################################
def calculator():
  sayi1=float(input("What is the first number? : "))
  symbol=[]
  for i in operations:
  #print(i)
    symbol.append(i)
  will_finish=False
  while not will_finish:
    operation_symbol=input(f"Pick an operation -> {symbol} :")
    sayi2=float(input("What is the second number? : "))
    chosen_operation = operations[operation_symbol]
    answer=chosen_operation(sayi1,sayi2)

    print(f"{sayi1} {operation_symbol} {sayi2} = {answer} ")
    user_answer=input("If you want to continue with the result, Type 'yes'.\nIf you want to recalculate, Type 'no'.\nTo finish calculation type 'finish' ")
    if user_answer=="yes":
      sayi1=answer
    elif user_answer=="no":
      will_finish= False
      calculator()
    else:
      will_finish= True
      print("I'm tried. Good bye!")
##################################
calculator()
