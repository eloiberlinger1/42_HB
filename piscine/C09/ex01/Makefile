.SHELLFLAGS = -x

LIBNAME = libft.a
CC = cc
C_FLAGS = -Wall -Wextra -Werror -c

SRC_DIR = srcs
INC_DIR = includes

H_FILES = $(INC_DIR)/ft.h

C_FILES = $(SRC_DIR)/ft_putchar.c \
			$(SRC_DIR)/ft_putstr.c \
			$(SRC_DIR)/ft_strcmp.c \
			$(SRC_DIR)/ft_strlen.c \
			$(SRC_DIR)/ft_swap.c

O_FILES = $(C_FILES:.c=.o)

all: $(LIBNAME)

.c.o: 
	$(CC) $(C_FLAGS) $< -o $@ -I $(H_FILES)

$(LIBNAME) : $(O_FILES)
	ar rc $(LIBNAME) $(O_FILES)
	ranlib $(LIBNAME)

clean:
	rm -f $(O_FILES)

fclean: clean
	rm -f $(LIBNAME)

re: fclean all

.PHONY: all clean fclean re