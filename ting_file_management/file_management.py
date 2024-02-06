import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    list = []
    try:
        with open(path_file, 'r') as file:
            if not path_file.endswith('.txt'):
                sys.stderr.write('Formato inválido')
            for line in file:
                list.append(line.strip())
            return list
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')