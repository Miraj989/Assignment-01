# i = 1
# sum = 0
# while i <=100:
#     sum = sum+i
#     i+=1
number = int(input('enter a positive number: '))
while number < 0:
    number = int(input('enter a positive number'))
print('Square number of', number, 'is', number** 0.5)