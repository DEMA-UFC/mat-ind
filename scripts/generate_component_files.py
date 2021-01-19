import json


def main():
    with open("./_data/componentes-curriculares.json", "r") as file:
        componentes = json.load(file)
    for componente in componentes:
        codigo = componente['codigo']
        print('Gerando Componente', componente['codigo'], ' - ', componente['nome'])
        text = f"---\ncodigo: {codigo}\nlayout: componente\n---\n"
        local = f"./curso/componentes/{codigo.lower()}.html"
        with open(local, "w") as file:
            file.write(text)


if __name__ == "__main__":
    main()
