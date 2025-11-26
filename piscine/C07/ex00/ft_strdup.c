/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/15 08:56:02 by eberling          #+#    #+#             */
/*   Updated: 2025/05/15 08:56:30 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

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

char	*ft_strdup(char *src)
{
	int		size;
	int		i;
	char	*ptr;

	size = ft_strlen(src);
	ptr = (char *) malloc(size * sizeof(char) + 1);
	if (ptr == NULL)
		return (NULL);
	i = 0;
	while (src[i] != '\0')
	{
		ptr[i] = src[i];
		i++;
	}
	ptr[i] = '\0';
	return (ptr);
}
/* 
#include <stdio.h>
int main(void)
{
	char tst[] = "test\0test";
	char *test = ft_strdup(tst);
	printf("%s \n", test);
} */