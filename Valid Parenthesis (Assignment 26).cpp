/*
In any language program mostly syntax error occurs due to unbalancing delimiter such as
(),{},[]. Write C++ program using stack to check whether given expression is well parenthesized or not.
*/

#include <iostream>
#define max 10
using namespace std;

class Stack{
    public:
    int top;
    char stk[max];

    Stack(){
        top = -1;
    }

    void push (char c){
        top = top + 1;
        stk[top] = c;
    }

    char pop (){
        char temp;
        temp = stk[top];
        top = top - 1;
        return temp;
    }

    bool empty(){
        if(top == -1){
            return true;
        }
        else{
            return false;
        }
    }

    bool full(){
        if(top == max){
            return true;
        }
        else{
            return false;
        }
    }

    char chk(){
        int temp;
        temp = stk[top];
        return temp;
    }
};

int main(){

    Stack s;

    string exp;
    char ch;
    int i = 0;

    cout<<"Enter the expression you want to check : "<<endl;
    cin>>exp;

    while(exp[i] != '\0'){
        ch = exp[i];

        switch(ch){
            case '(' : s.push(ch);
                       break;
            case '[' : s.push(ch);
                       break;
            case '{' : s.push(ch);
                       break;
            case ')' : if(s.empty() || s.chk() != '('){
                        return false;
                       }
                       else{
                        s.pop();
                       }
                       break;
            case ']' : if(s.empty() || s.chk() != '['){
                        return false;
                       }
                       else{
                        s.pop();
                       }
                       break;
            case '}' : if(s.empty() || s.chk() != '{'){
                        return false;
                       }
                       else{
                        s.pop();
                       }
                       break;
        }

        i = i+1;
    }

    if(s.empty()){
        cout<<"Given Expression is well parenthesized"<<endl;
    }
    else{
        cout<<"Given Expression is not well parenthesized"<<endl;
    }
    return 0;
}

// Example Expression : {a+b[c-d(e/f)]}