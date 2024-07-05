# Rodrigo Valiante Tavares - TADS - 1º Semestre - EAD 

import json

def escrever_arquivos_estudantes(lista, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista, arquivo)

def ler_lista_do_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return []
    
def verificar_codigo_repetido(matriculas, codigo):
    for matricula in matriculas:
        if matricula["Codigo da Turma"] == codigo:
            return True
    return False

def menu_principal():
    print(""" 
    --- SEJA BEM VINDO AO PROJETO SISTEMA PUC ---
    --------------- MENU PRINCIPAL --------------
          
    (1) Gerenciar Estudantes
    (2) Gerenciar Professores
    (3) Gerenciar Disciplinas
    (4) Gerenciar Turmas
    (5) Gerenciar Matriculas
    (0) Sair
    """)

def menu_operacoes():
    print("""
    (1) Incluir
    (2) Listar
    (3) Atualizar
    (4) Excluir
    (0) Voltar ao menu anterior
            """)
def incluir(tipo_de_dado, nome_arquivo):
    if tipo_de_dado =="professores":
        professores = ler_lista_do_json(nome_arquivo)
        print("\n ===== INCLUSÃO =====")
        codigo_professor = int(input("Digite o Código do Professor: "))
        nome = input("Digite o Nome do Professor: ")
        cpf = input("Digite o CPF do Professor: ")
        print("Inclusão realizada.")
        professor = {"Codigo do Professor": codigo_professor, "Nome do Professor": nome, "CPF do Professor": cpf}
        professores.append(professor)
        escrever_arquivos_estudantes(professores, nome_arquivo)
    elif tipo_de_dado == "estudantes":
        estudantes = ler_lista_do_json(nome_arquivo)
        print("\n ===== INCLUSÃO =====")
        codigo_estudante = int(input("Digite o Código do Estudante: "))
        nome = input("Digite o Nome do Estudante: ")
        cpf = input("Digite o CPF do Estudante: ")
        print("Inclusão realizada.")
        estudante = {"Codigo do estudante": codigo_estudante, "Nome": nome, "CPF": cpf}
        estudantes.append(estudante)
        escrever_arquivos_estudantes(estudantes, nome_arquivo)
    elif tipo_de_dado =="disciplinas":
        disciplinas = ler_lista_do_json(nome_arquivo)
        print("\n ===== INCLUSÃO =====")
        codigo_disciplina = int(input("Digite o Código da Disciplina: "))
        nome = input("Digite o Nome da Disciplina: ")
        print("Inclusão realizada.")
        disciplina = {"Codigo da Disciplina": codigo_disciplina, "Nome da Disciplina": nome}
        disciplinas.append(disciplina)
        escrever_arquivos_estudantes(disciplinas, nome_arquivo)
    elif tipo_de_dado =="turmas":
        turmas = ler_lista_do_json(nome_arquivo)
        print("\n ===== INCLUSÃO =====")
        while True:
            codigo_turma = int(input("Digite o Código da Turma: "))
            if verificar_codigo_repetido(turmas, codigo_turma):
                print("Este código já foi registrado. Por favor, insira outro código.")
            else:
                break
        codigo_professor = int(input("Digite o Código do Professor: "))
        codigo_disciplina = int(input("Digite o Código da Disciplina: "))
        print("Inclusão realizada.")
        turma = {"Codigo da Turma": codigo_turma, "Codigo do Professor": codigo_professor, "Codigo da Disciplina": codigo_disciplina}
        turmas.append(turma)
        escrever_arquivos_estudantes(turmas, nome_arquivo)
    elif tipo_de_dado =="matriculas":
        matriculas = ler_lista_do_json(nome_arquivo)
        print("\n ===== INCLUSÃO =====")

        while True:
            codigo_turma = int(input("Digite o Código da Turma: "))
            if verificar_codigo_repetido(matriculas, codigo_turma):
                print("Este código já foi registrado. Por favor, insira outro código.")
            else:
                break

        codigo_estudante = int(input("Digite o Código do Estudante: "))
        print("Inclusão realizada.")
        matricula = {"Codigo da Turma": codigo_turma, "Codigo do Estudante": codigo_estudante}
        matriculas.append(matricula)
        escrever_arquivos_estudantes(matriculas, nome_arquivo)

