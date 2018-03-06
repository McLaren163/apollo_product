import os

from dandg_libs.door_strategy import (OpenOutBridgePanelStrategy, OpenOutBridgeNoneStrategy, OpenOutBridgeYesStrategy,
                                      OpenInBridgeNoneStrategy, OpenInBridgeYesStrategy, OpenInBridgePanelStrategy)

ICON_FILE = os.path.join('icons', 'logo.ico')

FONT_DEF = ('Calibri', '10')
FONT_BLOCK = FONT_DEF + ('bold',)

LABEL_WIDTH = 17

FONT_DIR = 'fonts'
FONT_BOARD = 'GOST_B.ttf'
FONT_BOARD_SIZE = 50
FONT_BOARD_SIZE_B = 60

BOARD_TMPL = 'tmpl_board'
BOARD_FILE = 'a4_portrait.png'  # 2480х3508 A4 300dpi
DOOR_TMPL = 'tmpl_door'

DOOR_GAP = 10
FILLING_GAP = 5

CRD_RIGHT_DRAW = (300, 130)
CRD_TOP_DRAW = (1360, 130)

OPEN_IN = 'во двор'
OPEN_OUT = 'на улицу'

SIDE_L = 'слева'
SIDE_R = 'справа'

BRIDGE_Y = 'с перемычкой'
BRIDGE_N = 'без перемычки'
BRIDGE_F = 'с фрамугой'

FILLING = {'AG/77'         : {'Прижимная рамка': '20x20',
                              'Створка'        : '40x20'},
           'PD/77'         : {'Прижимная рамка': '20x20',
                              'Створка'        : '40x20'},
           'AER55/S'       : {'Прижимная рамка': '25x25',
                              'Створка'        : '40x20'},
           'AER55/mS'      : {'Прижимная рамка': '25x25',
                              'Створка'        : '40x20'},
           'Профлист 1ст'  : {'Прижимная рамка': '30x30',
                              'Створка'        : '40x20'},
           'Профлист 2ст'  : {'Прижимная рамка': '20x20',
                              'Створка'        : '40x20'},
           'Сайдинг'       : {'Прижимная рамка': '20x20',
                              'Створка'        : '40x20'},
           'панель S-гофр' : {'Прижимная рамка': '20x20',
                              'Створка'        : '60x40'},
           'панель M-гофр' : {'Прижимная рамка': '20x20',
                              'Створка'        : '60x40'},
           'панель L-гофр' : {'Прижимная рамка': '20x20',
                              'Створка'        : '60x40'},
           'панель Филенка': {'Прижимная рамка': '20x20',
                              'Створка'        : '60x40'},
           'Заказчика 10мм': {'Прижимная рамка': '30x30',
                              'Створка'        : '40x20'},
           'Заказчика 15мм': {'Прижимная рамка': '25x25',
                              'Створка'        : '40x20'},
           'Заказчика 20мм': {'Прижимная рамка': '20x20',
                              'Створка'        : '40x20'},
           'Заказчика 40мм': {'Прижимная рамка': '20x20',
                              'Створка'        : '60x40'}}

DOOR_OPENING = (OPEN_OUT, OPEN_IN)

DOOR_BRIDGE = (BRIDGE_Y, BRIDGE_N, BRIDGE_F)

DOOR_SIDE = (SIDE_L, SIDE_R)

COLOR_TEXTURE = ('шагрень', 'глянец')

ORDERING_INFO = ('Информация о заказе',
                 ('№ Заказа',
                  'Заказчик',
                  'Дата монтажа',
                  'Инженер'))

DOORWAY_INFO = ('Размеры проема',
                ('Ширина',
                 'Высота'))

COLORING_INFO = ('Параметры покраски',
                 ('Цвет рамы',
                  'Цвет заполнения',
                  ['Структура', COLOR_TEXTURE]))

