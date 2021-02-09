ls0 = [' ', '|', ' ', '|', ' ']
ls1 = [' ', '|', ' ', '|', ' ']
ls2 = [' ', '|', ' ', '|', ' ']

def printer():
    print()
    print(''.join(ls0))
    print('-----')
    print(''.join(ls1))
    print('-----')
    print(''.join(ls2)) 
    print()

while True:
    ls = []
    coordinates = input()
    for i in coordinates:
        ls.append(i)
    x = int(ls[0])
    y = int(ls[2])

    if y == 0:
        if x == 0:
            ls0[0] = 'X'
        if x == 1:
            ls0[2] = 'X'
        if x == 2:
            ls0[4] = 'X'
    if y == 1:
        if x == 0:
            ls1[0] = 'X'
        if x == 1:
            ls1[2] = 'X'
        if x == 2:
            ls1[4] = 'X'    
    if y == 2:
        if x == 0:
            ls2[0] = 'X'
        if x == 1:
            ls2[2] = 'X'
        if x == 2:
            ls2[4] = 'X'


    if ls0[0] == 'X' and ls1[0] == 'X' and ls2[0] == 'X':
        print('X wins!')
        printer()
        break
    if ls0[2] == 'X' and ls1[2] == 'X' and ls2[2] == 'X':
        print('X wins!')
        printer()
        break
    if ls0[4] == 'X' and ls1[4] == 'X' and ls2[4] == 'X':
        print('X wins!')
        print()
        print(''.join(ls0))
        print('-----')
        print(''.join(ls1))
        print('-----')
        print(''.join(ls2))    
        print()     
        break
    if ls0[0] == 'O' and ls1[0] == 'O' and ls2[0] == 'O':
        print('O wins!')
        printer()
        break
    if ls0[2] == 'O' and ls1[2] == 'O' and ls2[2] == 'O':
        print('O wins!')
        printer()
        break
    if ls0[4] == 'O' and ls1[4] == 'O' and ls2[4] == 'O':
        print('O wins!')
        printer()
        break
    if ls0[0] == 'X' and ls0[2] == 'X' and ls0[4] == 'X':
        print('X wins!')
        printer()
        break
    if ls1[0] == 'X' and ls1[2] == 'X' and ls1[4] == 'X':
        print('X wins!')
        printer()
        break
    if ls2[0] == 'X' and ls2[2] == 'X' and ls2[4] == 'X':
        print('X wins!')
        printer()
        break    
    if ls0[0] == 'O' and ls0[2] == 'O' and ls0[4] == 'O':
        print('O wins!')
        printer()
        break
    if ls1[0] == 'O' and ls1[2] == 'O' and ls1[4] == 'O':
        print('O wins!')
        printer()
        break
    if ls2[0] == 'O' and ls2[2] == 'O' and ls2[4] == 'O':
        print('O wins!')
        printer()
        break
    if ls0[0] == 'X' and ls1[2] == 'X' and ls2[4] == 'X':
        print('X wins!')
        printer()
        break      
    if ls0[0] == 'O' and ls1[2] == 'O' and ls2[4] == 'O':
        print('O wins!')
        printer()
        break  
    if ls0[4] == 'X' and ls1[2] == 'X' and ls2[0] == 'X':
        print('X wins!')
        printer()
        break   
    if ls0[4] == 'O' and ls1[2] == 'O' and ls2[0] == 'O':
        print('O wins!')
        printer()
        break
    if ls0[0] != ' ' and ls0[2] != ' ' and ls0[4] != ' ' and ls1[0] != ' ' and ls1[2] != ' ' and ls1[4] != ' ' and ls2[0] != ' ' and ls2[2] != ' ' and ls2[4] != ' ':
        print('Draw')
        printer()
        break

    else:
        printer()

    ps = []
    coordinates = input()
    for i in coordinates:
        ps.append(i)
    x = int(ps[0])
    y = int(ps[2])

    if y == 0:
        if x == 0:
            ls0[0] = 'O'
        if x == 1:
            ls0[2] = 'O'
        if x == 2:
            ls0[4] = 'O'
    if y == 1:
        if x == 0:
            ls1[0] = 'O'
        if x == 1:
            ls1[2] = 'O'
        if x == 2:
            ls1[4] = 'O'    
    if y == 2:
        if x == 0:
            ls2[0] = 'O'
        if x == 1:
            ls2[2] = 'O'
        if x == 2:
            ls2[4] = 'O'

    if ls0[0] == 'X' and ls1[0] == 'X' and ls2[0] == 'X':
        print('X wins!')
        printer()
        break
    if ls0[2] == 'X' and ls1[2] == 'X' and ls2[2] == 'X':
        print('X wins!')
        printer()
        break
    if ls0[4] == 'X' and ls1[4] == 'X' and ls2[4] == 'X':
        print('X wins!')
        printer()
        break
    if ls0[0] == 'O' and ls1[0] == 'O' and ls2[0] == 'O':
        print('O wins!')
        printer()
        break
    if ls0[2] == 'O' and ls1[2] == 'O' and ls2[2] == 'O':
        print('O wins!')
        printer()
        break
    if ls0[4] == 'O' and ls1[4] == 'O' and ls2[4] == 'O':
        print('O wins!')
        printer()
        break
    if ls0[0] == 'X' and ls0[2] == 'X' and ls0[4] == 'X':
        print('X wins!')
        printer()
        break
    if ls1[0] == 'X' and ls1[2] == 'X' and ls1[4] == 'X':
        print('X wins!')
        printer()
        break
    if ls2[0] == 'X' and ls2[2] == 'X' and ls2[4] == 'X':
        print('X wins!')
        printer()
        break    
    if ls0[0] == 'O' and ls0[2] == 'O' and ls0[4] == 'O':
        print('O wins!')
        printer()
        break
    if ls1[0] == 'O' and ls1[2] == 'O' and ls1[4] == 'O':
        print('O wins!')
        printer()
        break
    if ls2[0] == 'O' and ls2[2] == 'O' and ls2[4] == 'O':
        print('O wins!')
        printer()
        break
    if ls0[0] == 'X' and ls1[2] == 'X' and ls2[4] == 'X':
        print('X wins!')
        printer()
        break      
    if ls0[0] == 'O' and ls1[2] == 'O' and ls2[4] == 'O':
        print('O wins!')
        printer()
        break  
    if ls0[4] == 'X' and ls1[2] == 'X' and ls2[0] == 'X':
        print('X wins!')
        printer()
        break   
    if ls0[4] == 'O' and ls1[2] == 'O' and ls2[0] == 'O':
        print('O wins!')
        printer()
        break
    if ls0[0] != ' ' and ls0[2] != ' ' and ls0[4] != ' ' and ls1[0] != ' ' and ls1[2] != ' ' and ls1[4] != ' ' and ls2[0] != ' ' and ls2[2] != ' ' and ls2[4] != ' ':
        print('Draw')
        printer()
        break

    else:
        printer()