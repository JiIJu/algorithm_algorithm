#include <stdio.h>

int main() {
	int N, X, arr;

	scanf("%d %d", &N, &X);

	for (int i = 0; i < N; i++) {
		scanf("%d", &arr);

		if (X > arr)
			printf("%d ", arr);
	}
}