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

function processData(input) {
    let data = input.split('\n');
    let queue = [];
    data.slice(1).map(item => {
        let set = item.split(' ').map(Number);
        if(set[0] === 1) {
            queue.push(set[1]);
        } else if(set[0] === 2) {
            queue.shift();
        } else if(set[0] === 3) {
            console.log(queue[0]);
        }
    });
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});