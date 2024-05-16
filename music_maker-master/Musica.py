from Note import Note
import numpy as np
#
# # ESTOS SON LOS VALORES NUMERICOS QUE VA A TENER CADA NOTA
# values = {
#     'C0': 0
#     , 'C#0': 1
#     , 'D0': 2
#     , 'Eb0': 3
#     , 'E0': 4
#     , 'F0': 5
#     , 'F#0': 6
#     , 'G0': 7
#     , 'Ab0': 8
#     , 'A0': 9
#     , 'Bb0': 10
#     , 'B0': 11
#     , 'C1': 12
#     , 'C#1': 13
#     , 'D1': 14
#     , 'Eb1': 15
#     , 'E1': 16
#     , 'F1': 17
#     , 'F#1': 18
#     , 'G1': 19
#     , 'Ab1': 20
#     , 'A1': 21
#     , 'Bb1': 22
#     , 'B1': 23
#     , 'C2': 24
#     , 'C#2': 25
#     , 'D2': 26
#     , 'Eb2': 27
#     , 'E2': 28
#     , 'F2': 29
#     , 'F#2': 30
#     , 'G2': 31
#     , 'Ab2': 32
#     , 'A2': 33
#     , 'Bb2': 34
#     , 'B2': 35
#     , 'C3': 36
#     , 'C#3': 37
#     , 'D3': 38
#     , 'Eb3': 39
#     , 'E3': 40
#     , 'F3': 41
#     , 'F#3': 42
#     , 'G3': 43
#     , 'Ab3': 44
#     , 'A3': 45
#     , 'Bb3': 46
#     , 'B3': 47
#     , 'C4': 48
#     , 'C#4': 49
#     , 'D4': 50
#     , 'Eb4': 51
#     , 'E4': 52
#     , 'F4': 53
#     , 'F#4': 54
#     , 'G4': 55
#     , 'Ab4': 56
#     , 'A4': 57
#     , 'Bb4': 58
#     , 'B4': 59
#     , 'C5': 60
#     , 'C#5': 61
#     , 'D5': 62
#     , 'Eb5': 63
#     , 'E5': 64
#     , 'F5': 65
#     , 'F#5': 66
#     , 'G5': 67
#     , 'Ab5': 68
#     , 'A5': 69
#     , 'Bb5': 70
#     , 'B5': 71
#     , 'C6': 72
#     , 'C#6': 73
#     , 'D6': 74
#     , 'Eb6': 75
#     , 'E6': 76
#     , 'F6': 77
#     , 'F#6': 78
#     , 'G6': 79
#     , 'Ab6': 80
#     , 'A6': 81
#     , 'Bb6': 82
#     , 'B6': 83
#     , 'C7': 84
#     , 'C#7': 85
#     , 'D7': 86
#     , 'Eb7': 87
#     , 'E7': 88
#     , 'F7': 89
#     , 'F#7': 90
#     , 'G7': 91
#     , 'Ab7': 92
#     , 'A7': 93
#     , 'Bb7': 94
#     , 'B7': 95
#     , 'C8': 96
#     , 'C#8': 97
#     , 'D8': 98
#     , 'Eb8': 99
#     , 'E8': 100
#     , 'F8': 101
#     , 'F#8': 102
#     , 'G8': 103
#     , 'Ab8': 104
#     , 'A8': 105
#     , 'Bb8': 106
#     , 'B8': 107
#
# }
#
#
# class Linked:
#     def __init__(self):
#         self.head = None
#
#     def insertAtBegin(self, data, duration):
#         new_node = Note(data, duration)
#         if self.head is None:
#             self.head = new_node
#             return
#         else:
#             new_node.next = self.head
#             self.head = new_node
#
#     def insertAtEnd(self, data, duration):
#         new_node = Note(data, duration)
#         if self.head is None:
#             self.head = new_node
#             return
#         current_node = self.head
#         while current_node.next:
#             current_node = current_node.next
#
#         current_node.next = new_node
#
#     def insert_silence(self, duration):
#
#         new_node = Note.rest(duration)
#         if self.head is None:
#             self.head = new_node
#             return
#         current_node = self.head
#         while current_node.next:
#             current_node = current_node.next
#
#         current_node.next = new_node
#
#     def tocar(self):
#
#         curr = self.head
#         while curr:
#             curr.play()
#             curr = curr.next
#
#     def imprimirNotas(self):
#         curr = self.head
#         while curr:
#             try:
#                 print(curr.note)
#                 curr = curr.next
#             except:
#
#                 print('silencio')
#                 curr = curr.next
#
#
# linked = Linked()
# linked.insertAtEnd('F4', 0.5)
# linked.insertAtEnd('g4', 0.5)
# linked.insertAtEnd('F4', 0.5)
# linked.insertAtEnd('Bb4', 0.5)
# linked.insertAtEnd('a4', 1)
# linked.insertAtEnd('F4', 0.5)
# linked.insertAtEnd('g4', 0.5)
# linked.insertAtEnd('F4', 0.5)
# linked.insertAtEnd('C5', 0.5)
# linked.insertAtEnd('Bb4', 1)
# linked.tocar()
# linked.imprimirNotas()
#



