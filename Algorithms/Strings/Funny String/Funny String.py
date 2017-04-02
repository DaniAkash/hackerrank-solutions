'''
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
'''

def check(a,b,c,d):
    ans1=ord(a)-ord(b)
    ans2=ord(c)-ord(d)
    if (abs(ans1)==abs(ans2)):
        return 1

def solution():
    S=input().strip()
    R=S[::-1]
    i=1
    while(i<len(S)):
        flag=check(S[i],S[i-1],R[i],R[i-1])
        if flag==1:
            i+=1
        else:
            return 'Not Funny'
    return 'Funny'

testcases=int(input().strip())
while(testcases):
    a=solution()
    print(a)
    testcases-=1