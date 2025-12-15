# push_swap

This project has been created as part of the 42 curriculum by eberling.

## Description

**push_swap** is a sorting algorithm project that sorts a stack of integers using a limited set of operations. The goal is to sort numbers in stack A using only the following operations:

- **Swap** (`sa`, `sb`, `ss`): Swap the first two elements at the top of a stack
- **Push** (`pa`, `pb`): Take the first element from one stack and put it at the top of another
- **Rotate** (`ra`, `rb`, `rr`): Shift all elements up by one (first element becomes last)
- **Reverse Rotate** (`rra`, `rrb`, `rrr`): Shift all elements down by one (last element becomes first)

The challenge is to find the most efficient sequence of operations to sort the stack with the minimum number of moves.

The project implements a hybrid sorting approach:
- **Small stacks (≤5 elements)**: Uses optimized hardcoded algorithms for maximum efficiency
- **Large stacks (>5 elements)**: Implements a Radix Sort algorithm based on binary representation

## Instructions

### Compilation

To compile the project, run:

```bash
make
```


### Others Make Targets

- `make` or `make all`: Compiles the project
- `make clean`: Removes object files
- `make fclean`: Removes object files and the executable
- `make re`: Recompiles everything from scratch


This will:
1. Compile the `ft_printf` library and its dependencies (`libft`)
2. Compile all source files
3. Link everything together to create the `push_swap` executable


### Execution

The program accepts integers as command-line arguments. You can provide them in two ways:

**Option 1: Separate arguments**
```bash
./push_swap 3 1 4 2 5
```

**Option 2: Single string argument (space-separated)**
```bash
./push_swap "3 1 4 2 5"
```

The program will output a sequence of operations to sort the stack:
```
pb
ra
pb
sa
ra
pa
pa
```

### Testing

You can test the program with the provided checker:

#### Get random integers list
https://www.random.org/integer-sets/?sets=1&num=500&min=-500&max=9000&seqnos=on&sort=on&order=index&format=html&rnd=new

Pipe the output to the checker:
```bash
ARG="3 1 4 2 5"; ./push_swap $ARG | ./checker_linux $ARG
```

## Resources

### Documentation
- [Linked Lists in C](https://www.geeksforgeeks.org/linked-list-set-1-introduction/)
- [Radix Sort Algorithm](https://en.wikipedia.org/wiki/Radix_sort)

### AI Usage

AI was used in the following parts of the project:

1. **Finding approach / Debugging**:
   - Analysis of input parsing logic to identify pointer manipulation bugs
   - The core algorithms (Radix sort, small stack sorting) were developed independently. AI assistance was primarily used to figure out the best approach to start the subject and find out wich problems i will have to go though.

2. **Documentation**:
   - Redaction of README file

## Project Structure

```
push_swap/
├── push_swap.c          # Main program entry point
├── push_swap.h          # Header file with function declarations
├── Makefile             # Build configuration
├── utils/
│   ├── parse_input.c    # Input parsing and validation
│   ├── check_sort.c    # Check if stack is sorted
│   ├── sorting_small.c  # Algorithms for small stacks
│   ├── sorting_main.c   # Radix sort for large stacks
│   ├── op_swap.c        # Swap operations
│   ├── op_push.c        # Push operations
│   ├── op_rotate.c      # Rotate operations
│   ├── op_rev_rotate.c  # Reverse rotate operations
│   ├── ft_lstutils.c    # Linked list utilities
│   └── utils.c          # Helper functions
└── ft_printf/           # Custom version of printf
    ├── libft/           # Custom version of libft
    └── ...
```
