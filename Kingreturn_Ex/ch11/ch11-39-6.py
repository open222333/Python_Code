# 更改裝飾器順序
def upper(func):  # 大寫裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        return newresult
    return newFunc


def bold(func):  # 加粗體字串裝飾器
    def wrapper(args):
        return 'bold' + func(args) + 'bold'
    return wrapper


@upper  # 設定大寫裝飾器
@bold  # 設定加粗體字串裝飾器
def greeting(string):  # 問候函數
    return string


print(greeting('Hello! iPhone'))