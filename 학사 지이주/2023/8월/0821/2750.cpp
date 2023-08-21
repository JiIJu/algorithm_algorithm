// 2750 수 정렬하기

#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	int data[N];
	for(int i=0;i<N;i++){
		cin >> data[i];
	}
	int temp;
	for(int i=0;i<N-1;i++){
		for(int j=i+1;j<N;j++){
			if (data[i]>data[j]){
				temp = data[i];
				data[i] = data[j];
				data[j] = temp;
			}
		}
	}
	for (int i =0;i<N;i++){
		cout << data[i] << '\n';
	}
}
