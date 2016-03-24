/*
Copyright 2016-Present Dani Akash

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
int solution(int n){
    int givenNumber=n,a=0,count=0;
    while(n>=1){
        a=n%10;
        if(a!=0 && givenNumber%a==0){
            count++;
        }
        n=n/10;
    }
    return count;
}
int main() {
    int testCases=0,x;
    cin>>testCases;
    while(testCases--){
        cin>>x;
        cout<<solution(x)<<endl;
    }
    return 0;
}
