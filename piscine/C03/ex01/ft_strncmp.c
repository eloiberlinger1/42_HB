/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/03 10:47:56 by eberling          #+#    #+#             */
/*   Updated: 2025/05/08 20:35:48 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strncmp(char *s1, char *s2, unsigned int n)
{
	unsigned int	i;

	i = 0;
	while (i < n && (*s1 != '\0' || *s2 != '\0'))
	{
		if (s1[i] != s2[i])
			return (((unsigned char)(s1[i])) - ((unsigned char)(s2[i])));
		i++;
	}
	return (0);
}
/* 
#include <stdio.h>
#include <string.h>

int	main(void){
	char myStr1[] = "";
	char myStr2[] = "";
	int cmp = strncmp(myStr1, myStr2, 3);
	printf("----------- Results using strncmp -----------\n");
	printf("cmp = %d\n\n", cmp);

	int cmp1 = ft_strncmp(myStr1, myStr2, 3);

	printf("----------- Results using ft_strncmp -----------\n");
	printf("cmp = %d\n\n", cmp1);
}
*/
