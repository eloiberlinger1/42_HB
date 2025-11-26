/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/14 16:12:27 by eberling          #+#    #+#             */
/*   Updated: 2025/05/16 10:47:12 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

char	*ft_strcat(char *dest, char *src)
{
	char	*dest_save;

	dest_save = dest;
	while (*dest != 0)
		dest++;
	while (*src != 0)
	{
		*dest = *src;
		src++;
		dest++;
	}
	*dest = 0;
	return (dest_save);
}

int	ft_strlen(char *str)
{
	int	i;
	int	counter;

	counter = 0;
	i = 0;
	while (str[i] != '\0')
	{
		counter++;
		i++;
	}
	return (counter);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	char	*result;
	int		i;
	int		result_size;

	i = 0;
	result_size = 0;
	while (i < size)
		result_size += ft_strlen(strs[i++]);
	if (size > 0)
		result_size += (ft_strlen(sep) * (size - 1));
	result = (char *) malloc(result_size + 1);
	result[0] = '\0';
	if (size <= 0)
		return (result);
	if (result == NULL)
		return (NULL);
	i = 0;
	while (i < size)
	{
		ft_strcat(result, strs[i]);
		if (i++ != size - 1)
			ft_strcat(result, sep);
	}
	result[result_size] = '\0';
	return (result);
}
/* 
#include <stdio.h>
#include <string.h>
int main(void)
{
	char *strs[] = { "Hello", "world", "asdf"};
	char sep[] = "-";

	printf("%s \n", ft_strjoin(3, strs, sep));
} 
 */