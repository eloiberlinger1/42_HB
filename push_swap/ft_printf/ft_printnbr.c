/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printnbr.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 16:00:31 by eberling          #+#    #+#             */
/*   Updated: 2025/11/04 17:25:27 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	process_int(va_list args)
{
	char	*temp;
	int		ret;
	int		i;

	i = va_arg(args, int);
	if (!i)
	{
		ret = ft_putstr_fd("0", 1);
		if (ret == -1)
			return (-1);
		return (ret);
	}
	temp = ft_itoa(i);
	if (!temp)
		return (-1);
	ret = ft_putstr_fd(temp, 1);
	if (ret == -1)
		return (-1);
	free(temp);
	return (ret);
}

static int	print_uint(unsigned int nbr)
{
	int	c;
	int	len;
	int	ret;

	len = 0;
	if (nbr >= 10)
	{
		ret = print_uint(nbr / 10);
		if (ret == -1)
			return (-1);
		len += ret;
	}
	c = (nbr % 10) + '0';
	ret = ft_putchar_fd(c, 1);
	if (ret == -1)
		return (-1);
	len += ret;
	return (len);
}

int	process_uint(va_list args)
{
	int	u;
	int	ret;

	u = va_arg(args, unsigned int);
	if (!u)
	{
		ret = ft_putstr_fd("0", 1);
		if (ret == -1)
			return (-1);
		return (ret);
	}
	return (print_uint(u));
}
