from colorama import init, Fore
from os import path, linesep
import mmap
yellow = Fore.YELLOW

blue = Fore.BLUE

green = Fore.GREEN


def count_lines(filename) -> int:
    with open(filename, "r+") as myfile:
      mm = mmap.mmap(myfile.fileno(), 0)
      total_lines = 0

    while mm.readline():
        total_lines += 1

    return total_lines

def main() -> None:
    print(yellow + '\t\t Welcome to this App with Docker \n\n')
    print(blue + '\t\t Please introduce you Text')

    filename = 'file.txt'

    if path.exists('file.txt'):
        print(green + '\t\t File already exists \n\n')
        f = open(filename,'a')
    else:
        print(green + '\t\t Creating File \n\n' + yellow)
        f = open(filename,'w')
    message = ''
    while len(message) == 0:
       message = input('\t Introduce your text \n\n\t' + yellow)

    f.write(message + linesep)

    f.close()

    print(count_lines(filename))

    



if __name__ == '__main__':
    init()
    main()