/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/06 00:28:34 by eberling          #+#    #+#             */
/*   Updated: 2025/05/13 13:02:16 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	handleminus(int *nb)
{
	if (*nb < 0)
	{
		ft_putchar('-');
		*nb = -*nb;
	}
}

void	ft_putnbr(int nb)
{
	char	digits[20];
	int		i;

	if (nb == -2147483648)
	{
		write(1, "-", 1);
		write(1, "2", 1);
		nb = 147483648;
	}
	handleminus(&nb);
	if (nb == 0)
		ft_putchar('0');
	else
	{
		i = 0;
		while (nb > 0)
		{
			digits[i++] = nb % 10 + '0';
			nb = nb / 10;
		}
		i--;
		while (i >= 0)
			ft_putchar(digits[i--]);
	}
}

#include <stdio.h>
int main(void){
	int nmbr = -2147483648;
	
	ft_putnbr(nmbr);
}