// 백준 1546 평균구하기

#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	double data[N];
	double ans;
	double maxv = 0;

	for(int i=0;i<N;i++){
		cin >> data[i];
	}
	for(int i=0;i<N;i++){
		if(maxv<data[i]){
			maxv = data[i];
		}
	}
	for(int i=0;i<N;i++){
		ans += (data[i]/maxv)*100.0;
	}
	
	cout << ans/N;
}
