/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 09:37:49 by eberling          #+#    #+#             */
/*   Updated: 2025/11/12 10:24:55 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

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
	i++;
	rest = malloc(ft_strlen(line + i) + 1);
	while (line[i])
		rest[j++] = line[i++];
	rest[j] = '\0';
	return (rest);
}

/*
 *This function is like get_remainder but get the first part before '\n' or '\0'
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
		free(buffer);
		free(tmp);
		return (NULL);
	}
	return (result);
}

static char	*ft_read(int fd, char *result)
{
	char	*buffer;
	int		read_i;

	buffer = malloc(sizeof(char) * (BFR_SIZE + 1));
	if (buffer == NULL)
		return (NULL);
	read_i = 1;
	while ((result == NULL || !contains('\n', result)) && read_i > 0)
	{
		read_i = read(fd, buffer, BFR_SIZE);
		if (read_i == -1)
		{
			free(buffer);
			free(result);
			return (NULL);
		}
		buffer[read_i] = '\0';
		result = join_and_free(result, buffer);
		if (result != NULL)
			free(result);
	}
	free(buffer);
	return (result);
}

char	*get_next_line(int fd)
{
	static char	*result;
	char		*tmp;
	char		*line;

	if (fd < 0 || BFR_SIZE <= 0)
		return (NULL);
	result = ft_read(fd, result);
	if (result == NULL)
		return (NULL);
	tmp = result;
	line = ft_cut_line(result);
	if (line == NULL)
	{
		free(tmp);
		result = NULL;
		return (NULL);
	}
	result = get_remainder(tmp);
	free(tmp);
	return (line);
}

// int	main(void)
// {
// 	int fd;
// 	fd = open("test.txt", O_RDONLY);

// 	if (fd == -1)
// 	{
// 		perror("Erreur lors de l'ouverture du fichier");
// 		return (1);
// 	}
// 	printf("\ngetnextlien result1 : \n\n%s\n\n", get_next_line(fd));
// 	printf("\ngetnextlien result2 : \n\n%s\n\n", get_next_line(fd));
// 	if (close(fd) == -1)
// 	{
// 		perror("Erreur lors de la fermeture du fichier");
// 		return (1);
// 	}
// 	printf("Termine.\n");
// 	return (0);
// }
