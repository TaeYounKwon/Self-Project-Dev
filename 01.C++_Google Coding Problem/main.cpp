#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
bool isNumber(const string& str)
{
    for (char const &c : str) {
        if (std::isdigit(c) == 0) return false;
    }
    return true;
}
int main(){

    int T;
    cin>>T;
    vector<int> length;
    vector<string> val;

    for(int i=0; i<T; i++){
        int val1;
        cin>>val1;
        string val2;
        cin>>val2;
        length.push_back(val1);
        val.push_back(val2);
    }


    int count=0;
    while(true) {

        if (count == val.size()) {
            goto loopOut;
        } else {
            int startVal = 0;

            while (true) {

                if (startVal+1 == val.at(count).size()) {
                    goto innerOut;
                }

                    string testVal = "";
                    testVal=val.at(count).substr(startVal,2);

                    if (testVal == "01") {
                        val.at(count).replace(startVal,  2, "2");
                        if (startVal != 0) {
                            startVal=startVal-1;
                        }
                    } else if (testVal == "12") {
                        val.at(count).replace(startVal, 2, "3");
                        if (startVal != 0) {
                            startVal=startVal-1;
                        }
                    } else if (testVal == "23") {
                        val.at(count).replace(startVal,  2, "4");
                        if (startVal != 0) {
                            startVal=startVal-1;
                        }
                    } else if (testVal == "34") {
                        val.at(count).replace(startVal,  2, "5");
                        if (startVal != 0) {
                            startVal=startVal-1;
                        }
                    } else if (testVal == "45") {
                        val.at(count).replace(startVal, 2, "6");
                        if (startVal != 0) {
                            startVal=startVal-1;
                        }
                    } else if (testVal == "56") {
                        val.at(count).replace(startVal,  2, "7");
                        if (startVal != 0) {
                            startVal=startVal-1;
                        }
                    } else if (testVal == "67") {
                        val.at(count).replace(startVal,  2, "8");
                        if (startVal != 0) {
                            startVal=startVal-1;
                        }
                    } else if (testVal == "78") {
                        val.at(count).replace(startVal,  2, "9");
                        if (startVal != 0) {
                            startVal=startVal-1;
                        }
                    } else if (testVal == "89") {
                        val.at(count).replace(startVal,  2, "0");
                        if (startVal != 0) {
                            startVal=startVal-1;
                        }
                    } else if (testVal == "90") {
                        val.at(count).replace(startVal,  2, "1");
                        if (startVal != 0) {
                            startVal=startVal-1;
                        }

                    } else {
                        startVal++;
                    }

            }
            innerOut:
            cout << "";
        } count++;
    }
    loopOut:
    for(int i=0; i<val.size(); i++){
        cout<<"Case #"<<i+1<<": "<< val.at(i)<<endl;
    };
    return 0;
}