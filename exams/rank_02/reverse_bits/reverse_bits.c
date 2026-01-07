
#include <unistd.h>
#include <stdio.h>

void	print_bits(unsigned char octet)
{
	int i = 7;

	char bit;

	while (i >= 0)
	{
		bit = (octet >> i & 1) + '0';

		write(1, &bit, 1);
		i--;
	}

}

unsigned char	reverse_bits(unsigned char octet)
{
	char bit;
	char temp;
	unsigned char ret = 0;
	int i = 0;

	while (i < 8)
	{
		temp = octet >> i & 1;
		ret = ret | temp << (7 - i);

		i++;
	}

	return ret;

}

int main()
{
	print_bits(38);
	printf("\n\n\n");
	print_bits(reverse_bits(38));
}
