'''
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
'''

import sys

time = input().strip()
hr=int(time[0:2])
mn=int(time[3:5])
ss=int(time[6:8])
if time[8:]=='PM':
    if hr!=12:
        hr+=12
else:
    if hr==12:
        hr=0
print('%02d:%02d:%02d'%(hr,mn,ss))
