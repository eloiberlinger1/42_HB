/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_toupper.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/12 11:54:27 by eberling          #+#    #+#             */
/*   Updated: 2025/10/12 12:03:26 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_toupper(int c)
{
	if (c >= 'a' && c <= 'z')
		return ('A' + c - 'a');
	return (c);
}

// #include <stdio.h>

// int main(){
//     char test = 'z';

// 	printf("%c\n", ft_toupper(test));
// }
