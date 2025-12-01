/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/12 12:06:28 by eberling          #+#    #+#             */
/*   Updated: 2025/10/17 18:07:53 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *str, int ch)
{
	char	*ret;

	ret = (char *)str;
	while (*ret != '\0')
	{
		if (*ret == (char)ch)
			return (ret);
		ret++;
	}
	if ((char)ch == '\0')
		return (ret);
	return (NULL);
}
// #include <stdio.h>
// int main()
// {
// 	char c = 'e';
// 	char string[] = "teste";

// 	printf("%s\n", ft_strchr(string, c));
// }