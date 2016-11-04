# def now():
#     print('2016-11-02')
#
#
# f = now
# f()
#
# print(now.__name__)
# print(f.__name__)


def log(func):
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2016-11-02')


# f = now
# f()
if __name__ == '__main__':
    now()
