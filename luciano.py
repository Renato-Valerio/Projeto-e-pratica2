import json
import os

USUARIOS_FILE = 'usuarios.json'

def carregar_usuarios():
    if not os.path.exists(USUARIOS_FILE):
        with open(USUARIOS_FILE, 'w') as f:
            json.dump([], f)
    with open(USUARIOS_FILE, 'r') as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(USUARIOS_FILE, 'w') as f:
        json.dump(usuarios, f, indent=4)

def inserir_usuario():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    usuarios = carregar_usuarios()
    usuarios.append({"cpf": cpf, "nome": nome})
    salvar_usuarios(usuarios)
    print("Usuário cadastrado!")

def listar_usuarios():
    usuarios = carregar_usuarios()
    for u in usuarios:
        print(f"CPF: {u['cpf']}, Nome: {u['nome']}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Inserir Usuário")
        print("2. Listar Usuários")
        print("3. Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            inserir_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    menu()
