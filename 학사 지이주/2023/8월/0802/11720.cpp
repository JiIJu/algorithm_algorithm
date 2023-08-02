// 코드잇 숫자의합 구하기

#include <iostream>
using namespace std;
	
int main() {
	int n;
	string data;
	int ans = 0;
	cin >> n;
	cin >> data;
	for(int i=0;i<n;i++){
		ans += data[i] - '0';
	}
	cout << ans;
	
}
