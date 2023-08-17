// 1940 주몽의 명령

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int N,M;
	cin >> N;
	cin >> M;
	vector<int> data(N,0);
	for(int i=0;i<N;i++){
		cin >> data[i];
	}
	sort(data.begin(),data.end());
	int ans=0;
	int s=0;
	int e=N-1;
	int check = 0;
	while(s<e){
		check = data[s] + data[e];
		if (check == M){
			ans+=1;
			s+=1;
			e-=1;
		}
		else if (check>M){
			e-=1;
		}
		else if (check<M){
			s+=1;
		}
	}
	cout << ans << '\n' ;
}
