/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/18 16:36:35 by eberling          #+#    #+#             */
/*   Updated: 2025/05/20 20:46:29 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	char_is_spacer(char c, char *base)
{
	while (*base)
	{
		if (*base == c && c != '\0')
			return (1);
		base++;
	}
	return (0);
}

int	ft_wrdlen(int i, char *str, char *charset)
{
	int	counter;

	counter = 0;
	while (str[i] != '\0' && !char_is_spacer(str[i], charset))
	{
		counter++;
		i++;
	}
	return (counter);
}

int	get_words_nbr(char *str, char *spacers)
{
	int	i;
	int	count;
	int	in_word;

	in_word = 0;
	count = 0;
	i = 0;
	while (str[i])
	{
		if (char_is_spacer(str[i], spacers))
		{
			if (in_word == 1)
				in_word = 0;
		}
		else
		{
			if (in_word == 0)
			{
				in_word = 1;
				count++;
			}
		}
		i++;
	}
	return (count);
}

char	**ft_split(char *str, char *charset)
{
	char	**arr;
	int		i;
	int		j;
	int		k;

	arr = malloc(sizeof(char *) * (get_words_nbr(str, charset) + 1));
	i = 0;
	j = 0;
	while (i < (get_words_nbr(str, charset)))
	{
		k = 0;
		while (char_is_spacer(str[j], charset))
			j++;
		arr[i] = malloc(sizeof(char) * (ft_wrdlen(j, str, charset) + 1));
		while (!char_is_spacer(str[j], charset) && str[j] != '\0')
			arr[i][k++] = str[j++];
		arr[i][k] = '\0';
		i++;
	}
	arr[i] = NULL;
	return (arr);
}

/* #include <string.h>
#include <stdio.h>
int main(void)
{
	char teststr[] = "sdsaasd";
	char separators[] = " ";
	char **split_result;
	int i = 0;
	
	split_result = ft_split(teststr, separators);

	while (i < 1)
	{
		printf("%s \n", split_result[i++]);
	}

	return (0);

} */