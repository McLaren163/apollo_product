import os

work_dir, _ = os.path.split(os.path.abspath(__file__))
os.chdir(work_dir)

import argparse
from tkinter import *

from config import ICON_FILE
from dandg_libs.gui import DoorGUI
from ext_libs.quitter import setAskOnCloseWin


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '-buyer', dest='buyer', help='Наименование заказчика')
    parser.add_argument('-o', '-order', dest='order', help='Номер заказа')
    parser.add_argument('-e', '-engineer', dest='engineer', help='ФИО инженера')
    parser.add_argument('-cfr', '-colorframe', dest='colorframe', help='Цвет рамы')
    parser.add_argument('-cfi', '-colorfill', dest='colorfill', help='Цвет заполнения')
    parser.add_argument('-W', '-width', dest='width', help='Ширина калитки')
    parser.add_argument('-H', '-height', dest='height', help='Высота калитки')
    parser.add_argument('-C', '-clearance', dest='clearance', help='Просвет')
    parser.add_argument('-br', '-bridge', dest='bridge', help='Перемычка')
    parser.add_argument('-brh', '-bridgeheight', dest='bridgeheight', help='Высота фрамуги')
    parser.add_argument('-open', dest='open', help='Открытие')
    parser.add_argument('-side', dest='side', help='Сторона петель')
    parser.add_argument('-fill', dest='fill', help='Заполнение')
    args = parser.parse_args()

    root = Tk()
    root.title('Калитка "АПОЛЛО"')
    root.iconbitmap(ICON_FILE)
    setAskOnCloseWin(root)
    props = {'buyer': args.buyer,
             'order': args.order,
             'engineer': args.engineer,
             'colorframe': args.colorframe,
             'colorfill': args.colorfill,
             'width': args.width,
             'height': args.height,
             'clearance': args.clearance,
             'bridge': args.bridge,
             'bridgeheight': args.bridgeheight,
             'open': args.open,
             'side': args.side,
             'fill': args.fill}
    DoorGUI(root, props).pack(expand=NO, fill=X)
    root.mainloop()


if __name__ == '__main__':
    main()
