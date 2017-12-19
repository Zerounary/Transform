# -*- coding: utf8 -*-
import sqlite3
import random
from ModesConfigures import rst
conn = sqlite3.connect('Transform.db')
cursor = conn.cursor()
table = ''
yesno = 'no'
isKey = True
r = rst
rows = []
virtual=[]
getItems = lambda t:cursor.execute('SELECT fact,c1,c0 FROM %s'%(t))
flush = lambda t,l:cursor.execute('UPDATE %s SET key=?,value=?,yes=?,no=? WHERE id=?'%(t),(l[1],l[2],l[3],l[4],l[0]))


def dumpRst():
    global r
    for row in r.rows:
        #print(table)
        #print(row)
        flush(table,row)
    conn.commit()

restrict = lambda j,coper:sum(coper)-coper[j]+sum(virtual)-virtual[j]
def getIndex():
    global r,virtual,yesno
    keys = r.col('key')
    coper = r.col(yesno)
    counter=[0 for i in range(len(keys))]
    index = -1
    flag = True
    while(flag):
        i = random.randint(0,len(keys)-1)
        counter[i]+=1
        for j in range(len(keys)):
            try:
                if restrict(j,coper) == counter[j]:
                    index = i
                    flag = False
                    break
            except IndexError as iderr:
                print(iderr,'j:%d,len(coper):%d'%(j,len(coper)))
                break;
    return index
def runCmd(cmd):
    global virtual,isKey,yesno
    if cmd.startswith(':q'):
        dumpRst()
    elif cmd.startswith(':e'):
        arg = cmd[3:]
        try:
            exec(arg)
        except NameError as namerr:
            print(namerr)
            pass
        except:
            print('未知错误')
            pass
    elif cmd.startswith(':vf'):
        args = cmd.split(' ')
        cmd = 0
        scope = 1
        num = 2
        print(args)
        #print('-' in args[scope] )
        if '-' in args[scope]:
            rtl = args[scope].split('-')
            try:
                l = int(rtl[0])
                r = int(rtl[1])
                n = int(args[num])
                for i in range(l,r+1):
                    virtual[i] = n
            except ValueError as valerr:
                print(valerr)
            except IndexError as iderr:
                print(iderr)
        elif args[scope].isdecimal():
            try:
                idx = int(args[scope])
                print(idx)
                n = int(args[num])
                virtual[idx] = n
                print(virtual)
            except ValueError as valerr:
                print(valerr)
            except IndexError as iderr:
                print(iderr)
        else:
            print('命令格式:\t:vf startIndex-endIndex virtualNumber')
    elif cmd.startswith(':chk'):
            args = cmd.split(' ')
            try:
                if isinstance(eval(args[1]),list):
                    for i in range(len(eval(args[1]))):
                        print('%2d:\t%s'%(i,eval(args[1])[i]))
                else:
                    print(eval(args[1]))
            except NameError as namerr:
                print(namerr)
                pass
    elif cmd.startswith(':mode'):
        
        args = cmd.split(' ')
        arg = args[1]
        if arg == 'key':
            isKey=True
        elif arg =='value':
            isKey=False
        elif arg == 'yes':
            yesno='yes'
        elif arg =='no':
            yesno='no'
        else:
            print('No feature with %s'%(arg))
        
    else:
        print('No feature with %s'%(answer))
def go(tname):
    global r,virtual,table,isKey
    table = tname
    r = rst('SELECT id,key,value,yes,no FROM %s'%(tname))
    virtual=[0 for i in range(len(r.col('key')))]
    answer = 'go'
    while(answer !=':q'):
        index = getIndex()
        if isKey:
            print(r.key(index))
        else:
            print(r.value(index))
        answer = input()
        value = ''
        if isKey:
            value = r.value(index)
        else:
            value = r.key(index)
        try:
            if(answer[0] !=':'):
                try:
                    if(answer == value):
                        print('\n+')
                        r.yes(index)
                    else:
                        print('\n' + str(value))
                        r.no(index)
                except TypeError as typerr:
                    print('Bad input:',typerr)
                    continue
                except SyntaxError as synerr:
                    #eval不能解析空串,当check_f为eval时会出这个错
                    print('Bad input:',synerr)
                    continue
                except NameError as namerr:
                    print('Bad input:',namerr)
                    continue
                except ValueError as valerr:
                    print('Bad input:',valerr)
            else:
                #print('runCmd')
                runCmd(answer)
            print('\n')
        except IndexError as idxerr:
            print(idxerr)
            pass
