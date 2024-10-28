import mysql.connector

#-------------------------

# Conexão com Banco de Dados

from mysql.connector import errorcode
try:
    db = mysql.connector.connect(
        host='localhost',
        user='root', 
        password='172127@Jlb', 
        database='caixa',
        auth_plugin="mysql_native_password"
    )
    print("Database connection made!")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print(error)


#---------------------------------------------------------------------
############ Funções ############

def verificar_login(nome_usuario, senha_usuario):
   
    sql = f'select * from usuarios WHERE login = "{nome_usuario}" and senha_usuario = "{senha_usuario}"'
    valores = (nome_usuario, senha_usuario)
    cursor = db.cursor()
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    
    for usuario in usuarios:
        
        print("bem vinda ao caixa eletronico", usuario[1])
 
    return usuarios 
   
    
####--------------------------------------------------------  

def inserirDados():
    nome = input("Digite seu Nome Completo: ")

    login = input("Digite seu nome de usuario: ")

    senha = input("Digite sua senha: ")

    dep = input("Quanto deseja depositar: ")

    pix = input("Cadastre sua Chave Pix: ")
    
    try:
        
        
        cursor = db.cursor()
        
        sql = 'INSERT INTO usuarios (nome, login, senha_usuario, saldo, pix) values(%s,%s,%s,%s,%s)'
        valores = (nome, login, senha, dep, pix)
        cursor = db.cursor()
        cursor.execute(sql, valores)
        db.commit()
    
        print("Conta criada com Sucesso")
       
    except mysql.connector.Error as e:
        print("Erro de conexão")
        db.rollback()
    finally:
        #cursor.close()
        #db.close()
        print("")
        

#------------------------------------------------------------
def menu ():
    print("\n*******************Caixa Eletronico ***********************")

    print("Selecione o número da operação desejada: \n""\n"
      "1 - Saque \n"
      "2 - Deposito \n"
      "3 - Transferencia \n"
      "4 - Sair \n")
    
#------------------------------------------------------
def sacar():
   
    try:
        
        cursor = db.cursor()
        
        sql = f'select saldo from usuarios WHERE login = "{nome_usuario}" and senha_usuario = "{senha_usuario}"'
        valores = (nome_usuario, senha_usuario)
        cursor = db.cursor()
        cursor.execute(sql)
        linhas = cursor.fetchone()
    
        if linhas:
            valorDados = linhas[0]
            if valorDados < dep:
                print("voce não possui saldo o suficiente: ")
            else:    
                soma = valorDados - dep
                print(f"Seu saldo é: {soma}")
            
                sql = f'UPDATE usuarios SET saldo = {soma} WHERE login = "{nome_usuario}" and senha_usuario = "{senha_usuario}"'
                valores = (nome_usuario, senha_usuario, dep)
                cursor = db.cursor()
                cursor.execute(sql)
                db.commit()
        else:
            print(f"Registro com ID {nome_usuario} não encontrado.")
    except mysql.connector.Error as e:
        print("erri".format(e))
        db.rollback()
    finally:
        #cursor.close()
        #db.close()
        print("")
#------------------------------------------------------
        
def deposito():
    try:
        
       # cursor = db.cursor()
        
        sql = f'select saldo from usuarios WHERE login = "{nome_usuario}" and senha_usuario = "{senha_usuario}"'
        valores = (nome_usuario, senha_usuario)
        cursor = db.cursor()
        cursor.execute(sql)
        linhas = cursor.fetchone()
    
        if linhas:
            valorDados = linhas[0]
            print(f"Valor Anterior: {valorDados}")
           
            soma = valorDados + dep
            print(f"Seu saldo é: {soma}")
            
            sql = f'UPDATE usuarios SET saldo = {soma} WHERE login = "{nome_usuario}" and senha_usuario = "{senha_usuario}"'
            valores = (nome_usuario, senha_usuario, soma)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
        else:
            print(f"Registro com ID {nome_usuario} não encontrado.")
    except mysql.connector.Error as e:
        print("erri".format(e))
        db.rollback()
    finally:
        #cursor.close()
        #db.close()
        print("")        
