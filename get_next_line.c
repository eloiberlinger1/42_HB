/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 09:37:49 by eberling          #+#    #+#             */
/*   Updated: 2025/11/07 10:14:17 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

int save_buffer(char *result, char *buffer)
{
    char *temp;

    // prendre la longueuur de result
    // prendre la longueur du buffer

    // additionner les deux

    // 

}

char *get_next_line(int fd)
{
    int     buffer_size;
    int     read_ret;
    char    *buffer;
    char    *result;

    buffer_size = 5;
    buffer = malloc(buffer_size);
    while (buffer_size-- >= 0)
    {
        if (buffer_size == 0)
        {
            buffer_size = 5;
            
        }
        read_ret = read(fd, buffer, buffer_size);
    }

    
}

int main(void)
{
    int fd;
    fd = open("test.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    
    if (fd == -1)
    {
        perror("Erreur lors de l'ouverture du fichier");
        return (1);
    }

    if (close(fd) == -1)
    {
        perror("Erreur lors de la fermeture du fichier");
        return (1);
    }
    printf("Termine.\n");
    return (0);
}