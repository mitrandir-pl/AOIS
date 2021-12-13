import random


LENGTH_OF_WORD = 8


def get_random_word():
    out = ""
    for _ in range(LENGTH_OF_WORD):
        out += str(int(random.randint(0, 100)%2))
    return out


def recursive_find(argument, word, i, mask=0):
    temp = {}
    temp1 = {}
    if i + 1 == (len(word) - mask):
        temp1["trigger_right"] = False
        temp1["trigger_left"] = False
    else:
        temp1 = recursive_find(argument, word, i + 1, mask)
    if (temp1["trigger_right"] or (argument[i] == "0" and word[i] == "1" and not(temp1["trigger_left"]))):
        temp["trigger_right"] = True
    else:
        temp["trigger_right"] = False
    if (temp1["trigger_left"] or (argument[i] == "1" and word[i] == "0" and not(temp1["trigger_right"]))):
        temp["trigger_left"] = True
    else:
        temp["trigger_left"] = False
    return temp


def nearest(book, word):
    lower_books, higher_books = [], []
    for i in book:
        for index in range(len(word)):
            if int(word[index]) == int(i[index]):
                continue
            elif int(word[index]) > int(i[index]):
                lower_books.append(i)
                break
            elif int(word[index]) < int(i[index]):
                higher_books.append(i)
                break
    highest = lower_books[0]
    for i in lower_books[1:]:
        for index in range(len(i)):
            if int(highest[index]) == int(i[index]):
                continue
            elif int(highest[index]) > int(i[index]):
                break
            elif int(highest[index]) < int(i[index]):
                highest = i
    print(highest)
    lowest = higher_books[0]
    for i in higher_books[1:]:
        for index in range(len(i)):
            if int(lowest[index]) == int(i[index]):
                continue
            elif int(lowest[index]) < int(i[index]):
                break
            elif int(lowest[index]) > int(i[index]):
                lowest = i
    print(lowest)
    return True


def main():
    book = []
    num_of_books = 30
    for i in range(num_of_books):
        boof = get_random_word()
        book.append(boof)
        print(f"[{i+1}] {boof}")
    try:
        word_to_search = input("Enter aword to search: ")
        mask = int(input("Enter mask: "))
        for index, i in enumerate(book):
            temp = recursive_find(word_to_search, i, 0, mask) 
            print(f"[{index+1}] {int(temp['trigger_right'])} {int(temp['trigger_left'])}")
        number = int(input("Input number: "))
        nearest(book, book[number])
    except ValueError:
        print("Invalid value")
    except IndexError:
        print("Invalid index")
    except Exception:
        print("something wrong")

if __name__ == '__main__':
    main()