#------------------------------------------------------
def transferir():    
    try:
        

        cursor = db.cursor()
        
        sql = f'select saldo from usuarios WHERE login = "{nome_usuario}" and senha_usuario = "{senha_usuario}"'
        valores = (nome_usuario, senha_usuario, dep)
        cursor = db.cursor()
        cursor.execute(sql)
        linhas = cursor.fetchone()
    
        if linhas:
            valorDados = linhas[0]
            if valorDados < dep:
                print("voce não possui saldo o suficiente: ")
            elif valorDados > dep:    
                soma = valorDados - dep
                #print(f"soma: {soma}")
                
                sql = f'UPDATE usuarios SET saldo = {soma} WHERE login = "{nome_usuario}" and senha_usuario = "{senha_usuario}"'
                valores = (nome_usuario, senha_usuario, soma)
                cursor = db.cursor()
                cursor.execute(sql)
                db.commit()
                #print("sucesso")
                somar()
            
                
        else:
            print(f"Registro com ID {nome_usuario} não encontrado.")
    except mysql.connector.Error as e:
        print("erri".format(e))
        db.rollback()
    finally:
        #cursor.close()
        #db.close()
        print("")       

#------------------------------------------------------
def somar():
    try:
        cursor = db.cursor()
        chave = input("Confirmar chave Pix: ")
        
                
        sql = f'select saldo from usuarios WHERE pix = "{chave}"'
        valores = (chave)
        cursor = db.cursor()
        cursor.execute(sql)
        linha = cursor.fetchone()
        if linha:
            saldos = linha[0]
            sal = saldos + dep
        
            
            sql = f'UPDATE usuarios SET saldo = {sal} WHERE pix = "{chave}"'
            valores = (chave,sal)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            print("Tranferencia feita com Sucesso")
        else:
            print(f"Registro com ID {nome_usuario} não encontrado.")
    except mysql.connector.Error as e:
        print("erri".format(e))
        db.rollback()
    finally:
        #cursor.close()
        #db.close()
        print("")

#------------------------------------------------------

'''def verificar_pix(chave_pix):

    sql = f'select * from usuarios WHERE pix = "{chave_pix}"'
    valores = (chave_pix)
    cursor = db.cursor()
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    
    for usuario in usuarios:
        print("Nome do usuario", usuario[1])
    return usuarios'''
    
def verificar_pix(chave_pix):
    sql = f'select * from usuarios WHERE pix = "{chave_pix}"'
    valores = (chave_pix)
    cursor = db.cursor()
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    
    for usuario in usuarios:
        print("bem vinda ao caixa eletronico", usuario[2])
        
    return usuarios

#------------------------------------------------------
        #Começo do app


print("******** BEM VINDO AO BANCO SLYHAN ******** \n")

esc1 = input("Já tem conta? S/N: ")
    
if ((esc1 !="s") and (esc1!="n")):
    print("Você Digitou algo errado!!")
    esc1 = input("Já tem conta? S/N: ")

    

if esc1 == "n": #se não tiver conta faz isso
    esc2 = input("Deseja fazer criar uma conta? S/N: ")
    if ((esc2 !="s") and (esc2 !="n")):
        print("voce digitou algo eeerrado")
        esc2 = input("Deseja fazer criar uma conta?: S/N ")
    if esc2 == "s":
        inserirDados()
    if esc2 == "n": #se não quiser criar sai
        print("bye bye")
        exit()
elif esc1 == "s":         
    nome_usuario = input("Digite o nome de usuário: ")
    senha_usuario = input("Digite a senha: ")

    if verificar_login(nome_usuario, senha_usuario):
        print("Login efetuado com sucesso!!")
        
    escolha = input("Deseja fazer alguma operação? S/N: ")

    if ((escolha !="s") and (escolha !="n")):
        print("voce sdigitou algo eeerrado")
        escolha = input("Deseja fazer alguma operação? S/N: ")

    while escolha == "s":
        menu()

        opcao = (input("Digite sua opção (1/2/3/4): "))
        if opcao == "1":
            dep = float(input("Qual valor deseja Sacar: "))
            sacar()
            escolha = input("Deseja fazer alguma operação? S/N: ")

        if opcao == "2":
            dep = float(input("Qual valor deseja Depositar: ")) 
            deposito()     
            escolha = input("Deseja fazer alguma operação? S/N: ")

        elif opcao == "3":
            chave_pix = float(input("Qual a chave Pix: ")) 
            verificar_pix(chave_pix)

            dep = float(input("Qual valor deseja Tranferir: "))
            transferir()
            
            escolha = input("Deseja fazer alguma operação? S/N: ")
           # cliente = input("Para qual conta deseja fazer a transferencia: ")
        #fazer_transf(cliente,cliente)

        elif opcao == "4":
            print("Obrigada, ate a proxima")
            exit()



    while escolha == "n":   
        print("Obrigada, ate a proxima")
        exit()

    else:
        print("Obrigada, ate a proxima")
        exit()

    
else:
    print("")

