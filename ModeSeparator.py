import ModesConfigures as cfg
from InputControl import cmdInput as input
class ms:
    def start(mode):
        if mode == 0:
            print('Create mode feture')
            tname = input('Table name:')
            source = input('Source file name:')
            cfg.initTable(tname,source)
            
    
        
