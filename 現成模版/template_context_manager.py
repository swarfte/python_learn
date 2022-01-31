class ContextManagerName(object):  # 在這裡修改方法的名
    def __init__(self) -> None:
        # 在這裡編寫要保存在物件中的屬性
        pass

    def __enter__(self):
        # 在這裡編寫要預先建立的代碼(開啟/打開/備份等)
        return None  # 返回一個文件流或/用於上下文操作的引用

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 在這裡編寫用於清理的代碼(保存,關閉,提交等)
        pass