# def playA():
#     nota = Note('A4', 0.1)
#     nota.play()
#     nota = Note.rest(0.08)
#     nota.play()
#     nota = Note('A4', 0.2)
#     nota.play()
# playA()
#
# def playE():
#     nota = Note('E4', 0.1)
#     nota.play()
#     nota = Note.rest(0.08)
#     nota.play()
#     nota = Note('E4', 0.2)
#     nota.play()
# playA()
# def playB():
#     nota = Note('B4', 0.1)
#     nota.play()
#     nota = Note.rest(0.08)
#     nota.play()
#     nota = Note('B4', 0.2)
#     nota.play()
# playA()
# def playA():
#     nota = Note('A4', 0.1)
#     nota.play()
#     nota = Note.rest(0.08)
#     nota.play()
#     nota = Note('A4', 0.2)
#     nota.play()
# playA()
# def playA():
#     nota = Note('A4', 0.1)
#     nota.play()
#     nota = Note.rest(0.08)
#     nota.play()
#     nota = Note('A4', 0.2)
#     nota.play()
# playA()


# por Leidy Carolina Obando Figueroa y imon  Martiez
class Node:
    def __init__(self, value, code):
        self.left = None
        self.right = None
        self.value = value
        self.code = code


class BinarySearchTree:
    def __init__(self):
        self.root = Node('', '')

    def insert(self, letter, code):
        if self.root is None:
            self.root = Node(letter, code)
        else:
            current_node = self.root
            for symbol in code:
                if symbol == ".":
                    if current_node.left is None:
                        current_node.left = Node(letter, code)
                    current_node = current_node.left
                elif symbol == "-":
                    if current_node.right is None:
                        current_node.right = Node(letter, code)
                    current_node = current_node.right

    #        codigo para traducir de morse a alfabeto

    def translateMorse(self, code):
        current = self.root
        for character in code:
            if character == '.':
                current = current.left
            else:
                current = current.right
        return current.value

    def translateToAlphabet(self, frase):
        ans = ''

        frases = frase.split('/')
        for word in frases:
            word = word.split(' ')
            for i in word:
                if self.translateMorse(i).isnumeric():
                    ans += ' '
                    ans += (self.translateMorse(i))
                    ans += ' '
                else:
                    ans += (self.translateMorse(i))

            ans += ' '
        return ans[:-1]


    # codigo para traducir de alfabeto a morse

    def lookup(self, node, value):
        current_node = node
        while current_node:
            if current_node.value == value:
                return current_node.code
            else:
                return self.lookup(current_node.left, value), self.lookup(current_node.right, value)

    def flatten_tuple(self, nested_tuple):
        flattened_list = []
        for item in nested_tuple:
            if isinstance(item, tuple):
                flattened_list.extend(self.flatten_tuple(item))
            elif item is not None:
                flattened_list.append(item)
        return flattened_list
    def morseOfLetter(self,letter):
        return self.flatten_tuple(self.lookup(self.root,letter))

    def translateToMorse(self, message):
        ans = ''
        for i in message:
            if i == ' ':
                ans += '/'
            else:
                ans += f'{self.morseOfLetter(i)[0]} '
        return ans[:-1]






codigo_morse = {
    # primer nivel
    "e": ".", "t": "-",
    # segundo nivel
    "m": "--", "n": "-.", "i": "..", "a": ".-",
    # tercer nivel
    "s": "...", "u": "..-", "r": ".-.", "w": ".--", "d": "-..", "k": "-.-", "g": "--.", "o": "---",
    # cuarto nivel
    "b": "-...", "c": "-.-.", "f": "..-.", "h": "....",
    "j": ".---", "l": ".-..", "p": ".--.", "q": "--.-",
    "v": "...-", "x": "-..-", "y": "-.--", "z": "--..", " ": "---.", "  ": "----", "": "..--", "     ": ".-.-",
    #     quinto nivel
    "5": ".....", "4": "....-", "2": "..---", "1": ".----", "6": "-....", "7": "--...",
    '0': "-----", '9': "----.", "8": "---..", "3": "...--", "+": ".-.-.", "=": "-...-", "/": "-..-."
}

tree = BinarySearchTree()
for key, item in codigo_morse.items():
    tree.insert(key, item)


# ------------------ la creacion del arbol va hasta aqui ----------------------

#    este metodo filtra la informacion que adquirimos del metodo loopup que tiene el arbol, ya que este retornaba una lista con otras muchas listas


def tocar(frase):
    frase = frase.lower()
    alturas = 'abcdefg'
    for i in frase.lower():
        if i in alturas:
            for j in codigo_morse[i]:
                if j == '-':
                    note = Note(f'{i}4',0.2)
                    note.play()
                elif j == '.':
                    note = Note(f'{i}4', 0.1)
                    note.play()

                nota = Note.rest(0.08)
                nota.play()
        nota = Note.rest(0.03)
        nota.play()


#     nota = Note('E4', 0.1)
#     nota.play()
#     nota = Note.rest(0.08)
#     nota.play()
#     nota = Note('E4', 0.2)
#     nota.play()





while True:
    print("Opciones:")
    print("1. traducir de morse a alfabeto")
    print("2. traducir del alfabeto a morse")
    print("3. traducir una frase de alfabeto a morse")
    print("4. Tocar morse con ABCDEFG")

    ans = input('eleccion:')

    if(ans == '1'):

        message = input('mensaje:').lower()
        print('traducción:')
        print(f'traduccion: "{tree.translateToAlphabet(message)}"\n')

    elif (ans == '2'):
        message = input('mensaje:').lower()
        print('traducción:')
        print(f'traduccion: "{tree.translateToMorse(message)}"\n')

    elif (ans == '3'):
        message = input('mensaje:').lower()
        print('traducción:')
        print(f'traduccion: "{tree.translateToMorse(message)}"\n')
    elif (ans == '4'):
        message = input('mensaje:').lower()
        tocar(message)

# melodia
