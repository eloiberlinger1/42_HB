/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 09:49:04 by eberling          #+#    #+#             */
/*   Updated: 2025/10/14 10:08:34 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	s1_len;
	size_t	s2_len;
	size_t	i;
	size_t	i_ret;
	char	*ret;

	s1_len = ft_strlen(s1);
	s2_len = ft_strlen(s2);
	ret = malloc(((s1_len + s2_len) + 1) * sizeof(char));
	if (ret == NULL)
		return (NULL);
	i = -1;
	while (++i < s1_len)
		ret[i] = s1[i];
	i_ret = i;
	i = -1;
	while (++i < s2_len)
		ret[i_ret + i] = s2[i];
	ret[i_ret + i] = '\0';
	return (ret);
}

// int main()
// {
// 	char test1[] = "asdasdasd";
// 	char test2[] = "1215156";
// 	printf("%s\n", ft_strjoin(test1, test2));
// }