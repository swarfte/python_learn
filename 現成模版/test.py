from functools import wraps


def check(variable):  # 在這裡修改裝飾器工廠的名稱
    # 在這裡加入裝飾器函數執行前的代碼
    print("input number is :", variable)

    def decorator_name(func):  # 在這裡修改裝飾器的名稱
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 在這裡加入被裝飾函數執行前的代碼
            # 根據需要調用被修飾函數，如有需要可返回其結果
            if args[0] % variable != 0:
                return func(*args, **kwargs)
            # 在這裡加入 代替被裝飾函數執行的代碼
            return "Wrong answer"
        return wrapper

    return decorator_name


@check(5)
def double(n):
    return n ** 2

if __name__ == '__main__':
    print(double(5))
