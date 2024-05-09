from pathlib import Path
from ExemploWorkshop.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType
import win32com.client as win32

ROOT_DIR = Path(__file__).parent.parent.parent.__str__()

class T2CSendEmailOutlook:
    """
    Classe responsável pelo envio de email pelo outlook, enviando usuario, senha e qual servidor vai ser usado
    
    Parâmetros:

    Retorna:

    """

    def __init__(self, arg_strNomeProcesso, arg_clssMaestro:T2CMaestro):
        """
        Construtor do envio de email.

        Parâmetros:
        - arg_strNomeProcesso (str): nome do processo.
        - arg_clssMaestro (T2CMaestro): instância da classe T2CMaestro.

        Retorna:

        """ 
        self.var_clssMaestro = arg_clssMaestro
        self.var_strNomeProcesso = arg_strNomeProcesso

    def send_email_inicial(self, arg_strEnvioPara:str, arg_strCC:str=None, arg_strBCC:str=None):
        """
        Envia o email inicial do robô, apenas precisando informar quem deve receber, separando por ;

        Parâmetros:
        - arg_strEnvioPara (str): destinatários separados por ';'.
        - arg_strCC (str): destinatários em cópia separados por ';' (opcional, default=None).
        - arg_strBCC (str): destinatários em cópia oculta separados por ';' (opcional, default=None).

        Retorna:

        """
        var_clssOutlook:win32.CDispatch = win32.Dispatch('outlook.application')
        var_clssMail:win32.CDispatch = var_clssOutlook.CreateItem(0) #Criando um item do tipo Email (0)

        #Lendo template
        var_fileTemplate = open(ROOT_DIR + "\\resources\\templates\\Email_Inicio.txt", "r")
        var_strEmailTexto = var_fileTemplate.read()
        var_fileTemplate.close()

        var_clssMail.HTMLBody = var_strEmailTexto.replace("*NOME_ROBO*", self.var_strNomeProcesso)
        var_clssMail.Subject = "Inicio execução: " + self.var_strNomeProcesso
        var_clssMail.To = arg_strEnvioPara

        if(arg_strCC is not None): var_clssMail.CC = arg_strCC
        if(arg_strBCC is not None): var_clssMail.BCC = arg_strBCC
        
        #Envia o email inicial
        try:
            self.var_clssMaestro.write_log("Enviando email inicial")
            var_clssMail.Send()
            self.var_clssMaestro.write_log("Email enviado com sucesso")
        except Exception:
            self.var_clssMaestro.write_log(arg_strMensagemLog="Erro enviando email inicial: " + str(Exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
            raise
      
    def send_email_final(self, arg_strHorarioInicio:str, arg_strHorarioFim:str, arg_strEnvioPara:str, arg_listAnexos:list=None, arg_boolSucesso:bool=True, arg_strCC:str=None, arg_strBCC:str=None):
        """
        Envia o email final do robô.
        Recebendo o horário do início da execução, o horário final, para quem é necessário enviar (separando por ;) e os relatórios finais
        
        Parâmetros:
        - arg_strHorarioInicio (str): horário de início da execução.
        - arg_strHorarioFim (str): horário de fim da execução.
        - arg_strEnvioPara (str): destinatários separados por ';'
        - arg_listAnexos (list): lista de anexos. (opcional, default=None)
        - arg_boolSucesso (bool): indica se a execução foi bem-sucedida. (opcional, default=True)
        - arg_strCC (str): destinatários em cópia separados por ';'. (opcional, default=None)
        - arg_strBCC (str): destinatários em cópia oculta separados por ';'. (opcional, default=None)

        Retorna:

        """
        var_clssOutlook:win32.CDispatch = win32.Dispatch('outlook.application')
        var_clssMail:win32.CDispatch = var_clssOutlook.CreateItem(0) #Criando um item do tipo Email (0)
        
        #Lendo template
        var_fileTemplate = open(ROOT_DIR + "\\resources\\templates\\Email_Final.txt", "r")
        var_strEmailTexto = var_fileTemplate.read()
        var_fileTemplate.close()

        var_strStatusFinalizacao = "com sucesso" if arg_boolSucesso else "com erros"
        var_clssMail.HTMLBody = var_strEmailTexto.replace("*NOME_ROBO*", self.var_strNomeProcesso).replace("*DATAHORA_INI*", arg_strHorarioInicio).replace("*DATAHORA_FIM*", arg_strHorarioFim).replace("*FINALIZACAO*", var_strStatusFinalizacao)
        var_clssMail.Subject = "Finalização da execução: " + self.var_strNomeProcesso
        var_clssMail.To = arg_strEnvioPara

        if(arg_strCC is not None): var_clssMail.CC = arg_strCC
        if(arg_strBCC is not None): var_clssMail.BCC = arg_strBCC
        
        #Inserindo anexos
        if(arg_listAnexos is not None):
            for var_strAnexo in arg_listAnexos:
                var_clssMail.Attachments.Add(var_strAnexo)

        #Envia o email de finalização
        try:
            self.var_clssMaestro.write_log("Enviando email de finalização")
            var_clssMail.Send()
            self.var_clssMaestro.write_log("Email enviado com sucesso")
        except Exception:
            self.var_clssMaestro.write_log(arg_strMensagemLog="Erro enviando email de finalização" + str(Exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
            raise

    def send_email_erro(self, arg_strEnvioPara:str, arg_listAnexos:list, arg_strDetalhesErro:str, arg_boolBusiness:bool=False, arg_strCC:str=None, arg_strBCC:str=None):
        """
        Envia um email em casos de erro.

        Parâmetros:
        - arg_strEnvioPara (str): destinatários separados por ';'.
        - arg_listAnexos (list): lista de anexos.
        - arg_strDetalhesErro (str): detalhes do erro.
        - arg_boolBusiness (bool): indica se o erro é de regra de negócio. (opcional, default=False)
        - arg_strCC (str): destinatários em cópia separados por ';'. (opcional, default=None)
        - arg_strBCC (str): destinatários em cópia oculta separados por ';'. (opcional, default=None)

        Retorna:

        """
        var_clssOutlook:win32.CDispatch = win32.Dispatch('outlook.application')
        var_clssMail:win32.CDispatch = var_clssOutlook.CreateItem(0) #Criando um item do tipo Email (0)

        #Lendo template
        var_fileTemplate = open(ROOT_DIR + "\\resources\\templates\\Email_ErroEncontrado.txt", "r")
        var_strEmailTexto = var_fileTemplate.read()
        var_fileTemplate.close()

        var_clssMail.HTMLBody = var_strEmailTexto.replace("*NOME_ROBO*", self.var_strNomeProcesso).replace("*ERRO_DETALHES*", arg_strDetalhesErro)
        var_clssMail.HTMLBody = var_clssMail.HTMLBody.replace("*ERRO_TIPO*", "ERRO DE REGRA DE NEGÓCIO") if arg_boolBusiness else var_clssMail.HTMLBody.replace("*ERRO_TIPO*", "ERRO INESPERADO")
        var_clssMail.Subject = "Erro durante a execução: " + self.var_strNomeProcesso
        var_clssMail.To = arg_strEnvioPara

        if(arg_strCC is not None): var_clssMail.CC = arg_strCC
        if(arg_strBCC is not None): var_clssMail.BCC = arg_strBCC
        
        #Inserindo anexos
        if(arg_listAnexos is not None):
            for var_strAnexo in arg_listAnexos:
                var_clssMail.Attachments.Add(var_strAnexo)

        #Envia o email inicial
        try:
            self.var_clssMaestro.write_log("Enviando email de erro")
            var_clssMail.Send()
            self.var_clssMaestro.write_log("Email enviado com sucesso")
        except Exception:
            self.var_clssMaestro.write_log(arg_strMensagemLog="Erro enviando email de erro: " + str(Exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
            raise
       
    def send_email(self, arg_strCorpoEmail:str, arg_strEnvioPara:str, arg_strAssunto:str, arg_listAnexos:list=None, arg_boolHtml:bool=False, arg_strCC:str=None, arg_strBCC:str=None):
        """
        Simplesmente envia um email normal. Pode ser usado em vários lugares no código, porém é necessário informar um corpo para o email.

        Parâmetros:
        - arg_strCorpoEmail (str): corpo do email.
        - arg_strEnvioPara (str): destinatários separados por ';'.
        - arg_strAssunto (str): assunto do email.
        - arg_listAnexos (list): lista de anexos. (opcional, default=None).
        - arg_boolHtml (bool): indica se o corpo do email é HTML (default=False).
        - arg_strCC (str): destinatários em cópia separados por ';' (opcional, default=None).
        - arg_strBCC (str): destinatários em cópia oculta separados por ';' (opcional, default=None).

        Retorna:
        
        """
        var_clssOutlook:win32.CDispatch = win32.Dispatch('outlook.application')
        var_clssMail:win32.CDispatch = var_clssOutlook.CreateItem(0) #Criando um item do tipo Email (0)
        
        if(arg_boolHtml):
            var_clssMail.HTMLBody = arg_strCorpoEmail
        else:
            var_clssMail.Body = arg_strCorpoEmail

        var_clssMail.Subject = arg_strAssunto
        var_clssMail.To = arg_strEnvioPara
        if(arg_strCC is not None): var_clssMail.CC = arg_strCC
        if(arg_strBCC is not None): var_clssMail.BCC = arg_strBCC
        
        #Inserindo anexos
        if(arg_listAnexos is not None):
            for var_strAnexo in arg_listAnexos:
                var_clssMail.Attachments.Add(var_strAnexo)

        #Envia o email customizado
        try:
            self.var_clssMaestro.write_log("Enviando email customizado")
            var_clssMail.Send()
            self.var_clssMaestro.write_log("Email enviado com sucesso")
        except Exception:
            self.var_clssMaestro.write_log(arg_strMensagemLog="Erro enviando email customizado: " +str(Exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
            raise
      