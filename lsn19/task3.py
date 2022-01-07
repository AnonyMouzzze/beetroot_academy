from sys import argv
import os


def args_checker():
    if os.path.exists(argv[-1]):
        FILE_DIRECTORY = argv[-1]
    else:
        raise FileExistsError

    chars = f'chars: {count_chars(FILE_DIRECTORY)}'
    lines = f'lines: {count_lines(FILE_DIRECTORY)}'

    if '-c' in argv and '-l' in argv:
        return f"{chars}\n{lines}"
    elif '-c' in argv:
        return chars
    elif '-l' in argv:
        return lines
    else:
        raise 'Arguments Error'


def count_chars(file_name):
    count = 0
    with open(f'{file_name}', 'r') as fp:
        for line in fp.readlines():
            count += len(line.strip())
        return count


def count_lines(file_name):
    with open(f'{file_name}', 'r') as fp:
        return len(fp.readlines())


print(args_checker())