def listar(nome_arquivo):
    itens = ler_lista_do_json(nome_arquivo)
    print("\n ===== LISTAGEM =====")
    for item in itens:
        print(item)

def atualizar(tipo_de_dado, nome_arquivo):
    if tipo_de_dado == "estudantes":
        estudantes = ler_lista_do_json(nome_arquivo)
        print("\n ===== ATUALIZAÇÃO =====")
        codigo_para_atualizar = int(input("Digite o Código do Estudante que deseja atualizar: "))
        atualizar_estudante = None
        for lista_estudantes in estudantes:
            if codigo_para_atualizar == lista_estudantes["Codigo do estudante"]:
                atualizar_estudante = lista_estudantes
                break
        if atualizar_estudante != None:
            atualizar_estudante["Codigo do estudante"] = int(input("Digite o novo Código do Estudante: "))
            atualizar_estudante["Nome"] = input("Digite o nome: ")
            atualizar_estudante["CPF"] = input("Digite o CPF: ")
            print("Estudante atualizado com sucesso.")
        else:
            print("Estudante não encontrado.")
        escrever_arquivos_estudantes(estudantes, nome_arquivo)
    elif tipo_de_dado == "professores":
        professores = ler_lista_do_json(nome_arquivo)
        print("\n ===== ATUALIZAÇÃO =====")
        codigo_para_atualizar = int(input("Digite o Código do Professor que deseja atualizar: "))
        atualizar_professor = None
        for lista_professores in professores:
            if codigo_para_atualizar == lista_professores["Codigo do Professor"]:
                atualizar_professor= lista_professores
                break
        if atualizar_professor != None:
            atualizar_professor["Codigo do Professor"] = int(input("Digite o novo Código do Professor: "))
            atualizar_professor["Nome do Professor"] = input("Digite o Nome do Professor: ")
            atualizar_professor["CPF do Professor"] = input("Digite o CPF do Professor: ")
            print("Professor atualizado com sucesso.")
        else:
            print("Professor não encontrado.")
        escrever_arquivos_estudantes(professores, nome_arquivo)
    elif tipo_de_dado == "disciplinas":
        disciplinas = ler_lista_do_json(nome_arquivo)
        print("\n ===== ATUALIZAÇÃO =====")
        codigo_para_atualizar = int(input("Digite o Código da disciplina que deseja atualizar: "))
        atualizar_disciplina = None
        for lista_disciplinas in disciplinas:
            if codigo_para_atualizar == lista_disciplinas["Codigo da Disciplina"]:
                atualizar_disciplina= lista_disciplinas
                break
        if atualizar_disciplina != None:
            atualizar_disciplina["Codigo da Disciplina"] = int(input("Digite o novo Código da disciplina: "))
            atualizar_disciplina["Nome da Disciplina"] = input("Digite o Nome da Disciplina: ")
            print("Disciplina atualizada com sucesso.")
        else:
            print("Disciplina não encontrada.")
        escrever_arquivos_estudantes(disciplinas, nome_arquivo)
    elif tipo_de_dado == "turmas":
        turmas = ler_lista_do_json(nome_arquivo)
        print("\n ===== ATUALIZAÇÃO =====")
        codigo_para_atualizar = int(input("Digite o Código da Turma que deseja atualizar: "))
        atualizar_turma= None
        for lista_turmas in turmas:
            if codigo_para_atualizar == lista_turmas["Codigo da Turma"]:
                atualizar_turma= lista_turmas
                break
        if atualizar_turma != None:
            atualizar_turma["Codigo da Turma"] = int(input("Digite o novo Código da Turma: "))
            atualizar_turma["Codigo do Professor"] = int(input("Digite o código do Professor: "))
            atualizar_turma["Codigo da Disciplina"] = int(input("Digite o código da Disciplina: "))
            print("Turma atualizada com sucesso.")
        else:
            print("Turma não encontrada.")
        escrever_arquivos_estudantes(turmas, nome_arquivo)
    elif tipo_de_dado == "matriculas":
        matriculas = ler_lista_do_json(nome_arquivo)
        print("\n ===== ATUALIZAÇÃO =====")
        codigo_para_atualizar = int(input("Digite o Código da Turma que deseja atualizar: "))
        atualizar_matricula= None
        for lista_matriculas in matriculas:
            if codigo_para_atualizar == lista_matriculas["Codigo da Turma"]:
                atualizar_matricula= lista_matriculas
                break
        if atualizar_matricula != None:
            atualizar_matricula["Codigo da Turma"] = int(input("Digite o novo Código da Turma: "))
            atualizar_matricula["Codigo do Estudante"] = int(input("Digite o código do Estudante: "))
            print("Matricula atualizada com sucesso.")
        else:
            print("Matricula não encontrada.")
        escrever_arquivos_estudantes(matriculas, nome_arquivo)
    
