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
    let t = parseInt(readLine());
    for(let a0 = 0; a0 < t; a0++){
        let expression = readLine();
        
        stack = [], isBroken = false;
        
        for(let i=0; i<expression.length; i++) {
            let type = expression[i];
            if(type === '[' || type === '{' || type === '(') {
                stack.push(type);
            } else {
                if(type === ']') {
                    if(stack[stack.length-1] === '[') {
                        stack.pop();
                    } else {
                        console.log('NO');
                        isBroken = true;
                        break;
                    }
                } else if(type === '}') {
                    if(stack[stack.length-1] === '{') {
                        stack.pop();
                    } else {
                        console.log('NO');
                        isBroken = true;
                        break;
                    }
                } else if(type === ')') {
                    if(stack[stack.length-1] === '(') {
                        stack.pop();
                    } else {
                        console.log('NO');
                        isBroken = true;
                        break;
                    }
                }
            }
        }
        
        if(!isBroken) {
            if(stack.length === 0) console.log('YES');
            else console.log('NO');
        }
    }
}
