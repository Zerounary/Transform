class ic:
    def mode():
        mode = input('>')
        while(not mode.isdigit()):
            print('Please input a number.')
            mode = input('>')
        return int(mode)
