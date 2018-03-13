def long_long_function(address_read):

    address_write = 'truncated_{}'.format(address_read)
    with open(address_write, 'w') as file_write:

        with open(address_read) as file_read:
            position = -1
            quantity_n = 0
            text = ''
            while True:
                try:
                    file_read.seek(position, 2)
                except IOError:
                    break
                simbol = file_read.read(1)
                if simbol == '\n':
                    quantity_n += 1
                    position -= 1
                    if quantity_n == 10:
                        break
                position -= 1
                text = '{}{}'.format(simbol, text)
        file_write.write(text)

long_long_function('test_file.txt')