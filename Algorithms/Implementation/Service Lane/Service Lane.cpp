/*
Copyright 2017-Present Dani Akash

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
    unsigned int length=0,testCases=0,vehicle=0;
    cin>>length>>testCases;
    unsigned long int lane[length]={0};
    for(int i=0;i<length;i++){
        cin>>lane[i];
    }
    while(testCases--){
        int start=0,end=0;
        cin>>start>>end;
        vehicle=lane[start];
        for(int i=start;i<=end;i++){
            if(lane[i]<vehicle){
                vehicle=lane[i];
            }
        }
        cout<<vehicle<<endl;
    }
    return 0;
}