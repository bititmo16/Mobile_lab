#include "readCSV.h"
int main(){

    int i;
    string number;
    cout << "Enter your number: ";
    cin >> number;

    cout << "Выбирайте вариант:\n1:Информация о звонке\n2:Тарификация выбранных записей\n";
    cout << "Твой вариант: ";
    cin >> i;

    switch(i){
    case 1:
        show_call(number);
        break;
    case 2:
        tariff(number);
        break;
    default:
        cout << "Выбирайте вариант!!!";
    }
    return 0;
}
