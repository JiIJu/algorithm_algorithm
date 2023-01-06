#include <stdio.h>
#include <stdlib.h>
int main() {
	int N = 0;
	scanf("%d", &N);
	int data[N];
	int maxv = 0;
	float avg = 0;
	for (int i = 0; i < N; i++) {
		scanf("%d", &data[i]);
		if (maxv < data[i]) {
			maxv = data[i];
		}
	}
	for (int i = 0; i < N; i++) {
		avg += ((double)data[i]/maxv)*100;
	}
	printf("%f", avg / N);
	return 0;
}
