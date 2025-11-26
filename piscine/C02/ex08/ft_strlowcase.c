/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlowcase.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/01 20:08:09 by eberling          #+#    #+#             */
/*   Updated: 2025/05/05 22:36:27 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strlowcase(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
		{
			str[i] = str[i] + 32;
		}
		i++;
	}
	return (str);
}

/*
#include <stdio.h>

int main(){
    char test[] = "aBonjOur";
	char test2[] = "ACAB;)";

	ft_strlowcase(test);

	printf("%s\n", ft_strlowcase(test));
	printf("%s\n", ft_strlowcase(test2));

}
    */