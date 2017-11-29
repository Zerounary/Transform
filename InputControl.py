# -*-  coding: utf-8 -*-
def runCmd(cmd):
    if cmd.startswith('chk'):
        args = cmd.split(' ')
        op = args[1]
        try:
            if isinstance(eval(op),list):
                for i in range(len(eval(op))):
                    print('%2d:\t%s'%(i,eval(op)[i]))
                else:
                    print(eval(op))
        except NameError as namerr:
            print(namerr)
            pass
def cmdInput(t=''):
    txt = input(t)
    if txt[0] == ':':
        runCmd(txt[1:])
    return txt       
class ic:
    def mode():
        mode = input()
        while(not mode.isdigit()):
            print('Please input a number.')
            mode = input('>')
        return int(mode)
    def load(fileName):
        f = open('files/' + fileName,'r')
        f.read() 
        

    
