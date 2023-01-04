#include <stdio.h>

int main(){
	int N,M;
	scanf("%d %d",&N,&M);
	int a;
	for(int i=0;i<N;i++){
		scanf("%d",&a);
		if(M>a){
			printf("%d ",a);
		}
	}
	
	return 0;
}
