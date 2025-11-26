/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/03 21:43:56 by eberling          #+#    #+#             */
/*   Updated: 2025/05/06 22:28:05 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*#include <string.h>
#include <unistd.h>
#include <stdio.h>*/
char	*ft_strstr(char *str, char *to_find)
{
	char	*str_save;
	char	*find_save;

	if (*to_find == 0)
		return (str);
	while (*str)
	{
		str_save = str;
		find_save = to_find;
		while (*(str++) == *(to_find++))
		{
			if (*to_find == 0)
				return (str_save);
		}
		str = str_save;
		to_find = find_save;
		str++;
	}
	return (0);
}

/*
//https://www.geeksforgeeks.org/strstr-in-ccpp/
int main(void){
	char test[] = "abcdefghij";
	char ft_test[] = "abcdefghij";
	char testin[] = "def";

	char *result = strstr(test, testin);
	char *ft_result = ft_strstr(ft_test, testin);

	printf("--------------------- Testing strstr ---------------------\n");
	printf("\n");
	printf("   result = %s\n", result);
	printf("--------------------- Testing ft_strstr ---------------------\n");
	printf("\n");
	printf("ft_result = %s\n", ft_result);


	return 0;
}
*/
/*
#include <stdio.h>
#include <string.h>
int main () {
	char str_1[100] = "aaabbbbbaaaaaaaabbaaabbaaaaaaaaaabbaaabbaabaaaaaa";
	char *str_2;
	str_2 = strstr(str_1, "aaaaaaaaaaaa");
	printf("\nSubstring is: %s", str_2);
	str_2 = ft_strstr(str_1, "aaaaaaaaaaaa");
	printf("\nSubstring is: %s", str_2);
	return 0;
}
*/