
#include <stdio.h>

int isvalid(int ch, int baselen)
{
	char base[]="0123456789abcdef";
	char baseMAJ[]="0123456789ABCDEF";
	int i = 0;

	while (i < baselen)
	{
		if (ch == base[i] || ch == baseMAJ[i])
			return (1);
		i++;
	}

	return (-1);
}

int	ft_atoi_base(const char *str, int str_base)
{
	int	i = 0;
	int inc = 0;
	int tt = 0;
	int digit = 1;

	if (str_base < 2 || str_base > 16)
		return (0);

	while (str[i] == '-')
	{
		digit *= -1;
		i++;
	}

	while(str[i])
	{
		if (isvalid(str[i], str_base) == -1)
			return (0);


		if (str[i] >= '0' && str[i] <= '9')
			tt = (tt * str_base) + str[i] - '0';
		else if (str[i] >= 'a' && str[i] <= 'f')
			tt = (tt * str_base) + 10 + str[i] - 'a';
		else if (str[i] >= 'A' && str[i] <= 'F')
			tt = (tt * str_base) + 10 + str[i] - 'A';

		i++;
	}

	return (tt * digit);
}

int main()
{
	char test[] = "---0123";

	printf("%d \n", ft_atoi_base(test, 10));
}
