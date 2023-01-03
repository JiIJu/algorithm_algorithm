#include <stdio.h>

int main(){
	int data[100];
	int maxv=0;
	int index = 0;
	
	for(int i=0;i<=8;i++){
		scanf("%d\n",&data[i]);
	}
	for(int i=0;i<=8;i++){
		if(maxv<data[i]){
			maxv = data[i];
			index = i+1;
		}
	}
	printf("%d\n%d",maxv,index);
}
