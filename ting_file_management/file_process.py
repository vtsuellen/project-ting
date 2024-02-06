from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            print(f'Arquivo {path_file} já importado')
            return
    file = txt_importer(path_file)
    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file),
        'linhas_do_arquivo': file
    }
    instance.enqueue(data)
    print(data)

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
