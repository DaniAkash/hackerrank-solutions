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
  let m_temp = readLine().split(' ');
  let m = parseInt(m_temp[0]);
  let n = parseInt(m_temp[1]);
  let magazine = readLine().split(' ');
  let ransom = readLine().split(' ');
  
  let magazineData = {};
  let possibility = 'Yes';
  
  magazine.map(word => {
    if(magazineData[word]) magazineData[word].push(word);
    else magazineData[word] = [word]
  });
  
  ransom.map(word => {
    if(magazineData[word].length>0) {
      magazineData[word].pop();
    } else {
      possibility = 'No';
    }
  });
  
  console.log(possibility); 
}