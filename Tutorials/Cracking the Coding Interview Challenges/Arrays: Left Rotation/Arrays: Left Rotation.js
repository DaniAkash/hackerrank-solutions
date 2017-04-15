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

function leftRotate(arr, arraySize, rotations) {
  let i,j,k,temp;
  for(i=0; i<gcd(arraySize, rotations); i++) {
    temp = arr[i];
    j = i;
    while(true) {
      k = j+rotations;
      
      if(k>=arraySize) k = k-arraySize;
      
      if(k===i) break;
      
      arr[j] = arr[k]
      
      j = k;
    }
    arr[j] = temp;
  }
  return;
}

function gcd(a,b) {
  if(b==0) return a;
  return gcd(b, a%b);
}

function print(arr) {
  arr.map(each => process.stdout.write(`${each} `))
}

function main() {
  let n_temp = readLine().split(' ');
  let arraySize = parseInt(n_temp[0]);
  let rotations = parseInt(n_temp[1]);
  arr = readLine().split(' ');
  arr = arr.map(Number);
  
  leftRotate(arr, arraySize, rotations);
  print(arr)
}
