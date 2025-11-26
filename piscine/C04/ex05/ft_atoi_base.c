/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/12 00:54:30 by eberling          #+#    #+#             */
/*   Updated: 2025/05/12 14:59:15 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
		i++;
	return (i);
}

int	char_in_base(char c, char *base)
{
	while (*base)
	{
		if (*base == c)
			return (1);
		base++;
	}
	return (0);
}

int	get_index(char c, char *base)
{
	int	i;

	i = 0;
	while (*base)
	{
		if (*base == c)
			return (i);
		i++;
		base++;
	}
	return (0);
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
		return (0);
	return (1);
}

int	ft_atoi_base(char *str, char *base)
{
	int	result;
	int	digit;
	int	i;

	digit = 1;
	result = 0;
	i = 0;
	if (!checkbase(base))
		return (0);
	while ((str[i] == '\t' || str[i] == '\n' || str[i] == '\v'
			|| str[i] == '\f' || str[i] == '\r' || str[i] == ' '))
		i++;
	while (str[i] == '+' || str[i] == '-')
	{
		if (str[i] == '-')
			digit = digit * (-1);
		i++;
	}
	while (char_in_base(str[i], base))
	{
		result = (result * ft_strlen(base)) + get_index(str[i], base);
		i++;
	}
	return (digit * result);
}
/* 
#include <stdio.h>
int main(void)
{
	char test[60] = "	  ---p 1231";
	printf("%d\n", ft_atoi_base(test, "poneyvif"));
	//ft_atoi_base(test, "01");
} */