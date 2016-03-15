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
    int T=0,a[1000]={0};
    cin>>T;
    for(int n=0;n<T;n++){
        int N=0,K=0,isPresent=0;
        cin>>N>>K;
        for(int i=0;i<N;i++){
            cin>>a[i];
            if(a[i]<=0){
                isPresent+=1;
            }
        }
        if(isPresent>=K){
            cout<<"NO"<<endl;
        }
        else{
            cout<<"YES"<<endl;
        }
    }
    return 0;
}
