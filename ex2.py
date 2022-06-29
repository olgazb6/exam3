# Напишите функцию, которая проверяет: является ли слово палиндромом

def fact(n):
    if len(n)<1:
        return True
    if n[0] != n[-1]:
        return False
    return fact(n[1:-1])

print(fact('шалаш'))