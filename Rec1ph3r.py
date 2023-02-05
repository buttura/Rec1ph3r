#  /$$                           /$$$$$$     /$$$$$$$              /$$     /$$
# | $$                         /$$$__  $$$  | $$__  $$            | $$    | $$
# | $$$$$$$  /$$   /$$        /$$_/  \_  $$ | $$  \ $$ /$$   /$$ /$$$$$$ /$$$$$$   /$$   /$$  /$$$$$$  /$$$$$$
# | $$__  $$| $$  | $$       /$$/ /$$$$$  $$| $$$$$$$ | $$  | $$|_  $$_/|_  $$_/  | $$  | $$ /$$__  $$|____  $$
# | $$  \ $$| $$  | $$      | $$ /$$  $$| $$| $$__  $$| $$  | $$  | $$    | $$    | $$  | $$| $$  \__/ /$$$$$$$
# | $$  | $$| $$  | $$      | $$| $$\ $$| $$| $$  \ $$| $$  | $$  | $$ /$$| $$ /$$| $$  | $$| $$      /$$__  $$
# | $$$$$$$/|  $$$$$$$      | $$|  $$$$$$$$/| $$$$$$$/|  $$$$$$/  |  $$$$/|  $$$$/|  $$$$$$/| $$     |  $$$$$$$
# |_______/  \____  $$      |  $$\________/ |_______/  \______/    \___/   \___/   \______/ |__/      \_______/
#            /$$  | $$       \  $$$   /$$$
#           |  $$$$$$/        \_  $$$$$$_/
#            \______/           \______/


def printBannerAndMenu():
    print('\033[m\n\033[1;32m')
    print('''                          d88          888     ,8,"88b,        ''')
    print('''888,8,  ,e e,   e88'888  d888 888 88e  888 ee   " ,88P' 888,8, ''')
    print('''888 "  d88 88b d888  '8 d"888 888 888b 888 88b    C8K   888 "  ''')
    print('''888    888   , Y888   ,   888 888 888P 888 888  e `88b, 888    ''')
    print('''888     "YeeP"  "88,e8'   888 888 88"  888 888 "8",88P' 888    ''')
    print('''                              888                              ''')
    print('''                              888                              ''')
    f = 'Developed with <3 by \033[1;33mHigor Buttura\033[m'
    print(f"\033[m\033[0;32m{f:>71}\n\033[m\n", end="\n")
    print("\033[1;32m[1]\033[m \033[1;34mRecon\033[m")
    print("\033[1;32m[2]\033[m \033[1;34mCiphers\033[m\n")

def ImportPackages():
    listPackages = ["argparse", "sys", "re", "requests", "nmap", "urllib.request", "time", "webbrowser", "sublist3r", "dirbpy", "glob", "logging", "subprocess"]
    for value in listPackages:
        try:
            __import__(value)
        except ImportError:
            print(f"\033[1;31m[!]\033[m \033[0;31mFailed to import\033[m \033[1;32m{value}\033[m")
            choice = ""
            try:
                choice = str(input(f"\033[1;32m[*]\033[m \033[1;38mAttempt to Auto-install\033[m \033[1;32m{value}\033[m\033[1;38m? [Y/n] \033[1;32m>>\033[m ")).strip().lower()[0]
            except:
                choice = 'y'
            if choice == 'y':
                print(f"\033[1;32m[*]\033[m \033[1;38mAttempting to Install \033[1;32m{value}\033[m\033[1;38m...\033[m ")
                try:
                    import pip
                    pip.main(['install', '-q', f'{value}'])
                    __import__(value)
                    print("\033[1;32m[DONE]\033[m")
                except:
                    print("\033[1;31m[FAIL]\033[m")
                    exit()
            elif choice == 'n':
                print("\033[1;31m[*]\033[m \033[0;31mUser Denied Auto-install\033[m")
                exit()
            else:
                print("\033[1;31m[!]\033[m \033[0;31mInvalid Decision\033[m")
                exit()


ImportPackages()

import argparse
from sys import exit, stdout
parser = argparse.ArgumentParser(description='rec1ph3r Tool')
parser.add_argument('--recon', '-r', help='Option of Recon', action='store', default=False, dest='recon')
parser.add_argument('--cipher', '-c', help='Option of Cipher', action='store', default=False, dest='cipher')
# Ciphers
parser.add_argument('--code', help='Code for Caesars Cipher', action='store', default=False, dest='code')
parser.add_argument('--position', help='Position of Code in the Caesars Cipher', action='store', default=False, dest='position')
parser.add_argument('--encode', help='Encode for Transposition & Vigenere Cipher', action='store', default=False, dest='encode')
parser.add_argument('--decode', help='Decode for Transposition & Vigenere Cipher', action='store', default=False, dest='decode')
parser.add_argument('--key', help='Key for Transposition & Vigenere Cipher', action='store', default=False, dest='key')
parser.add_argument('--text', help='Text for Reverse Cipher', action='store', default=False, dest='text')
# Recon
parser.add_argument('--domain', '-d', help='Domain for Subdiscoverer Tool', action='store', default=False, dest='domain')
parser.add_argument('--wordlist', '-w', help='Wordlist for Recon', action='store', default=False, dest='wordlist')
parser.add_argument('--file', '-f', help='File for Recon', action='store', default=False, dest='file')
parser.add_argument('--statuscode', '-s', help='Statuscode for Recon', action='store', default=False, dest='statuscode')
parser.add_argument('--url', '-u', help='URL for Recon', action='store', default=False, dest='url')
parser.add_argument('--ports', '-p', help='Ports for Recon', action='store', default=False, dest='ports')
parser.add_argument('--option', '-o', help='Option for Google Hacking', action='store', default=False, dest='option')
parser.add_argument('--thread', '-t', help='Thread for Recon (Dirb)', action='store', default=False, dest='thread')

args = parser.parse_args()


