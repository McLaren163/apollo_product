from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageFont, ImageDraw

from config import *
from dandg_libs.door import DoorStreet
from dandg_libs.exeptions import *
from dandg_libs.widgets import LabelEntryBlock, ListBoxTableBlock, TextBlock, AboutLabel, PreviewWin


class DoorGUI(Frame):
    def __init__(self, parent, setup_values):
        super().__init__(parent)
        self.door = None
        self.data = {}
        self.door_type = {}
        self._makeWidgets()
        self.setValues(**setup_values)

    def _makeWidgets(self):
        frm_buttons = Frame(self)
        Button(frm_buttons, text='Чертеж', command=self.start).pack(side=RIGHT, padx=3, pady=3)
        about = AboutLabel(frm_buttons)
        about.pack(side=LEFT, fill=X, padx=3, pady=3)
        frm_buttons.pack(side=BOTTOM, expand=NO, fill=X)

        frm_widgets = Frame(self)

        self.blocks = []

        self.order = order = LabelEntryBlock(frm_widgets, name=ORDERING_INFO[0], labels=ORDERING_INFO[1])
        order.grid(row=0, column=1, sticky='new', padx=3, pady=3)
        self.blocks.append(order)

        doorway = LabelEntryBlock(frm_widgets, name=DOORWAY_INFO[0], labels=DOORWAY_INFO[1])
        doorway.grid(row=1, column=1, sticky='new', padx=3, pady=3)
        self.blocks.append(doorway)

        self.color = color = LabelEntryBlock(frm_widgets, name=COLORING_INFO[0], labels=COLORING_INFO[1])
        color.grid(row=2, column=1, sticky='new', padx=3, pady=3)
        self.blocks.append(color)

        self.door = door = LabelEntryBlock(frm_widgets, name=DOOR_PARAM[0], labels=DOOR_PARAM[1])
        door.grid(row=0, column=0, rowspan=3, sticky='new', padx=3, pady=3)
        self.blocks.append(door)

        kit = ListBoxTableBlock(frm_widgets, name='Комплектация',
                                column_names=('Наименование', 'Кол-во'),
                                menu_items=DOOR_ITEMS)
        kit.grid(row=3, column=0, sticky='new', padx=3, pady=3)
        self.blocks.append(kit)

        extra = ListBoxTableBlock(frm_widgets, name='Дополнительно',
                                  column_names=('Наименование', 'Размер', 'Цвет', 'Кол-во'),
                                  menu_items=METALL_ITEMS)
        extra.grid(row=3, column=1, sticky='new', padx=3, pady=3)
        self.blocks.append(extra)

        note = TextBlock(frm_widgets, name='Примечание')
        note.grid(row=4, columnspan=2, sticky='new', padx=3, pady=3)
        self.blocks.append(note)

        frm_widgets.columnconfigure(0, weight=1)
        frm_widgets.columnconfigure(1, weight=1)

        frm_widgets.pack(side=TOP, expand=NO, fill=X)

    def setValues(self, buyer=None, order=None, engineer=None, colorframe=None, colorfill=None,
                  width=None, height=None, clearance=None, bridge=None, bridgeheight=None,
                  open=None, side=None, fill=None):
        order_props = {}
        if buyer:
            order_props['Заказчик'] = buyer
        if order:
            order_props['№ Заказа'] = order
        if engineer:
            order_props['Инженер'] = engineer
        color_props = {}
        if colorframe:
            color_props['Цвет рамы'] = colorframe
        if colorfill:
            color_props['Цвет заполнения'] = colorfill
        door_props = {}
        if width:
            door_props['Ширина рамы'] = width
        if height:
            door_props['Высота рамы'] = height
        if clearance:
            door_props['Просвет'] = clearance
        if bridge in DOOR_BRIDGE:
            door_props['Перемычка'] = bridge
        if bridgeheight:
            door_props['Высота фрамуги'] = bridgeheight
        if open in DOOR_OPENING:
            door_props['Открытие'] = open
        if side in DOOR_SIDE:
            door_props['Петли'] = side
        if fill in FILLING:
            door_props['Заполнение'] = fill
        self.order.setValues(order_props)
        self.color.setValues(color_props)
        self.door.setValues(door_props)

    def start(self):
        try:
            self._collectValues()
            self._render()
        except ApolloEx as ex:
            messagebox.showerror('Ошибка', ex)

    def _collectValues(self):
        #  сбор данных из формы
        self.data.clear()

        for block in self.blocks:
            self.data.update(block.getDict())
        print(self.data)
        self.door = DoorStreet(self.data)

    def _renderViews(self, board, views):
        for (file, crd) in views:
            im = loadImageTemplate(DOOR_TMPL, file)
            x1, y1 = crd
            x2, y2 = (x1 + im.size[0], y1 + im.size[1])
            board.paste(im, (x1, y1, x2, y2))

    def _render(self):
        board = loadImageTemplate(BOARD_TMPL, BOARD_FILE)
        draw = ImageDraw.Draw(board)
        font_b = ImageFont.truetype(os.path.join(FONT_DIR, FONT_BOARD), FONT_BOARD_SIZE_B)
        font = ImageFont.truetype(os.path.join(FONT_DIR, FONT_BOARD), FONT_BOARD_SIZE)
        #  отрисовка чертежей
        self._renderViews(board, self.door.views)

        ######### первый столбец ###########
        x, y = 300, 1450
        two_columns = (20, 550)
        four_columns = (20, 550, 200, 200)

        # отрисовка параметров изделия
        values = self.door.frameInfo()
        x, y = renderTable(draw, (x, y), 'Параметры калитки', values, two_columns, font_b, font)

        # отрисовка створки
        x, y = x, y + FONT_BOARD_SIZE
        values = self.door.doorInfo()
        x, y = renderTable(draw, (x, y), 'Параметры створки', values, two_columns, font_b, font)

        # отрисовка заполнения
        x, y = x, y + FONT_BOARD_SIZE
        values = self.door.fillingInfo()
        x, y = renderTable(draw, (x, y), 'Параметры заполнения', values, two_columns, font_b, font)

        # отрисовка цвета
        x, y = x, y + FONT_BOARD_SIZE
        values = self.door.colorInfo()
        x, y = renderTable(draw, (x, y), 'Параметры покраски', values, two_columns, font_b, font)

        # отрисовка параметров проема
        x, y = x, y + FONT_BOARD_SIZE
        values = self.door.doorwayInfo()
        x, y = renderTable(draw, (x, y), 'Размеры проема', values, two_columns, font_b, font)

        ######### второй столбец ###########
        x, y = 1250, 1450

        # отрисовка комплектации
        values = self.door.kitInfo()
        x, y = renderTable(draw, (x, y), 'Комплектация', values, two_columns, font_b, font,
                           headers=('Наименование', 'Кол-во'))

        # отрисовка доп металла
        x, y = x, y + FONT_BOARD_SIZE
        values = self.door.extraInfo()
        x, y = renderTable(draw, (x, y), 'Дополнительно', values, four_columns, font_b, font,
                           headers=('Наименование', 'Размер', 'Цвет', 'Кол-во'))

        # отрисовка нарезки
        x, y = x, y + FONT_BOARD_SIZE
        values = self.door.slicesInfo()
        x, y = renderTable(draw, (x, y), 'Нарезка', values, four_columns, font_b, font,
                           headers=('Металл', 'Размер', 'Кол-во'))

        # отрисовка примечания
        x, y = x, y + FONT_BOARD_SIZE
        values = self.door.noteInfo()
        x, y = renderTable(draw, (x, y), 'Примечание', values, (20,), font_b, font)

        ######### отрисовка информации о заказке #########
        x = 550
        y = 3245

        order = self.data['№ Заказа']
        order = order if order else '000'
        buyer = self.data['Заказчик']
        buyer = buyer if buyer else 'Предварительный чертеж'
        draw.text((x, y), text=buyer, fill=(0, 0, 0), font=font_b)
        draw.text((x + 1370, y), text=order, fill=(0, 0, 0), font=font_b)
        draw.text((x, y + 120), text=self.data['Инженер'], fill=(0, 0, 0), font=font_b)
        draw.text((x + 1370, y + 120), text=self.data['Дата монтажа'], fill=(0, 0, 0), font=font_b)

        filename = order + ' ' + buyer
        # board.show()
        PreviewWin('Чертеж', board, filename=filename, icon=ICON_FILE)


def loadImageTemplate(dir, file):
    file = os.path.join(dir, file)
    try:
        image = Image.open(file)
    except FileNotFoundError:
        raise ApolloOpenFileEx(file)
    else:
        return image


def renderTable(draw, crd, title, data, shift_column, font_title, font, headers=None, color=(0, 0, 0)):
    x, y = crd
    size_f_t = font_title.size
    size_f = font.size
    draw.text((x, y), text=title + ':', fill=color, font=font_title)
    y += size_f_t
    if headers:
        col = x
        for n, header in enumerate(headers):
            col += shift_column[n]
            if not header: header = ' '
            draw.text((col, y), text=header, fill=color, font=font)
        y += size_f
    col = x
    for n, col_items in enumerate(data):
        col += shift_column[n]
        row = y
        for item in col_items:
            if not item: item = ' '
            draw.text((col, row), text=item, fill=color, font=font)
            row += size_f
    return x, row
