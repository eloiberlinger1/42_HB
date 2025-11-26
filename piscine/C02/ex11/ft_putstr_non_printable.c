/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_non_printable.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/03 21:57:39 by eberling          #+#    #+#             */
/*   Updated: 2025/05/06 16:05:03 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	dec2hex(unsigned char num)
{
	ft_putchar('\\');
	ft_putchar("0123456789abcdef"[num / 16]);
	ft_putchar("0123456789abcdef"[num % 16]);
}

void	ft_putstr_non_printable(char *str)
{
	int		i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] < 32 || str[i] == 127)
		{
			dec2hex(str[i]);
		}
		else
			write(1, &str[i], 1);
		i++;
	}
}
/*
#include <stdio.h>
int main(void){
	char teststring[] = "Hello How are you?";
	teststring[5] = -10;
	
	ft_putstr_non_printable(teststring);
	
	
	int i=0;
	char testchar=-127;
	while(i != 20000){

		teststring[5] = testchar;
		
		printf("\n------------ testing n=%d -----------\n", i);
		printf("caractere numero = %d\n", testchar);
		printf("caractere affiche = %c\n", testchar);
		printf("\nfunction running output : \n");
		
		ft_putstr_non_printable(teststring);
		testchar++;
		i++;
	}
}
*/