def ReconOrCiphers():
    if not not args.recon or not not args.cipher:
        if not not args.recon:
            return True
        else:
            return False
    else:
        printBannerAndMenu()
        try:
            option = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mYour option:\033[m \033[1;32m>> \033[m\033[1;31m"))
            try:
                if 1 <= int(option) <= 2:
                    if int(option) == 1:
                        return True
                    else:
                        return False
                else:
                    return True
            except:
                return True
        except:
            return True


ReconOrCiphers = ReconOrCiphers()


def MenuCiphers():
    print("\033[m")
    print("\033[1;32m[1]\033[m \033[1;34mCaesars Cipher\033[m")
    print("\033[1;32m[2]\033[m \033[1;34mTransposition Cipher\033[m")
    print("\033[1;32m[3]\033[m \033[1;34mVigenere Cipher\033[m")
    print("\033[1;32m[4]\033[m \033[1;34mReverse Cipher\033[m")
    print("\033[m")


def MenuRecon():
    print("\033[m")
    print("\033[1;32m[1]\033[m \033[1;34msubdiscoverer\033[m")
    print("\033[1;32m[2]\033[m \033[1;34msublist3r\033[m")
    print("\033[1;32m[3]\033[m \033[1;34mhttpx\033[m")
    print("\033[1;32m[4]\033[m \033[1;34mnmap\033[m")
    print("\033[1;32m[5]\033[m \033[1;34mfindir\033[m")
    print("\033[1;32m[6]\033[m \033[1;34mdirb\033[m")
    print("\033[1;32m[7]\033[m \033[1;34mgoogle hacking\033[m")
    print("\033[1;32m[8]\033[m \033[1;34mphattack\033[m")
    print("\033[1;32m[9]\033[m \033[1;34mgeolocation\033[m \033[0;34m(maintenance)\033[m")
    print("\033[m")


def optionArg(ReconOrCiphers):
    if ReconOrCiphers:
        return args.recon
    else:
        return args.cipher


def yourOption(ReconOrCiphers):
    option = optionArg(ReconOrCiphers)
    if not option:
        try:
            if ReconOrCiphers:
                MenuRecon()
            else:
                MenuCiphers()
            option = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mYour option:\033[m \033[1;32m>> \033[m\033[1;31m"))
            return option
        except:
            exit()
    else:
        return option


if not ReconOrCiphers:
    def caesarsCipher():
        def printBannerCaesarsCipher():
            print('''\n\033[m\033[1;36m''')
            print('''   ___                         ''')
            print('''  / __|__ _ ___ _____ _ _ _ ___''')
            print(''' | (__/ _` / -_|_-< _` | '_(_-<''')
            print('''  \___\__,_\___/__|__,_|_| /__/''')
            print('''  / __(_)_ __| |_  ___ _ _     ''')
            print(''' | (__| | '_ \ ' \/ -_) '_|    ''')
            print('''  \___|_| .__/_||_\___|_|      ''')
            print('''        |_|                    \n\033[m''')
            print('''\033[1;37mUsage:\033[m \033[1;32m./Rec1ph3r.py\033[m \033[1;35m[ --cipher\033[m \033[0;35mcaesars\033[m \033[1;35m]\033[m \033[1;34m[ --code \033[0;34mpaymycoffee\033[m \033[1;34m]\033[m \033[1;31m[ --position\033[m \033[0;31m3 \033[1;31m]\033[m\n''')


        printBannerCaesarsCipher()


        def getCode():
            if not not args.code:
                return args.code
            else:
                phrase = ""
                try:
                    phrase = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mCode:\033[m \033[1;32m>> \033[m\033[1;31m")).strip()
                except:
                    phrase = ""
                finally:
                    return phrase


        def yesOrNo():
            if not not args.position and args.position.isnumeric():
                return True
            else:
                yesorno = ""
                try:
                    yesorno = str(input("\033[m\033[1;32m[!]\033[m \033[1;31mDo you want to enter the exact position of the cipher?\033[m [N/y] \033[1;32m>> \033[m\033[1;31m")).lower()[0]
                except:
                    return False
                finally:
                    if yesorno == "y":
                        return True
                    else:
                        return False


        def getPosition():
            position = ""
            if yesOrNo():
                if not not args.position and args.position.isnumeric():
                    return int(args.position)
                else:
                    s = 0
                    while True:
                        try:
                            position = int(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mPosition: \033[m\033[1;32m>> \033[m\033[1;31m"))
                        except:
                            s += 1
                            print(f"({s}) Enter a valid value, try again.", end=" ")
                        if type(position) == int:
                            return position


        alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


        def Decipher(letter, positions):
            codes = ""
            if letter in alphabet:
                if alphabet.index(letter) + positions > 25:
                    codes += alphabet[alphabet.index(letter) + positions - 26]
                else:
                    codes += alphabet[alphabet.index(letter) + positions]
            else:
                codes += letter
            return codes


        def caesarsCipher(phrase):
            listpositions = list()
            codes = ""
            for positions in range(len(alphabet)):
                for value in phrase:
                    if value.lower() in alphabet:
                        codes += Decipher(value.lower(), positions)
                    else:
                        codes += value
                listpositions.append(codes)
                codes = ""
            return listpositions


        def IfCodeIsUpper(phrase, listpositions):
            listcodestemp = list()
            listcodes = list()
            codes = ""
            for x in range(len(listpositions)):
                for i in range(len(listpositions[x])):
                    if phrase[i].isupper():
                        codes += listpositions[x][i].upper()
                    else:
                        codes += listpositions[x][i]
                listcodestemp.append(codes)
                listcodes += listcodestemp.copy()
                codes = ""
                listcodestemp.clear()
            return listcodes


        def displayOnScreen(listcodes):
            position = getPosition()
            listcodes = IfCodeIsUpper(phrase, listcodes)
            print("")
            if type(position) == int:
                print(f"\033[m\033[1;32m{int(position):2}\033[mo. Position: \033[1;32m{listcodes[int(position) - 1]}\033[m")
            else:
                for i, value in enumerate(listcodes):
                    print(f"\033[m\033[1;32m{i + 1:2}\033[mo. Position: \033[1;32m{value}\033[m")
        phrase = getCode()
        listpositions = caesarsCipher(phrase)
        ifcodeisupper = IfCodeIsUpper(phrase, listpositions)
        displayOnScreen(ifcodeisupper)


    # ==================================================================================================================


    def transpositionCipher():
        def printBannerTranspositionCipher():
            print('''\n\033[m\033[1;36m''')
            print('''  _____                              _ _   _          ''')
            print(''' |_   _| _ __ _ _ _  ____ __  ___ __(_) |_(_)___ _ _  ''')
            print('''   | || '_/ _` | ' \(_-< '_ \/ _ (_-< |  _| / _ \ ' \ ''')
            print('''   |_||_| \__,_|_||_/__/ .__/\___/__/_|\__|_\___/_||_|''')
            print('''  / __(_)_ __| |_  ___ |_|                            ''')
            print(''' | (__| | '_ \ ' \/ -_) '_|                           ''')
            print('''  \___|_| .__/_||_\___|_|                             ''')
            print('''        |_|                                           \n\033[m''')
            print('''\033[1;37mUsage:\033[m \033[1;32m./Rec1ph3r.py\033[m \033[1;35m[ --cipher\033[m \033[0;35mtransposition\033[m \033[1;35m]\033[m \033[1;34m[ --encode \033[0;34mpaymycoffee\033[m \033[1;34m]\033[m \033[1;34m[ --decode \033[0;34mmfXyoeacepyf\033[m \033[1;34m]\033[m \033[1;31m[ --key\033[m \033[0;31m4321 \033[1;31m]\033[m\n''')


        def optionsEncodeDecode():
            print(f"\033[1;32m[1]\033[m \033[1;34mEncode\033[m")
            print(f"\033[1;32m[2]\033[m \033[1;34mDecode\033[m\n")


        printBannerTranspositionCipher()


        def yourOption():
            if not not args.encode:
                return True
            elif not not args.decode:
                return False
            else:
                try:
                    optionsEncodeDecode()
                    option = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mYour option:\033[m \033[1;32m>> \033[m\033[1;31m"))
                    if 1 <= int(option) <= 2:
                        if int(option) == 1:
                            return True
                        else:
                            return False
                except:
                    return True


        def plainText():
            if not not args.encode:
                return args.encode
            elif not not args.decode:
                return args.decode
            else:
                plaintext = ""
                try:
                    plaintext = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mPlaintext:\033[m \033[1;32m>> \033[m\033[1;31m"))
                except:
                    plaintext = ""
                finally:
                    return plaintext


        def keyword():
            if not not args.key:
                return args.key
            else:
                try:
                    s = 0
                    while True:
                        keyword = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mKeyword [just numbers]: \033[m\033[1;32m>> \033[m\033[1;31m"))
                        s += 1
                        if keyword.isnumeric():
                            return keyword
                        else:
                            print(f'\033[m\033[1;31m(\033[m\033[1;31m{s}\033[m\033[1;31m)\033[m', end=" ")
                except:
                    keyword = ""
                return keyword


        def plainTextList(plaintext):
            listValues = []
            for value in plaintext:
                listValues.append(value)
            return listValues


        def cipherText1(option, plaintextlist, keyword):
            ListValues = []
            phrase = plaintextlist.copy()
            if option:
                while True:
                    for value in keyword:
                        try:
                            ListValues.append(phrase[int(value) - 1])
                        except:
                            ListValues.append("X")
                    for i in range(len(keyword)):
                        if len(phrase) != 0:
                            phrase.pop(0)
                    if len(phrase) == 0:
                        break
            else:
                rows = len(phrase) / len(keyword)
                for r in range(int(rows)):
                    for c in range(len(keyword)):
                        for x in range(len(keyword)):
                            if int(keyword[x]) - 1 == c:
                                ListValues.append(phrase[x])
                    del phrase[0:len(keyword)]
                if 'X' in ListValues:
                    while True:
                        ListValues.remove('X')
                        if 'X' not in ListValues:
                            break
            return ListValues


        def cipherText2(list, keyword, option):
            code = ""
            rows = len(list) / len(keyword)
            if option:
                for c in range(len(keyword)):
                    s = 0
                    for r in range(int(rows)):
                        try:
                            code += f"{list[s + c]}"
                            s += len(keyword)
                        except:
                            break
            else:
                for r in range(int(rows)):
                    s = 0
                    for c in range(len(keyword)):
                        try:
                            code += f"{list[s + r]}"
                            s += int(rows)
                        except:
                            break
            return code


        option = yourOption()
        plaintext = plainText()
        keyword = keyword()
        plaintextlist = plainTextList(plaintext)
        if option:
            rowscipher = cipherText1(option, plaintextlist, keyword)
            code = cipherText2(rowscipher, keyword, option)
        else:
            code = cipherText2(plaintextlist, keyword, option)
            l = []
            for value in code:
                l.append(value)
            rowscipher = cipherText1(option, l, keyword)
            code = ''
            for value in rowscipher:
                code += value
        print("")
        print(f"\033[m\033[1;38m[+]\033[m \033[1;32m{code}\033[m")


    # ==================================================================================================================


    def vigenereCipher():
        def printBannerVigenereCipher():
            print('''\n\033[m\033[1;36m''')
            print(''' __   ___                           ''')
            print(''' \ \ / (_)__ _ ___ _ _  ___ _ _ ___ ''')
            print('''  \ V /| / _` / -_) ' \/ -_) '_/ -_)''')
            print('''   \_/ |_\__, \___|_||_\___|_| \___|''')
            print('''  / __(_)|___/ |_  ___ _ _          ''')
            print(''' | (__| | '_ \ ' \/ -_) '_|         ''')
            print('''  \___|_| .__/_||_\___|_|           ''')
            print('''        |_|                         \n\033[m''')
            print('''\033[1;37mUsage:\033[m \033[1;32m./Rec1ph3r.py\033[m \033[1;35m[ --cipher\033[m \033[0;35mvigenere\033[m \033[1;35m]\033[m \033[1;34m[ --encode \033[0;34mpaymycoffee\033[m \033[1;34m]\033[m \033[1;34m[ --decode \033[0;34mmrodrcgqtkji\033[m \033[1;34m]\033[m \033[1;31m[ --key\033[m \033[0;31mcoffee \033[1;31m]\033[m\n''')

        def optionsEncodeDecode():
            print(f"\033[1;32m[1]\033[m \033[1;34mEncode\033[m")
            print(f"\033[1;32m[2]\033[m \033[1;34mDecode\033[m\n")


        printBannerVigenereCipher()


        def yourOption():
            if not not args.encode:
                return True
            elif not not args.decode:
                return False
            else:
                try:
                    optionsEncodeDecode()
                    option = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mYour option:\033[m \033[1;32m>> \033[m\033[1;31m")).strip()
                    if option != '2':
                        return True
                    else:
                        return False
                except:
                    return True


        def getCode():
            if not not args.encode:
                return args.encode
            elif not not args.decode:
                return args.decode
            else:
                try:
                    code = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mCode:\033[m \033[1;32m>> \033[m\033[1;31m")).strip()
                except:
                    code = ""
                return code


        def getKey():
            if not not args.key:
                return args.key
            else:
                try:
                    key = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mKey:\033[m \033[1;32m>> \033[m\033[1;31m"))
                    for value in key:
                        if value not in alphabet:
                            return ""
                except:
                    key = ""
                return key


        def keyStream(key, code):
            keystream = key
            if len(code) > len(key):
                while True:
                    for value in key:
                        keystream += value
                        if len(keystream) == len(code):
                            return keystream
            else:
                return keystream


        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


        def getCodeKeystreamNumber(code, keystream):
            listNumbers = [[], []]
            listNumbersTemp = list()
            listCodeKey = [code, keystream]
            for i in range(len(listCodeKey)):
                for value in listCodeKey[i]:
                    if value.lower() in alphabet:
                        s = alphabet.index(value.lower())
                    else:
                        s = value
                    listNumbersTemp.append(s)
                listNumbers[i] = listNumbersTemp[:]
                listNumbersTemp.clear()
            return listNumbers


        def RemoveString(listnumbers):
            listnumbersint = [[], []]
            for i in range(2):
                for value in listnumbers[i]:
                    if isinstance(value, int):
                        listnumbersint[i].append(value)
            return listnumbersint


        def sumOrSubtractListNumbers(listnumbers, option):
            sumOrSubstractListNumbers = list()
            for i in range(len(listnumbers[0])):
                if option:
                    s = listnumbers[0][i] + listnumbers[1][i]
                else:
                    s = listnumbers[0][i] - listnumbers[1][i]
                sumOrSubstractListNumbers.append(s)
            for i in range(len(listnumbers[1])):
                if type(listnumbers[1][i]) == str:
                    return []
            return sumOrSubstractListNumbers


        def cipherText(sumorsubstractlistnumbers):
            ciphertext = ""
            for i, value in enumerate(sumorsubstractlistnumbers):
                if type(value) == int:
                    if value < len(alphabet):
                        ciphertext += alphabet[value]
                    else:
                        ciphertext += alphabet[value - 26]
            listciphertext = list()
            for value in ciphertext:
                listciphertext.append(value)
            return listciphertext


        def IfNotInAlphabet(listciphertext, code):
            for i, value in enumerate(code):
                if value.lower() not in alphabet:
                    listciphertext.insert(i, value)
            return listciphertext


        def IfCodeIsUpper(listciphertext, code):
            ciphertext = ""
            for i in range(len(listciphertext)):
                if code[i].isupper():
                    listciphertext[i] = listciphertext[i].upper()
            for value in listciphertext:
                ciphertext += value
            return ciphertext


        option = yourOption()
        codes = getCode()
        key = getKey()
        if key != "":
            keystream = keyStream(key, codes)
            listnumbers = getCodeKeystreamNumber(codes, keystream)
            removestringList = RemoveString(listnumbers)
            sumorsubtractlistnumbers = sumOrSubtractListNumbers(removestringList, option)
            ciphertextlist = cipherText(sumorsubtractlistnumbers)
            ifnotinalphabetresults = IfNotInAlphabet(ciphertextlist, codes)
            ciphertextresults = IfCodeIsUpper(ifnotinalphabetresults, codes)
            print(f"\n\033[m\033[1;38m[+]\033[m \033[1;32m{ciphertextresults}\033[m\033[m")


    # ==================================================================================================================


    def reverseCipher():
        def printBannerReverseCipher():
            print('''\n\033[m\033[1;36m''')
            print('''                              ____ ''')
            print(''' ___  ___ __ _ _____   _____ / _  |''')
            print('''/ _ \|__ |__` / _ \ \ / / _ | (_| |''')
            print('''\__  / __/  | \__  \ V /\__  > _  |''')
            print('''|___/\___|  |_|___/ \_/ |___/_/ |_|''')
            print('''   ___ _      _            ''')
            print('''  / __(_)_ __| |_  ___ _ _ ''')
            print(''' | (__| | '_ \ ' \/ -_) '_|''')
            print('''  \___|_| .__/_||_\___|_|  ''')
            print('''        |_|                \n\033[m''')
            print('''\033[1;37mUsage:\033[m \033[1;32m./Rec1ph3r.py\033[m \033[1;35m[ --cipher\033[m \033[0;35mreverse\033[m \033[1;35m]\033[m \033[1;34m[ --text \033[0;34mpaymycoffee\033[m \033[1;34m]\033[m\n''')


        printBannerReverseCipher()


        def Text():
            if not not args.text:
                return args.text
            else:
                text = ""
                try:
                    text = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mPlaintext:\033[m \033[1;32m>> \033[m\033[1;31m")).strip()
                except:
                    text = ""
                finally:
                    return text


        def ciphertext(text):
            f = ""
            for i in range(1, len(text) + 1):
                f += text[-i]
            return f


        text = Text()
        ciphertext = ciphertext(text)
        print(f"\n\033[m\033[1;38m[+]\033[m \033[1;32m{ciphertext}\033[m")


    # ==================================================================================================================


    option = yourOption(ReconOrCiphers)
    if option == "1" or option == "caesars" or option == "caesars-cipher":
        caesarsCipher()
    if option == "2" or option == "transposition" or option == "transposition-cipher":
        transpositionCipher()
    if option == "3" or option == "vigenere" or option == "vigenere-cipher":
        vigenereCipher()
    if option == "4" or option == "reverse" or option == "reverse-cipher":
        reverseCipher()


    # ==================================================================================================================


else:
    def subdiscoverer():
        import re
        import requests
        def printBannerSubdiscoverer():
            print('''\n\033[m\033[1;36m''')
            print('''   _____       __        ___                                         ''')
            print('''  / ___/__  __/ /_  ____/ (_)_____________ _   _____  ________  _____''')
            print('''  \__ \/ / / / __ \/ __  / / ___/ ___/ __ \ | / / _ \/ ___/ _ \/ ___/''')
            print(''' ___/ / /_/ / /_/ / /_/ / (__  ) /__/ /_/ / |/ /  __/ /  /  __/ /    ''')
            print('''/____/\__,_/_.___/\__,_/_/____/\___/\____/|___/\___/_/   \___/_/     \n\033[m''')
            print('''\033[1;37mUsage:\033[m \033[1;32m./Rec1ph3r.py\033[m \033[1;35m[ --recon\033[m \033[0;35msubdiscoverer\033[m \033[1;35m]\033[m \033[1;34m[ --domain \033[0;34site.com\033[m \033[1;34m]\033[m \033[1;31m[ --wordlist\033[m \033[0;31msubdomains.txt \033[1;31m]\033[m\n''')


        printBannerSubdiscoverer()


        def getDomain():
            if not not args.domain:
                domain = args.domain
            else:
                try:
                    domain = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mEnter the domain:\033[m \033[1;32m>> \033[m\033[1;31m"))
                except:
                    exit()
            regex = validateDomain(domain)
            if regex is not None:
                return domain.lower()
            else:
                exit()


        def validateDomain(domain):
            regex = re.findall(r"^[a-zA-Z]*\.[a-zA-Z]+(.[a-zA-Z]+)*?$", domain, flags=re.M)
            if len(regex) != 0:
                return regex


        def getRouteWordlist():
            if not not args.wordlist:
                return args.wordlist
            else:
                return None


        def do_request_with_online_file(dict_url):
            data = requests.get(dict_url)
            dict_list = str(data.content).replace('\\r', ' ').replace('\\n', ' ').split()
            return dict_list

        def output(domain, wordlist):
            if wordlist == None:
                entry = "https://raw.githubusercontent.com/danTaler/WordLists/master/Subdomain.txt"
                entry = do_request_with_online_file(entry)
            else:
                try:
                    entry = open(wordlist, 'r')
                except:
                    exit()
            output = open(f"subdiscoverer.txt", 'wt+')
            if wordlist == None:
                lines = entry
            else:
                lines = entry.readlines()
            for value in lines:
                urlwithsub = f"{value.strip()}.{domain}"
                print(f"\033[m\033[1;38m[+]\033[m \033[1;32m{urlwithsub}\033[m")
                output.write(f"{urlwithsub}\n")
            if wordlist != None:
                entry.close()
            output.close()


        domain = getDomain()
        wordlist = getRouteWordlist()
        output = output(domain, wordlist)


    # ==================================================================================================================

    def httpx():
        import requests
        def printBannerHTTPX():
            print("\n\033[m\033[1;36m")
            print('''    __    __  __            ''')
            print('''   / /_  / /_/ /_____  _  __''')
            print('''  / __ \/ __/ __/ __ \| |/_/''')
            print(''' / / / / /_/ /_/ /_/ />  <  ''')
            print('''/_/ /_/\__/\__/ .___/_/|_|  ''')
            print('''             /_/            \033[m\n''')
            print('''\033[1;37mUsage:\033[m \033[1;32m./Rec1ph3r.py\033[m \033[1;35m[ --recon\033[m \033[0;35mhttpx\033[m \033[1;35m]\033[m \033[1;34m[ --file \033[0;34murls.txt\033[m \033[1;34m]\033[m \033[1;31m[ --statuscode\033[m \033[0;31m200,301 \033[1;31m]\033[m\n''')


        printBannerHTTPX()


        def getArchive():
            if not not args.file:
                return args.file
            else:
                return None


        def statusCodes():
            if not not args.statuscode:
                return args.statuscode
            else:
                return None


        def listStatusCode(statuscode):
            listStatus = list()
            if statuscode == None:
                for i in range(100, 400):
                    listStatus.append(i)
                listStatus.append(406)
            else:
                try:
                    statuscode += ","
                    listStatus = statuscode.split(",")
                except:
                    if str(statuscode).strip().isnumeric():
                        listStatus.append(str(statuscode).strip())
                for value in listStatus:
                    if value.isnumeric() and value != "":
                        listStatus[listStatus.index(value)] = int(listStatus[listStatus.index(value)])
                    else:
                        listStatus.remove(value)
            return listStatus


        def existsFile(file):
            if file == "":
                return False
            else:
                try:
                    f = open(file, "rt")
                    f.close()
                except:
                    return False
                else:
                    return True


        def httpAppendAndValidateIfOnAndOutput(exists, file, statusCodeList):
            if exists and file != "":
                output = open("httpx.txt", "wt+")
                with open(file, "r") as file:
                    for line in file.readlines():
                        if "http://" or "https://" in line.rstrip():
                            return ""
                        else:
                            url = f"http://{line.rstrip()}"
                            try:
                                r = requests.get(url, timeout=3.05)
                                statuscode = r.status_code
                                if statuscode in statusCodeList:
                                    print(f"\033[m\033[0;31m{url}\033[m \033[1;32m[{statuscode}]\033[m")
                                    output.write(f"{url}\n")
                            except:
                                continue
            else:
                return ""


        file = getArchive()
        exists = existsFile(file)
        statuscode = statusCodes()
        statuscodelist = listStatusCode(statuscode)
        http = httpAppendAndValidateIfOnAndOutput(exists, file, statuscodelist)


    # ==================================================================================================================


    def sublist3r():
        import sublist3r
        import re

        print("\n\033[1;36m")
        print('''                 __     __ _        __  _____      ''')
        print('''   _____ __  __ / /_   / /(_)_____ / /_|__  / _____''')
        print('''  / ___// / / // __ \ / // // ___// __/ /_ < / ___/''')
        print(''' (__  )/ /_/ // /_/ // // /(__  )/ /_ ___/ // /    ''')
        print('''/____/ \__,_//_.___//_//_//____/ \__//____//_/     ''')
        print("\n\033[m")


        def getDomain():
            if not not args.domain:
                return args.domain
            else:
                try:
                    return str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mEnter the domain:\033[m \033[1;32m>> \033[m\033[1;31m"))
                except:
                    exit()


        def validateDomain(domain):
            regex = re.findall(r"^[a-zA-Z]*\.[a-zA-Z]+(.[a-zA-Z]+)*?$", domain, flags=re.M)
            if len(regex) != 0:
                return regex
            else:
                exit()


        def getThreads():
            if not not args.threads:
                return args.threads
            else:
                try:
                    return str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mThreads:\033[m \033[1;32m>> \033[m\033[1;31m")).strip()
                except:
                    return 4

        def getSaveFile():
            if not not args.output:
                return args.output
            else:
                return None


        def getPorts():
            if not not args.ports:
                return args.ports
            else:
                try:
                    return str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mPorts:\033[m \033[1;32m>> \033[m\033[1;31m")).strip()
                except:
                    return "80,443"


        def getSilent():
            if not not args.silent:
                return args.silent
            else:
                try:
                    silent = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mSilent: [y/N]\033[m \033[1;32m>> \033[m\033[1;31m")).lower().strip()[0]
                    if silent == "y":
                        return True
                    else:
                        return False
                except:
                    return False


        def getVerbose():
            if not not args.verbose:
                return args.verbose
            else:
                try:
                    verbose = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mVerbose: [y/N]\033[m \033[1;32m>> \033[m\033[1;31m")).lower().strip()[0]
                    if verbose == "y":
                        return True
                    else:
                        return False
                except:
                    return False


        def enableBruteForce():
            if not not args.bruteforce:
                return args.bruteforce
            else:
                try:
                    bruteforce = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mBrute Force: [y/N]\033[m \033[1;32m>> \033[m\033[1;31m")).lower().strip()[0]
                    if bruteforce == "y":
                        return True
                    else:
                        return False
                except:
                    return False


        def engines():
            if not not args.engine:
                return args.engine
            else:
                try:
                    return str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mEngines:\033[m \033[1;32m>> \033[m\033[1;31m")).lower().strip()
                except:
                    return None


        domain = getDomain()
        domain = validateDomain(domain)
        threads = getThreads()
        output = getSaveFile()
        ports = getPorts()
        silent = getSilent()
        verbose = getVerbose()
        bruteforce = enableBruteForce()
        engines = engines()
        sublist3r.main(domain, threads, output, ports, silent, verbose, bruteforce, engines)


    # ==================================================================================================================


    def nmap():
        import nmap
        import re
        from sys import exit
        def printBannerNMAP():
            print("\n\033[m\033[1;36m")
            print('''    _   __                    ''')
            print('''   / | / /___ ___  ____ _____ ''')
            print('''  /  |/ / __ `__ \/ __ `/ __ \'''')
            print(''' / /|  / / / / / / /_/ / /_/ /''')
            print('''/_/ |_/_/ /_/ /_/\__,_/ .___/ ''')
            print('''                     /_/      \n\033[m''')
            print('''\033[1;37mUsage:\033[m \033[1;32m./Rec1ph3r.py\033[m \033[1;35m[ --recon\033[m \033[0;35mnmap\033[m \033[1;35m]\033[m \033[1;34m[ --file \033[0;34murls.txt\033[m \033[1;34m]\033[m \033[1;31m[ --url\033[m \033[0;31mwww.site.com \033[1;31m]\033[m \033[1;33m[ --ports\033[m \033[0;33m80,443\033[m \033[1;33m]\033[m\n''')


        printBannerNMAP()


        def getArchiveOrUrlOrIp():
            if not not args.file:
                return args.file
            elif not not args.url:
                return args.url
            else:
                url = None
                try:
                    url = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mEnter the URL:\033[m \033[1;32m>> \033[m\033[1;31m"))
                except:
                    return url
                finally:
                    print("")
                    return url


        def validateURL(urlOrFile):
            try:
                regex = re.findall(r"^[a-zA-Z]*\.[a-zA-Z]+(.[a-zA-Z]+)*?$", urlOrFile, flags=re.M)
                if len(regex) != 0:
                    return urlOrFile
                else:
                    regex = re.findall(r"^[0-9]{1,3}?.[0-9]{1,3}?.[0-9]{1,3}?.[0-9]{1,3}?$", urlOrFile, flags=re.M)
                    if len(regex) != 0:
                        return urlOrFile
                    else:
                        return None
            except:
                return urlOrFile


        def getPorts():
            if not not args.ports:
                return args.ports
            else:
                return "21-443"


        def nmapExecutionWithOutput(file, ports):
            url = None
            nm = None
            try:
                file = open(file, "r")
            except:
                url = file
            finally:
                try:
                    for line in file.readlines():
                        try:
                            nm = nmap.PortScanner()
                            nm.scan(line.rstrip(), ports)
                        except:
                            continue
                except:
                    try:
                        nm = nmap.PortScanner()
                        nm.scan(url.rstrip(), ports)
                    except:
                        exit()
                finally:
                    if nm.all_hosts():
                        output = open("nmap.txt", "wt+")
                        print(f"\033[1;34m{'=' * 50}\033[m")
                        print(f"\033[1;32m{nm.command_line()}\033[m")
                        print(f"\033[1;34m{'=' * 50}\033[m")
                        for host in nm.all_hosts():
                            print(f"\033[1;32mHost :\033[m \033[1;31m{host}\033[m")
                            print(f"\033[1;32mState :\033[m \033[1;31m{nm[host].state()}")
                            print(f"\033[1;34m{'-'*30}\033[m")
                            for protocol in nm[host].all_protocols():
                                print(f"\033[1;32mProtocol :\033[m \033[1;31m{protocol}\033[m")
                                lport = nm[host][protocol].keys()
                                for port in lport:
                                    print(f"\033[1;32mport : \033[m\033[1;31m{port}\t\033[1;32mstate : \033[m", end="")
                                    if nm[host][protocol][port]['state'] == "open":
                                        print(f"\033[1;33mopen\033[m")
                                    else:
                                        print(f"\033[1;31m{nm[host][protocol][port]['state']}\033[m")
                        print("")
                        output.write(nm.csv())


        archive = getArchiveOrUrlOrIp()
        archive = validateURL(archive)
        ports = getPorts()
        nmapExecutionWithOutput(archive, ports)


    # ==================================================================================================================


    def findir():
        import urllib.request
        from time import sleep
        import re
        import requests
        def printBannerFindir():
            print("\n\033[m\033[1;36m")
            print('''    _____           ___     ''')
            print('''   / __(_)___  ____/ (_)____''')
            print('''  / /_/ / __ \/ __  / / ___/''')
            print(''' / __/ / / / / /_/ / / /    ''')
            print('''/_/ /_/_/ /_/\__,_/_/_/     \033[m\n''')
            print('''\033[1;37mUsage:\033[m \033[1;32m./Rec1ph3r.py\033[m \033[1;35m[ --recon\033[m \033[0;35mfindir\033[m \033[1;35m]\033[m \033[1;34m[ --file \033[0;34murls.txt\033[m \033[1;34m]\033[m \033[1;31m[ --url\033[m \033[0;31mwww.site.com \033[1;31m]\033[m \033[1;33m[ --wordlist\033[m \033[0;33mdirectories.txt\033[m \033[1;33m]\033[m\n''')


        printBannerFindir()


        def getFile():
            if not not args.file:
                return args.file
            else:
                return None


        def getURL(file):
            if file == None:
                if not not args.url:
                    return args.url
                else:
                    try:
                        url = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mEnter the URL:\033[m \033[1;32m>> \033[m\033[1;31m"))
                    except:
                        return None
                    else:
                        return url
            else:
                return file


        def getWordlist():
            if not not args.wordlist:
                return args.wordlist
            else:
                return None


        def do_request_with_online_file(dict_url):
            data = requests.get(dict_url)
            dict_list = str(data.content).replace('\\r', ' ').replace('\\n', ' ').split()
            return dict_list


        def findirExecutionAndOutput(inputURL, wordlist):
            output = open("findir.txt", "wt+")
            try:
                wordlist = open(wordlist, "r")
            except:
                try:
                    wordlist = "https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/directory-list-2.3-small.txt"
                    wordlist = do_request_with_online_file(wordlist)
                except:
                    exit()
            finally:
                try:
                    if not bool(re.findall(r"^http[s]?://[a-zA-Z]*\.[a-zA-Z]+(.[a-zA-Z]+)*?$", inputURL)):
                        exit()
                except:
                    exit()
                try:
                    urls = open(inputURL, "r")
                    for line in urls.readlines():
                        if "http://" or "https://" in line.strip():
                            for word in wordlist:
                                url = f"{line.rstrip()}/{word.rstrip()}"
                                sleep(3.05)
                                try:
                                    statuscode = urllib.request.urlopen(url, timeout=10).getcode()
                                    if statuscode != 404:
                                        output.write(f"{url}\n")
                                        print(f"\033[1;38m[+]\033[m \033[1;32m{url}\033[m \033[1;36m[\033[m\033[0;36m{statuscode}\033[m\033[1;36m]\033[m")
                                except:
                                    continue
                        else:
                            continue
                except:
                    url = inputURL
                    for directory in wordlist:
                        urlDir = f"{url}/{directory.rstrip()}"
                        sleep(3.05)
                        try:
                            statuscode = urllib.request.urlopen(urlDir, timeout=10).getcode()
                            if statuscode != 404:
                                output.write(f"{url}\n")
                                print(f"\033[1;38m[+]\033[m \033[1;32m{url}\033[m \033[1;36m[\033[m\033[0;36m{statuscode}\033[m\033[1;36m]\033[m")
                        except:
                            continue


        file = getFile()
        url = getURL(file)
        wordlist = getWordlist()
        findirExecutionAndOutput(url, wordlist)


    # ==================================================================================================================


    def dirb():
        import dirbpy
        def printBannerDirb():
            print("\n\033[m\033[1;36m")
            print('''       ___      __  ''')
            print('''  ____/ (_)____/ /_ ''')
            print(''' / __  / / ___/ __ \'''')
            print('''/ /_/ / / /  / /_/ /''')
            print('''\__,_/_/_/  /_.___/ \n\033[m''')
            print('''\033[1;37mUsage:\033[m \033[1;32m./Rec1ph3r.py\033[m \033[1;35m[ --recon\033[m \033[0;35mdirb\033[m \033[1;35m]\033[m \033[1;34m[ --url \033[0;34mhttps://www.site.com\033[m \033[1;34m]\033[m \033[1;31m[ --file\033[m \033[0;31msites.txt \033[1;31m]\033[m \033[1;33m[ --thread\033[m \033[0;33m5\033[m \033[1;33m]\033[m \033[1;36m[ --save\033[m \033[0;36moutput.txt\033[m \033[1;36m]\033[m\n''')


        printBannerDirb()


        import sys
        import argparse
        import glob
        import logging

        import requests

        from _dirbpy.URLBruteforcer import URLBruteforcer
        from _dirbpy.WordDictonary import WordDictonary
        from _dirbpy.FileJSONFormatter import FileJSONFormatter

        BLUE = "\033[1;34m"
        GREEN = "\033[0;32m"
        RESET = "\033[0;0m"

        NUMBER_OF_THREAD_PARAMETER_ERROR = 'The number of thread is to high. Current: {}, Max: {}'
        GENERATED_WORD_MESSAGE = "Generated words: {}"

        FORMAT = '{}[%(asctime)s]{} {}[%(levelname)s]{} %(message)s'.format(GREEN, RESET, BLUE, RESET)
        logging.basicConfig(format=FORMAT, level=logging.INFO)
        ROOT_LOGGER = logging.getLogger()


        def remove_none_value_in_kwargs(params_dict: dict) -> dict:
            return {k: v for k, v in params_dict.items() if v is not None}


        def do_request_with_online_file(dict_url: str, host: str, **kwargs) -> None:
            data = requests.get(dict_url)
            dict_list = str(data.content).replace('\\r', ' ').replace('\\n', ' ').split()
            use_url_bruteforcer(dict_list, host, **kwargs)


        def do_request_with_dictionary(file_dict, host: str, **kwargs) -> None:
            word_dictionary = WordDictonary(file_dict)
            use_url_bruteforcer(word_dictionary, host, **kwargs)


        def use_url_bruteforcer(words: list, host: str, **kwargs) -> None:
            params = remove_none_value_in_kwargs(kwargs)
            ROOT_LOGGER.info(GENERATED_WORD_MESSAGE.format(len(words)))
            request_handler = URLBruteforcer(host, words, **params)
            request_handler.send_requests_with_all_words()


        def number_of_thread(value: int) -> int:
            value = int(value)
            if value > URLBruteforcer.MAX_NUMBER_REQUEST:
                raise argparse.ArgumentTypeError(
                    NUMBER_OF_THREAD_PARAMETER_ERROR.format(value, URLBruteforcer.MAX_NUMBER_REQUEST))
            return value


        def get_parser():
            parser = argparse.ArgumentParser()
            parser.add_argument('-r', '--recon',
                                type=str,
                                help='Recon Dirb')
            parser.add_argument('-u', '--url',
                                type=str,
                                help='This is the url to scan')
            parser.add_argument('-f', '--file',
                                type=str,
                                help='Input file with words.')
            parser.add_argument('-o', '--online',
                                type=str,
                                help='URL with raw dictionary')
            parser.add_argument('-d', '--directory',
                                type=str,
                                help='Input directory with dictionaries (.txt).')
            parser.add_argument('-t', '--thread',
                                type=number_of_thread,
                                help='Number of thread, the max value is {}'.format(URLBruteforcer.MAX_NUMBER_REQUEST))
            parser.add_argument('-c', '--status-code',
                                nargs='*',
                                type=int,
                                help='Status codes list to accept, the default list is: {}'.format(
                                    URLBruteforcer.VALID_STATUS_CODE))
            parser.add_argument('-p', '--proxy',
                                nargs='*',
                                type=str,
                                help='Specify the url of the proxy if you want to use one. (Ex: localhost:8080)')
            parser.add_argument('-i', '--ignore',
                                nargs='*',
                                type=str,
                                help='Ignore a directory (Ex: css images)')
            parser.add_argument('--no-duplicate',
                                action='store_false',
                                help='Don\'t display duplicate logs')
            parser.add_argument('-s', '--save',
                                type=str,
                                help='Output file.')
            parser.add_argument('--hosts-file',
                                type=argparse.FileType('r'),
                                help='File with urls to scan')
            return parser


        def get_parsed_args(parser, args):
            args_parsed = parser.parse_args(args)
            if not args_parsed.url and not args_parsed.hosts_file:
                exit()
            return args_parsed


        def main():
            parser = get_parser()
            args = get_parsed_args(parser, sys.argv[1:])

            if args.proxy:
                proxy = args.proxy[0]
                print(f'Using proxy: {proxy}\n')
            else:
                proxy = None

            status_code = None
            if args.status_code:
                status_code = args.status_code

            directories_to_ignore = args.ignore
            dict_url = None
            if args.online:
                dict_url = args.online
            elif not args.file and not args.directory:
                dict_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt"

            params = {
                "nb_thread": args.thread,
                "status_code": status_code,
                "proxy": proxy,
                "directories_to_ignore": directories_to_ignore,
                "duplicate_log": args.no_duplicate
            }

            if args.save:
                file_handler = logging.FileHandler(args.save)
                formatter = FileJSONFormatter()
                file_handler.setFormatter(formatter)
                ROOT_LOGGER.addHandler(file_handler)

            hosts = []
            if args.hosts_file:
                hosts = args.hosts_file.readlines()
                hosts = [host.rstrip('\n') for host in hosts]

            for host in hosts or [args.url]:
                if args.directory:
                    for file in glob.glob(
                            "{}*.txt".format(args.directory if args.directory.endswith('/') else args.directory + '/')):
                        ROOT_LOGGER.info('Current file: {}'.format(file))
                        with open(file, 'r') as opened_file:
                            do_request_with_dictionary(opened_file, host, **params)
                elif dict_url:
                    do_request_with_online_file(dict_url, host, **params)
                else:
                    with open(args.file, 'r') as opened_file:
                        do_request_with_dictionary(opened_file, host, **params)

        dirbpy.main()


    # ==================================================================================================================


    def googleHacking():
        def printBannerGoogleHacking():
            print("\n\033[m\033[1;36m")
            print('''   ______                  __          ''')
            print('''  / ____/___  ____  ____ _/ /__        ''')
            print(''' / / __/ __ \/ __ \/ __ `/ / _ \       ''')
            print('''/ /_/ / /_/ / /_/ / /_/ / /  __/       ''')
            print('''\____/\____/\____/\__, /_/\___/        ''')
            print('''    __  __       /_____   _            ''')
            print('''   / / / /___ ______/ /__(_)___  ____ _''')
            print('''  / /_/ / __ `/ ___/ //_/ / __ \/ __ `/''')
            print(''' / __  / /_/ / /__/ ,< / / / / / /_/ / ''')
            print('''/_/ /_/\__,_/\___/_/|_/_/_/ /_/\__, /  ''')
            print('''                              /____/   \033[m\n''')
            print('''\033[1;37mUsage:\033[m \033[1;32m./Rec1ph3r.py\033[m \033[1;35m[ --recon\033[m \033[0;35mgooglehacking\033[m \033[1;35m]\033[m \033[1;34m[ --option \033[0;34m3\033[m \033[1;34m]\033[m \033[1;31m[ --url\033[m \033[0;31mwww.site.com \033[1;31m]\033[m\n''')


        printBannerGoogleHacking()


        def Menu():
            print("\033[1;32m[01]\033[m \033[1;34mDirectory Listing\033[m")
            print("\033[1;32m[02]\033[m \033[1;34mConfiguration Files\033[m")
            print("\033[1;32m[03]\033[m \033[1;34mDatabase Files\033[m")
            print("\033[1;32m[04]\033[m \033[1;34mLog Files\033[m")
            print("\033[1;32m[05]\033[m \033[1;34mBackup and Old Files\033[m")
            print("\033[1;32m[06]\033[m \033[1;34mLogin Pages\033[m")
            print("\033[1;32m[07]\033[m \033[1;34mSQL Errors\033[m")
            print("\033[1;32m[08]\033[m \033[1;34mPublicly Exposed Documents\033[m")
            print("\033[1;32m[09]\033[m \033[1;34mphpinfo()\033[m")
            print("\033[1;32m[10]\033[m \033[1;34mGoogle Hacking Database\033[m\n")


        def yourOption():
            if not not args.option:
                try:
                    if 1 <= int(args.option) <= 10:
                        return int(args.option)
                    else:
                        return None
                except:
                    return None
            else:
                try:
                    Menu()
                    return str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mYour option:\033[m \033[1;32m>> \033[m\033[1;31m"))
                except:
                    return None


        def regexUrl(url):
            import re
            from sys import exit
            if not bool(re.findall(r"^http[s]?://[a-zA-Z]*\.[a-zA-Z]+(.[a-zA-Z]+)*?$", url)) or not bool(re.findall(r"^[a-zA-Z]*\.[a-zA-Z]+(.[a-zA-Z]+)*?$", url)):
                if re.findall(r"^http[s]?://", url):
                    try:
                        url = url.replace("https://", "")
                    except:
                        url = url.replace("http://", "")
                    finally:
                        return url
                else:
                    return url
            else:
                exit()


        def getUrl(choice):
            if str(choice) != "10":
                if not not args.url:
                    return args.url
                else:
                    url = None
                    try:
                        url = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mEnter the URL:\033[m \033[1;32m>> \033[m\033[1;31m"))
                    except:
                        return None
                    finally:
                        return regexUrl(url)
            else:
                return None


        def openNewTab(choice, url):
            import sys
            from webbrowser import open_new_tab
            search = "https://www.google.com/search?q="
            if str(choice) == "1":
                open_new_tab(f"{search}site:{url}+intitle:index.of")
            elif str(choice) == "2":
                open_new_tab(f"{search}site:{url}+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini")
            elif str(choice) == "3":
                open_new_tab(f"{search}site:{url}+ext:sql+|+ext:dbf+|+ext:mdb")
            elif str(choice) == "4":
                open_new_tab(f"{search}site:{url}+ext:log")
            elif str(choice) == "5":
                open_new_tab(f"{search}site:{url}+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup")
            elif str(choice) == "6":
                open_new_tab(f"{search}site:{url}+inurl:login | admin | user | cpanel | account | moderator | /cp")
            elif str(choice) == "7":
                open_new_tab(f'{search}site:{url}+intext:"sql+syntax+near"+|+intext:"syntax+error+has+occurred"+|+intext:"incorrect+syntax+near"+|+intext:"unexpected+end+of+SQL+command"+|+intext:"Warning:+mysql_connect()"+|+intext:"Warning:+mysql_query()"+|+intext:"Warning:+pg_connect()"')
            elif str(choice) == "8":
                open_new_tab(f'{search}site:{url}+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv')
            elif str(choice) == "9":
                open_new_tab(f'{search}site:{url}+ext:php+intitle:phpinfo+"published+by+the+PHP+Group"')
            elif str(choice) == "10":
                open_new_tab(f'https://www.exploit-db.com/google-hacking-database/')
            else:
                sys.exit()


        youroption = yourOption()
        url = getUrl(youroption)
        openNewTab(youroption, url)


    # ==================================================================================================================


    def phattack():
        import sys, subprocess

        def printBannerPhattack():
            print('''\n\033[m\033[1;36m''')
            print('''           __          __  __             __  ''')
            print('''    ____  / /_  ____ _/ /_/ /_____ ______/ /__''')
            print('''   / __ \/ __ \/ __ `/ __/ __/ __ `/ ___/ //_/''')
            print('''  / /_/ / / / / /_/ / /_/ /_/ /_/ / /__/ ,<   ''')
            print(''' / .___/_/ /_/\__,_/\__/\__/\__,_/\___/_/|_|  ''')
            print('''/_/                                           \n\033[m''')


        def printMenuPhattack():
            print('''\n\033[1;32mTemplates:\033[m\n''')
            print('''\033[1;32m[1]\033[m \033[1;34mInstagram\033[m''')
            print('''\033[1;32m[2]\033[m \033[1;34mFacebook\033[m''')
            print('''\033[1;32m[3]\033[m \033[1;34mSnapchat\033[m''')
            print('''\033[1;32m[4]\033[m \033[1;34mTwitter\033[m''')
            print('''\033[1;32m[5]\033[m \033[1;34mGitHub\033[m''')
            print('''\033[1;32m[6]\033[m \033[1;34mGoogle\033[m''')
            print('''\033[1;32m[7]\033[m \033[1;34mSpotify\033[m''')
            print('''\033[1;32m[8]\033[m \033[1;34mNetflix\033[m''')
            print('''\033[1;32m[9]\033[m \033[1;34mProtonmail\033[m\n''')


        try:
            printBannerPhattack()
            printMenuPhattack()
            templates = {
                '1': 'instagram',
                '2': 'facebook',
                '3': 'snapchat',
                '4': 'twitter',
                '5': 'github',
                '6': 'google',
                '7': 'spotify',
                '8': 'netflix',
                '9': 'protonmail',
            }
            subdom = choice = 0
            try:
                number = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mYour option:\033[m \033[1;32m>> \033[m\033[1;31m"))
                choice = templates[number]
                subdom = str(input("\033[m\033[1;32m[+]\033[m \033[m\033[1;38mSubdomain:\033[m \033[1;32m>> \033[m\033[1;31m"))
            except:
                exit()
            print(f"\033[m\033[1;32m[+]\033[m Starting Server at \033[1;32m{subdom}.serveo.net\033[m...")
            print(f"\033[1;32m[+]\033[m Logs can be found in \033[1;32msites/{choice}/ip.txt\033[m and \033[1;32msites/{choice}/usernames.txt\033[m")
            cmd_line = f"php -t sites/{choice} -S 127.0.0.1:80 & ssh -R {subdom}.serveo.net:80:127.0.0.1:80 serveo.net"
            p = subprocess.Popen(cmd_line, shell=True)
            out = p.communicate()[0]
        except KeyboardInterrupt:
            pass


    # ==================================================================================================================


    def geolocation():
        from geoip import geolite2
        import requests

        def myIp(Ip):
            reader = geolite2.reader()
            location = reader.get(Ip)

            a = (location['city']['names']['en'])
            b = (location['continent']['names']['en'])
            c = (location['country']['names']['en'])
            d = (location['location'])
            e = (location['postal'])
            f = (location['registered_country']['names']['en'])
            g = (location['subdivisions'][0]['names']['en'])

            print(f"\033[1;32m[+]\033[m \033[1;38mcity:\033[m \033[1;32m{a}\033[m")
            print(f"\033[1;32m[+]\033[m \033[1;38mcontinent:\033[m \033[1;32m{b}\033[m")
            print(f"\033[1;32m[+]\033[m \033[1;38mcountry:\033[m \033[1;32m{c}\033[m")
            print(f"\033[1;32m[+]\033[m \033[1;38mlocation:\033[m \033[1;32m{d}\033[m")
            print(f"\033[1;32m[+]\033[m \033[1;38mpostal:\033[m \033[1;32m{e}\033[m")
            print(f"\033[1;32m[+]\033[m \033[1;38mregistered_country:\033[m \033[1;32m{f}\033[m")
            print(f"\033[1;32m[+]\033[m \033[1;38msubdivisions:\033[m \033[1;32m{g}\033[m")

        myip = requests.get('https://api.ipify.org').text

        myIp(myip)

    # ==================================================================================================================


    option = yourOption(ReconOrCiphers)
    if option == "1" or option == "subdiscoverer":
        subdiscoverer()
    if option == "2" or option == "sublist3r":
        sublist3r()
    if option == "3" or option == "httpx":
        httpx()
    if option == "4" or option == "nmap":
        nmap()
    if option == "5" or option == "findir":
        findir()
    if option == "6" or option == "dirb":
        dirb()
    if option == "7" or option == "googlehacking":
        googleHacking()
    if option == "8" or option == "phattack":
        phattack()
    if option == "9" or option == "geolocation":
        geolocation()

    # ==================================================================================================================
