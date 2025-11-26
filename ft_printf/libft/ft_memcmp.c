/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/12 14:39:22 by eberling          #+#    #+#             */
/*   Updated: 2025/10/13 11:03:38 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	size_t			i;
	unsigned char	*ns1;
	unsigned char	*ns2;

	ns1 = (unsigned char *)s1;
	ns2 = (unsigned char *)s2;
	i = 0;
	while (i < n)
	{
		if (ns1[i] != ns2[i])
			return ((int)ns1[i] - (int)ns2[i]);
		i++;
	}
	return (0);
}

// #include <string.h>
// #include <stdio.h>
// int main()
// {
// 	int test1[] = {1,2,3,4};
// 	int test2[] = {1,2,3,5};

// 	printf("%d\n", ft_memcmp(test1, test2, sizeof(test2)));
// }