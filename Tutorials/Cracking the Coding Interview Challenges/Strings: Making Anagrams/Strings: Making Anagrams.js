/*
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
*/

function main() {
  let string1 = readLine();
  let string2 = readLine();
  
  let array1 = Array(26).fill(0);
  let array2 = Array(26).fill(0);
  
  for(let i=0; i<string1.length; i++) {
    array1[string1[i].charCodeAt(0) - 'a'.charCodeAt(0)]++;
  }
  for(let i=0; i<string2.length; i++) {
    array2[string2[i].charCodeAt(0) - 'a'.charCodeAt(0)]++;
  }
  let difference = 0;
  for(let i=0; i<26; i++) {
    difference = difference + array1[i] + array2[i] - 2*(Math.min(array1[i], array2[i]));
  }
  console.log(difference);
}