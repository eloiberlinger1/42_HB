/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/04 22:35:25 by eberling          #+#    #+#             */
/*   Updated: 2025/05/09 01:05:37 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

unsigned int	ft_strlen(char *str)
{
	unsigned int	i;
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

unsigned int	ft_strlcat(char *dest, char *src, unsigned int size)
{
	unsigned int	i;
	unsigned int	dest_len;
	unsigned int	src_len;

	src_len = ft_strlen(src);
	dest_len = ft_strlen(dest);
	if (size <= dest_len)
		return (src_len + size);
	i = 0;
	while (src[i] && i + dest_len < (size - 1))
	{
		dest[dest_len + i] = src[i];
		i++;
	}
	dest[i + dest_len] = '\0';
	return (dest_len + src_len);
}
/* 
#include <stdio.h>
#include <string.h>
int	main(void){
	char myStr[14] = "12345678";
	char myStr2[14] = "12345678";
	char world[] = "abcde";
	char world2[] = "abcde";

	unsigned int test1 = strlcat(myStr, world, 14);
	printf("----------- Results using strlcat -----------\n");
	printf("return = %d\n", test1);
	printf("result = %s\n\n", myStr);
	
	unsigned int test2 = ft_strlcat(myStr2, world2, 14);
	printf("----------- Results using ft_strlcat -----------\n");
	printf("return = %d\n", test2);
	printf("result = %s\n\n", myStr2);

	return 0;
}
 */