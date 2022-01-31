from functools import wraps


def decorator_name(func):  # 在這裡修改裝飾器的名稱
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1 在這裡加入被裝飾函數執行前的代碼
        # 2 根據需要調用修飾函數，如有需要可返回其結果
        return func(*args, **kwargs)
        # 3 在這裡加入 代替被裝飾函數執行的代碼

    return wrapper
