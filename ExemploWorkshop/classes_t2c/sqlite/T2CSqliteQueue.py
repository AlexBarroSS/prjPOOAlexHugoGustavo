import sqlite3
import datetime
from pathlib import Path
from ExemploWorkshop.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType

ROOT_DIR = Path(__file__).parent.parent.parent.__str__()

"""
ESTRUTURA ESPERADA POR ESSA CLASSE:

Create table tbl_Fila_Processamento(
    id integer primary key,
    referencia varchar(200),
    datahora_criado varchar(50),
    ultima_atualizacao varchar(50),
    nome_maquina varchar(200),
    status varchar(100),
    obs varchar(500));

COLUNAS PODEM SER ADICIONADAS, MAS NUNCA EXCLUÍDAS OU MOVIDAS
O ARQUIVO DO BANCO LOCALIZADO EM resources/sqlite/banco_dados.db JÁ POSSUI ESSA TABELA CRIADA E VAZIA
"""

class T2CSqliteQueue:
    """
    Classe responsável para manipulação do sqlite e controle de fila.
    
    Parâmetros:

    Retorna:
    """

    def __init__(self, arg_clssMaestro:T2CMaestro, arg_strCaminhoBd:str=None, arg_strTabelaFila:str=None, arg_strNomeMaquina:str=None):
        """
        Inicializa a classe T2CSqliteQueue.
        - Cria a conexão com o banco
        - Nome da máquina precisa ser algum identificador único por execução
        - CaminhoBD e TabelaFila não precisam ser informados por padrão
        
        Parâmetros:
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.
        - arg_strCaminhoBd (str): caminho do banco de dados (opcional, default=None).
        - arg_strTabelaFila (str): nome da tabela da fila (opcional, default=None).
        - arg_strNomeMaquina (str): nome da máquina (opcional, default=None).

        Retorna:
        """

        self.var_clssMaestro = arg_clssMaestro
        #Se o caminho não for especificado, usa a configuração padrão
        self.var_strTabelaFila = "tbl_Fila_Processamento" if(arg_strTabelaFila is None) else arg_strTabelaFila
        self.var_strPathToDb = ROOT_DIR + "\\resources\\sqlite\\banco_dados.db" if(arg_strCaminhoBd is None) else arg_strCaminhoBd
        var_csrCursor = sqlite3.connect(self.var_strPathToDb).execute("SELECT * FROM " + self.var_strTabelaFila + " WHERE status = 'NEW'")

        self.var_intItemsQueue = len(var_csrCursor.fetchall())
        self.var_strNomeMaquina = arg_strNomeMaquina
        var_csrCursor.close()

    def update(self):
        """
        Atualiza a própria classe, usado em vários pontos do projeto para atualizar os itens na fila
        
        Parâmetros:

        Retorna:
        """

        var_csrCursor = sqlite3.connect(self.var_strPathToDb).execute("SELECT * FROM " + self.var_strTabelaFila + " WHERE status = 'NEW'")
        self.var_intItemsQueue = len(var_csrCursor.fetchall())
        var_csrCursor.close()

    def insert_new_queue_item(self, arg_strReferencia:str, arg_listInfAdicional:list = None):
        """
        Insere um item na tabela especificada, com a referência e com os valores adicionais
        - IMPORTANTE: Criar colunas extras para informações a mais informadas em arg_listInfAdicional, não cria colunas sozinho
        
        Parâmetros:
        - arg_strReferencia (str): referência do item.
        - arg_listInfAdicional (list): informações adicionais (opcional, default=None).

        Retorna:
        """

        #Aqui eu insiro com o nome da máquina vazio, para que qualquer máquina possa processar em paralelo mais a frente
        var_strNow = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        var_listValues = [arg_strReferencia, var_strNow, var_strNow, "", "NEW", ""]
        var_listColumns = []
        
        var_csrCursor = sqlite3.connect(self.var_strPathToDb).execute("SELECT * FROM " + self.var_strTabelaFila + " WHERE id = 0")
        for description in var_csrCursor.description:
            if(description[0] != "id"): var_listColumns.append(description[0])

        if(arg_listInfAdicional is not None): var_listValues.extend(arg_listInfAdicional)

        self.update()

        #Construindo o comando insert
        var_strInsert = "INSERT INTO " + self.var_strTabelaFila + " (" + var_listColumns.__str__() + ") VALUES (" + var_listValues.__str__() + ")"
        var_strInsert = var_strInsert.replace("[", "").replace("]", "")
        
        #Executando o comando insert
        try:
            var_csrCursor.execute(var_strInsert)
            var_csrCursor.connection.commit()
        except Exception:
            self.var_clssMaestro.write_log(arg_strMensagemLog="Erro ao inserir linhas: " + str(Exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
            raise

        var_csrCursor.close()
        self.update()

    def get_specific_queue_item(self, arg_intIndex:int) -> tuple:
        """
        Retorna um item específico da fila.

        Parâmetros:
        - arg_intIndex (int): índice do item.

        Retorna:
        - tuple: tupla com as informações do item.
        """
        var_csrCursor = sqlite3.connect(self.var_strPathToDb).execute("SELECT * FROM " + self.var_strTabelaFila + " WHERE id = " + arg_intIndex.__str__())
        var_tplRow = var_csrCursor.fetchone()
        var_csrCursor.close()

        self.update()
        return var_tplRow
   
    def get_next_queue_item(self) -> tuple:
        """
        Retorna o próximo item da fila que não foi processado e não possui máquina alocada, None se não existe nenhum item assim.

        Parâmetros:

        Retorna:
        - tuple: tupla com as informações do próximo item da fila.
        """
        var_strNow = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        var_csrCursor = sqlite3.connect(self.var_strPathToDb).execute("UPDATE " + self.var_strTabelaFila + " SET ultima_atualizacao = '" + var_strNow + "', nome_maquina = '" + self.var_strNomeMaquina + "', status = 'ON QUEUE' WHERE id = (SELECT MIN(id) FROM " + self.var_strTabelaFila + " WHERE status = 'NEW')").connection.commit()
        var_csrCursor = sqlite3.connect(self.var_strPathToDb).execute("SELECT * FROM " + self.var_strTabelaFila + " WHERE nome_maquina = '" + self.var_strNomeMaquina + "' and status = 'ON QUEUE' ORDER BY id LIMIT 1")
        var_tplRow:tuple = var_csrCursor.fetchone()
        if(var_tplRow is not None): var_csrCursor.execute("UPDATE " + self.var_strTabelaFila + " SET status = 'RUNNING' WHERE id = " + var_tplRow[0].__str__()).connection.commit()

        var_csrCursor.close()
        self.update()

        return var_tplRow

    def update_status_item(self, arg_intIndex:int, arg_strNovoStatus:str, arg_strObs:str=""):
        """
        Atualiza o status de um item com um determinado índice.

        Parâmetros:
        - arg_intIndex (int): índice do item.
        - arg_strNovoStatus (str): novo status do item.
        - arg_strObs (str): observação (opcional, default= "").

        Retorna:
        """

        #Tratando os casos onde obs vem com quotes, trocando por *
        arg_strObs = arg_strObs.replace('"', '*').replace("'", '*')

        var_strNow = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        var_csrCursor = sqlite3.connect(self.var_strPathToDb).execute("UPDATE " + self.var_strTabelaFila + " SET ultima_atualizacao = '" + var_strNow + "', status = '" + arg_strNovoStatus + "', obs = '" + arg_strObs + "' WHERE id = " + arg_intIndex.__str__())
        var_csrCursor.connection.commit()
   
        var_csrCursor.close()
        self.update()

    def abandon_queue(self):
        """
        Marca todos os itens com status NEW como ABANDONED.
        
        Parâmetros:

        Retorna:
        """

        var_csrCursor = sqlite3.connect(self.var_strPathToDb).execute("UPDATE " + self.var_strTabelaFila + " SET status = 'ABANDONED' WHERE status = 'NEW'")
        var_csrCursor.connection.commit()

        var_csrCursor.close()
        self.update()
   