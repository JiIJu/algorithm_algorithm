// 1427 내림차순으로 자릿수 정렬하기

#include <iostream>

using namespace std;

int main() {
	string data;
	cin >> data;
	int l;
	l = data.size();
	// int check[l] = {};
	// for(int i=0;i<l;i++){
	// 	check[i] = data[i];
	// }
	for(int i=0;i<l-1;i++){
		int maxv = data[i];
		int maxv_idx = i;
		for(int j=i+1;j<l;j++){
			if(data[j]>maxv){
				maxv = data[j];
				maxv_idx = j;
			}
		}
		if(maxv>data[i]){
			data[maxv_idx] = data[i];
			data[i] = maxv;
		}
	}
	for(int i=0;i<l;i++){
		cout << data[i];
	}
}
