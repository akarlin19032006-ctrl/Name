#include <iostream>
#include <vector>
#include <string>
#include <stack>

int main() {
    #Создание массива типа список
    std::vector<std::string> suslo = {"aka", "bob", "z"};

    #Организация стека
    std::stack<std::string> stack;

    stack.push("zoi");
    stack.push("apapaa");
    stack.push("m");
    
    #Удаление из стека
    int top = stack.top();  
    stack.pop();            

    std::cout << "Верхний элемент: " << top << std::endl;
    std::cout << "Размер стека после pop: " << stack.size() << std::endl;

    return 0;
}
 