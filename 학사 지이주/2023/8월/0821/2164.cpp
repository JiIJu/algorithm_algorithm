// 2164 카드2

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(){
	int N;
	cin >> N;
	queue<int> data;
	for(int i=0;i<N;i++){
		data.push(i+1);
	}
	while(data.size()>1){
		data.pop();
		data.push(data.front());
		data.pop();
	}
	cout << data.front();
	
}
