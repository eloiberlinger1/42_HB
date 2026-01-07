# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>

void sort_int_tab(int *tab, unsigned int size)
{

	int i = 0;
	int temp = 0;

	while (i < size)
	{
		if (tab[i] > tab[i+1])
		{
			temp = tab[i];
			tab[i] = tab[i+1];
			tab[i+1] = temp;
		}
		i++;
	}

	return (tab);

}

int main()
{
	int array[3];
	array[0] = 1;
	array[1] = 1;
	array[3] = 1;

	sort_int_tab(array, 3);
	printf(array);

}
