def best_value():
    print('start')
    run = True
    values = []
    while run == True:
        x = input('Enter odds or enter x to exit: ')
        y = input('Enter odds or enter x to exit: ')
        if x == 'x':
            run = False

        values.append(x)
    print(values)

best_value()