# -*- coding: utf-8 -*-

from time import *
from thread import *
from Tkinter import *


def initUI():
    root = Tk()

    btn1 = Button(root, text="1")
    btn2 = Button(root, text="2")
    btn3 = Button(root, text="3")
    btn4 = Button(root, text="4")
    btn5 = Button(root, text="5")
    btn6 = Button(root, text="6")
    btn7 = Button(root, text="7")
    btn8 = Button(root, text="8")
    btn9 = Button(root, text="9")
    btn0 = Button(root, text="0")
    btn1.pack(side=LEFT)
    btn2.pack(after=btn1)
    btn3.pack(after=btn2)
    # 进入消息循环
    root.mainloop()


def main():
    initUI()

if __name__ == '__main__':
    main()
