/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printchar.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 16:01:21 by eberling          #+#    #+#             */
/*   Updated: 2025/11/04 17:27:00 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	process_char(va_list args)
{
	int	c;
	int	result;

	c = va_arg(args, int);
	result = write(1, &c, 1);
	if (result == -1)
		return (-1);
	return (1);
}

int	process_str(va_list args)
{
	char	*value;
	int		result;

	value = va_arg(args, char *);
	if (!value)
	{
		result = ft_putstr_fd("(null)", 1);
		if (result == -1)
			return (-1);
		return (result);
	}
	result = (ft_putstr_fd(value, 1));
	if (result == -1)
		return (-1);
	return (result);
}

int	process_unknown(char f)
{
	int	result;
	int	tt;

	tt = 0;
	result = write(1, "%%", 1);
	if (result == -1)
		return (-1);
	tt += result;
	result = write(1, &f, 1);
	if (result == -1)
		return (-1);
	tt += result;
	return (tt);
}
