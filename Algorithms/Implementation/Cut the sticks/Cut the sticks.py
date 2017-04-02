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

import sys

def cut(arr):
    arr.sort()
    print(len(arr))
    i = 0
    l = arr[0]

    arr1 = [each-l for each in arr]
    arr2 = []
    for each in arr1:
        if each != 0:
            arr2.append(each)

    if len(arr2) != 0:
        return cut(arr2)
    else:
        return 0

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
a = cut(arr)