DOOR_PARAM = ('Параметры калитки',
              ('Ширина рамы',
               'Высота рамы',
               'Просвет',
               ['Перемычка', DOOR_BRIDGE],
               'Высота фрамуги',
               ['Открытие', DOOR_OPENING],
               ['Петли', DOOR_SIDE],
               ['Заполнение', list(sorted(FILLING.keys()))]))

DOOR_VIEWS = []
DOOR_VIEWS.append({'views'    : (('40x20_out_side_yes.png', CRD_RIGHT_DRAW),
                                 ('40х20_out_top_l.png', CRD_TOP_DRAW), ('40х20_out_top_r.png', CRD_TOP_DRAW)),
                   'Strategy' : OpenOutBridgeYesStrategy,
                   'Перемычка': BRIDGE_Y,
                   'Открытие' : OPEN_OUT,
                   'Створка'  : '40x20',
                   'Рама'     : '40x40',
                   'Полоса'   : '60x4'})
DOOR_VIEWS.append({'views'    : (('40x20_in_side_yes.png', CRD_RIGHT_DRAW),
                                 ('40х20_in_top_l.png', CRD_TOP_DRAW), ('40х20_in_top_r.png', CRD_TOP_DRAW)),
                   'Strategy' : OpenInBridgeYesStrategy,
                   'Перемычка': BRIDGE_Y,
                   'Открытие' : OPEN_IN,
                   'Створка'  : '40x20',
                   'Рама'     : '50x50',
                   'Полоса'   : '40x4',
                   'Полоса2'  : '70x4'})
DOOR_VIEWS.append({'views'    : (('40x20_out_side_no.png', CRD_RIGHT_DRAW),
                                 ('40х20_out_top_l.png', CRD_TOP_DRAW), ('40х20_out_top_r.png', CRD_TOP_DRAW)),
                   'Strategy' : OpenOutBridgeNoneStrategy,
                   'Перемычка': BRIDGE_N,
                   'Открытие' : OPEN_OUT,
                   'Створка'  : '40x20',
                   'Рама'     : '40x40',
                   'Полоса'   : '60x4'})
DOOR_VIEWS.append({'views'    : (('40x20_in_side_no.png', CRD_RIGHT_DRAW),
                                 ('40х20_in_top_l.png', CRD_TOP_DRAW), ('40х20_in_top_r.png', CRD_TOP_DRAW)),
                   'Strategy' : OpenInBridgeNoneStrategy,
                   'Перемычка': BRIDGE_N,
                   'Открытие' : OPEN_IN,
                   'Створка'  : '40x20',
                   'Рама'     : '50x50',
                   'Полоса'   : '40x4',
                   'Полоса2'  : '70x4'})
DOOR_VIEWS.append({'views'    : (('40x20_out_side_panel.png', CRD_RIGHT_DRAW),
                                 ('40х20_out_top_l.png', CRD_TOP_DRAW), ('40х20_out_top_r.png', CRD_TOP_DRAW)),
                   'Strategy' : OpenOutBridgePanelStrategy,
                   'Перемычка': BRIDGE_F,
                   'Открытие' : OPEN_OUT,
                   'Створка'  : '40x20',
                   'Рама'     : '40x40',
                   'Полоса'   : '60x4'})
DOOR_VIEWS.append({'views'    : (('40x20_in_side_panel.png', CRD_RIGHT_DRAW),
                                 ('40х20_in_top_l.png', CRD_TOP_DRAW), ('40х20_in_top_r.png', CRD_TOP_DRAW)),
                   'Strategy' : OpenInBridgePanelStrategy,
                   'Перемычка': BRIDGE_F,
                   'Открытие' : OPEN_IN,
                   'Створка'  : '40x20',
                   'Рама'     : '50x50',
                   'Полоса'   : '40x4',
                   'Полоса2'  : '70x4'})
