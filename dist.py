import json
import re 

def update_word_count(word, word_counts):
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

def main(inp):
    word_counts = {}

    try:
        with open('words.json', 'r') as file:
            word_counts = json.load(file)
    except FileNotFoundError:
        pass
    word_to_process = inp
    update_word_count(word_to_process, word_counts)

    with open('words.json', 'w') as file:
        json.dump(word_counts, file, indent=2)






def line():
    with open('chat.txt', 'r',encoding="utf8") as file:
        for w in list(file):
            x = w.partition(':')[2]
            y = x.partition(":")[2]
            phrase = y.partition(":")[2]
            p = re.findall(r"[\w']+|[.,!?;:#@/£$%&()]",phrase.lower(), re.UNICODE)
            for i in p:
                main(i)


def order():
    with open('words.json', 'r') as file:
        data = json.load(file)

        sort = sorted(data.items(), key=lambda x:x[1], reverse=True)

       

        with open('list.txt', 'w',encoding="utf8") as f:
            
            formatted = [str(item) + '\n' for item in sort]

            result = ''.join(formatted)
            f.write(result)


def line2():
    with open('chat.txt', 'r') as file:
        for w in list(file):
            x = w.partition(':')[2]
            y = x.partition(":")[2]
            phrase = y.partition(":")[2]
            p = phrase.lower().split()
            print(p)


def total():
    with open('words.json', 'r', encoding="utf8") as f:
        data = json.load(f)

        total = sum(data.values())


        print(total)


#line()
#order()
total()