#include <stdio.h>

int main(){
	int n;
	int data[43];
	for(int i=0;i<43;i++){
		data[i]=0;
	}
	for(int i=0;i<10;i++){
		scanf("%d",&n);
		data[n%42]=1;
	}
	int ans=0;
	for(int i=0;i<43;i++){
		ans+=data[i];
	}
	printf("%d",ans);
	
}
