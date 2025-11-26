/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/01 14:08:40 by eberling          #+#    #+#             */
/*   Updated: 2025/05/06 16:09:43 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strncpy(char *dest, char *src, unsigned int n)
{
	unsigned int	i;

	i = 0;
	while (i < n && src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	while (i < n)
	{
		dest[i] = '\0';
		i++;
	}
	return (dest);
}
/*
#include <stdio.h>
#include <string.h>

int main(void){

	char test_src[] = "ABCa";
	char destination[20] = "12";
	char *test_perso_function_return;
	test_perso_function_return = ft_strncpy(destination, test_src, 3);

	char test_src_string[] = "ABCa";
	char destination_string[20] = "12";
	char *test_string_function_return;
	test_string_function_return = 
	strncpy(destination_string, test_src_string, 3);


	printf("----- Personal function tests -----\n");
	printf("%s\n", destination);
	printf("%c\n", *test_perso_function_return);
	
	printf("----- String function tests -----\n");
	printf("%s\n", destination_string);
	printf("%c\n", *test_string_function_return);
}
*/