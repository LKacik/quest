def door_mat(width: int):

    length = 3 * width

    for i in range(1, width, 2):
        print(str('.|.' * i).center(length, '-'))
    print('WELCOME'.center(length, '-'))
    for i in range(width - 2, 0, -2):
        print(str('.|.' * i).center(length, '-'))
