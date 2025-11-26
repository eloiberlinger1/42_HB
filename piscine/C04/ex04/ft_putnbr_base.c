/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/08 20:40:02 by eberling          #+#    #+#             */
/*   Updated: 2025/05/13 15:11:05 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

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

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
		i++;
	return (i);
}

int	checkbase(char *str)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	while (str[i] != '\0')
	{
		if (str[i] == '+' || str[i] == '-')
			return (0);
		j = i;
		while (str[j + 1] != '\0')
		{
			if (str[i] == str[j + 1])
			{
				return (0);
			}
			j++;
		}
		i++;
	}
	if (ft_strlen(str) <= 1)
	{
		return (0);
	}
	return (1);
}

void	handleminus(long int *nb)
{
	if (*nb < 0)
	{
		write(1, "-", 1);
		*nb = -*nb;
	}
}

void	ft_putnbr_base(int nbr, char *base)
{
	int			base_len;
	int			i;
	char		result[500];
	long int	longnbr;

	base_len = ft_strlen(base);
	longnbr = nbr;
	if (!checkbase(base))
		return ;
	handleminus(&longnbr);
	i = 0;
	while (longnbr > 0)
	{
		result[i++] = base[longnbr % base_len];
		longnbr = longnbr / base_len;
	}
	if (longnbr == 0 && i == 0)
	{
		write(1, &base[0], 1);
		return ;
	}
	i--;
	while (i >= 0)
		write(1, &result[i--], 1);
}

#include <stdio.h>
int main(){
	int nbr = -45645649;

	ft_putnbr_base(nbr, "012abcdefghjikl;34567");

	// -2147483648 .. 2147483647
	// -2147483648 * -1 = 2147483648 = -2147483648 
}
