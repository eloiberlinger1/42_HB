/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/02 10:33:55 by eberling          #+#    #+#             */
/*   Updated: 2025/05/06 22:27:19 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] != '\0' || s2[i] != '\0')
	{
		if (s1[i] != s2[i])
		{
			return (((unsigned char)(s1[i])) - ((unsigned char)(s2[i])));
		}
		i++;
	}
	return (0);
}
/*
//https://www.programiz.com/c-programming/library-function/string.h/strcmp
#include <stdio.h>
#include <string.h>
int main(void){

    char str1[] = "abc", str2[] = "ab\200", str3[] = "abcd";
    int result;
  
    printf("-------- strcmp function results --------  \n");
    printf("\n");

    
    // comparing strings str1 and str2
    result = strcmp(str1, str2);
    printf("strcmp(str1, str2) = %d\n", result);
  
    // comparing strings str1 and str3
    result = strcmp(str1, str3);
    printf("strcmp(str1, str3) = %d\n", result);

    printf("\n");
    printf("\n");

    printf("-------- ft_strcmp function results --------  \n");

    printf("\n");

    
    // comparing strings str1 and str2
    result = ft_strcmp(str1, str2);
    printf("ft_strcmp(str1, str2) = %d\n", result);
  
    // comparing strings str1 and str3
    result = ft_strcmp(str1, str3);
    printf("ft_strcmp(str1, str3) = %d\n", result);

    
    return 0;
    
}
*/