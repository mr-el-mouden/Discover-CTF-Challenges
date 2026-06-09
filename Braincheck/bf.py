import sys

def run_bf(code):
    tape = [0] * 30000
    ptr = 0
    i = 0
    out = []

    stack = []
    jump = {}

    for pos, c in enumerate(code):
        if c == "[":
            stack.append(pos)
        elif c == "]":
            start = stack.pop()
            jump[start] = pos
            jump[pos] = start

    while i < len(code):
        c = code[i]

        if c == ">":
            ptr += 1
        elif c == "<":
            ptr -= 1
        elif c == "+":
            tape[ptr] = (tape[ptr] + 1) % 256
        elif c == "-":
            tape[ptr] = (tape[ptr] - 1) % 256
        elif c == ".":
            out.append(chr(tape[ptr]))
        elif c == ",":
            tape[ptr] = ord(sys.stdin.read(1) or "\0")
        elif c == "[":
            if tape[ptr] == 0:
                i = jump[i]
        elif c == "]":
            if tape[ptr] != 0:
                i = jump[i]

        i += 1

    return "".join(out)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    code = f.read()

print(run_bf(code), end="")
