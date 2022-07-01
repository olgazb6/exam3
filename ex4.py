class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):                  # вывод в консоль букв алфавита
        print(self.letters)

    def letters_num(self):            # метод вернет количество букв в алфавите
        len(self.letters)

class EngAlphabet(Alphabet):

    def __init__(self):
        super().__init__('En', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')      #обозначение языка и строка,состоящая из всех букв алфавита

    __letters_num = 26                         #количество букв в англ алфавите

    def is_en_letter(self, letter):                 #проверка относится ли буква к англ алфавиту
        if letter in self.letters:
            return True
        else:
            return False

    def letters_num(self):                     #возвращает значение свойства __letters_num
        return EngAlphabet.__letters_num

    def example():
        print('Example text in English')

#Тесты
eng = EngAlphabet()
eng.print()
print(eng.letters_num())
print(eng.is_en_letter('F'))
print(eng.is_en_letter('Щ'))
EngAlphabet.example()

