



class UnicodeGenerator:
    def __init__(self):
        pass

    def generate_unicode(self, start, end):
        for i in range(start, end+1):
            yield chr(i)



unicode_gen = UnicodeGenerator()


while True:
    start = int(input("\n\nСогласно стандарту Юникод, всего существует **137,929** кодовых точек, которые могут быть использованы для представления символов из разных языков.\n\nЧтобы это посмотреть, \nВведите начало диапазона символов в Юникоде (или 0 для выхода): "))
    if start == 0:
        print("\nПрограмма завершена.")
        break
    end = int(input("\nВведите конец диапазона символов в Юникоде: "))
    for char in unicode_gen.generate_unicode(start, end):
        print(char, end='   ')










