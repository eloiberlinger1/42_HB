/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 20:52:43 by eberling          #+#    #+#             */
/*   Updated: 2025/10/22 19:52:49 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static char	*return_zero_string_in_less_than_25_lines(void)
{
	char	*ret;

	ret = (char *) malloc(1 * sizeof(char));
	if (ret == NULL)
		return (NULL);
	ret[0] = '\0';
	return (ret);
}

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	size_t	i;
	size_t	sub_len;
	size_t	s_len;
	char	*ret;

	if (!s)
		return (NULL);
	s_len = ft_strlen(s);
	if (start > s_len)
		return (return_zero_string_in_less_than_25_lines());
	sub_len = s_len - start;
	if (sub_len > len)
		sub_len = len;
	ret = (char *) malloc((sub_len + 1) * sizeof(char));
	if (ret == NULL)
		return (NULL);
	i = 0;
	while (i < sub_len && i < len)
	{
		ret[i] = s[start + i];
		i++;
	}
	ret[i] = '\0';
	return (ret);
}
// int main()
// {
// 	char test[] = "bonjour";
// 	printf("%s\n", ft_substr(test, 2, 4));
// }