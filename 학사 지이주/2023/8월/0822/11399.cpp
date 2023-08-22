// 11399 ATM

#include <iostream>
#include <vector>
using namespace std;

int main(){
	int N;
	cin >> N;
	vector<int> ans(N,0);
	vector<int> data(N,0);
	
	for(int i=0;i<N;i++){
		cin >> data[i];
	}
	for(int i=1;i<N;i++){
		int point = i;
		int value = data[i];
		for(int j=i-1;j>=0;j--){
			if(data[i]>data[j]){
				point = j+1;
				break;
			}
			if(j==0){
				point = 0;
			}
		}
		for(int j=i;j>point;j--){
			data[j] = data[j-1];
		}
		data[point] = value;
	}
	ans[0] = data[0];
	for(int i=1;i<N;i++){
		ans[i] = ans[i-1]+data[i];
	}
	int answer = 0;
	for(int i=0;i<N;i++){
		answer += ans[i];
	}
	cout << answer;
}
