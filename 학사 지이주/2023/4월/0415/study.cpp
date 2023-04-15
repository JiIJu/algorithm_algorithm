#include <iostream>

using namespace std;
int main() {
    int n;
    int* data = new int[n];
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> data[i];
    }
    int cnt = 0;
    int v;
    cin >> v;
    for(int i=0;i<n;i++){
        if(data[i]==v){
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}