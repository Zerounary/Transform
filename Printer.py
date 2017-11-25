import ModesConfigures as cfg
class ptr:

    def menu():
        mds = cfg.modules
        print('0.创建映射表')
        for i in range(0,len(mds)):
            print(str(i+1) + '.' + mds[i][1])

    def help():
        print('Help')
