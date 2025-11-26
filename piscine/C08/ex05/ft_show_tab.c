/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_show_tab.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/15 14:14:16 by eberling          #+#    #+#             */
/*   Updated: 2025/05/21 21:39:18 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include "ft_stock_str.h"
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

void	ft_putstr(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		write(1, &str[i], 1);
		i++;
	}
}

void	ft_show_tab(struct s_stock_str *par)
{
	int	i;

	i = 0;
	while (par[i].str)
	{
		ft_putstr(par[i].str);
		ft_putstr("\n");
		ft_putnbr(par[i].size);
		ft_putstr("\n");
		ft_putstr(par[i].copy);
		ft_putstr("\n");
		i++;
	}
}
