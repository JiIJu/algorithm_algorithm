#include <stdio.h>

int main()
{
	int score;
	scanf("%d", &score);
	char rank;
	if (score >= 90 && score <= 100) {
		rank = 'A';
	}
	else if (score >= 80 && score <= 89) {
		rank = 'B';
	}
	else if (score >= 70 && score <= 79) {
		rank = 'C';
	}
	else if (score >= 60 && score <= 69) {
		rank = 'D';
	}
	else {
		rank = 'F';
	}

	printf("%c", rank);

	return 0;
}