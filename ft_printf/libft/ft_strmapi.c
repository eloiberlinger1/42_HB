/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 09:26:34 by eberling          #+#    #+#             */
/*   Updated: 2025/10/15 10:50:41 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	int		i;
	char	*ret;

	if (!s || !f)
		return (NULL);
	i = 0;
	ret = (char *) malloc(ft_strlen(s) + 1);
	if (!ret)
		return (NULL);
	while (s[i] != '\0')
	{
		ret[i] = f((unsigned int) i, (char) s[i]);
		i++;
	}
	ret[i] = '\0';
	return (ret);
}

// char ft_test(unsigned int i, char c)
// {
// 	if(i == 0 || i == 1)
// 		c = '>';
// 	return (c);
// }

// #include <stdio.h>
// int main()
// {
// 	char *test;

// 	test = ft_strmapi("   This is a testing string", ft_test);
// 	printf("%s\n", test);
// }
