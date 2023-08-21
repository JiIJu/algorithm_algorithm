// 11286 절댓값 힙 구학

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct compare {
	bool operator()(int o1,int o2) {
		int first_abs = abs(o1);
		int secont_abs = abs(o2);
		if (first_abs == secont_abs){
			return o1>o2;
		}
		else {
			return first_abs>secont_abs;
		}
	}
};

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N;
	cin >> N;
	priority_queue<int,vector<int>,compare> MyQueue;
	
	for ( int i = 0; i<N;i++){
		int temp;
		cin >> temp;
		if (temp==0){
			if (MyQueue.size() == 0){
				cout << 0 << '\n';
			}
			else {
				cout << MyQueue.top() << '\n';
				MyQueue.pop();
			}}
		else{
			MyQueue.push(temp);
		}
		
	}
}
