from ExemploWorkshop.classes_t2c.utils.T2CMaestro import T2CMaestro
import datetime
import pyodbc

class T2CSqlAnaliticoSintetico:
    """
    Classe usada para gravar dados da execução no SQL Server, geralmente no banco da T2C.
    
    Parâmetros:

    Retorna:
    """

    def __init__(self, arg_clssMaestro:T2CMaestro, arg_dictConfig:dict):
        """
        Inicia uma instância da classe T2CSqlAnaliticoSintetico, realizando a criação de uma conexão e um cursor.

        Parâmetros:
            - arg_dictConfig (dict): Dicionário de configuração do framework.
            - arg_clssMaestro (T2CMaestro): Instância de uma classe T2CMaestro.
        
        Retorna:
        """
        self.var_dictConfig = arg_dictConfig
        self.var_clssMaestro = arg_clssMaestro
        

    def connect(self):
        """
        Realiza a conexão com o SQL Server.
        
        Parâmetros:

        Retorna:
        """

        var_strDbServer = self.var_dictConfig["BdServer"]
        var_strDbDatabase = self.var_dictConfig["BdDatabase"]
        var_strDbUser = self.var_dictConfig["BdUsuario"]

        #Troque para var_strDbSenha = self.var_dictConfig["BdSenha"] em casos onde não é possível usar credenciais (developers, por exemplo)
        var_strDbPassword = self.var_clssMaestro.get_credential(self.var_dictConfig["BdSenha"])
        
        var_strConnectionString = ("DRIVER={SQL Server}" + 
                                   ";SERVER=" + var_strDbServer + 
                                   #";PORT=1443" +                      #Porta usada na conexão, para casos onde precisa usar uma específica devido firewall
                                   ";DATABASE=" + var_strDbDatabase + 
                                   ";UID=" + var_strDbUser + 
                                   ";PWD=" + var_strDbPassword)
       
       # print(pyodbc.drivers()) #Descomente para verificar drivers instalados

        try:
            #Tenta criar uma conexão e instanciar um novo cursor
            self.var_sqlConn = pyodbc.connect(var_strConnectionString)
            self.var_csrCursor = self.var_sqlConn.cursor()
        except Exception as exception:
            self.var_clssMaestro.write_log("Erro ao conectar ao SQL Server")
            self.var_clssMaestro.write_log(str(exception))


    def disconnect(self):
        """
        Desconecta do SQL Server.
        
        Parâmetros:

        Retorna:
        """

        try:
            self.var_sqlConn.close()
        except Exception as exception:
            self.var_clssMaestro.write_log("Erro ao desconectar do SQL Server")
            self.var_clssMaestro.write_log(str(exception))


    def insert_linha_inicio_sintetico(self, arg_strNomeMaquina:str, 
                                      arg_boolUsaCaptcha:bool, 
                                      arg_boolUsaOCR:bool, arg_boolUsaAPI:bool, 
                                      arg_dateInicioExecucao:datetime):
        """
        Insere uma nova linha na tabela tbl_dados_sinteticos. Esse método é executado no começo do processo.

        Parâmetros:
            - arg_strNomeMaquina (str): Nome da máquina.
            - arg_boolUsaCaptcha (bool): Booleana indicando se o processo usa captcha ou não.
            - arg_boolUsaOCR (bool): Booleana indicando se o processo usa OCR ou não.
            - arg_boolUsaAPI (bool): Booleada indicando se o processo uda API ou não.
            - arg_dateInicioExecucao (datetime): Datetime representando o inicio da execução.
        
        Retorna:    
        """
        var_strCaptcha = "S" if arg_boolUsaCaptcha else "N"
        var_strOCR = "S" if arg_boolUsaOCR else "N"
        var_strAPI = "S" if arg_boolUsaAPI else "N"

        self.var_clssMaestro.write_log("Incluindo linha na tabela tbl_dados_sinteticos no SQL Server")

        #Conectando ao SQL Server
        self.connect()

        try:
            #Insert inicial
            self.var_csrCursor.execute("INSERT INTO tbl_dados_sinteticos (" + 
                                        "Ferramenta"
                                        ",Cliente"
                                        ",tenant"
                                        ",nome_processo" 
                                        ",descri_processo"
                                        ",Nome_maquina"
                                        ",Resolucao"
                                        ",Serv_Captcha"
                                        ",Serv_Ocr"
                                        ",Serv_Api"
                                        ",inicio" 
                                        ") VALUES ("
                                        "'BotCity'"                                             #Ferramenta
                                        ",'" + self.var_dictConfig["DadosCliente"] + "'"        #cliente 
                                        ",'" + self.var_dictConfig["MaestroServer"] + "'"       #tenant
                                        ",'" + self.var_dictConfig["NomeProcesso"] + "'"        #nome_processo 
                                        ",'" + self.var_dictConfig["DescricaoProcesso"] + "'"   #descri_processo
                                        ",'" + arg_strNomeMaquina + "'"                         #nome_maquina
                                        ",'" + self.var_dictConfig["DadosResolucao"] + "'"      #resolucao 
                                        ",'" + var_strCaptcha + "'"                             #captcha 
                                        ",'" + var_strOCR + "'"                                 #ocr 
                                        ",'" + var_strAPI + "'"                                 #api 
                                        ",?"                                                    #inicio
                                        ")", arg_dateInicioExecucao)
            
            #Pegando o identity gerado e salvando numa variável
            var_rowIdentitySintetico = self.var_csrCursor.execute("SELECT @@IDENTITY").fetchone()
            self.var_strIdentitySintetico = str(var_rowIdentitySintetico[0])

            self.var_csrCursor.commit()
        except Exception as exception:
            self.var_clssMaestro.write_log("Erro ao incluir linha no SQL Server")
            self.var_clssMaestro.write_log(str(exception))
            
        #Desconectando do SQL Server
        self.disconnect()


    def update_linha_fim_sintetico(self, 
                                   arg_intQtdeCaptcha:int, 
                                   arg_intQtdeOcr:int, 
                                   arg_intQtdeApi:int, 
                                   arg_intTotalItens:int,
                                   arg_intTotalItensSucesso:int,
                                   arg_intTotalItensBusinessEx:int,
                                   arg_intTotalItensAppEx:int, 
                                   arg_dateFimExecucao:datetime):
        """
        Inserindo campos novos em um update na linha na tabela tbl_dados_sinteticos. Esse método é executado no fim do processo.

        Parâmetros:
            - arg_intQtdeCaptcha (int): Int contador de quantidade de captchas usadas no processo.
            - arg_intQtdeOcr (int): Int contador de quantidade de OCRs usados no processo.
            - arg_intQtdeApi (int): Int contador de quantidade de chamadas de api usadas no processo.
            - arg_intTotalItens (int): Total de itens processados no total.
            - arg_intTotalItensSucesso (int): Total de itens processados com sucesso.
            - arg_intTotalItensBusinessEx (int): Total de itens processados com business exception.
            - arg_intTotalItensAppEx (int): Total de itens processados com app exceptions.
            - arg_dateFimExecucao (datetime): Datetime representando o final da execução.
        
        Retorna:
        """

        self.var_clssMaestro.write_log("Atualizando linha na tabela tbl_dados_sinteticos no SQL Server com os dados finais")

        #Conectando ao SQL Server
        self.connect()

        try:
            #Fazendo update com base no id salvo anteriormente
            self.var_csrCursor.execute("UPDATE tbl_dados_sinteticos SET " +
                                    "Qtd_captcha = " + str(arg_intQtdeCaptcha) + 
                                    ",Qtd_Ocr = " + str(arg_intQtdeOcr) + 
                                    ",Qtd_Api = " + str(arg_intQtdeApi)+ 
                                    ",fim = ?" +                                                                    #FimExecucao
                                    ",total_itens = " + str(arg_intTotalItens) + 
                                    ",total_itens_sucesso = " + str(arg_intTotalItensSucesso) + 
                                    ",total_itens_negocios = " + str(arg_intTotalItensBusinessEx) + 
                                    ",total_itens_aplicacao = " + str(arg_intTotalItensAppEx)+ 
                                    "WHERE  Id_sintetico = " + self.var_strIdentitySintetico, arg_dateFimExecucao)
            self.var_csrCursor.commit()
        except Exception as exception:
            self.var_clssMaestro.write_log("Erro ao atualizar linha no SQL Server")
            self.var_clssMaestro.write_log(str(exception))

        #Desconectando do SQL Server
        self.disconnect()


    def insert_linha_analitico(self, 
                               arg_tplItemFila:tuple,
                               arg_strNomeFila:str,  
                               arg_strStatusItem:str,
                               arg_dateInicioItem:datetime, 
                               arg_dateFimItem:datetime, 
                               arg_strTipoExcecao:str="", 
                               arg_strDescricaoExcecao:str=""
                               ):
        """
        Insere uma nova linha na tabela tbl_dados_analiticos. Esse método é executado no final de cada item.

        Parâmetros:
            arg_tplItemFila (tuple): Tupla referente ao item da fila por completo.
            arg_strNomeFila (str): Nome da fila (no caso do BotCity, nome da tabela de fila).
            arg_strStatusItem (str): Status final do item.
            arg_strTipoExcecao (str): Tipo de exceção (se alguma) do item. (default="")
            arg_strDescricaoExcecao (str): Descrição da exceção. (default="")
            arg_dateInicioItem (datetime): Datetime do início da execução do item.
            arg_dateFimItem (datetime): Datetime do final da execução do item.
        
        Retorna:
        """

        self.var_clssMaestro.write_log("Incluindo linha na tabela tbl_dados_analiticos no SQL Server")

        #Realizando assigns e tratando variáveis
        var_strReferencia = arg_tplItemFila[1]
        var_strItemFila = arg_tplItemFila.__str__().replace("(", "").replace(")", "")
        var_strDescricaoExcecao = arg_strDescricaoExcecao.replace('"', "*").replace("'", "*")

        #Conectando ao SQL Server
        self.connect()

        try:
            #Comando Insert
            self.var_csrCursor.execute("INSERT INTO tbl_dados_analiticos ("
                                       "id_Sintetico"
                                       ",nome_fila"
                                       ",referencia"
                                       ",item_fila"
                                       ",inicio"
                                       ",fim"
                                       ",status_item_fila"
                                       ",tipo_excecao"
                                       ",descr_excecao) VALUES(" +
                                       self.var_strIdentitySintetico +                          #IdSintetico
                                       ",'" + arg_strNomeFila + "'" +                           #NomeFila
                                       ",'" + var_strReferencia + "'" +                         #Referencia
                                       ",?,?,?"                                                 #Parâmetros ItemFila, DataInicioItem e DataFimItem
                                       ",'" + arg_strStatusItem + "'"                           #StatusItem
                                       ",'" + arg_strTipoExcecao + "'"                          #TipoExcecao
                                       ",?)", var_strItemFila, arg_dateInicioItem, arg_dateFimItem, var_strDescricaoExcecao) #Parâmetros
            self.var_csrCursor.commit()
        except Exception as exception:
            self.var_clssMaestro.write_log("Erro ao incluir linha no SQL Server")
            self.var_clssMaestro.write_log(str(exception))

        #Desconectando do SQL Server
        self.disconnect()
