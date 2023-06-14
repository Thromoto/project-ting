def exists_word(word, instance):
    result = []
    for index in range(len(instance)):
        path = instance.search(index)
        file = {
            "palavra": word,
            "arquivo": path["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for p in path["linhas_do_arquivo"]:
            if word.lower() in p.lower():
                file["ocorrencias"].append(
                    {"linha": path["linhas_do_arquivo"].index(p) + 1}
                )
        if file["ocorrencias"]:
            result.append(file)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
