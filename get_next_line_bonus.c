/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 09:37:49 by eberling          #+#    #+#             */
/*   Updated: 2025/11/12 16:38:37 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

/*
 * Get the rest of a line after the first occurence of '\n'
 *	1. Take a backup of the line pointer
 *	2. Loop over it untill you reach newline or EOS
 *	3. Malloc for only what's after it
 *	4. Loop over it and copy from ptr to previously allocated string (3)
 *
 *	Input:
 *		char *line: a pointer to an array caracters that
 *		represent the line of the function
 *		int size: the number of elements in the array
 *
 *	Output:
 *		char* : The part of the inputed line.
 *		(only including what's after the first \n starting from left)
 *		(Returend string is allocated with malloc so has to be free())
 */
static char	*get_remainder(char *line)
{
	int		i;
	int		j;
	char	*rest;

	i = 0;
	j = 0;
	while (line[i] != '\n' && line[i] != '\0')
		i++;
	if (line[i] == '\0')
		return (NULL);
	if (line[i++] == '\0')
		return (NULL);
	rest = malloc(ft_strlen(line + i) + 1);
	if (rest == NULL)
		return (NULL);
	while (line[i])
		rest[j++] = line[i++];
	rest[j] = '\0';
	return (rest);
}

/*
 * Like get_remainder but get the first part before '\n' or '\0'
 *
 *Input:
 *	char *result : readed line from the read() function
 *
 *Output:
 *	char* : An allocated string with malloc that has to be free()
 *	containing the first part of (result)
 */
static char	*ft_cut_line(char *result)
{
	int		i;
	int		len;
	char	*line;

	i = 0;
	while (result[i] != '\n' && result[i] != '\0')
		i++;
	if (i == 0 && result[i] == '\0')
		return (NULL);
	len = i;
	if (result[i] == '\n')
		len++;
	if (len == 0)
		return (NULL);
	line = malloc(len + 1);
	if (!line)
		return (NULL);
	i = 0;
	while (i < len)
	{
		line[i] = result[i];
		i++;
	}
	line[i] = '\0';
	return (line);
}

/*
 * join the readed buffer to the result
 * 1. put result into another variable (tmp)
 * 2. write result using strjoin (first time : strdup)
 * 3. make sure to free malloc variables & return result
 * 
 * Input:
 *	char *result : 
 *	char *buffer : 
 *
 * Output:
 *	char* : the previous result + buffer
 */
static char	*join_and_free(char *result, char *buffer)
{
	char	*tmp;

	tmp = result;
	if (result == NULL)
		result = ft_strdup(buffer);
	else
		result = ft_strjoin(tmp, buffer);
	if (result == NULL)
	{
		free(tmp);
		return (NULL);
	}
	free(tmp);
	return (result);
}

/*
 * Reading the file and writing the buffer in the result
 *
 * Input:
 *	int fd : file descriptor
 *	char *result : static result variable from entrypoint
 *
 * Output:
 *	char* : all the buffer joined together to make one string
 *	representing the readed line.
 */
static char	*ft_read(int fd, char *result)
{
	char	*buffer;
	int		read_i;

	buffer = malloc(sizeof(char) * (BUFFER_SIZE + 1));
	if (buffer == NULL)
		return (free(result), NULL);
	read_i = 1;
	while (result == NULL || read_i > 0)
	{
		read_i = read(fd, buffer, BUFFER_SIZE);
		if (read_i == -1)
		{
			free(buffer);
			free(result);
			return (NULL);
		}
		if (read_i == 0)
			break ;
		buffer[read_i] = '\0';
		result = join_and_free(result, buffer);
		if (result == NULL || contains('\n', buffer))
			break ;
	}
	free(buffer);
	return (result);
}

char	*get_next_line(int fd)
{
	static char	*result[1024];
	char		*tmp;
	char		*line;

	if (fd < 0 || fd > 1024 || BUFFER_SIZE <= 0)
		return (NULL);
	result[fd] = ft_read(fd, result[fd]);
	if (result[fd] == NULL)
		return (NULL);
	tmp = result[fd];
	line = ft_cut_line(result[fd]);
	if (line == NULL)
	{
		free(tmp);
		result[fd] = NULL;
		return (NULL);
	}
	result[fd] = get_remainder(tmp);
	free(tmp);
	return (line);
}

int main(void)
{
    int fd1;
    int fd2;
    char *line1;
    char *line2;

    fd1 = open("test.txt", O_RDONLY);
    if (fd1 == -1)
    {
        perror("Erreur lors de l'ouverture de test1.txt");
        return (1);
    }

    fd2 = open("test2.txt", O_RDONLY);
    if (fd2 == -1)
    {
        perror("Erreur lors de l'ouverture de test2.txt");
        close(fd1);
        return (1);
    }

    printf("--- Début de la lecture simultanée ---\n\n");

    line1 = get_next_line(fd1);
    printf("FD1 (L1) : %s", line1 ? line1 : "(NULL - EOF ou Erreur)\n");
    free(line1); 

    line2 = get_next_line(fd2);
    printf("FD2 (L1) : %s", line2 ? line2 : "(NULL - EOF ou Erreur)\n");
    free(line2);

    line1 = get_next_line(fd1);
    printf("FD1 (L2) : %s", line1 ? line1 : "(NULL - EOF ou Erreur)\n");
    free(line1);

    line2 = get_next_line(fd2);
    printf("FD2 (L2) : %s", line2 ? line2 : "(NULL - EOF ou Erreur)\n");
    free(line2);

    if (close(fd1) == -1)
    {
        perror("Erreur lors de la fermeture de test1.txt");
        return (1);
    }
    if (close(fd2) == -1)
    {
        perror("Erreur lors de la fermeture de test2.txt");
        return (1);
    }
    printf("\n--- Terminé : Les descripteurs sont fermés. ---\n");
    return (0);
}