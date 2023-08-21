// 1377 버블소트

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int N;
	cin >> N;
	vector<pair<int,int>> A(N);
	for(int i=0;i<N;i++){
		cin >> A[i].first;
		A[i].second = i;
	}
	int maxv = 0;
	sort(A.begin(),A.end());
	for(int i=0;i<N;i++){
		if (maxv<A[i].second - i){
			maxv = A[i].second - i;
		}
	}
	cout << maxv+1;
}
