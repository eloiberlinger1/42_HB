/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/10 11:35:34 by eberling          #+#    #+#             */
/*   Updated: 2025/10/24 11:55:40 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t size)
{
	unsigned char		*d;
	const unsigned char	*s;

	if (size == 0)
		return (dest);
	if (!dest && !src)
		return (NULL);
	d = (unsigned char *) dest;
	s = (const unsigned char *) src;
	while (size--)
		*d++ = *s++;
	return (dest);
}

// #include <stdio.h>
// int main()
// {
// 	int test1[6] = {1,2,3,4,5,6};
// 	int test2[6] = {1,9,9,4,2,0};

// 	ft_memcpy(test2, test1, 3*sizeof(int));

// 	printf("%d\n", test2[0]);
// 	printf("%d\n", test2[1]);
// 	printf("%d\n", test2[2]);

// }