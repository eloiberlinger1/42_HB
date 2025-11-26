/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/12 22:53:36 by eberling          #+#    #+#             */
/*   Updated: 2025/10/17 16:08:30 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *haystack, const char *needle, size_t len)
{
	size_t	i;
	size_t	n;

	i = 0;
	n = 0;
	if (needle[0] == '\0')
		return ((char *)haystack);
	while (haystack[i] && i < len)
	{
		while (needle[n] == haystack[i + n] && haystack[i + n] && i + n < len)
		{
			n++;
			if (needle[n] == '\0')
				return ((char *)haystack + i);
		}
		i++;
		n = 0;
	}
	return (NULL);
}
// #include <stdio.h>
// int main()
// {
// 	char test1[] = "1234";
// 	char test2[] = "23";

// 	char *test = ft_strnstr(test1, test2, 2);

// 	printf("%s\n", test);
// }
