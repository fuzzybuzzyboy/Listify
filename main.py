from local_colorama import *
import os
loadedfromdatabase=False
def load_database():
    global database, loadedfromdatabase
    with open('database.txt', 'r') as f: displaydata = f.read().split(', ')
    if int(input('Do you want to read your database from a file? ' + Fore.YELLOW + '(1: yes, 2: no)' + Fore.RESET+ '\nFile contains: ' + Fore.MAGENTA + f'{displaydata}' + Fore.RESET + '\n')) == 1:
        with open('database.txt', 'r') as f: database = f.read().split(', '); loadedfromdatabase=True
    else: pass
def save_database(database):
    if int(input('\nDo you want to save your database? (1: yes, 2: no)\n')) == 1:
        if os.path.exists('database.txt'): os.remove('database.txt')
        with open('database.txt', 'a') as f: f.write(', '.join(database)); f.close()
    else: exit()
print("Hello, to create a list and to input your inputs, devide each value by an ', '.")
if os.path.exists('database.txt'): load_database()
if loadedfromdatabase == False: database=input('Database: ').split(', ')
else: pass
searchterm=input('Search term: ').split(', ')# ; print(f'{things}\n{thingys}\n')
for i in range(len(searchterm)):
    if searchterm[i] in database: print(Fore.GREEN + 'Yes' + Fore.WHITE + ': \'' + Fore.BLUE + f'{searchterm[i]}' + Style.RESET+ '\' Is in the list') 
    else: print(Fore.RED + ' No' + Fore.WHITE + ': \'' + Style.REVERSE + Fore.BLUE + f'{searchterm[i]}' + Style.RESET + '\' Is not in the list')

if loadedfromdatabase==False: save_database(database)
