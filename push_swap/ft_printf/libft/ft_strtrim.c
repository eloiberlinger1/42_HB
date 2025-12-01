/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 10:08:22 by eberling          #+#    #+#             */
/*   Updated: 2025/10/22 19:52:41 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>

static int	contains(char c, char *set)
{
	while (*set)
		if (c == *set++)
			return (1);
	return (0);
}

static size_t	get_trim_len(
	char const *s1, char const *set, size_t *start_ret, size_t *end_ret)
{
	size_t	trim_len;
	size_t	start;
	size_t	end;

	trim_len = 0;
	start = 0;
	end = ft_strlen(s1);
	while (s1[start] != '\0' && contains(s1[start], (char *)set))
		start++;
	if (end > start)
		while (contains(s1[end - 1], (char *)set))
			end--;
	if (end <= start)
		trim_len = 0;
	else
		trim_len = end - start;
	*start_ret = start;
	*end_ret = end;
	return (trim_len);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t		start;
	size_t		end;
	size_t		trim_len;
	size_t		n;
	char		*ret;

	if (!s1 || !set)
		return (NULL);
	trim_len = get_trim_len(s1, set, &start, &end);
	ret = (char *)malloc(trim_len + 1);
	if (ret == NULL)
		return (NULL);
	n = 0;
	while (n < trim_len)
	{
		ret[n] = s1[start + n];
		n++;
	}
	ret[n] = '\0';
	return (ret);
}

// int main()
// {
// 	char test1[] = "***Hello Wo*rld ***";
// 	char set[] = "*";

// 	printf("%s\n", ft_strtrim(test1, set));
// }