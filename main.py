from local_colorama import *
import os
loadedfromdatabase=False
def case_sesitive(database, searchterm):
    if int(input('Do you want the search term and database to be non case sensetive? ' + Fore.YELLOW + '(1: yes, 2: no)' + Fore.RESET + '\n')) == 1:
        case_sesitive=True
        for i in range(len(database)): database[i] = database[i].lower()
        for i in range(len(searchterm)): test = searchterm[i]; searchterm[i] = searchterm[i].lower() + f" ({test})"
    else: case_sesitive = False; pass
    return database, searchterm, case_sesitive
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
database, searchterm, case_sesitive = case_sesitive(database, searchterm)
for i in range(len(searchterm)):
    if case_sesitive and searchterm[i].split(f' ({searchterm[i].split(" (")[1].rstrip(")")})')[0] in database: print(Fore.GREEN + 'Yes' + Fore.WHITE + ': \'' + Fore.BLUE + f'{searchterm[i]}' + Style.RESET+ '\' Is in the list') 
    elif not case_sesitive and searchterm[i] in database: print(Fore.GREEN + 'Yes' + Fore.WHITE + ': \'' + Fore.BLUE + f'{searchterm[i]}' + Style.RESET+ '\' Is in the list') 
    else: print(Fore.RED + ' No' + Fore.WHITE + ': \'' + Style.REVERSE + Fore.BLUE + f'{searchterm[i]}' + Style.RESET + '\' Is not in the list')

if not loadedfromdatabase: save_database(database)
