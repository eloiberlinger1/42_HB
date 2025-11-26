## libft (42 Heilbronn)

### Overview
`libft` is your first C library at 42. You will re-implement a curated subset of standard C utility functions and bundle them into a static library named `libft.a`. The goal is to deepen your understanding of C fundamentals, memory management, strings, and basic data structures, while learning to build, test, and ship reusable code.

### Learning Objectives
- Re-implement core string, memory, and character functions
- Practice precise memory management and pointer arithmetic
- Design a clean public API via a single header (`libft.h`)
- Learn to compile and archive a static library (`ar`, `ranlib`, `Makefile`)
- Follow the 42 coding style and project constraints

### What You Will Build
- A static library: `libft.a`
- A public header: `libft.h`
- A `Makefile` to build the library and its optional bonus

The library provides common helper functions you can reuse in later 42 projects.

### Typical Function Groups
The exact list is defined by the subject. A typical `libft` includes:

- Character classification and conversion:
  - `ft_isalpha`, `ft_isdigit`, `ft_isalnum`, `ft_isascii`, `ft_isprint`, `ft_toupper`, `ft_tolower`
- Memory handling:
  - `ft_memset`, `ft_bzero`, `ft_memcpy`, `ft_memmove`, `ft_memchr`, `ft_memcmp`, `ft_calloc`
- String handling:
  - `ft_strlen`, `ft_strlcpy`, `ft_strlcat`, `ft_strchr`, `ft_strrchr`, `ft_strncmp`, `ft_strnstr`, `ft_strdup`
  - `ft_substr`, `ft_strjoin`, `ft_strtrim`, `ft_split`, `ft_itoa`, `ft_strmapi`, `ft_striteri`
- File descriptor I/O helpers:
  - `ft_putchar_fd`, `ft_putstr_fd`, `ft_putendl_fd`, `ft_putnbr_fd`
- Bonus (linked list API):
  - `t_list`, `ft_lstnew`, `ft_lstadd_front`, `ft_lstsize`, `ft_lstlast`, `ft_lstadd_back`, `ft_lstdelone`, `ft_lstclear`, `ft_lstiter`, `ft_lstmap`

Always check your project PDF for the authoritative list and exact prototypes.

### Constraints and Rules
- Respect the 42 coding style (subject and style checker rules apply)
- Do not use external libraries; only what the subject explicitly allows
- Handle edge cases carefully (null pointers, empty strings, overlapping memory, etc.)
- No memory leaks: every allocation you make must be properly managed

### Project Structure (example)
Your repository may look like this (the exact layout can vary):

```
libft/
├─ include/
│  └─ libft.h
├─ src/
│  ├─ string/
│  ├─ memory/
│  ├─ char/
│  ├─ io/
│  └─ list/        # bonus
├─ Makefile
└─ libft.a         # built artifact
```

### Building
Use the provided `Makefile` targets (names may vary by template):

```
make         # builds libft.a
make bonus   # builds bonus objects into libft.a (if applicable)
make clean   # removes object files
make fclean  # removes objects and libft.a
make re      # fclean + make
```

### Using the Library in Your Projects
1) Add the header include path and link with the static library:

```
cc your_code.c -I include -L . -lft -o your_program
```

2) In your code, include the library header:

```c
#include "libft.h"
```

> Note: The `-L` path should point to the directory containing `libft.a`, and `-I` should point to the directory where `libft.h` resides.

### Testing
- Create small test programs for each function
- Validate behavior against the C standard (where applicable) and your subject specs
- Check edge cases: empty strings, `NULL` pointers (when permitted), boundary sizes, overlapping memory regions, etc.
- Use sanitizers and valgrind (when available) to catch memory issues

### Common Pitfalls
- Off-by-one errors in `strlcpy`/`strlcat`
- Overlap handling in `memmove` vs `memcpy`
- Returning correct types and values on errors
- Ensuring NUL-termination in string functions when required
- Avoiding undefined behavior with invalid pointers

### Evaluation Tips
- Ensure your `Makefile` works on a clean clone without manual steps
- Provide a clean and minimal public API in `libft.h`
- Keep implementations consistent, readable, and thoroughly tested
- Bonus functions should be separated and built only with `make bonus`

### License
This project is part of the 42 curriculum and intended for educational use.

### Acknowledgements
Thanks to the 42 community and peers for discussions, testing ideas, and helpful reviews.


