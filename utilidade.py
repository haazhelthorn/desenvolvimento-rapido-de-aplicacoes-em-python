import sqlite3

def criar_tabela(nome_tabela, colunas):
  conn = sqlite3.connect('meudb.db')
  cursor = conn.cursor()

  colunas_str = ', '.join(colunas)
  cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({colunas_str})")

  conn.commit()
  conn.close()


def cadastrar_medico():
  conn = sqlite3.connect('meudb.db')
  cursor = conn.cursor()
  print("--- Cadastrar médico ---")
  
  crm = input("CRM: ")
  cpf = input("CPF: ")
  nome = input("Nome: ")
  rua = input("Rua: ")
  bairro = input("Bairro: ")
  cidade = input("Cidade: ")
  cep = input("CEP: ")

  cursor.execute("INSERT INTO Medicos (crm, cpf, nome, rua, bairro, cidade, cep) VALUES (?, ?, ?, ?, ?, ?, ?)",
                 (crm, cpf, nome, rua, bairro, cidade, cep))
   
  conn.commit()  
  print("Médico cadastrado com sucesso!")
  conn.close()


def cadastrar_paciente():
  conn = sqlite3.connect('meudb.db')
  cursor = conn.cursor()
  print("--- Cadastrar paciente ---")

  cpf = input("CPF: ")
  rg = input("RG: ")
  nome = input("Nome: ")
  rua = input("Rua: ")
  bairro = input("Bairro: ")
  cidade = input("Cidade: ")
  cep = input("CEP: ")
  
  cursor.execute("INSERT INTO Pacientes (cpf, rg, nome, rua, bairro, cidade, cep) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                 (cpf, rg, nome, rua, bairro, cidade, cep))
  
  conn.commit()
  print("Paciente cadastrado com sucesso!")
  conn.close()


def cadastrar_hospital():
  conn = sqlite3.connect('meudb.db')
  cursor = conn.cursor()
  print("--- Cadastrar Hospital ---")
    
  cnpj = input("CNPJ: ")
  nome = input("Nome: ")
  rua = input("Rua: ")
  bairro = input("Bairro: ")
  cidade = input("Cidade: ")
  cep = input("CEP: ")
   
  cursor.execute("INSERT INTO Hospitais (cnpj, nome, rua, bairro, cidade, cep) VALUES (?, ?, ?, ?, ?, ?)",
                 (cnpj, nome, rua, bairro, cidade, cep))
  
  conn.commit()
  print("Hospital cadastrado com sucesso!")
  conn.close()


def cadastrar_especialidade():
  conn = sqlite3.connect("meudb.db")
  cursor = conn.cursor()
  print("--- Cadastrar especialidade ---")

  cod = input("código: ")
  documento = input("documento: ")
  especialidade = input("especialidade: ")

  cursor.execute("INSERT INTO Especialidades (cod, documento, especialidade) VALUES (?, ?, ?)",
                 (cod, documento, especialidade))

  conn.commit()
  print("Especialidade cadastrada com sucesso!")
  conn.close()


def cadastrar_enfermeira():
  conn = sqlite3.connect('meudb.db')
  cursor = conn.cursor()
  print("--- Cadastrar Enfermeira ---")
    
  corem = input("COREM: ")
  cpf = input("CPF: ")
  nome = input("Nome: ")
  rua = input("Rua: ")
  bairro = input("Bairro: ")
  cidade = input("Cidade: ")
  cep = input("CEP: ")

  cursor.execute("INSERT INTO Enfermeiras (corem, cpf, nome, rua, bairro, cidade, cep) VALUES (?, ?, ?, ?, ?, ?, ?)",
                 (corem, cpf, nome, rua, bairro, cidade, cep))
  
  conn.commit()
  print("Enfermeira cadastrado com sucesso!")
  conn.close()


def cadastrar_telefones():
  conn = sqlite3.connect("meudb.db")
  cursor = conn.cursor()
  print("--- Cadastrar telefone ---")

  cod = input("código: ")
  documento = input("documento: ")
  telefone = input("telefone: ")

  cursor.execute("INSERT INTO Telefones (cod, documento, telefone) VALUES (?, ?, ?)",
                 (cod, documento, telefone))

  conn.commit()
  print("Telefone cadastrado com sucesso!")
  conn.close()



def listar_medicos_pacientes_hospitais():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Medicos")
    medicos = cursor.fetchall()
    print("Médicos:")
    for medico in medicos:
        print(medico)
    print("\n")

    cursor.execute("SELECT * FROM Pacientes")
    pacientes = cursor.fetchall()
    print("Pacientes:")
    for paciente in pacientes:
      print(paciente)
    print("\n")

    cursor.execute("SELECT * FROM Hospitais")
    hospitais = cursor.fetchall()
    print("Hospitais:")
    for hospital in hospitais:
      print(hospital)
    print("\n")
    
    conn.close()


def listar_pacientes_centro_aracaju():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Pacientes WHERE cidade = 'Aracaju' AND bairro = 'Centro'")
    pacientes = cursor.fetchall()
    
    for paciente in pacientes:
        print(paciente)
    
    conn.close()


def listar_medicos_telefones():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT Medicos.nome, Telefones.telefone FROM Medicos INNER JOIN Telefones ON Medicos.crm = Telefones.documento")
    medicos_telefones = cursor.fetchall()
    
    for medico_telefone in medicos_telefones:
        print(medico_telefone)
    
    conn.close()


def listar_corpo_clinico_hospital():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT Hospitais.nome, Medicos.nome FROM Medicos INNER JOIN Hospitais ON Medicos.cpf = Hospitais.cnpj")
    corpo_clinico = cursor.fetchall()
    
    for item in corpo_clinico:
        print(item)
    
    conn.close()


def atualizar_medico():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    crm = input("Digite o CRM do médico que deseja atualizar: ")
    
    cursor.execute("SELECT * FROM Medicos WHERE crm = ?", (crm,))
    medico = cursor.fetchone()
    
    if medico is None:
        print("Médico não encontrado.")
        conn.close()
        return
    
    cpf = input("Digite o nome cpf do médico: ")
    nome = input("Digite o novo nome do médico: ")
    rua = input("Digite a nova rua do médico: ")
    bairro = input("Digite o novo bairro do médico: ")
    cidade = input("Digite a nova cidade do médico: ")
    cep = input("Digite o novo CEP do médico: ")
    
    cursor.execute("UPDATE Medicos SET cpf = ?, nome = ?, rua = ?, bairro = ?, cidade = ?, cep = ? WHERE crm = ?",
                   (cpf, nome, rua, bairro, cidade, cep, crm))
    
    conn.commit()
    conn.close()
    print("Dados do médico atualizados com sucesso.")
  

def atualizar_paciente():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    cpf = input("Digite o CPF do paciente que deseja atualizar: ")
    
    cursor.execute("SELECT * FROM Pacientes WHERE cpf = ?", (cpf,))
    paciente = cursor.fetchone()
    
    if paciente is None:
        print("Paciente não encontrado.")
        conn.close()
        return
    
    rg = input("Digite o novo rg do paciente: ")
    nome = input("Digite o novo nome do paciente: ")
    rua = input("Digite a nova rua do paciente: ")
    bairro = input("Digite o novo bairro do paciente: ")
    cidade = input("Digite a nova cidade do paciente: ")
    cep = input("Digite o novo CEP do paciente: ")
    
    cursor.execute("UPDATE Pacientes SET rg = ?, nome = ?, rua = ?, bairro = ?, cidade = ?, cep = ? WHERE cpf = ?",
                   (rg, nome, rua, bairro, cidade, cep, cpf))
    
    conn.commit()
    conn.close()
    print("Dados do paciente atualizados com sucesso.")

def atualizar_hospital():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    cnpj = input("Digite o CNPJ do hospital que deseja atualizar: ")
    
    cursor.execute("SELECT * FROM Hospitais WHERE cnpj = ?", (cnpj,))
    hospital = cursor.fetchone()
    
    if hospital is None:
        print("Hospital não encontrado.")
        conn.close()
        return
    
    nome = input("Digite o novo nome do hospital: ")
    rua = input("Digite a nova rua do hospital: ")
    bairro = input("Digite o novo bairro do hospital: ")
    cidade = input("Digite a nova cidade do hospital: ")
    cep = input("Digite o novo CEP do hospital: ")
    
    cursor.execute("UPDATE Hospitais SET nome = ?, rua = ?, bairro = ?, cidade = ?, cep = ? WHERE cnpj = ?",
                   (nome, rua, bairro, cidade, cep, cnpj))
    
    conn.commit()
    conn.close()
    print("Dados do hospital atualizados com sucesso.")

def atualizar_enfermeira():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    corem = input("Digite o COREM da enfermeira que deseja atualizar: ")
    
    cursor.execute("SELECT * FROM Enfermeiras WHERE corem = ?", (corem,))
    enfermeira = cursor.fetchone()
    
    if enfermeira is None:
        print("Enfermeira não encontrado.")
        conn.close()
        return
    
    cpf = input("Digite o novo cpf da enfermeira: ")
    nome = input("Digite o novo nome da enfermeira: ")
    rua = input("Digite a nova rua da enfermeira: ")
    bairro = input("Digite o novo bairro da enfermeira: ")
    cidade = input("Digite a nova cidade da enfermeira: ")
    cep = input("Digite o novo CEP da enfermeira: ")
    
    cursor.execute("UPDATE Enfermeiras SET cpf = ?, nome = ?, rua = ?, bairro = ?, cidade = ?, cep = ? WHERE corem = ?",
                   (cpf, nome, rua, bairro, cidade, cep, corem))
    
    conn.commit()
    conn.close()
    print("Dados da enfermeira atualizados com sucesso.")

def atualizar_especialidade():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    cod_esp = input("Digite o código da especialidade que deseja atualizar: ")
    
    cursor.execute("SELECT * FROM Especialidades WHERE cod_esp = ?", (cod_esp,))
    especialidade = cursor.fetchone()
    
    if especialidade is None:
        print("Especialidade não encontrado.")
        conn.close()
        return
    
    documento = input("Digite o novo documento da especialidade: ")
    especialidade = input("Digite a nova especialidade: ")
    
    cursor.execute("UPDATE Especialidades SET documento = ?, especialidade = ? WHERE cod_esp = ?",
                   (documento, especialidade, cod_esp))
    
    conn.commit()
    conn.close()
    print("Dados da especialidade atualizados com sucesso.")

def atualizar_telefone():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    cod_tel = input("Digite o código do telefone que deseja atualizar: ")
    
    cursor.execute("SELECT * FROM Telefones WHERE cod_tel = ?", (cod_tel,))
    telefone = cursor.fetchone()
    
    if telefone is None:
        print("Telefone não encontrado.")
        conn.close()
        return
    
    documento = input("Digite o novo documento do telefone: ")
    telefone = input("Digite o novo telefone: ")
    
    cursor.execute("UPDATE Telefones SET documento = ?, telefone = ? WHERE cod_tel = ?",
                   (documento, telefone, cod_tel))
    
    conn.commit()
    conn.close()
    print("Dados do telefone atualizados com sucesso.")

def deletar_medico():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    
    crm = input("Digite o CRM do médico que deseja excluir: ")
    
    cursor.execute("SELECT * FROM Medicos WHERE crm = ?", (crm,))
    medico = cursor.fetchone()
    
    if medico is None:
        print("Médico não encontrado.")
        conn.close()
        return
    
    cursor.execute("DELETE FROM Medicos WHERE crm = ?", (crm,))
    
    conn.commit()
    conn.close()
    print("Médico excluído com sucesso.")

def deletar_hospital():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    
    cnpj = input("Digite o CNPJ do hospital que deseja excluir: ")
    
    cursor.execute("SELECT * FROM Hospitais WHERE cnpj = ?", (cnpj,))
    hospital = cursor.fetchone()
    
    if hospital is None:
        print("Hospital não encontrado.")
        conn.close()
        return
    
    cursor.execute("DELETE FROM Hospitais WHERE cnpj = ?", (cnpj,))
    
    conn.commit()
    conn.close()
    print("Hospital excluído com sucesso.")
    
    
def deletar_enfermeira():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    
    corem = input("Digite o COREM da enfermeira que deseja excluir: ")
    
    cursor.execute("SELECT * FROM Enfermeiras WHERE corem = ?", (corem,))
    enfermeira = cursor.fetchone()
    
    if enfermeira is None:
        print("Enfermeira não encontrado.")
        conn.close()
        return
    
    cursor.execute("DELETE FROM Enfermeiras WHERE corem = ?", (corem,))
    
    conn.commit()
    conn.close()
    print("Enfermeira excluída com sucesso.")

def deletar_paciente():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    
    cpf = input("Digite o CPF do paciente que deseja excluir: ")
    
    cursor.execute("SELECT * FROM Pacientes WHERE cpf = ?", (cpf,))
    paciente = cursor.fetchone()
    
    if paciente is None:
        print("Paciente não encontrado.")
        conn.close()
        return
    
    cursor.execute("DELETE FROM Pacientes WHERE cpf = ?", (cpf,))
    
    conn.commit()
    conn.close()
    print("Paciente excluído com sucesso.")

def deletar_especialidade():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    
    cod_esp = input("Digite o código da especialidade que deseja excluir: ")
    
    cursor.execute("SELECT * FROM Especialidades WHERE cod_esp = ?", (cod_esp,))
    especialidade = cursor.fetchone()
    
    if especialidade is None:
        print("Especialidade não encontrada.")
        conn.close()
        return
    
    cursor.execute("DELETE FROM Especialidades WHERE cod_esp = ?", (cod_esp,))
    
    conn.commit()
    conn.close()
    print("Especialidade excluída com sucesso.")

def deletar_telefone():
    conn = sqlite3.connect('meudb.db')
    cursor = conn.cursor()
    
    cod_tel = input("Digite o código do telefone que deseja excluir: ")
    
    cursor.execute("SELECT * FROM Telefones WHERE cod_tel = ?", (cod_tel,))
    telefone = cursor.fetchone()
    
    if telefone is None:
        print("Telefone não encontrado.")
        conn.close()
        return
    
    cursor.execute("DELETE FROM Telefones WHERE cod_tel = ?", (cod_tel,))
    
    conn.commit()
    conn.close()
    print("Telefone excluído com sucesso.")

def menu_crud():
  print("="*30)
  print("\t Menu CRUD")
  print("="*30)
  print("1 - Cadastrar")
  print("2 - Relatório")
  print("3 - Atualizar")
  print("4 - Deletar")
  print("0 - Sair")


def menu_cadastro():
  #os.system('cls' if os.name == 'nt' else 'clear')
  print("----- Cadastrar -----")
  print("1 - Cadastrar Médico")
  print("2 - Cadastrar Paciente")
  print("3 - Cadastrar Hospital")
  print("4 - Cadastrar Especialidade")
  print("5 - Cadastrar Enfermeira")
  print("6 - Cadastrar Telefone")
  print("0 - Voltar")


def menu_relatorio():
  print("------ RELATÓRIOS ------")
  print("1 - Listar todos os médicos, pacientes e hospitais")
  print("2 - Listar pacientes que moram no Centro de Aracaju")
  print("3 - Listar médicos e seus telefones")
  print("4 - Listar corpo clínico do Hospital")
  print("0 - Voltar")

def menu_atualizar():
  print("----- Atualizar dados -----")
  print("1 - Atualizar dados do médico")
  print("2 - Atualizar dados do paciente")
  print("3 - Atualizar dados do hospital")
  print("4 - Atualizar dados da enfermeira")
  print("5 - Atualizar dados de telefone")
  print("6 - Atualizar dados de especialidade")
  print("0 - Voltar")

def menu_deletar():
  print("----- Deletar dados -----")
  print("1 - Deletar dados de médico")
  print("2 - Deletar dados de paciente")
  print("3 - Deletar dados de hospital")
  print("4 - Deletar dados de enfermeira")
  print("5 - Deletar dados de telefone")
  print("6 - Deletar dados de especialidade")
  print("0 - Voltar")
