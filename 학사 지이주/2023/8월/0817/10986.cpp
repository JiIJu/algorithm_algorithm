// 10986 나머지합

#include <iostream>

using namespace std;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N,M;
	long ans = 0;
	cin >> N >> M;
	long data[N] = {};
	long remainder[M] = {};
	for(int i=0;i<N;i++){
		cin >> data[i];
	}
	int check[N+1] = {};
	for(int i=1;i<N+1;i++){
		check[i] = (check[i-1] + data[i-1])%M;
	}
	for(int i=1;i<N+1;i++){
		if(check[i]==0){
			ans+=1;
		}
		remainder[check[i]] += 1;
		}
	for(int i=0;i<M;i++){
		if (remainder[i]>1){
		ans += (remainder[i] * (remainder[i]-1)/2);
	
		}}
	
	cout << ans << '\n';
}
