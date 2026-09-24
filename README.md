# CutePy

CutePy is a small, custom programming language and compiler implemented in Python, built as part of a university course on Compilers.

The project implements the full pipeline of a traditional compiler, from raw source code down to executable RISC-V assembly:

1. **Lexical Analysis** — a hand-written lexer built around a finite-state automaton (FSA), driven by a transition table, which tokenizes CutePy source code and detects lexical errors (unsupported symbols, etc.).
2. **Syntax Analysis** — a recursive-descent parser that validates the program against CutePy's grammar, including expressions with correct operator precedence, conditionals, and loops.
3. **Intermediate Code Generation** — generates quads for each operation, using the classic **backpatching** technique to resolve forward jumps in `if`/`else`/`while` constructs.
4. **Symbol Table** — tracks variables, parameters, and functions across nested scopes, computing stack offsets used later during code generation.
5. **Final Code Generation** — translates the intermediate quads into **RISC-V assembly**.

## Language Features

CutePy supports:
- Function definitions (`def`) with parameters and return values
- Variable declarations (`#declare`)
- Arithmetic expressions (`+ - * //`) with correct operator precedence
- Conditionals (`if` / `else`, including `else if` chains)
- Loops (`while`)
- Boolean logic (`and`, `or`, `not`)
- Input/output (`input`, `print`)
- Comments (`#{ ... #}`)

## Usage

```bash
python cutePy.py your_program.cpy
```

This produces three output files:
- `your_program.sym` — symbol table dump
- `your_program.int` — intermediate code (quads)
- `your_program.asm` — final RISC-V assembly



## Example

add.cpy is a program written in cutePy.

## Background

This project was developed for a Compilers class, covering the theory and practice of how a programming language is translated into executable machine code.

## License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.