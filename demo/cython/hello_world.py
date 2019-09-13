def demo1():
    """
    通过 Cython 将 Python 代码编译成 C 语言再编译成 .so 文件供 Python 调用.
    由于 Python 中的有些数据类型是 C 语言中没有的.
    所以, 当存在不能转换为 C 语言的数据类型时, C 代码执行时需要与 Python 进行数据类型转换.
    在这种情况下, 代码运行的速度可能不能够提高多少.
    """
    from cython_support import hello_world

    result = hello_world.hello_cython("hello world")
    print(result)
    return


if __name__ == '__main__':
    demo1()
