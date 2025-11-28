#include <stdlib.h>
#include <stdio.h>

int main()
{
    char    line[] = "asdasdasdas\n645asd";
    char    *lineptr;
	char	*tmp;
	int 	i;

	i = 0;
	while (line[i] && line[i] != '\n')
		i++;
	if (line[i] == '\n')
		i++;
	tmp = (char *)malloc((i + 1) * sizeof(char));
	if (!tmp)
		return (0);
    lineptr = line;
    i = 0;
	while (*lineptr && *lineptr != '\n')
		tmp[i++] = *lineptr++;
	if (*lineptr == '\n')
		tmp[i++] = *lineptr++;
	tmp[i] = '\0';

    printf("%s", tmp);
	return (0);
}