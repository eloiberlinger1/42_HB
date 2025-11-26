/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/03 16:17:26 by eberling          #+#    #+#             */
/*   Updated: 2025/05/14 13:59:55 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strncat(char *dest, char *src, unsigned int nb)
{
	char	*dest_save;

	dest_save = dest;
	while (*dest != 0)
	{
		dest++;
	}
	while (*src && nb > 0)
	{
		*dest = *src;
		dest++;
		src++;
		nb--;
	}
	*dest = 0;
	return (dest_save);
}
/* 
#include <stdio.h>
#include <string.h>

int	main(void){
	char myStr[8] = "Hello";
	char myStr2[8] = "Hello";


	char *test1 = strncat(myStr, "World", 2);
	char *test2 = ft_strncat(myStr2, "World", 2);

	printf("----------- Results using strncat -----------\n");
	printf("result = %s\n\n", test1);

	printf("----------- Results using ft_strncat -----------\n");
	printf("result = %s\n\n", test2);



	return 0;
}
 */