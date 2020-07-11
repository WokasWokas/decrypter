"""
Импортируем модули, для корректной работы программы
"""
import sys, os, random
random.seed(version=2)
""" 
Всё, что находится ниже - параметры (изменять не рекомендуется)
"""
keys = []
cryptLetters = {}
encryptLetters = {}
""" 
Всё, что находится выше - параметры (изменять не рекомендуется)
 
 
Всё, что находится ниже - константа
"""
words = [" ", "1", "2", "3", '4', '5', '6', '7', '8', '9', '0',
         "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]",
         "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "|", "z",
         "x", "c", "v", "b", "n", "m", ",", ".", "/", "Q", "W", "E",
         "R", "T", "Y", "U", "I", "O", "P", "{", "}", "A", "S", "D",
         "F", "G", "H", "J", "K", "L", ":", "Z", "X", "C", "V", "B",
         "N", "M", ",", "?", "!", "@", "#", "$", "%", "^", "&", "*",
         "(", ")", "_", "-", "=", "+", "'", "й", "ц", "у", "к", "е",
         "н", "г", "ш", "щ", "з", "х", "ъ", "ф", "ы", "в", "а", "п",
         "р", "о", "л", "д", "ж", "э", "я", "ч", "с", "м", "и", "т",
         "ь", "б", "ю", "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ",
         "З", "Х", "Ъ", "Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д",
         "Ж", "Э", "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю"]
codeWords = ["1", "2", "3", '4', '5', '6', '7', '8', '9', '0', "q",
            "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]",
            "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "|",
            "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "Q",
            "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}",
            "A", "S", "D", "F", "G", "H", "J", "K", "L", ":", "Z",
            "X", "C", "V", "B", "N", "M", ",", "?", "!", "@", "#",
            "$", "%", "^", "&", "*", "(", ")", "_", "й", "ц", "у",
            "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "ф", "ы",
            "в", "а", "п", "р", "о", "л", "д", "ж", "э", "я", "ч",
            "с", "м", "и", "т", "ь", "б", "ю", "Й", "Ц" "У", "К",
            "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ", "Ф", "Ы", "В",
            "А", "П", "Р", "О", "Л", "Д", "Ж", "Э", "Я", "Ч", "С",
            "М", "И", "Т", "Ь", "Б", "Ю"]
""" 
Всё, что находится выше - константа
"""


class Work:
    def crypt():
        print("[|]")
        text = input("[+] text > ")
        textl = len(text)
        text = list(text)

        cryptedText = ""
        cryptedTetter = ""

        for letter in range(0, textl, 1):
            cryptedLetter = cryptLetters.get(text[letter])

            cryptedText = str(cryptedText) + str(cryptedLetter) + "04gwh56j567k6kнгаанд6ss"

        print("[|]")
        print("[*] Crypted text > " + cryptedText)
        return

    def decrypt():
        print("[|]")
        text = input("[+] Crypted text > ")

        text = text.split("04gwh56j567k6kнгаанд6ss")
        del text[-1]
        textLen = len(text)

        encryptedText = ""
        encryptedLetter = ""

        for letter in range(0, textLen, 1):
            encryptedLetter = encryptLetters.get(text[letter])

            encryptedText = str(encryptedText) + str(encryptedLetter)

        print("[|]")
        print("[*] Encrypted text > " + encryptedText)
        return

    def generator():

        print("[|]")
        path = input("[+] Path to file (Without 'C:/') > ")

        element = 0

        if os.path.exists(path):
            file = open(path, 'w')
        else:
            print('[|]')
            print('[-] File not found!')
            print('[|]')
            create = input('[*] Create file? y/n > ')
            if create == 'y' or create == 'н':
                try:
                    open(path, 'x')
                    file = open(path, 'w')
                except:
                    path = path.split('/')
                    del path[-1]
                    pathFile = "C:/"
                    for i in range(len(path)):
                        pathFile += str(path[i]) + '/'
                    try:
                        os.makedirs(pathFile, mode=0o777, exist_ok=False)
                        name = 0
                        for i in range(100):
                            name += 1
                            opx = os.path.exists(pathFile + str(name) + ".txt")
                            if not opx:
                                open(pathFile + str(name) + ".txt", 'x')
                                file = open(pathFile + str(name) + ".txt", 'w')
                                del name
                                break
                    except OSError:
                        print('[|]')
                        print('[-]File or catalog not found!')
                        return
            else:
                return

        while len(cryptLetters) != 152:
            key = ""
            letter = ""
            for b in words:
                index = random.choice(codeWords)
                if len(key) == int("8"):
                    break
                else:
                    key = key + letter
                    letter = index
            ind = words[element]
            keys.append('' + key)
            cryptLetters[ind] = key
            encryptLetters[key] = ind
            element += 1
        file.write(str(keys))
        print('[|]')
        print('[+] Crypt succefully created!')
        return

    def write():
        print("[|]")
        path = 'C:/'
        path += input("[+] Path to file (Without C:/ ) > ")
        if os.path.exists(path):
            file = open(path, 'r').read()
            fileContent = file.split("'")
            for i in range(306):
                if fileContent[i] != ", ":
                    keys.append(fileContent[i])
            del keys[0]
            for crypted in range(152):
                cryptLetters[words[crypted]] = keys[crypted]
                encryptLetters[keys[crypted]] = words[crypted]
            print("[|]")
            print("[+] Crypt succefully writed")
            return
        else:
            print('[|]')
            print('[-] File not found!')
            return

class Task:
    def cryptTask():
        Work.crypt()
        return
    def decryptTask():
        Work.decrypt()
        return
    def generatorTask():
        Work.generator()
        return
    def writeTask():
        Work.write()
        return
    def exitTask():
        print('[|]')
        exit('[+]Good luck!')

class CheckOption:
    def checkIf(option):
        if option == 1:
            Task.cryptTask()
            return
        elif option == 2:
            Task.decryptTask()
            return
        elif option == 3:
            Task.generatorTask()
            return
        elif option == 4:
            Task.writeTask()
            return
        elif option == 5:
            Task.exitTask()
            return
        else:
            return 0

class Main:
    def menu():
        while True:
            print("[|]")
            print("[+] 1) DeCrypt text")
            print("[+] 2) Encrypt text")
            print("[+] 3) Generate crypt keys")
            print("[+] 4) Write keys out of file")
            print("[+] 5) leave")
            print("[|]")

            option = input("[+] Schose > ")

            try:
                option = int(option)
            except:
                print("[|]")
                print("[-] Wrong number!")
                continue
            checkOp = CheckOption.checkIf(option)
            if checkOp == 0:
                print('[|]')
                print('[-] Wrong number!')
                continue
            continue

Main.menu()
