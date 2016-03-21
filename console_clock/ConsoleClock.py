# -*- coding: utf-8 -*-
import time
import thread
from Tkinter import *

num0 = ('*****', '*   *', '*   *', '*   *', '*****')
num1 = ('  *  ', '  *  ', '  *  ', '  *  ', '  *  ')
num2 = ('*****', '    *', '*****', '*    ', '*****')
num3 = ('*****', '    *', '*****', '    *', '*****')
num4 = ('*   *', '*   *', '*****', '    *', '    *')
num5 = ('*****', '*    ', '*****', '    *', '*****')
num6 = ('*****', '*    ', '*****', '*   *', '*****')
num7 = ('*****', '    *', '    *', '    *', '    *')
num8 = ('*****', '*   *', '*****', '*   *', '*****')
num9 = ('*****', '*   *', '*****', '    *', '*****')
num = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]


def main():
    top = Tk()
    # 进入消息循环

    t = formatClock()
    label = Label(top, text=t, command=cmd)
    label.setvar = t
    label.pack()
    top.mainloop()


def cmd():
    while True:

        time.sleep(1)
        t = formatClock()


def formatClock():

    t = clock()
    tm_hour = t[3]
    tm_min = t[4]
    tm_sec = t[5]
    nums = [tm_hour / 10, tm_hour % 10, 0, tm_min / 10,
            tm_min % 10, 0, tm_sec / 10, tm_sec % 10]
    str = ''
    for i in range(0, 5):
        for j in range(len(nums)):
            if j != 2 and j != 5:
                n = nums[j]
                str = str + num[n][i] + " "
            else:
                if (i == 2):
                    str = str + "  **  "
                else:
                    str = str + "      "
        str = str + '\n'

    return str


def clock():
    localtime = time.localtime(time.time())
    return localtime


if __name__ == '__main__':
    main()
