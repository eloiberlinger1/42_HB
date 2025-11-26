/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 14:08:33 by eberling          #+#    #+#             */
/*   Updated: 2025/10/23 15:05:48 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	word_count(char const *s, char sep)
{
	int	count;

	if (!s)
		return (0);
	count = 0;
	while (*s)
	{
		while (*s == sep)
			s++;
		if (*s)
			count++;
		while (*s && *s != sep)
			s++;
	}
	return (count);
}

static int	get_wordsize(const char *s, char c, int i)
{
	int	wordsize;

	wordsize = 0;
	while (s[i + wordsize] != c && s[i + wordsize] != '\0')
		wordsize++;
	return (wordsize);
}

static void	free_words(char **ret, int w)
{
	int	i;

	i = 0;
	while (i < w)
	{
		free(ret[i++]);
	}
	free(ret);
}

static int	write_words(const char *s, int words, char c, char **ret)
{
	int			wordsize;
	int			i;
	int			j;
	int			w;

	i = 0;
	w = 0;
	while (w < words)
	{
		while (s[i] == c)
			i++;
		j = 0;
		wordsize = get_wordsize(s, c, i);
		ret[w] = (char *) malloc((wordsize + 1) * sizeof(char));
		if (!ret[w])
		{
			free_words(ret, w);
			return (0);
		}
		while (j < wordsize)
			ret[w][j++] = s[i++];
		ret[w][j] = '\0';
		w++;
	}
	return (1);
}

char	**ft_split(char const *s, char c)
{
	int			words;
	char		**ret;

	if (!s)
		return (NULL);
	words = word_count(s, c);
	ret = (char **) malloc((words + 1) * sizeof(char *));
	if (!ret)
		return (NULL);
	if (!write_words(s, words, c, ret))
		return (NULL);
	ret[words] = NULL;
	return (ret);
}
// #include <stdio.h>
// int main()
// {
// 	int i = 0;
// 	char test[] = "hello!";
// 	char **recup = ft_split(test, 32);
// 	int it = word_count(test, ' ');
// 	while(i<it)
// 	{
// 		printf("%s\n", recup[i]);
// 		i++;
// 	}
// }