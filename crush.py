import sys

# BANNER
print("""
   █████████  ███████████   █████  █████  █████████  █████   █████
  ███░░░░░███░░███░░░░░███ ░░███  ░░███  ███░░░░░███░░███   ░░███ 
 ███     ░░░  ░███    ░███  ░███   ░███ ░███    ░░░  ░███    ░███ 
░███          ░██████████   ░███   ░███ ░░█████████  ░███████████ 
░███          ░███░░░░░███  ░███   ░███  ░░░░░░░░███ ░███░░░░░███ 
░░███     ███ ░███    ░███  ░███   ░███  ███    ░███ ░███    ░███ 
 ░░█████████  █████   █████ ░░████████  ░░█████████  █████   █████
  ░░░░░░░░░  ░░░░░   ░░░░░   ░░░░░░░░    ░░░░░░░░░  ░░░░░   ░░░░░
  
[!] Made by: github.com/titiomathias/ [!]
[+] Wordlist maker tool to Pentest Security [+]
""")


# MENU
def how_to_use():
    print("""HOW TO USE THE CRUSH - Let's match the perfect password to you <3

Use: crush.py -kw <"your keywords or wordlist"> -wordlist <use your personal chars or combinations> -s <saveyourfiles>

Example: crush.py "user; admin; elliot" -s wordlist.txt -> This command will make a keywords combination using the default script list and save like "wordlist.txt".

Some useful arguments:
-h          |   You can access the menu! It's here!
-s          |   You can save your wordlist. Example: crush.py -kw mywords.txt -s mywordlist.txt
-kw         |   You can use specific keywords or wordlists. Example: crush.py -kw "user;User;birthday" -s wordlist_personal.txt (IF YOU ARE GOING TO USE SPECIFIC WORDS, USE QUOTES!)
-wordlist   |   You can use a wordlist with specific combinations for your keywords. Example: crush.py -kw "user;User;Users" -wordlist streets.txt -s new_wordlist.txt
""")


# FUNCTION TO MAKE DEFAULT COMBINATIONS.
def keywordlist(lista):
    with open("default_wordlist_combination.txt") as default_file:
        default = default_file.readlines()

    with open("special_chars.txt") as special_chars_file:
        special_chars = special_chars_file.readlines()

    final_list = []
    for item in lista:
        for default_item in default:
            new_item = item.rstrip("\n") + default_item.rstrip("\n")
            final_list.append(new_item)
    for i in lista:
        for char in special_chars:
            for default_item in default:
                new_item = i.rstrip("\n") + char.rstrip("\n") + default_item.rstrip("\n")
                final_list.append(new_item)
    final_list_ofc = list(set(final_list))
    final_list_ofc.sort()
    return final_list_ofc


# FUNCTION TO MAKE PERSONAL COMBINATIONS.
def personal_keywordlist(lista, wordlist):
    final_list = []
    for item in lista:
        for word in wordlist:
            new_item = item.rstrip("\n")+word.rstrip("\n")
            final_list.append(new_item)
    final_list_ofc = list(set(final_list))
    final_list_ofc.sort()
    return final_list_ofc


# READING THE ARGUMENTS.
arg = sys.argv
index = len(arg)-1


# JUST EXECUTING THE SCRIPT, THE HELP_MENU WILL BE OPENED.
if index == 0:
    how_to_use()

elif index == 1:
    how_to_use()

# MAKING WORDLISTS TO BE PRINTED IN THE SCREEN.
elif index == 2:
    if arg[1] == "-kw":
        if ".txt" in arg[2]:
            with open(arg[2]) as keylist:
                keywords = keylist.readlines()
            resultado = keywordlist(keywords)
            print("Let's match the perfect password to you! <3\n")
            for item in resultado:
                print(item)
        else:
            keywords = arg[2].replace(" ", "").split(";")
            resultado = keywordlist(keywords)
            print("Let's match the perfect password to you! <3\n")
            for item in resultado:
                print(item)
    elif arg[1] == "-h":
        how_to_use()
    elif arg[1] == "-s":
        print("\nNo data to save.\n")
    elif arg[1] == "-wordlist":
        print("\nYou don't need to use '-wordlist' for use a keywords list!\n")
        how_to_use()
    else:
        print("Invalid! MISSING OR INVALID ARGUMENTS! Use crush.py -h")

