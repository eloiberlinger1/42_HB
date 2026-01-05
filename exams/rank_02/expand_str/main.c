# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>


int ft_strlen(char *str)
{
	int c = 0;
	while (str[c] != 0)
		c++;
	return (c);
}

void expand_str(char *str)
{
	int i = 0;
	int stringsize = ft_strlen(str);
	int space_count = 0;


	while (str[i] == ' ')
		i++;
	while (i <= stringsize)
	{
		space_count = 0;
		while (str[i] == ' ')
		{
			space_count = 1;
			i++;
		}
		while (space_count != 0 && ++space_count <= 3+1)
			write(1, "-", 1);
		write(1, &str[i], 1);
		i++;
	}

}

int main(int argc, char **argv)
{
	if(argc > 1)
	{
		expand_str(argv[1]);
	}
}
