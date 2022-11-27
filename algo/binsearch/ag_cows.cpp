#include<iostream>
#include <bits/stdc++.h>

using namespace std;

bool safe_Distance(vector<int> &stalls,int n,int m,int mid){
    int distance=stalls[0];
    int cows=1;

    for(int j=0;j<m;j++){
        if (stalls[j] - distance >= mid)
        {
            cows++;
            if(cows == m){
                return true;
            }
            distance=stalls[j];
        }
        

    }
    return false;


}

long long agCows(vector<int> &stalls,int n,int m){
    // making vector sorted first 
    sort(stalls.begin(),stalls.end());
    int low=0;
    int high=0;
    for(int i=0;i<n;i++){
        high+=stalls[i];
    }

    int ans=-1;

    while (low<=high)
    {
        int mid=(low+high)/2;
        if(safe_Distance(stalls,n,m,mid)){
            ans=mid;
            low=mid+1;
        }else{
            high=mid-1;
        }


    }
    
    return ans;

}

int main(){

}
