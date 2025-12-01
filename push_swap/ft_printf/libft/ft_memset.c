/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 17:43:26 by eberling          #+#    #+#             */
/*   Updated: 2025/10/13 11:03:49 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *s, int c, size_t n)
{
	size_t	i;
	char	*ptr;

	i = 0;
	ptr = (char *)s;
	while (i != n)
	{
		ptr[i] = (char)c;
		i++;
	}
	return (s);
}

// #include <stdio.h>
// int main()
// {
// 	char test[] = "bonjour       123";
// 	ft_memset(test, '#', 6);
// 	printf("%s\n", test);
// }