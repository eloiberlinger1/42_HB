/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/06 10:23:29 by eberling          #+#    #+#             */
/*   Updated: 2025/05/14 17:01:19 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_isspace(char c)
{
	if (c == '\t' || c == '\n' || c == '\v'
		|| c == '\f' || c == '\r' || c == ' ')
		return (1);
	else
		return (0);
}

int	ft_atoi(char *str)
{
	int	digit;
	int	tt;
	int	i;

	i = 0;
	tt = 0;
	digit = 1;
	while (ft_isspace(str[i]))
		i++;
	while (str[i] == '+' || str[i] == '-')
	{
		if (str[i] == '-')
			digit = digit * (-1);
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9')
	{
		if (str[i] >= '0' && str[i] <= '9')
			tt = (tt * 10) + (str[i] - '0');
		i++;
	}
	return (tt * digit);
}
#include <stdio.h>
int main(void)
{
	char test[60] = "	  --+223 1231";
	printf("%d\n", ft_atoi(test));
	//ft_atoi(test);
}