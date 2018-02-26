from dandg_libs.exeptions import ApolloPasreTubeEx, ApolloEmptyValueEx, ApolloConvertToIntEx


def parseTube(tube_type):
    sizes = tube_type.split('x')  # икс
    if len(sizes) < 2:
        sizes = tube_type.split('х')  # хэ
    try:
        res = list(map(int, sizes))
        if len(res) < 2: raise ValueError()
    except ValueError:
        raise ApolloPasreTubeEx(tube_type)
    return res


def convertToInt(value, param_name):
    if not value:
        raise ApolloEmptyValueEx(param_name)
    try:
        i = int(value)
    except ValueError:
        raise ApolloConvertToIntEx(value, param_name)
    else:
        return i

def addToSlicesDict(slices_dict, name_tube, size, number):
    if name_tube in slices_dict:
        slices = slices_dict[name_tube]
    else:
        slices_dict[name_tube] = slices = {}
    size = str(size)
    slices[size] = slices.get(size, 0) + number

def getParamsOfList(keys, data):
    col1, col2 = [], []
    for key in keys:
        value = data.get(key)
        if value:
            col1.append(key)
            col2.append(value)
    return col1, col2