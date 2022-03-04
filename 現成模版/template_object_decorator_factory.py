class DecoratorFactoryName(object):  # 裝飾函數的裝飾器
    def __init__(self, *args, **kwargs):  # 獲取裝飾器初始化的傳入參數
        super(DecoratorFactoryName, self).__init__()
        self.func = None  # 所裝飾的函數
        self.decorator_args = args  # 對像裝飾器自身的可變位置參數
        self.decorator_kwargs = kwargs  # 對像裝飾器自身的關鍵字參數

    def __call__(self, func):  # 當作函數比調用時接收的參數(接收函數作為參數->裝飾器)
        self.func = func
        return self.wrapper

    def wrapper(self, *args, **kwargs):  # 調用被裝飾的函數
        result = self.func(*args, **kwargs)
        return result

