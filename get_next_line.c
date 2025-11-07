/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 09:37:49 by eberling          #+#    #+#             */
/*   Updated: 2025/11/07 12:24:40 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"


static int	contains(char c, char *set)
{
	while (*set)
		if (c == *set++)
			return (1);
	return (0);
}

static char *save_buffer(char *result, char *buffer, size_t buffer_size)
{
    char *temp;
    size_t result_len;
    size_t  i;

    result_len = 0;
    if(result != NULL)
        while (result[result_len])
            result_len++;
    temp = malloc(result_len + buffer_size + 1);
    if (temp == NULL)
        return (NULL);
    i = -1;
    while (++i < result_len)
        temp[i] = result[i];
    i = -1;
    while (++i < buffer_size)
        temp[result_len + i] = buffer[i];    
    temp[i++] = '\0';
    free (result);
    return (temp);
}

char *get_next_line(int fd)
{
    size_t     buffer_size;
    int     read_ret;
    static char *stock;
    char    *buffer;
    char    *result;

    buffer_size = BUFFER_SIZE;
    result = NULL;
    buffer = malloc(buffer_size);
    while (buffer_size-- >= 0)
    {
        if (buffer_size == 0)
        {
            buffer_size = BUFFER_SIZE;
            result = save_buffer(result, buffer, buffer_size);
            if (contains('\n', result))
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
    fd = open("test.txt", O_RDONLY);
    
    if (fd == -1)
    {
        perror("Erreur lors de l'ouverture du fichier");
        return (1);
    }
    printf("\ngetnextlien result : \n\n%s\n\n", get_next_line(fd));
    if (close(fd) == -1)
    {
        perror("Erreur lors de la fermeture du fichier");
        return (1);
    }
    printf("Termine.\n");
    return (0);
}