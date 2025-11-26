/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_uppercase.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/01 19:29:00 by eberling          #+#    #+#             */
/*   Updated: 2025/05/01 19:31:04 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_uppercase(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] < 'A' || str[i] > 'Z')
		{
			return (0);
		}
		i++;
	}
	return (1);
}

/*
#include <stdio.h>

int main(void){

	char teststr[] = "ACAB";
	int isalpha;

	isalpha = 0;
	
	isalpha = ft_str_is_uppercase(teststr);

	printf("\n%d", isalpha);
}
*/