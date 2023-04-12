#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int a,b;
    int ans=0;
    int cnt=0;
    int temp=0;
    cin>>a;
    cin>>b;
    while (b>0){
        temp = a*(b%10);
        cout << temp<<endl;
        b = b / 10;
        ans += temp*pow(10,cnt);
        // cout << ans<<endl;
        cnt+=1;
    }
    cout << ans;



    return 0;
}