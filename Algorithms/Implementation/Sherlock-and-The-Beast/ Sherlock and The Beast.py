'''
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
'''

import sys

def solution(n):
    l=[]
    while n > 0:
        if n < 3:
            return -1
        else:
            if n % 5 == 0 and n % 3 == 0:
                l+=[5,5,5]
                n-=3
            if n % 5 > 0 :
                l+=[5,5,5]
                n-=3
            else:
                l+=[3,3,3,3,3]
                n-=5
    l.sort()
    l=l[::-1]
    l=''.join(map(str, l))
    return l

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x=solution(n)
    print(x)
