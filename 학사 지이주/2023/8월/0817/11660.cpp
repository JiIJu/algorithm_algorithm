// 11660 구간합구하기2

#include <iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N,M;
	cin >> N >> M;
	int data[N][N];
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			cin >> data[i][j];
		}
	}
	int check[N+1][N+1] = {};
	for(int i=1;i<N+1;i++){
		for(int j=1;j<N+1;j++){
			check[i][j] = check[i-1][j] + check[i][j-1] + data[i-1][j-1]-check[i-1][j-1];
		}
	}
	// for(int i=0;i<N+1;i++){
	// 	for(int j=0;j<N+1;j++){
	// 		cout << check[i][j] << ' ';
	// 	}
	// 	cout << endl;
	// }
	for(int i=0;i<M;i++){
		int x1,x2,y1,y2;
		cin >> x1 >> y1 >> x2 >> y2 ;
		cout << check[x2][y2] - check[x1-1][y2] - check[x2][y1-1] + check[x1-1][y1-1] << endl;
	}

}
