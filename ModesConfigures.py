import sqlite3
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
            table_name txt not null,
            size INTEGER not null,
            enf txt not null,
            def txt not null
        )''')
    except:
        pass
    finally:
        modules=rst('SELECT id,table_name,size,enf,def FROM init').col('table_name')
    print('Modules loaded.')

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
        print(str(self.rows))
        colindex = self.cols.index(col)
        print(str(colindex))
        for row in self.rows:
            print(str(row[1]))
            l.append(row[colindex])
        return l
    
    def __init__(self,sql):
        self.cols = self.getFromSql(sql)
        self.rows = list(cursor.execute(sql))
#cfg.modules.append(modeEntity('五十音图'))
