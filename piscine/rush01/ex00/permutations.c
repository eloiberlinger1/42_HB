#include <stdio.h>
#include <stdlib.h>

void	ft_swap(int *a, int *b)
{
	int	temp;

	temp = *b;
	*b = *a;
	*a = temp;
}

void	perm(int c[4], int a, int n)
{
	int j;
	int i;
	if(a == n){// display
		i = 0;
		while (i < 4)
		{
			printf("%d ", c[i]);
		}
		
		printf("\n");
	}
	else
	{
		for(j=a; j<=n; j++)
		{
			ft_swap((c + a), (c + j));
			perm(c, a+1, n);
			ft_swap((c + a), (c + j));
		}
	}
}

void	get_permutations(int *permut[24][4])
{

	int c[4] = {1,2,3,4};
	perm(c, 0, 0);

}
