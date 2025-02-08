from flask import Flask, Response
import time

app = Flask(__name__)

# Colores ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Letras en ASCII con colores
letters = {
    'A': [
        f"{RED}   A   {RESET}",
        f"{RED}  A A  {RESET}",
        f"{RED} A   A {RESET}",
        f"{RED} AAAAA {RESET}",
        f"{RED} A   A {RESET}",
        f"{RED} A   A {RESET}"
    ],
    'L': [
        f"{GREEN} L     {RESET}",
        f"{GREEN} L     {RESET}",
        f"{GREEN} L     {RESET}",
        f"{GREEN} L     {RESET}",
        f"{GREEN} L     {RESET}",
        f"{GREEN} LLLLL {RESET}"
    ],
    'C': [
        f"{YELLOW}  CCC  {RESET}",
        f"{YELLOW} C     {RESET}",
        f"{YELLOW} C     {RESET}",
        f"{YELLOW} C     {RESET}",
        f"{YELLOW} C     {RESET}",
        f"{YELLOW}  CCC  {RESET}"
    ],
    'H': [
        f"{BLUE} H   H {RESET}",
        f"{BLUE} H   H {RESET}",
        f"{BLUE} HHHHH {RESET}",
        f"{BLUE} H   H {RESET}",
        f"{BLUE} H   H {RESET}",
        f"{BLUE} H   H {RESET}"
    ],
    'S': [
        f"{MAGENTA}  SSS  {RESET}",
        f"{MAGENTA} S     {RESET}",
        f"{MAGENTA}  SSS  {RESET}",
        f"{MAGENTA}     S {RESET}",
        f"{MAGENTA} S     {RESET}",
        f"{MAGENTA}  SSS  {RESET}"
    ]
}

word = "ALCHACAS"


@app.route('/')
def stream():
    def generate():
        while True:
            for i in range(1, len(word) + 1):
                lines = [""] * 6  # Seis líneas para las letras
                for letter in word[:i]:  # Agregar una letra más en cada iteración
                    for j, line in enumerate(letters[letter]):
                        lines[j] += line + "  "  # Espaciado entre letras

                yield "\033c" + "\n".join(lines) + "\n"  # Limpiar y mostrar
                time.sleep(0.1)  # Velocidad de animación

    return Response(generate(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
