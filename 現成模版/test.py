from functools import wraps
from decorators import BaseDecorator
from template_object_decorator_factory import DecoratorFactoryName as DFN


def check(variable):  # 在這裡修改裝飾器工廠的名稱
    # 在這裡加入裝飾器函數執行前的代碼
    # print("input number is :", variable)

    def decorator_name(func):  # 在這裡修改裝飾器的名稱
        print("input number is :", variable)

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


class log(BaseDecorator):
    def __init__(self, *args, **kwargs):
        super(log, self).__init__(*args, **kwargs)

    def before_invoke(self):
        print("start")

    def after_invoke(self):
        print("end")


# @check(5)
def double(n):
    return n ** 2

@DFN(123)
def three(n):
    print(n * 3)
    return (n)


@log(456)
def four(n):
    print(n * 4)
    return (n)

if __name__ == '__main__':
    # print(double(5))
    three(3)
    four(5)
    pass
