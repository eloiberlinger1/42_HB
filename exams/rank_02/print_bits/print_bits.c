
#include <unistd.h>

void	print_bits(unsigned char octet)
{
	int i = 7;

	char bit;

	while (i >= 0)
	{
		bit = (octet >> i & 1) + '0';

		write(1, &bit,1);
		i--;
	}

}

int main()
{
	print_bits(2);
}
