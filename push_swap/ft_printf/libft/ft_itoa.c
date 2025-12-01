/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 17:07:26 by eberling          #+#    #+#             */
/*   Updated: 2025/10/22 19:51:03 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	get_char_size(long long n)
{
	int	c;

	c = 0;
	if (n == 0)
		return (1);
	if (n < 0)
	{
		c++;
		n = -n;
	}
	while (n > 0)
	{
		n /= 10;
		c++;
	}
	return (c);
}

char	*ft_itoa(int nb)
{
	char		*ret;
	long long	n;
	size_t		i;

	n = (long long) nb;
	i = get_char_size(n);
	ret = (char *) malloc((i + 1) * sizeof(char));
	if (!ret)
		return (NULL);
	ret[i] = '\0';
	if (n == 0)
		ret[0] = '0';
	if (n < 0)
	{
		ret[0] = '-';
		n = -n;
	}
	while (n > 0)
	{
		i--;
		ret[i] = (n % 10) + '0';
		n /= 10;
	}
	return (ret);
}

// #include <stdio.h>
// int main()
// {
// 	int test = -2147483648;
//     printf("%s\n", ft_itoa(test));
// 	test = -5465;
//     printf("%s\n", ft_itoa(test));
// }