def excluir(tipo_de_dado, nome_arquivo):
    if tipo_de_dado == "estudantes":
        estudantes = ler_lista_do_json(nome_arquivo)
        print("\n ===== EXCLUSÃO =====")
        codigo_para_excluir = int(input("Digite o Código do Estudante que deseja excluir: "))
        remover_estudante = None
        for lista_estudantes in estudantes:
            if codigo_para_excluir == lista_estudantes["Codigo do estudante"]:
                remover_estudante = lista_estudantes
                break
        if remover_estudante != None:
            estudantes.remove(remover_estudante)
            print("Estudante removido com sucesso.")
        else:
            print("Estudante não encontrado.")    
        escrever_arquivos_estudantes(estudantes, nome_arquivo)
    elif tipo_de_dado == "professores":
        professores = ler_lista_do_json(nome_arquivo)
        print("\n ===== EXCLUSÃO =====")
        codigo_para_excluir = int(input("Digite o Código do Professor que deseja excluir: "))
        remover_professor = None
        for lista_professores in professores:
            if codigo_para_excluir == lista_professores["Codigo do Professor"]:
                remover_professor = lista_professores
                break
        if remover_professor != None:
            professores.remove(remover_professor)
            print("Professor removido com sucesso.")
        else:
            print("Professor não encontrado.")    
        escrever_arquivos_estudantes(professores, nome_arquivo)
    elif tipo_de_dado == "disciplinas":
        disciplinas = ler_lista_do_json(nome_arquivo)
        print("\n ===== EXCLUSÃO =====")
        codigo_para_excluir = int(input("Digite o Código da Disciplina que deseja excluir: "))
        remover_disciplina = None
        for lista_disciplinas in disciplinas:
            if codigo_para_excluir == lista_disciplinas["Codigo da Disciplina"]:
                remover_disciplina = lista_disciplinas
                break
        if remover_disciplina != None:
            disciplinas.remove(remover_disciplina)
            print("Disciplina removida com sucesso.")
        else:
            print("Disciplina não encontrada.")    
        escrever_arquivos_estudantes(disciplinas, nome_arquivo)
    elif tipo_de_dado == "turmas":
        turmas = ler_lista_do_json(nome_arquivo)
        print("\n ===== EXCLUSÃO =====")
        codigo_para_excluir = int(input("Digite o Código da Turma que deseja excluir: "))
        remover_turma = None
        for lista_turmas in turmas:
            if codigo_para_excluir == lista_turmas["Codigo da Turma"]:
                remover_turma = lista_turmas
                break
        if remover_turma != None:
            turmas.remove(remover_turma)
            print("Turma removida com sucesso.")
        else:
            print("Turma não encontrada.")    
        escrever_arquivos_estudantes(turmas, nome_arquivo)
    elif tipo_de_dado == "matriculas":
        matriculas = ler_lista_do_json(nome_arquivo)
        print("\n ===== EXCLUSÃO =====")
        codigo_para_excluir = int(input("Digite o Código da Turma que deseja excluir: "))
        remover_matricula = None
        for lista_matriculas in matriculas:
            if codigo_para_excluir == lista_matriculas["Codigo da Turma"]:
                remover_matricula = lista_matriculas
                break
        if remover_matricula != None:
            matriculas.remove(remover_matricula)
            print("Matricula removida com sucesso.")
        else:
            print("Matricula não encontrada.")    
        escrever_arquivos_estudantes(matriculas, nome_arquivo)

