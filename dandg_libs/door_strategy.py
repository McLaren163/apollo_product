from dandg_libs.utility import parseTube, convertToInt, addToSlicesDict


class BaseStrategy:
    def __init__(self):
        pass

    def calculate(self, door, door_gap, filling_gap):
        self.data = door.data
        self.DOOR_GAP = door_gap
        self.FILLING_GAP = filling_gap
        self.slices = {}
        self.data['Нарезка'] = self.slices

        self._getTubeSizes()
        self._calculateSizes()
        self._calculateSlices()

        print(self.slices)

    def _getTubeSizes(self):
        self.FRAME_TUBE_SIZES = parseTube(self.data['Рама'])
        self.DOOR_TUBE_SIZES = parseTube(self.data['Створка'])

    def _calculateSizes(self):
        self._calcFrameWidth()
        self._calcFrameHeight()
        self._calcBridgeHeight()
        self._calcDoorWidth()
        self._calcDoorHeight()
        self._calcFilling()
        self._calcFillingBridge()

    def _calculateSlices(self):
        self._calcFrameSlices()
        self._calcDoorSlices()
        self._calcDoorGasketSlices()
        self._calcBridgeGasketSlices()
        self._calcStripeSlices()

    def _calcFrameWidth(self):
        """Расчитать ширину рамы"""
        self.FRAME_W = convertToInt(self.data['Ширина рамы'], 'Ширина рамы')

    def _calcFrameHeight(self):
        """Расчитать высоту рамы"""
        self.FRAME_H = convertToInt(self.data['Высота рамы'], 'Высота рамы')

    def _calcDoorWidth(self):
        """Расчитать ширину створки"""
        frame_tube_side = self.FRAME_TUBE_SIZES[1]
        door_w = self.FRAME_W - self.DOOR_GAP * 2 - frame_tube_side * 2
        self.DOOR_W = door_w
        self.data['Ширина створки'] = str(door_w)

    def _calcBridgeHeight(self):
        """Расчитать высоту перемычки/фрамуги"""
        self.BRIDGE_H = 0

    def _calcDoorHeight(self):
        """Расчитать высоту створки"""
        clearance = convertToInt(self.data['Просвет'], 'Просвет')
        lowering = (self.BRIDGE_H + self.DOOR_GAP) if self.BRIDGE_H > 0 else self.BRIDGE_H
        self.DOOR_H = self.FRAME_H - clearance - lowering
        self.data['Высота створки'] = str(self.DOOR_H)

    def _calcFilling(self):
        """Расчитать размер заполения на створку"""
        tube_side = self.DOOR_TUBE_SIZES[1]
        self.FILLING_W = self.DOOR_W - tube_side * 2 - self.FILLING_GAP
        self.FILLING_H = self.DOOR_H - tube_side * 2 - self.FILLING_GAP
        self.data['Заполнение на створку'] = '{}x{}'.format(str(self.FILLING_W), str(self.FILLING_H))

    def _calcFillingBridge(self):
        """Раситать размер заполнения на фрамугу"""
        pass  # перелпределить в подклассе

    def _calcFrameSlices(self):
        """Расчитать нарезку на раму"""
        pass

    def _calcDoorSlices(self):
        """Расчитать нарезку на створку"""
        addToSlicesDict(self.slices, self.data['Створка'], self.DOOR_W, 2)
        addToSlicesDict(self.slices, self.data['Створка'], self.DOOR_H, 2)

    def _calcDoorGasketSlices(self):
        """Раситать нарезку прижимной рамки на створку"""
        vertical = self.DOOR_H - self.DOOR_TUBE_SIZES[1] * 2
        horizontal = self.DOOR_W - self.DOOR_TUBE_SIZES[1] * 2
        addToSlicesDict(self.slices, self.data['Прижимная рамка'], vertical, 2)
        addToSlicesDict(self.slices, self.data['Прижимная рамка'], horizontal, 3)

    def _calcBridgeGasketSlices(self):
        """Расчитать нарезку прижимной рамки на фрамугу"""
        pass

    def _calcStripeSlices(self):
        """Расчитать нарезку полосы на изделие"""
        pass


