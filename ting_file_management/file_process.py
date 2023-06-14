from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(result)
    print(result, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        file_deleted = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {file_deleted} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    if position > len(instance):
        print("Posição inválida", file=sys.stderr)
    else:
        file = instance.search(position)
        print(file, file=sys.stdout)
