from lab_python_oop.figure import Figure
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import colorama


def main():
    r = Rectangle("синего", n, n)
    c = Circle("зеленого", n)
    s = Square("красного", n)
    print(colorama.Fore.RED + str(r), colorama.Style.RESET_ALL)
    print(colorama.Back.GREEN + str(c), colorama.Style.RESET_ALL)
    print(colorama.Style.BRIGHT + str(s), colorama.Style.RESET_ALL)

if __name__ == "__main__":
    n = int(input("Введи номер варианта: "))
    main()