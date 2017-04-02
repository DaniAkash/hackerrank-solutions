#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int testCases,cash,cost,wrapper;
    cin>>testCases;
    while(testCases--){
        cin>>cash>>cost>>wrapper;
        int chocolates=0,temp=0;
        chocolates=cash/cost;
        if(chocolates>=wrapper){
            temp=chocolates;
            do{
                temp-=wrapper;
                chocolates++;
                temp++;
            }while(temp>=wrapper);
        }
        cout<<chocolates<<endl;
    }
    return 0;
}