arquivo_estudantes = 'estudantes.json'
arquivo_professores = 'professores.json'
arquivo_disciplinas = 'disciplinas.json'
arquivo_turmas = 'turmas.json'
arquivo_matriculas = 'matriculas.json'
tipo_de_dado = ""
        
while True: 
    menu_principal()

    opcao = input("Informe a opção desejada e pressione ENTER para avançar: ") 
    if opcao == "2": 
        tipo_de_dado = "professores"
        while True:
            print("\n***** [PROFESSORES] MENU DE OPERAÇÕES *****  ")
            menu_operacoes()
            opcao = input("Informe a opção desejada e pressione ENTER para avançar: ")
            if opcao == "0":
                break 
            elif opcao == "1":
                incluir(tipo_de_dado, arquivo_professores)
            elif opcao == "2":
                listar(arquivo_professores)
            elif opcao == "3":
                atualizar(tipo_de_dado, arquivo_professores)
            elif opcao == "4":
                excluir(tipo_de_dado, arquivo_professores)
            else:
                print("\n Você digitou um valor inválido.")
    elif opcao =="3":
        tipo_de_dado = "disciplinas"
        while True:
            print("\n***** [DISCIPLINAS] MENU DE OPERAÇÕES *****  ")
            menu_operacoes()
            opcao = input("Informe a opção desejada e pressione ENTER para avançar: ")
            if opcao == "0":
                break 
            elif opcao == "1":
                incluir(tipo_de_dado, arquivo_disciplinas)
            elif opcao == "2":
                listar(arquivo_disciplinas)
            elif opcao == "3":
                atualizar(tipo_de_dado, arquivo_disciplinas)
            elif opcao == "4":
                excluir(tipo_de_dado, arquivo_disciplinas)
            else:
                print("\n Você digitou um valor inválido.")
    elif opcao =="4":
        tipo_de_dado = "turmas"
        while True:
            print("\n***** [TURMAS] MENU DE OPERAÇÕES *****  ")
            menu_operacoes()
            opcao = input("Informe a opção desejada e pressione ENTER para avançar: ")
            if opcao == "0":
                break 
            elif opcao == "1":
                incluir(tipo_de_dado, arquivo_turmas)
            elif opcao == "2":
                listar(arquivo_turmas)
            elif opcao == "3":
                atualizar(tipo_de_dado, arquivo_turmas)
            elif opcao == "4":
                excluir(tipo_de_dado, arquivo_turmas)
            else:
                print("\n Você digitou um valor inválido.")
    elif opcao =="5":
        tipo_de_dado = "matriculas"
        while True:
            print("\n***** [MATRICULAS] MENU DE OPERAÇÕES *****  ")
            menu_operacoes()
            opcao = input("Informe a opção desejada e pressione ENTER para avançar: ")
            if opcao == "0":
                break 
            elif opcao == "1":
                incluir(tipo_de_dado, arquivo_matriculas)
            elif opcao == "2":
                listar(arquivo_matriculas)
            elif opcao == "3":
                atualizar(tipo_de_dado, arquivo_matriculas)
            elif opcao == "4":
                excluir(tipo_de_dado, arquivo_matriculas)
            else:
                print("\n Você digitou um valor inválido.")
    elif opcao == "0": 
        print("\n Você está saindo do programa.")
        break 
    elif opcao != "1": 
        print("\n Você digitou um valor inválido.")

    elif opcao == "1": 
        tipo_de_dado = "estudantes"
        while True:
            print("\n***** [ESTUDANTES] MENU DE OPERAÇÕES *****  ")
            menu_operacoes()
            opcao = input("Informe a opção desejada e pressione ENTER para avançar: ")
            if opcao == "0":
                break 
            elif opcao == "1":
                incluir(tipo_de_dado, arquivo_estudantes)
            elif opcao == "2":
                listar(arquivo_estudantes)
            elif opcao == "3":
                atualizar(tipo_de_dado, arquivo_estudantes)
            elif opcao == "4":
                excluir(tipo_de_dado, arquivo_estudantes)
            else:
                print("\n Você digitou um valor inválido.")
            