#include <stdio.h>

int main(){
	int N,M;
	scanf("%d %d" ,&N,&M);
	int new_N,new_M;
	new_N = 100*(N%10)+10*((N/10)%10)+N/100;
	new_M = 100*(M%10)+10*((M/10)%10)+M/100;

	if(new_M<new_N){
		printf("%d",new_N);
	}
	else{
		printf("%d",new_M);
	}
	
}
