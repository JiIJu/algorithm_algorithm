// 1253 좋은수 구하기

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int N;
	cin >> N;
	vector<int> data(N,0);
	for(int i=0;i<N;i++){
		cin >> data[i];
	}
	sort(data.begin(),data.end());
	int S,E,check,ans;
	long temp;
	long find;
	ans = 0;
	for(int i=0;i<N;i++){
		find = data[i];
		S = 0;
		E = N-1;
		temp = 0;
		while(S<E){
			temp = data[S] + data[E];
			if(temp == find){
				if (i!=S && i!=E){
				ans+=1;
				break;
				}
				else if(i==S){
					S+=1;
				}
				else if(i==E){
					E-=1;
				}
			}
			else if(temp > find){
				E-=1;
			}
			else if(temp < find){
				S +=1;
			}
		}
	}
	cout << ans << '\n';
	
}
