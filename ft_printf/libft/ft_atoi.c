/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 21:31:50 by eberling          #+#    #+#             */
/*   Updated: 2025/10/24 12:02:19 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

static int	ft_isspace(char c)
{
	if (c == '\t' || c == '\n' || c == '\v'
		|| c == '\f' || c == '\r' || c == ' ')
		return (1);
	return (0);
}

int	ft_atoi(const char *num)
{
	int	digit;
	int	tt;
	int	i;

	tt = 0;
	digit = 1;
	i = 0;
	while (ft_isspace(num[i]))
		i++;
	if (num[i] == '+' || num[i] == '-')
	{
		if (num[i] == '-')
			digit = digit * (-1);
		i++;
	}
	while (num[i] >= '0' && num[i] <= '9')
	{
		tt = (tt * 10) + (num[i] - '0');
		i++;
	}
	return (tt * digit);
}

// #include <stdio.h>
// int main(void)
// {
// 	char test[60] = "	  --+223 1231";
// 	printf("%d\n", ft_atoi(test));
// 	ft_atoi(test);
// }