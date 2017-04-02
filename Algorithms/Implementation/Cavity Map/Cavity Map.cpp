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

#include<iostream>  
 using namespace std;  
 int main(){  
   int n,i,j;  
   cin>>n;  
   string inp[n];  
   for(i=0;i<n;i++)  
   {  
     cin>>inp[i];    
   }  
   for(i=0;i<n;i++)  
   {  
     for(j=0;j<n;j++)  
     {  
       if(i == 0 || j == 0 || i == n-1 || j == n-1 )  
       {  
         cout<<inp[i][j];  
       }  
       else if(inp[i][j] > inp[i][j-1] && inp[i][j] > inp[i][j+1] && inp[i][j] >inp[i-1][j] && inp[i][j] > inp[i+1][j])  
       {  
         cout<<"X" ;    
       }  
       else  
       {  
         cout<<inp[i][j];  
       }  
     }  
     cout<<endl;  
   }  
   return 0;  
 }