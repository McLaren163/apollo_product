from tkinter import *
from tkinter.messagebox import askokcancel

class Quitter(Frame):
    def __init__(self, parent=None, **option):
        Frame.__init__(self, parent)
        self.pack()
        btn = Button(self, text='Quit', command=lambda: askQuit(self), **option)
        btn.pack(side=RIGHT, expand=NO, fill=BOTH)


class QuitButton(Button):
    def __init__(self, parent=None, **option):
        super().__init__(parent)
        self.config(text='Quit', command=lambda: askQuit(parent), **option)


def setAskOnCloseWin(root):
    root.protocol('WM_DELETE_WINDOW', lambda: askQuit(root))

def askQuit(root):
    ans = askokcancel('Подтверждение выхода', 'Закрыть программу?')
    if ans:
        root.quit()
