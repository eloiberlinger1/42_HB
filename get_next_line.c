/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 09:37:49 by eberling          #+#    #+#             */
/*   Updated: 2025/11/07 10:42:47 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char *save_buffer(char *result, char *buffer, size_t buffer_size)
{
    char *temp;
    size_t result_len;

    temp = result;
    while (result++)
        result_len++;
    result = temp;
    temp = malloc(result_len + buffer_size);
    while (result++)
        *temp++ = result;
    while (buffer++)
        *temp++ = buffer;
        
    free (result);
    return (temp);

}

char *get_next_line(int fd)
{
    size_t     buffer_size;
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
            result = save_buffer(result, buffer, buffer_size);
            if (contains(buffer, '\n'))
                break ;
        }
        read_ret = read(fd, buffer, buffer_size);
    }
    free(buffer);
    return (result);
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