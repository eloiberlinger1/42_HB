#include <stdio.h>
# include <stdlib.h>
// Plus grand commun diviseur
//if (nbr1 % i == 0 && nbr2 % i == 0)



int main(int argc, char **argv)
{

	int max, a, b, i = 0;

	if (argc == 3)
	{
		a = atoi(argv[1]);
		b = atoi(argv[2]);
		i = a;
		if (a<b)
			max = b;
		else if (a>b)
			max = a;

		if (a > 0 && b > 0)
		{

			while (a != b)
			{
				if (a > b)
					a = a - b;
				else
					b = b -a;
			}
			printf("%d", a);
		}
	} else
		printf("\n");
	return (0);
}
