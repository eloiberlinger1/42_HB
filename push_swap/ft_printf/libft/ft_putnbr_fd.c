/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 11:20:25 by eberling          #+#    #+#             */
/*   Updated: 2025/10/22 21:17:27 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	int		i;
	long	nb;
	char	buffer[11];

	nb = n;
	if (nb == 0)
	{
		ft_putchar_fd('0', fd);
		return ;
	}
	i = 0;
	if (nb < 0)
	{
		ft_putchar_fd('-', fd);
		nb *= -1;
	}
	while (nb > 0)
	{
		buffer[i++] = '0' + nb % 10;
		nb /= 10;
	}
	while (i-- > 0)
		ft_putchar_fd(buffer[i], fd);
}
// #include <fcntl.h>  
// #include <stdio.h>
// int main(void)
// {
//     int fd;
//     fd = open("test.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
//     if (fd == -1)
//     {
//         perror("Erreur lors de l'ouverture du fichier");
//         return (1);
//     }
//     printf("Debut de l'ecriture dans test.txt (FD: %d)...\n", fd);
//     ft_putnbr_fd(-55469810, fd);
//     if (close(fd) == -1)
//     {
//         perror("Erreur lors de la fermeture du fichier");
//         return (1);
//     }
//     printf("Termine. Veuillez verifier le contenu de 'test.txt'.\n");
//     return (0);
// }