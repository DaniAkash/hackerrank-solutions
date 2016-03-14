/*
Copyright 2016 Dani Akash

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

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
