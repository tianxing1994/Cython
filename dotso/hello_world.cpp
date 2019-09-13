// 执行命令, 将本文件编译成 .so 文件, 以供 Python 调用
// g++ -o hello_world.so -shared -fPIC hello_world.cpp
#include <iostream>

using namespace std;


class HelloWorld
{
    public:
        void helloWorld();
};


void HelloWorld::helloWorld(){
    cout << "C++ Compile to dotso file: <我想从 Python 传一个字符串进来, 但是不知道怎么实现.>" << endl;
};


extern "C"
{
    // 因为 Python ctypes 只能调用 C 语言代码, 所以这里需要将 C++ 代码转成 C 的形式.
    // 具体的道理, 我也不会.
    HelloWorld obj;
    void helloWorld(){
        obj.helloWorld();
    }
}
