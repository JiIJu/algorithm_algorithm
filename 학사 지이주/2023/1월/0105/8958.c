#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
	int n;
	
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		char data[81];
		scanf("%s\n",data);
		int len_data = strlen(data);
		int num[len_data];
		if(data[0]=='O'){
			num[0]=1;
		}
		else{
			num[0]=0;
		}
		for(int j=1;j<len_data;j++){
			num[j]=0;
		}
		for(int j=1;j<len_data;j++){
			if(data[j]=='O'){
			num[j]= num[j-1]+1;
		}
		else{
			num[j]=0;
		}
		}
		int ans=0;
		for(int j=0;j<len_data;j++){
			ans+=num[j];
		}
		printf("%d\n",ans);
	}
}
