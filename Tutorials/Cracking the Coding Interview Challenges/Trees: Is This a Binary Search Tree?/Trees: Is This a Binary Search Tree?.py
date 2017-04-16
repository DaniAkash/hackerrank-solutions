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

maximum = 4294967296
minimum = -4294967296

def isBst(node, minimum, maximum):
    if node is None: return True
    
    if node.data<minimum or node.data>maximum: return False
    
    return isBst(node.left, minimum, node.data-1) and isBst(node.right, node.data+1, maximum)

def check_binary_search_tree_(root):
    return isBst(root, minimum, maximum)
