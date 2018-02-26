from config import FILLING, DOOR_VIEWS, DOOR_SIDE, FILLING_GAP, DOOR_GAP
from dandg_libs.exeptions import ApolloEmptyValueEx, ApolloNotFoundType
from dandg_libs.utility import getParamsOfList


class DoorStreet:
    def __init__(self, data):
        self.data = data
        self._checkData()
        self._calculateFullParams()

    def _checkData(self):
        checklist_to_empty = ('Ширина', 'Высота', 'Цвет рамы', 'Цвет заполнения')
        for prop in checklist_to_empty:
            if not self.data.get(prop): raise ApolloEmptyValueEx(prop)

    def _calculateFullParams(self):
        self.type = self._getType()
        self._updateData(self.type)
        self.views = self._getViews(self.type)
        self.strategy = self.type['Strategy']()  # создать объект стратегии

        self.strategy.calculate(self, DOOR_GAP, FILLING_GAP)

    def _getType(self):
        filter_mask = {}
        filling = self.data['Заполнение'] or emptyValueExWrapper('Заполнение')
        filter_mask['Створка'] = FILLING[filling]['Створка']
        filter_mask['Открытие'] = self.data['Открытие'] or emptyValueExWrapper('Открытие')
        filter_mask['Перемычка'] = self.data['Перемычка'] or emptyValueExWrapper('Перемычка')

        try:
            door_type = next(filter(lambda x: filterFunc(filter_mask, x), DOOR_VIEWS))
        except StopIteration:
            raise ApolloNotFoundType()

        return door_type

    def _getViews(self, type):
        views = type['views']
        side = self.data['Петли'] or emptyValueExWrapper('Петли')
        i = 1 + DOOR_SIDE.index(side)
        return views[0], views[i]

    def _updateData(self, door_type):
        self.data.update(door_type)
        # self.data['Рама'] = door_type['Рама']
        # self.data['Створка'] = door_type['Створка']
        # self.data['Полоса'] = door_type['Полоса']
        filling = self.data['Заполнение']
        self.data['Прижимная рамка'] = FILLING[filling]['Прижимная рамка']

    def doorwayInfo(self):
        keys = ('Ширина', 'Высота')
        return getParamsOfList(keys, self.data)

    def frameInfo(self):
        keys = ('Ширина рамы', 'Высота рамы', 'Просвет', 'Перемычка', 'Высота фрамуги', 'Открытие', 'Петли', 'Рама')
        return getParamsOfList(keys, self.data)

    def fillingInfo(self):
        keys = ('Заполнение', 'Заполнение на створку', 'Заполнение на фрамугу')
        return getParamsOfList(keys, self.data)

    def doorInfo(self):
        keys = ('Ширина створки', 'Высота створки', 'Створка', 'Прижимная рамка')
        return getParamsOfList(keys, self.data)

    def colorInfo(self):
        keys = ('Цвет рамы', 'Цвет заполнения', 'Структура')
        return getParamsOfList(keys, self.data)

    def kitInfo(self):
        return self.data['Комплектация']['Наименование'], self.data['Комплектация']['Кол-во']

    def extraInfo(self):
        col1 = self.data['Дополнительно']['Наименование']
        col2 = self.data['Дополнительно']['Размер']
        col3 = self.data['Дополнительно']['Цвет']
        col4 = self.data['Дополнительно']['Кол-во']
        return col1, col2, col3, col4

    def noteInfo(self):
        return self.data['Примечание']

    def slicesInfo(self):
        col1, col2, col3 = [], [], []
        slices = self.data['Нарезка']
        for name, sizes in slices.items():
            for size, num in sizes.items():
                col1.append(name)
                col2.append(size)
                col3.append(str(num))
        return col1, col2, col3


def filterFunc(mask, values):
    for k in mask:
        if mask[k] != values[k]: return False
    return True

def emptyValueExWrapper(name):
    raise ApolloEmptyValueEx(name)
