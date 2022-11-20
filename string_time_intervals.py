'''Sa se scrie o functie care primeste ca parametri 2 intregi start_hour (ex. 9)
si end_hour (ex. 17), si genereaza o lista
 de string-uri de intervale orare: ['9:00 - 10:00', '10:00 - 11:00', ..., '16:00 - 17:00'. '''


def interval_orar(start, final):
    if start.isalpha() or final.isalpha():
        return 'invalid'
    else:
        return [f'{i}:00 - {i + 1}:00' for i in range(start, final)]
#
#
# print(interval_orar('aa', 'bb'))
for i in range(4, 0, -2):
    print(i)
