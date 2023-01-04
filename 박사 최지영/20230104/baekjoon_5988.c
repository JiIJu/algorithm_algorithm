#include <stdio.h>

int main(void) {

	int N, len;
	char arr[70];

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		scanf("%s", arr);
		len = strlen(arr);

		if (arr[len - 1] % 2 == 0)
			printf("even\n");

		else if (arr[len - 1] % 2 == 1)
			printf("odd\n");
	}

	return 0;

}