def demo1():
    """传入 char * 传数. 方法 1"""
    from dotso import hello_world

    string = 'Hello World'
    string = string.encode()
    hello_world.helloWorld(string)
    return


def demo2():
    """传入 char * 传数. 方法 2"""
    from dotso import hello_world

    hello_world.helloWorld(b'Hello World')
    return


if __name__ == '__main__':
    demo2()
