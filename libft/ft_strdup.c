/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 13:03:16 by eberling          #+#    #+#             */
/*   Updated: 2025/10/18 16:10:22 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	size_t		len;
	size_t		i;
	char		*ret;

	len = ft_strlen(s);
	ret = (char *) malloc((len + 1) * sizeof(char));
	if (ret == NULL)
		return (NULL);
	i = 0;
	while (i < len)
	{
		ret[i] = s[i];
		i++;
	}
	ret[i] = '\0';
	return (ret);
}

// #include <stdio.h>

// int main()
// {
// 	char test[] = "dadaskndkla";

// 	char *test2 = ft_strdup(test);

// 	printf("%s\n", test2);
// }