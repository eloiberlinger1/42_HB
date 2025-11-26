/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcat.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/03 16:17:26 by eberling          #+#    #+#             */
/*   Updated: 2025/05/09 01:18:33 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strcat(char *dest, char *src)
{
	char	*dest_save;

	dest_save = dest;
	while (*dest != 0)
	{
		dest++;
	}
	while (*src != 0)
	{
		*dest = *src;
		src++;
		dest++;
	}
	*dest = 0;
	return (dest_save);
}
/* 
#include <stdio.h>
#include <string.h>

int	main(void){
	char myStr1[80] = "pouic";
	char myStr2[] = "pouic";
	char myStr11[80] = "pouic";
	char myStr22[] = "pouic";
	char *cmp;
	char *cmp1;
    
    cmp = strcat(myStr1, myStr2);

	printf("----------- Results using strcat -----------\n");
	printf("cmp = %s\n\n", cmp);

	cmp1 = ft_strcat(myStr11, myStr22);

	printf("----------- Results using ft_strcat -----------\n");
	printf("cmp = %s\n\n", cmp1);
}
 */