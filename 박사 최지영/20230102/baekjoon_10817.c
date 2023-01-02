#include <stdio.h>



int main(void) {

	int A, B, C;
	scanf("%d %d %d", &A, &B, &C);

	if ((A <= B) && (A <= C)) {
		if ((B <= C)) {
			printf("%d", B);
		}
		else {
			printf("%d", C);
		}
	}

	else if ((A > B) && (A > C)) {
		if (B > C) {
			printf("%d",B);
		}
		else {
			printf("%d", C);
		}
	}

	else {
		printf("%d", A);
	}

	return 0;

}