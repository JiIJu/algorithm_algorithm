#include <stdio.h>

int main(){
	int N;
	scanf("%d",&N);
	char M[N];
	scanf("%s",M);
	int sum=0;
	for(int i=0;i<N;i++){
		sum += M[i]-'0';
	}
	printf("%d",sum);
}