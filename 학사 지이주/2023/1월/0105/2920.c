#include <stdio.h>

int main(){
	int data[8];
	for(int i=0;i<8;i++){
		scanf("%d",&data[i]);
	}
	int temp=data[0];
	int check[7];
	
	for(int i=1;i<8;i++){
		if(data[i]>temp){
			check[i-1]=1;
		}
		else{
			check[i-1]=-1;
		}
		temp = data[i];
	}
	int ans =0;
	for(int i=0;i<7;i++){
		ans+=check[i];
	}
	if(ans==7){
		printf("%s","ascending");
	}else if(ans==-7){
		printf("%s","descending");
	}else{
		printf("%s","mixed");
	}
}
