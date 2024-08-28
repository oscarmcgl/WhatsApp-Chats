import json
import re 

total_words = 0
total_msgs = 0


def update_word_count(word, word_counts):
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


def analyse(word):
    word_counts = {}

    try: #opening file to store word counts
        with open('words.json', 'r') as file:
            word_counts = json.load(file)
    except FileNotFoundError:
        print("Could not find file words.json. Starting with an empty dictionary.")
        with open('words.json', 'w') as file:
            json.dump(word_counts, file, indent=2)

    update_word_count(word, word_counts)
    with open('words.json', 'w') as file:
        json.dump(word_counts, file, indent=2)


def open_chat(): 
    global total_words, total_msgs
    with open('chat.txt', 'r',encoding="utf8") as file:
        for w in list(file):
            x = w.partition(':')[2]
            y = x.partition(":")[2]
            phrase = y.partition(":")[2]
            p = re.findall(r"[\w']+|[.,!?;:#@/£$%&()]",phrase.lower(), re.UNICODE)
            total_msgs += 1
            for word in p:
                total_words += 1
                analyse(word.lower())


def order():
    with open('words.json', 'r') as file:
        data = json.load(file)

        sort = sorted(data.items(), key=lambda x:x[1], reverse=True)

       

        with open('list.txt', 'w',encoding="utf8") as f:
            
            formatted = [str(item) + '\n' for item in sort]

            result = ''.join(formatted)
            f.write(result)


def common_words():
    common = []
    with open("list.txt", "r") as file:
        data = file.readlines()
        for line in data[:10]:
            word = line.split(",")[0]
            word = word.split("'")[1]
            num = line.split(",")[1]
            num = num.split(")")[0]
            common.append(f"\n{word} - {num}")
    
    return ''.join(common)

def results():
    print(f"Your Chat Results.\nTotal Words: {total_words}\nTotal Messages: {total_msgs}\n\nYour top 10 words were: {common_words()}.")
    choice = input("1. More Detailed Results\n2. Restart\n3. Exit")
    if choice == "1":
        detailed()
    elif choice == "2":
        menu()
    else:
        exit()

def detailed():
    print("Let's see more top words. How many of the top words would you like to view?")
    try:
        num = int(input("Enter a number: "))
    except:
        print("Please enter a number.")
        detailed()
    common = []
    with open("list.txt", "r") as file:
        with open("list.txt", "r") as file:
            data = file.readlines()
            for line in data[:num]:
                word = line.split(",")[0]
                word = word.split("'")[1]
                num = line.split(",")[1]
                num = num.split(")")[0]
                common.append(f"\n{word} - {num}")
    
    print (f"Your top {num} words were: {''.join(common)}")

    choice = input("1. Restart\n2. Exit")
    if choice == "1":
        menu()
    else:
        exit()



def menu():
    choice = input("1. Analyse Chat\n2. Exit")
    if choice == "1":
        start()
    else:
        exit()


def start():
    try:
        with open('chat.txt', 'w') as file:
            pass
    
        print("Analyzing chat. Please wait...")
        open_chat()
        order()
        results()
    except FileNotFoundError:
        print("Could not find file chat.txt. Please place the file in the same directory as this script. How to get file? (y/n)")
        if input().lower() == "y":
            print("Choose export chat from whatsapp. Place in the same directory as this script. Ensure it is named chat.txt")
            
        menu()
    except PermissionError:
        print("Please close the chat.txt file and try again.")
        menu()
    except Exception as e:
        print(f"An error occured: {e}")
        menu()



print("Welcome to WhatsApp Chat Analyser")
menu()