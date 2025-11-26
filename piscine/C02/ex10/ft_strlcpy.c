/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/01 20:20:51 by eberling          #+#    #+#             */
/*   Updated: 2025/05/06 17:32:45 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

unsigned int	ft_strlen(char *str)
{
	int				i;
	unsigned int	counter;

	counter = 0;
	i = 0;
	while (str[i] != '\0')
	{
		counter++;
		i++;
	}
	return (counter);
}

unsigned int	ft_strlcpy(char *dest, char *src, unsigned int size)
{
	unsigned int	src_size;
	unsigned int	i;

	src_size = ft_strlen(src);
	i = 0;
	if (size == 0)
		return (src_size);
	while (i < size - 1 && src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	while (i < ft_strlen(dest))
	{
		dest[i] = '\0';
		i++;
	}
	return (src_size);
}
/*
#include <stdio.h>
#include <string.h>

int main(void)
{
    char dest[] = "1234576891011";
    char src[] = "abc";
    unsigned int r;

    char dest2[] = "1234576891011";
    char src2[] = "abc";
    unsigned int r2;

    r = ft_strlcpy(dest,src,7);
	r2 = strlcpy(dest2,src2,7);

    printf("Copied '%s' into '%s', length %d\n\n\n",
            src,
            dest,
            r
          );

	printf("Copied '%s' into '%s', length %d\n",
			src2,
			dest2,
			r2
		);
}*/