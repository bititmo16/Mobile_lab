#include "readCSV.h"

typedef struct infor{
    string timestamp;
    string msisdn_origin;
    string msisdn_dest;
    string call_duration;
    string sms_number;
}bill_infor;

    float call_out ;
    float call_in;
    int sms;
    string call_1, call_2;

void readCSV(string num)
{
    ifstream fin("../data.csv");
    if(!fin.is_open()){
        cout << "File failed to open!!" << endl;
    }

    string line;
    struct infor client;

    while(getline(fin, line)){
        stringstream ss(line);
        getline(ss, client.timestamp, ',');
        getline(ss, client.msisdn_origin, ',');
        getline(ss, client.msisdn_dest, ',');
        getline(ss, client.call_duration, ',');
        getline(ss, client.sms_number, ',');

        if(client.msisdn_origin == num){
            call_out = atof(client.call_duration.c_str());
            sms = atoi(client.sms_number.c_str());
            call_1 =line;

        }

        if(client.msisdn_dest == num){
            call_in = atof(client.call_duration.c_str());
            call_2 = line;
        }
    }
        fin.close();
}

void show_call(string num){
    readCSV(num);
    cout << "Information on your calls: " << endl << "timestamp, msisdn_origin,msisdn_dest,call_duration,sms_number " << endl;
    cout << "Call out: " << call_1 << endl;
    cout << "Call in: " << call_2 << endl;

}
void tariff(string num){
    float sum;
    int call_out_coef = 1;
    int call_in_coef = 1;
    int sms_coef =1;
    int sms_free = 5;

    readCSV(num);
    cout << "Call in duration: " << call_in <<  endl;
    cout << "Call out duration: " << call_out <<  endl;
    cout << "Number of SMS: " << sms <<  endl;

    sum = call_in*call_in_coef + call_out*call_out_coef + (sms-sms_free)*sms_coef;
    cout << "Invoices: " << sum;

}

