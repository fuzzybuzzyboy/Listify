from local_colorama import *; import os; used_texts = []; print("Hello, to create a list and to input your inputs, divide each value by an ','.")
def case_sesitive(database, searchterm):
    if int(input(Fore.RESET + 'Do you want the search term and database to be non case sensetive? ' + Fore.YELLOW + '(1: yes, 2: no)' + Fore.RESET + '\n' + Fore.BLUE)) == 1:
        case_sesitive=True
        for i in range(len(database)): database[i] = database[i].capitalize()
        for i in range(len(searchterm)): test = searchterm[i]; searchterm[i] = searchterm[i].capitalize() + f" ({test})"
    else: case_sesitive = False; pass
    print('\b\b' + Fore.RESET); return database, searchterm, case_sesitive
def load_database():
    global database
    with open('database.txt', 'r') as f: displaydata = f.read()
    if int(input('Do you want to read your database from a file? ' + Fore.YELLOW + '(1: yes, 2: no)' + Fore.RESET+ '\nFile contains: ' + Fore.MAGENTA + f'{displaydata}' + Fore.RESET + '\n' + Fore.BLUE)) == 1:
        with open('database.txt', 'r') as f: database = f.read().split(', '); return True
    else: return
def save_database(database):
    if int(input('\nDo you want to save your database? (1: yes, 2: no)\n' + Fore.BLUE)) == 1:
        if os.path.exists('database.txt'): os.remove('database.txt')
        with open('database.txt', 'a') as f: f.write(', '.join(database)); f.close()
    else: exit()
if os.path.exists('database.txt'): loadedfromdatabase = load_database()
database=input(Fore.RESET + 'Database: ' + Fore.BLUE).split(',') if not loadedfromdatabase else database
searchterm=input(Fore.RESET + 'Search term: ' + Fore.BLUE).split(',')
if int(input(Fore.RESET + 'Do you want to allow duplicates? ' + Fore.YELLOW + '(1: yes, 2: no)' + '\n' + Fore.BLUE)) == 1: allow_duplicates = True
else: allow_duplicates = False
database, searchterm, case_sesitive = case_sesitive(database, searchterm)
# print(f'{len(searchterm)} search terms\n{len(database)} database words.\n')
for i in range(len(searchterm)):
    if case_sesitive and searchterm[i].split(f' ({searchterm[i].split(" (")[1].rstrip(")")})')[0] in database and searchterm[i].split(f' ({searchterm[i].split(" (")[1].rstrip(")")})')[0] not in used_texts: ignore=searchterm[i].split(f' ({searchterm[i].split(" (")[1].rstrip(")")})')[0]; print(Fore.GREEN + 'Yes' + Fore.WHITE + ': \'' + Fore.BLUE + f'{searchterm[i]}' + Style.RESET+ f'\' Is in the list (in database spot {database.index(ignore)+1})') 
    elif not case_sesitive and searchterm[i] in database and searchterm[i] not in used_texts: print(Fore.GREEN + 'Yes' + Fore.WHITE + ': \'' + Fore.BLUE + f'{searchterm[i]}' + Style.RESET+ f'\' Is in the list (in database spot {database.index(searchterm[i])+1})') 
    else:
        if case_sesitive: print(Fore.RED + ' No' + Fore.WHITE + ': \'' + Style.REVERSE + Fore.BLUE + f'{searchterm[i]}' + Style.RESET + Fore.RESET + '\' Is not in the list') if searchterm[i].split(f' ({searchterm[i].split(" (")[1].rstrip(")")})')[0] not in used_texts else None
        else: print(Fore.RED + ' No' + Fore.WHITE + ': \'' + Style.REVERSE + Fore.BLUE + f'{searchterm[i]}' + Style.RESET + Fore.RESET + '\' Is not in the list') if searchterm[i] not in used_texts else None
    if case_sesitive and searchterm[i].split(f' ({searchterm[i].split(" (")[1].rstrip(")")})')[0] not in used_texts and not allow_duplicates:
        used_texts.append(searchterm[i].split(f' ({searchterm[i].split(" (")[1].rstrip(")")})')[0]) if case_sesitive else used_texts.append(searchterm[i])
    else: pass
if not loadedfromdatabase: save_database(database)
