import ModesConfigures as cfg
from Printer import ptr
from InputControl import ic
from ModeSeparator import ms

if __name__ == "__main__":
    cfg.init()
    ptr.menu()
    ms.start(ic.mode())
