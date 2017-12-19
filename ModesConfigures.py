import sqlite3
import configparser
import os
conf = configparser.ConfigParser()
conf_encoding='utf-8-sig'
source_path='sources/'
conn = sqlite3.connect('Transform.db')
cursor = conn.cursor()
modules=[]
virtual=[]
def init():
    global modules
    try:
        cursor.execute('''
        CREATE TABLE init(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            table_name txt not null unique,
            kvf txt not null,
            vkf txt not null
        )''')
    except:
        pass
    finally:
        modules=rst('SELECT id,table_name,kvf,vkf FROM init').col('table_name')
    print('Modules loaded.')

def initTable(tname,source):
    #try:
    cursor.execute('''
    CREATE TABLE %s(
        id   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        key   TXT     NOT NULL,
        value TXT     not null,
        yes  INTEGER  default 0,
        no   INTEGER  default 0
    )'''%(tname))
    fname = source_path +source+'.ini'
    while not os.path.exists(fname):
        fname = input('Source not exists:')
    conf.read(fname,encoding=conf_encoding)
    l = conf.items('key-value')
    print(l)
    k_f = source_path + source+'_k.py'
    v_f = source_path + source+'_v.py'
    while not os.path.exists(k_f) or not os.path.exists(v_f):
        print(k_f + ' or ' + v_f + ' not exists.')
        input()
    kvf = open(k_f).read()
    print(type(kvf))
    print(kvf)
    vkf = open(v_f).read()
    print(type(vkf))
    print(vkf)
    cursor.executemany('''
    INSERT INTO %s (key,value)
    VALUES (?,?)'''%(tname),l)
    cursor.execute('INSERT INTO init(table_name,kvf,vkf) values(?,?,?)',(tname,kvf,vkf))
    conn.commit()
    print('OK!')
    #except:
    #   cursor.execute('DROP TABLE %s'%(tname))
    #    print('Init table fail!')
        
        

class rst:
    rows = []
    cols = []
    def getFromSql(self,sql):
        i1 = sql.index('SELECT') + len('SELECT')
        i2 = sql.index('FROM')
        cstr = sql[i1:i2].strip()
        return cstr.split(',')
    def col(self,col):
        l = []
        #print(str(self.rows))
        colindex = self.cols.index(col)
        #print(str(colindex))
        for row in self.rows:
            #print(str(row[1]))
            l.append(row[colindex])
        return l
    def set(self,sql):
        self.cols = self.getFromSql(sql)
        l=[]
        self.rows = list(cursor.execute(sql))
        for r in self.rows:
            l.append(list(r))
        self.rows = l
    def key(self,index):
        row = self.rows[index]
        #print(row)
        i = self.cols.index('key')
        return row[i]
    def yes(self,index):
        row = self.rows[index]
        #print('org:' + str(row))
        i = self.cols.index('yes')
        row[i] = row[i] + 1
        #print('chg:' + str(row))
        #print('rows:' + str(self.rows))
    def no(self,index):
        row = self.rows[index]
        #print('org:' + str(row))
        i = self.cols.index('no')
        row[i] = row[i] + 1
        #print('chg:' + str(row))
        #print('rows:' + str(self.rows))
    def value(self,index):
        row = self.rows[index]
        i = self.cols.index('value')
        return row[i]
        #print(row)
    def __init__(self,sql):
        self.cols = self.getFromSql(sql)
        l=[]
        self.rows = list(cursor.execute(sql))
        for r in self.rows:
            l.append(list(r))
        self.rows = l
        
        
#cfg.modules.append(modeEntity('五十音图'))
