import ModesConfigures as cfg
from InputControl import cmdInput as input
import Interaction as action
class ms:
    def start(mode):
        if mode == 0:
            print('Create mode feture')
            tname = input('Table name:')
            source = input('Source file name:')
            cfg.initTable(tname,source)
        else:
            tname = cfg.modules[mode-1]
            action.go(tname)
            
            
    
        
