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

n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)
sump,sums=0,0
for i in range(n):
    sump+=a[i][i]
    sums+=a[i][n-1-i]
diff=abs(sump-sums)
print(diff)
