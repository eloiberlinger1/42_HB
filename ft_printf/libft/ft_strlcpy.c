/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/10 17:55:15 by eberling          #+#    #+#             */
/*   Updated: 2025/10/17 11:26:12 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	i;

	if (size == 0)
		return (ft_strlen(src));
	i = 0;
	while (i < size - 1 && src[i] != '\0')
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (ft_strlen(src));
}

// #include <stdio.h>
// int main(){

// 	char test1[] = "adasdasd";
// 	char test2[3];
// 	char test3[3];

// 	printf("ft result :\n");
// 	ft_strlcpy(test2, "aaa", 0);
// 	printf("%s\n", test2);
// 	printf("string.h result :\n");
// 	strlcpy(test3, "aaa", 0);
// 	printf("%s\n", test3);

// }