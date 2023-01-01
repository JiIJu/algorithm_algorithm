#include <stdio.h>

int main()
{
	int n;
	int sum = 0;
	scanf("%d", &n);
	for (int j = 1; j <= n; j++)
	{
		sum += j;

	}
	printf("%d", sum);

	return 0;
}