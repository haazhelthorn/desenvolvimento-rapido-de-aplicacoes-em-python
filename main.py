from utilidade import *

def menu():

  criar_tabela('Hospitais', ['cnpj INT PRIMARY KEY NOT NULL', 'nome TEXT', 'rua TEXT', 'bairro TEXT', 'cidade TEXT', 'cep INT'])
  criar_tabela('Medicos', ['crm INTEGER PRIMARY KEY', 'cpf INTEGER', 'nome TEXT', 'rua TEXT', 'bairro TEXT', 'cidade TEXT', 'cep INTEGER'])
  criar_tabela('Enfermeiras', ['corem INTEGER PRIMARY KEY', 'cpf INTEGER', 'nome TEXT', 'rua TEXT', 'bairro TEXT', 'cidade TEXT', 'cep INTEGER'])
  criar_tabela('Pacientes', ['cpf INTEGER PRIMARY KEY', 'rg INTEGER', 'nome TEXT', 'rua TEXT', 'bairro TEXT', 'cidade TEXT', 'cep INTEGER'])
  criar_tabela('Especialidades', ['cod_esp INTEGER PRIMARY KEY', 'documento TEXT', 'especialidade TEXT'])
  criar_tabela('Telefones', ['cod_tel INTEGER PRIMARY KEY', 'documento TEXT', 'telefone INTEGER'])
  
  while True:
    menu_crud()
    try:
      opcao = int(input("Selecione a opção desejada: "))
    except ValueError:
      input("Por favor, digite um número válido.\nPressione Enter para continuar.")
    finally:
      match opcao:
        case 1:
            menu_cadastro()
            try:
              opcao_cadastro = int(input("Selecione a opção desejada: "))
            except ValueError:
              input("Por favor, digite um número válido.\nPressione Enter para continuar.")
            finally:
              match opcao_cadastro:
                case 1:
                  cadastrar_medico()
                case 2:
                  cadastrar_paciente()
                case 3:
                  cadastrar_hospital()
                case 4:
                  cadastrar_especialidade()
                case 5:
                  cadastrar_enfermeira()
                case 6:
                  cadastrar_telefones()
        case 2:
            while True:
              menu_relatorio()
              try:
                opcao_relatorio = int(input("Selecione a opção desejada: "))
              except ValueError:
                input("Por favor, digite um número válido.\nPressione Enter para continuar.")
              finally:
                match opcao_relatorio:
                  case 1:
                    listar_medicos_pacientes_hospitais()
                  case 2:
                    listar_pacientes_centro_aracaju()
                  case 3:
                    listar_medicos_telefones()
                  case 4:
                    listar_corpo_clinico_hospital()
                  case 0:
                    break
        case 3:
            while True:
              menu_atualizar()
              try:
                opcao_atualizar = int(input("Selecione a opção desejada: "))
              except ValueError:
                input("Por favor, digite um número válido.\nPressione Enter para continuar.")
              finally:
                match opcao_atualizar:
                  case 1:
                    atualizar_medico()
                  case 2:
                    atualizar_paciente()
                  case 3:
                    atualizar_hospital()
                  case 4:
                    atualizar_enfermeira()
                  case 5:
                    atualizar_telefone()
                  case 6:
                    atualizar_especialidade()
                  case 0:
                    break
        case 4:
            while True:
              menu_deletar()
              try:
                opcao_deletar = int(input("Selecione a opção desejada: "))
              except ValueError:
                input("Por favor, digite um número válido.\nPressione Enter para continuar.")
              finally:
                match opcao_deletar:
                  case 1:
                    deletar_medico()
                  case 2:
                    deletar_paciente()
                  case 3:
                    deletar_hospital()
                  case 4:
                    deletar_enfermeira()
                  case 5:
                    deletar_telefone()
                  case 6:
                    deletar_especialidade()
                  case 0:
                    break
        case 0:
            print("Saindo do programa.")
            break
 

menu()