class OpenOutBridgePanelStrategy(BaseStrategy):
    def _calcFillingBridge(self):
        tube_side = self.FRAME_TUBE_SIZES[1]
        self.FILLING_BRIDGE_W = self.FRAME_W - tube_side * 2 - self.FILLING_GAP
        self.FILLING_BRIDGE_H = self.BRIDGE_H - tube_side * 2 - self.FILLING_GAP
        self.data['Заполнение на фрамугу'] = '{}x{}'.format(str(self.FILLING_BRIDGE_W), str(self.FILLING_BRIDGE_H))

    def _calcBridgeHeight(self):
        self.BRIDGE_H = convertToInt(self.data['Высота фрамуги'], 'Высота фрамуги')

    def _calcFrameSlices(self):
        addToSlicesDict(self.slices, self.data['Рама'], self.FRAME_H, 2)
        addToSlicesDict(self.slices, self.data['Рама'], self.FRAME_W, 1)

        addToSlicesDict(self.slices, self.data['Рама'], self.FRAME_W - self.FRAME_TUBE_SIZES[0] * 2, 1)

    def _calcBridgeGasketSlices(self):
        addToSlicesDict(self.slices, self.data['Прижимная рамка'], self.BRIDGE_H - self.FRAME_TUBE_SIZES[1] * 2, 2)
        addToSlicesDict(self.slices, self.data['Прижимная рамка'], self.FRAME_W - self.FRAME_TUBE_SIZES[1] * 2, 2)

    def _calcStripeSlices(self):
        addToSlicesDict(self.slices, self.data['Полоса'], self.DOOR_H + 20, 2)
        addToSlicesDict(self.slices, self.data['Полоса'], self.DOOR_W + 20 * 2, 2)
        addToSlicesDict(self.slices, self.data['Полоса'], self.FRAME_W, 2)
        addToSlicesDict(self.slices, self.data['Полоса'], self.BRIDGE_H - 15, 2)


class OpenOutBridgeNoneStrategy(BaseStrategy):
    def _calcBridgeHeight(self):
        del self.data['Высота фрамуги']
        self.BRIDGE_H = 0

    def _calcFrameSlices(self):
        addToSlicesDict(self.slices, self.data['Рама'], self.FRAME_H, 2)

    def _calcStripeSlices(self):
        addToSlicesDict(self.slices, self.data['Полоса'], self.DOOR_H, 2)
        addToSlicesDict(self.slices, self.data['Полоса'], self.DOOR_W + 20 * 2, 2)


class OpenOutBridgeYesStrategy(BaseStrategy):
    def _calcBridgeHeight(self):
        del self.data['Высота фрамуги']
        self.BRIDGE_H = self.FRAME_TUBE_SIZES[1]

    def _calcFrameSlices(self):
        addToSlicesDict(self.slices, self.data['Рама'], self.FRAME_H, 2)
        addToSlicesDict(self.slices, self.data['Рама'], self.FRAME_W, 1)

    def _calcStripeSlices(self):
        addToSlicesDict(self.slices, self.data['Полоса'], self.DOOR_H + 20, 2)
        addToSlicesDict(self.slices, self.data['Полоса'], self.DOOR_W + 20 * 2, 2)


class OpenInBridgeNoneStrategy(OpenOutBridgeNoneStrategy):
    def _calcStripeSlices(self):
        addToSlicesDict(self.slices, self.data['Полоса'], self.DOOR_H, 2)
        addToSlicesDict(self.slices, self.data['Полоса'], self.DOOR_W, 2)
        addToSlicesDict(self.slices, self.data['Полоса2'], self.FRAME_H, 2)


class OpenInBridgeYesStrategy(OpenOutBridgeYesStrategy):
    def _calcStripeSlices(self):
        addToSlicesDict(self.slices, self.data['Полоса'], self.DOOR_H, 2)
        addToSlicesDict(self.slices, self.data['Полоса'], self.DOOR_W, 2)
        addToSlicesDict(self.slices, self.data['Полоса2'], self.FRAME_H, 2)
        addToSlicesDict(self.slices, self.data['Полоса2'], self.FRAME_W, 1)


class OpenInBridgePanelStrategy(OpenOutBridgePanelStrategy):
    def _calcStripeSlices(self):
        addToSlicesDict(self.slices, self.data['Полоса'], self.DOOR_H, 2)
        addToSlicesDict(self.slices, self.data['Полоса'], self.DOOR_W, 2)
        addToSlicesDict(self.slices, self.data['Полоса2'], self.FRAME_H, 2)
        addToSlicesDict(self.slices, self.data['Полоса2'], self.FRAME_W, 1)
        strip_size = parseTube(self.data['Полоса2'])[0]
        addToSlicesDict(self.slices, self.data['Полоса2'], self.FRAME_W - strip_size * 2, 1)
