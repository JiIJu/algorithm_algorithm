// 12891 DNA비밀번호

#include <iostream>
using namespace std;

int main(){
	int check[4] = {};
	// A C G T
	int dna[4] = {};
	int ans = 0;
	int P,S;
	cin >> P >> S;
	string data;
	cin >> data;
	for(int i=0;i<4;i++){
		cin >> dna[i];
	}
	for(int j=0;j<S;j++){
			if (data[j]=='A'){
				check[0]+=1;
			}
			else if (data[j]=='C'){
				check[1] +=1;
			}
			else if (data[j]=='G'){
				check[2]+=1;
			}
			else if (data[j]=='T'){
				check[3]+=1;
			}
		}
	if(check[0]>=dna[0] && check[1]>=dna[1] && check[2]>=dna[2] && check[3]>=dna[3] ){
		ans+=1;
	}
	int temp;
	for(int i=S;i<P;i++){
		if (data[i]=='A'){
				check[0]+=1;
			}
		else if (data[i]=='C'){
			check[1] +=1;
		}
		else if (data[i]=='G'){
			check[2]+=1;
		}
		else if (data[i]=='T'){
			check[3]+=1;
		}
		if (data[i-S]=='A'){
			check[0]-=1;
			}
		else if (data[i-S]=='C'){
			check[1] -=1;
		}
		else if (data[i-S]=='G'){
			check[2]-=1;
		}
		else if (data[i-S]=='T'){
			check[3]-=1;
		}
		if(check[0]>=dna[0] && check[1]>=dna[1] && check[2]>=dna[2] && check[3]>=dna[3] ){
		ans+=1;
	}
	}
	cout << ans << '\n';
	
}
