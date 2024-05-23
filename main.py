from local_colorama import *
print("Hello, to create a list and to input your inputs, devide each value by an ', '.")
listthing=input('list: '); things=listthing.split(', ')
thingy=input('inputs: '); thingys=thingy.split(', ')
#print(f'{things}\n{thingys}\n')
for i in range(len(thingys)):
    if thingys[i] in things: print(Fore.GREEN + 'Yes' + Fore.WHITE + ': \'' + Fore.BLUE + f'{thingys[i]}' + Style.RESET_ALL+ '\' Is in the list') 
    else: print(Fore.RED + ' No' + Fore.WHITE + ': \'' + Fore.BLUE + f'{thingys[i]}' + Style.RESET_ALL + '\' Is not in the list')
