import sys

if len(sys.argv) != 2:
    print("Usage: python3 file_to_brainfuck.py <fichier>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "rb") as f:
        data = f.read()
except FileNotFoundError:
    print("Erreur : fichier introuvable.")
    sys.exit(1)

brainfuck_code = ""
current_value = 0

for byte in data:
    difference = byte - current_value

    if difference > 0:
        brainfuck_code += "+" * difference
    elif difference < 0:
        brainfuck_code += "-" * abs(difference)

    brainfuck_code += "."
    current_value = byte

print(brainfuck_code)