# ARGUMENTS ARE USUALLY IN PAIRS.
elif index == 3:
    print("Invalid! MISSING ARGUMENTS! Use crush.py -h")


# MAKING CUSTOMIZATION OR SAVING FILES.
elif index == 4:
    if arg[1] == "-kw":
        if ".txt" in arg[2] and arg[3] == "-wordlist":
            with open(arg[2]) as keylist:
                keywords = keylist.readlines()

            with open(arg[4]) as wordlist:
                personal = wordlist.readlines()

            resultado = personal_keywordlist(keywords, personal)
            print("Let's match the perfect password to you! <3\n")
            for item in resultado:
                print(item)

        elif ".txt" in arg[2] and arg[3] == "-s":
            with open(arg[2]) as keylist:
                keywords = keylist.readlines()
                resultado = keywordlist(keywords)
                print("Let's match the perfect password to you! <3\n")
                arquivo_final = open(arg[4], "w")
                for linha in resultado:
                    arquivo_final.write(linha + "\n")
                arquivo_final.close()
                print("File saved!")

        elif ".txt" not in arg[2] and arg[3] == "-wordlist":
            keywords = arg[2].replace(" ", "").split(";")
            with open(arg[4]) as wordlist:
                personal = wordlist.readlines()

            resultado = personal_keywordlist(keywords, personal)
            print("Let's match the perfect password to you! <3\n")
            for item in resultado:
                print(item)

        elif ".txt" not in arg[2] and arg[3] == "-s":
            keywords = arg[2].replace(" ", "").split(";")
            resultado = keywordlist(keywords)
            print("Let's match the perfect password to you! <3\n")
            arquivo_final = open(arg[4], "w")
            for linha in resultado:
                arquivo_final.write(linha + "\n")
            arquivo_final.close()
            print("File saved!")

        else:
            print("Invalid! MISSING OR INVALID ARGUMENTS! Use crush.py -h")

    elif arg[1] == "-h":
        how_to_use()
    elif arg[1] == "-s":
        print("\nNo data to save.\n")
    elif arg[1] == "-wordlist":
        print("\nYou don't need to use '-wordlist' for use a keywords list!\n")
        how_to_use()
    else:
        print("Invalid! MISSING OR INVALID ARGUMENTS!")
        print("Use crush.py -h")


# ARGUMENTS ARE USUALLY IN PAIRS.
elif index == 5:
    print("Invalid! MISSING ARGUMENTS! Use crush.py -h")


# MAKING CUSTOMIZATION AND SAVING FILES.
elif index == 6:
    if arg[1] == "-kw":
        if ".txt" in arg[2] and arg[3] == "-wordlist" and arg[5] == "-s":
            with open(arg[2]) as keylist:
                keywords = keylist.readlines()

            with open(arg[4]) as wordlist:
                personal = wordlist.readlines()

            resultado = personal_keywordlist(keywords, personal)

            print("Let's match the perfect password to you! <3\n")

            arquivo_final = open(arg[6], "w")
            for linha in resultado:
                arquivo_final.write(linha + "\n")
            arquivo_final.close()
            print("File saved!")

        elif ".txt" not in arg[2] and arg[3] == "-wordlist" and arg[5] == "-s":
            keywords = arg[2].replace(" ", "").split(";")
            with open(arg[4]) as wordlist:
                personal = wordlist.readlines()

            resultado = personal_keywordlist(keywords, personal)

            print("Let's match the perfect password to you! <3\n")

            arquivo_final = open(arg[6], "w")
            for linha in resultado:
                arquivo_final.write(linha + "\n")
            arquivo_final.close()
            print("File saved!")

        else:
            print("Invalid! MISSING OR INVALID ARGUMENTS! Use crush.py -h")

    elif arg[1] == "-h":
        how_to_use()
    elif arg[1] == "-s":
        print("\nNo data to save.\n")
    elif arg[1] == "-wordlist":
        print("\nYou don't need to use '-wordlist' for use a keywords list!\n")
        how_to_use()
    else:
        print("Invalid! MISSING OR INVALID ARGUMENTS! Use crush.py -h")

# A MAXIMUM OF 6 ARGUMENTS ARE ALLOWED.
else:
    print("Invalid! TOO MANY ARGUMENTS!\n")
    how_to_use()