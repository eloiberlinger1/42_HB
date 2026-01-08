
# include <stdio.h>
# include <stdlib.h>

int     *ft_range(int start, int end)
{
	int i = 0;
	int size = end - start;
	int *array = malloc(sizeof(int)*(size));

	if (!array)
		return (NULL);

	while (i <= (size))
	{
		array[i] = start + i;
		i++;
	}

	printf("%d\n", array[0]);
	printf("%d\n", array[1]);
	printf("%d\n", array[2]);
	return (array);
}

int main()
{
	ft_range(1, 3);
}
