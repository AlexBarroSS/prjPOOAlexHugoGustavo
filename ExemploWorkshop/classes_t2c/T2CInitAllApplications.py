from botcity.web import WebBot, Browser
from botcity.core import DesktopBot
from ExemploWorkshop.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType
from ExemploWorkshop.classes_t2c.utils.T2CExceptions import BusinessRuleException
from ExemploWorkshop.classes_t2c.sqlite.T2CSqliteQueue import T2CSqliteQueue

# TODO o texto que eu quiser comentar
class T2CInitAllApplications:
    """
    Classe feita para ser invocada principalmente no começo de um processo, para iniciar os processos necessários para a automação.
    """

    #Iniciando a classe, pedindo um dicionário config e o bot que vai ser usado e enviando uma exceção caso nenhum for informado
    def __init__(self, arg_dictConfig:dict, arg_clssMaestro:T2CMaestro, arg_botWebbot:WebBot=None, arg_botDesktopbot:DesktopBot=None, arg_clssSqliteQueue:T2CSqliteQueue=None):
        """
        Inicializa a classe T2CInitAllApplications.

        Parâmetros:
        - arg_dictConfig (dict): dicionário de configuração.
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.
        - arg_botWebbot (WebBot): instância de WebBot (opcional, default=None).
        - arg_botDesktopbot (DesktopBot): instância de DesktopBot (opcional, default=None).
        - arg_clssSqliteQueue (T2CSqliteQueue): instância de T2CSqliteQueue (opcional, default=None).

        Retorna:
        """
        
        if(arg_botWebbot is None and arg_botDesktopbot is None): raise Exception("Não foi possível inicializar a classe, forneça pelo menos um bot")
        else:
            self.var_botWebbot = arg_botWebbot
            self.var_botDesktopbot = arg_botDesktopbot
            self.var_dictConfig = arg_dictConfig
            self.var_clssMaestro = arg_clssMaestro
            self.var_clssSqliteQueue = arg_clssSqliteQueue

    def add_to_queue(self):
        """
        Adiciona itens à fila no início do processo, se necessário.

        Observação:
        - Código placeholder.
        - Se o seu projeto precisa de mais do que um método simples para subir a sua fila, considere fazer um projeto dispatcher.

        Parâmetros:
        """
        True

    def execute(self, arg_boolFirstRun=False, arg_clssSqliteQueue=None):
        """
        Executa a inicialização dos aplicativos necessários.

        Parâmetros:
        - arg_boolFirstRun (bool): indica se é a primeira execução (default=False).
        - arg_clssSqliteQueue (T2CSqliteQueue): instância da classe T2CSqliteQueue (opcional, default=None).
        
        Observação:
        - Edite o valor da variável `var_intMaxTentativas` no arquivo Config.xlsx.
        
        Retorna:

        Raises:
        - BusinessRuleException: em caso de erro de regra de negócio.
        - Exception: em caso de erro geral.
        """

        #Chama o método para subir a fila, apenas se for a primeira vez
        if(arg_boolFirstRun):
            self.add_to_queue()

        #Edite o valor dessa variável a no arquivo Config.xlsx
        var_intMaxTentativas = self.var_dictConfig["MaxRetryNumber"]
        
        for var_intTentativa in range(var_intMaxTentativas):
            try:
                self.var_clssMaestro.write_log("Iniciando aplicativos, tentativa " + (var_intTentativa+1).__str__())
                #Insira aqui seu código para iniciar os aplicativos
            except BusinessRuleException as exception:
                self.var_clssMaestro.write_log(arg_strMensagemLog="Erro de negócio: " + str(exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.BUSINESS_ERROR)

                raise
            except Exception as exception:
                self.var_clssMaestro.write_log(arg_strMensagemLog="Erro, tentativa " + (var_intTentativa+1).__str__() + ": " + str(exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)

                if(var_intTentativa+1 == var_intMaxTentativas): raise
                else: 
                    #inclua aqui seu código para tentar novamente
                    
                    continue
            else:
                self.var_clssMaestro.write_log("Aplicativos iniciados, continuando processamento...")
                break
            
