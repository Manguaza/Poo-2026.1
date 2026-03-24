#include <iostream>

using namespace std;

class contaBancaria {
    public:
    string titular = "";
    string numero = "";
    double saldo = 0;
void deposisat (double v) {
        this->saldo += v;
    }
    void sacar (double v) {
        this ->saldo -= v;
    }
};

int main () {
    contaBancaria *x =  new contaBancaria
    x->titular = "eduardo";
    x->numero = "123";
    cout << x-saldo << endl;
}
