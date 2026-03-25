def resumo_notas(notas):
    if not notas:  # evita lista vazia
        return "Lista de notas vazia"

    soma = sum(notas)
    media = soma / len(notas)
    maior = max(notas)
    menor = min(notas)

    return {
        "soma": soma,
        "media": media,
        "maior": maior,
        "menor": menor
    }


# Exemplo de uso:
notas_aluno = [7.5, 8.0, 6.5, 9.0, 5.5]
resultado = resumo_notas(notas_aluno)

print(resultado)