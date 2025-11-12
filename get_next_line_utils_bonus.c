/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils_bonus.c                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 09:38:31 by eberling          #+#    #+#             */
/*   Updated: 2025/11/12 16:06:02 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

int	contains(char c, char *set)
{
	if (set == NULL)
		return (0);
	while (*set)
		if (c == *set++)
			return (1);
	return (0);
}

int	ft_strlen(const char *s)
{
	int	i;

	i = 0;
	while (s[i] != '\0')
		i++;
	return (i);
}

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

char	*ft_strdup(const char *s)
{
	size_t	len;
	size_t	i;
	char	*ret;

	len = ft_strlen(s);
	ret = (char *)malloc((len + 1) * sizeof(char));
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
