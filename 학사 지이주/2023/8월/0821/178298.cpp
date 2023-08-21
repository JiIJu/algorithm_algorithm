// 17298 오큰수

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main(){
	int N;
	cin >> N;
	stack<int> s;
	int ans[N];
	int data[N];
	
	for(int i=0;i<N;i++){
		cin >> data[i];
	}
	for (int i=N-1;i>=0;i--){
		while(s.size()>0 && s.top()<=data[i]){
			s.pop();
		}
		if(s.size()==0){
			ans[i]=-1;
		}
		else{
			ans[i] = s.top();
		}
		s.push(data[i]);
	}
	for(int i = 0;i<N;i++){
		cout<<ans[i]<<" ";
	}	
}