DOOR_VIEWS.append({'views'    : (('60x40_out_side_yes.png', CRD_RIGHT_DRAW),
                                 ('60х40_out_top_l.png', CRD_TOP_DRAW), ('60х40_out_top_r.png', CRD_TOP_DRAW)),
                   'Strategy' : OpenOutBridgeYesStrategy,
                   'Перемычка': BRIDGE_Y,
                   'Открытие' : OPEN_OUT,
                   'Створка'  : '60x40',
                   'Рама'     : '60x40',
                   'Полоса'   : '80x4'})
DOOR_VIEWS.append({'views'    : (('60x40_in_side_yes.png', CRD_RIGHT_DRAW),
                                 ('60х40_in_top_l.png', CRD_TOP_DRAW), ('60х40_in_top_r.png', CRD_TOP_DRAW)),
                   'Strategy' : OpenInBridgeYesStrategy,
                   'Перемычка': BRIDGE_Y,
                   'Открытие' : OPEN_IN,
                   'Створка'  : '60x40',
                   'Рама'     : '60x40',
                   'Полоса'   : '60x4',
                   'Полоса2'  : '60x4'})
DOOR_VIEWS.append({'views'    : (('60x40_out_side_no.png', CRD_RIGHT_DRAW),
                                 ('60х40_out_top_l.png', CRD_TOP_DRAW), ('60х40_out_top_r.png', CRD_TOP_DRAW)),
                   'Strategy' : OpenOutBridgeNoneStrategy,
                   'Перемычка': BRIDGE_N,
                   'Открытие' : OPEN_OUT,
                   'Створка'  : '60x40',
                   'Рама'     : '60x40',
                   'Полоса'   : '80x4'})
DOOR_VIEWS.append({'views'    : (('60x40_in_side_no.png', CRD_RIGHT_DRAW),
                                 ('60х40_in_top_l.png', CRD_TOP_DRAW), ('60х40_in_top_r.png', CRD_TOP_DRAW)),
                   'Strategy' : OpenInBridgeNoneStrategy,
                   'Перемычка': BRIDGE_N,
                   'Открытие' : OPEN_IN,
                   'Створка'  : '60x40',
                   'Рама'     : '60x40',
                   'Полоса'   : '60x4',
                   'Полоса2'  : '60x4'})
DOOR_VIEWS.append({'views'    : (('60x40_out_side_panel.png', CRD_RIGHT_DRAW),
                                 ('60х40_out_top_l.png', CRD_TOP_DRAW), ('60х40_out_top_r.png', CRD_TOP_DRAW)),
                   'Strategy' : OpenOutBridgePanelStrategy,
                   'Перемычка': BRIDGE_F,
                   'Открытие' : OPEN_OUT,
                   'Створка'  : '60x40',
                   'Рама'     : '60x40',
                   'Полоса'   : '80x4'})
DOOR_VIEWS.append({'views'    : (('60x40_in_side_panel.png', CRD_RIGHT_DRAW),
                                 ('60х40_in_top_l.png', CRD_TOP_DRAW), ('60х40_in_top_r.png', CRD_TOP_DRAW)),
                   'Strategy' : OpenInBridgePanelStrategy,
                   'Перемычка': BRIDGE_F,
                   'Открытие' : OPEN_IN,
                   'Створка'  : '60x40',
                   'Рама'     : '60x40',
                   'Полоса'   : '60x4',
                   'Полоса2'  : '60x4'})

DOOR_ITEMS = (('Замок', ('Замок CISA + козырек',
                         'Эл.защелка',
                         'Замок механический APEX',
                         'Задвижка с ушками',
                         'Площадка под замок',
                         'Замок заказчика')),
              ('Ручка', ('Ручка Грибок',
                         'Ручка Скоба',
                         'Ручка заказчика')),
              'Сталька',
              'Доводчик',
              '>Input<')

METALL_ITEMS = (('Нащельник', ('Нащельник 30х30 сталь',
                               'Нащельник 30х20 алюм')),
                ('Труба', ('Труба 20х20',
                           'Труба 40х40',
                           'Труба 60х60',
                           'Труба 80х80')),
                ('Уголок', ('Уголок 50',
                            'Уголок 63',
                            'Уголок 75')),
                '>Input<')
