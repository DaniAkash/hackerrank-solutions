#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N,c,a;
    cin>>N;
    if(N>=1 && N<=100){
        for(int i=1;i<=N;i++){
            a=N-i;
            for(int j=1;j<=a;j++){
                cout<<" ";
            }
            for(int k=a;k<N;k++){
                cout<<"#";
            }
            cout<<"\n";
        }
    }
    return 0;
}
