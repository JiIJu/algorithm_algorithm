// 2018 연속된 자연수의 합 구하기

#include <iostream>
using namespace std;

int main(){
	int N,S,E;
	S = 1;
	E = 1;
	int ans = 1;
	int sum=1;
	cin >> N;
	while(E!=N){
		if(sum==N){
			ans+=1;
			E +=1;
			sum += E;
		}
		else if(sum<N){
			E +=1;
			sum +=E;
		}
		else if(sum>N){
			sum -=S;
			S+=1;
		}		
	}
	cout << ans << '\n';
}
