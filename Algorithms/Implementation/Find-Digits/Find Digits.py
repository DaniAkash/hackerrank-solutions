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

def solution(givenNumber):
    count = 0
    for digit in givenNumber:
        if (int(digit)!=0 and int(givenNumber)%int(digit) == 0):
            count+=1
    return count

t = int(input().strip())
for each in range(t):
    givenNumber = str(input().strip())
    print(solution(givenNumber))
