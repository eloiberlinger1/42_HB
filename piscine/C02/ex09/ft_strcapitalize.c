/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/07 10:59:48 by eberling          #+#    #+#             */
/*   Updated: 2025/05/08 15:35:54 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	isalph(char c)
{
	if (c < 'A' || c > 'z')
		return (0);
	else if (c > 'Z' && c < 'a')
		return (0);
	return (1);
}

int	isnum(char c)
{
	if (c < '0' || c > '9')
		return (0);
	return (1);
}

char	*ft_strlowcase(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
			str[i] = str[i] + 32;
		i++;
	}
	return (str);
}

char	*ft_strcapitalize(char *str)
{
	int	i;

	str = ft_strlowcase(str);
	i = 0;
	while (str[i] != '\0')
	{
		if (i == 0 && (str[0] >= 'a' && str[0] <= 'z'))
			str[i] = str[i] - 32;
		else
			if ((!isnum(str[i])) && (!isalph(str[i])) && isalph(str[i + 1]))
				str[i + 1] = str[i + 1] - 32;
		i++;
	}
	return (str);
}


int main(){
    char test[] = "ssonjou j&aIme les 153, MaIs oa toi1!";
	//char test2[] = "bonjou j'aime les 153, nais oa toi1!";

	printf("%s\n", ft_strcapitalize(test));

	printf("\n");
	printf("\n");
	printf("\n");
	//printf("%s\n", ft_strcapitalize(test2));
	printf("\n");
}
