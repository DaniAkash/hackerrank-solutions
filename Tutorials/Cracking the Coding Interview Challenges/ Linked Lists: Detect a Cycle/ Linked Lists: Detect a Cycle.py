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

def has_cycle(head):
  slowNode = fastNode1 = fastNode2 = head;
  if(fastNode2): fastNode1 = fastNode2.next
  if(fastNode1): fastNode2 = fastNode1.next
  while(slowNode and fastNode1 and fastNode2):
    if(slowNode == fastNode1 or slowNode == fastNode2): return True
    slowNode = fastNode1 = fastNode2 = slowNode.next
    if(fastNode2): fastNode1 = fastNode2.next
    if(fastNode1): fastNode2 = fastNode1.next
  return False