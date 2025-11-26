/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/01 13:53:35 by eberling          #+#    #+#             */
/*   Updated: 2025/05/06 16:09:49 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strcpy(char *dest, char *src)
{
	int	i;

	i = 0;
	while (src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (dest);
}
/*
#include <stdio.h>
#include <string.h>

int main(void){

	char test_src[] = "Bonjour";
	char destination[] = "123456789";
	char *test_perso_function_return;
	test_perso_function_return = ft_strcpy(destination, test_src);

	char test_src_string[] = "Bonjour";
	char destination_string[] = "123456789";
	char *test_string_function_return;
	test_string_function_return = strcpy(destination_string, test_src_string);


	printf("----- Personal function tests -----\n");
	printf("%s\n", test_src);
	printf("%s\n", destination);
	printf("%c\n", *test_perso_function_return);
	
	printf("----- String function tests -----\n");
	printf("%s\n", test_src_string);
	printf("%s\n", destination_string);
	printf("%c\n", *test_string_function_return);
}
*/