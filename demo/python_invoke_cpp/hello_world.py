import ctypes


def demo0():
    from dotso import hello_world
    hello_world.helloWorld()
    return


def demo1():
    """传入 char * 传数. 方法 1"""
    from dotso import hello_world
    hello_world.helloWorld.argtypes = (ctypes.c_char_p,)
    hello_world.helloWorld.restype = ctypes.c_char_p

    string = 'Hello World'
    string = string.encode()
    result = hello_world.helloWorld(string)
    result = result.decode('utf-8')
    print(result)
    return


def demo2():
    """传入 char * 传数. 方法 2"""
    from dotso import hello_world
    # 声明 helloWorld 的输入参数为 ctypes.c_char_p
    # 输出值为 ctypes.c_char_p. 因为 C/C++ 只能有一个返回值, 所以 .restype 只有一个值.
    hello_world.helloWorld.argtypes = (ctypes.c_char_p,)
    hello_world.helloWorld.restype = ctypes.c_char_p

    result = hello_world.helloWorld(b'Hello World')
    result = result.decode('utf-8')
    print(result)
    return


if __name__ == '__main__':
    demo2()
