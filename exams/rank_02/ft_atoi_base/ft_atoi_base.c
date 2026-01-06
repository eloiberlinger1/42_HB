
# include <stdio.h>
# include <stdlib.h>

int checkbase(char c, int baselen)
{
	char base[] = "0123456789abcdef";
	char base1[] = "0123456789ABCDEF";
	int i = 0;

	while (i < baselen)
	{
		if (c == base1[i] || c == base[i])
			return (1);
		i++;
	}
	return (-1);
}

int	ft_atoi_base(const char *str, int str_base)
{
	int i = 0;
	int tt = 0;
	int digit = 1;

	if (str[i] == '-')
{
	digit = -1;
	i++;
}

	while (str[i])
	{

		if (checkbase(str[i], str_base) == -1)
			return (0);

		if (str[i] >= '0' && str[i] <= '9')
			tt = (tt * str_base) + str[i] - '0';
		else if (str[i] >= 'a' && str[i] <= 'z')
			tt = (tt * str_base) + str[i] + 10 - 'a';
		else if (str[i] >= 'A' && str[i] <= 'Z')
			tt = (tt * str_base) + str[i] + 10 - 'A';

		i++;
	}
	return (tt * digit);
}


int main()
{
	char test[] = "123";

	printf("%d\n", ft_atoi_base(test, 10));
}
