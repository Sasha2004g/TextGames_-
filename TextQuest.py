print('Здравствуйте. Вы очнулись в заброшенном осабнике на 3 этаже.')
print('Перед вами 3 прохода под номерами: 1, 2 или 3.')
print('В первом проходе вы видите пропасть, за второй лестницу вниз, за третьей злая собака на цепи')
b1 = input()
if b1 == '3':
    print('Вас съела собака')
elif b1 == '1':
    print('Вы прошли в пропасть')
if b1 == '2':
    print('Вы на первом этаже')
    print('Выход отсюда возможен через 2 двери.')
    print('Дверь справа под номером 1, дверь слева под номером 2,')
    print('над дверью слева написано: выход в двери под номером 2.')
    print('Выход справа или слева?')
    c2 = input()
    if c2 == 'справа':
        print('Вы открыли правую дверь. Но за ней вас подстерегал крокодил ')
    elif c2 == 'слева':
        print('Вы на улице!')
