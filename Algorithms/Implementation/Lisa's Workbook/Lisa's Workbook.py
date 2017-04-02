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

z = input().strip().split(' ')
maxChapters = int(z[0])
probsPerPage = int(z[1])
problems = [int(each) for each in input().strip().split(' ')]
i = 0
page = 0
count = 0
while i<maxChapters:
    total = problems[i]
    prob = 0
    while prob<total:
        page+=1
        for each in range(probsPerPage):
            if prob<total:
                prob+=1
                if prob == page:
                    count+=1
    i+=1
print(count)