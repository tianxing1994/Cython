// 执行命令, 将本文件编译成 .so 文件, 以供 Python 调用
// g++ -o hello_world.so -shared -fPIC hello_world.cpp
#include <iostream>
#include <cstring>


using namespace std;

class HelloWorld
{
    public:
        static void helloWorldDisplay();
        static char *helloWorld(char *c);
};


void HelloWorld::helloWorldDisplay()
{
    cout << "C++ compile to .so file: Hello World" << endl;
};


char *HelloWorld::helloWorld(char *c)
{
    char c0[] = "C++ compile to .so file: ";
    char *ret= new char {'\0'};

    strcat(ret, c0);
    strcat(ret, c);
    return ret;
};


extern "C"
{
    HelloWorld obj;
    void helloWorldDisplay(){
        obj.helloWorldDisplay();
    };

    char *helloWorld(char *c){
        char *ret;
        ret = obj.helloWorld(c);
        return ret;
    };
}
