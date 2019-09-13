// 执行命令, 将本文件编译成 .so 文件, 以供 Python 调用
// g++ -o hello_world.so -shared -fPIC hello_world.cpp
#include <iostream>

using namespace std;

class HelloWorld
{
    public:
        static void helloWorld(char *c);
};


void HelloWorld::helloWorld(char *c){
    cout << "C++ HelloWorld::helloWorld" << endl;
    cout << c << endl;
};


extern "C"
{
    HelloWorld obj;
    void helloWorld(char *c){
        obj.helloWorld(c);
    }
}
