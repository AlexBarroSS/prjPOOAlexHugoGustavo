from botcity.plugins.email import BotEmailPlugin
from pathlib import Path
from ExemploWorkshop.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType

ROOT_DIR = Path(__file__).parent.parent.parent.__str__()

class T2CSendEmail:
    """
    Classe responsável pelo envio de email, enviando usuario, senha e qual servidor vai ser usado
    
    Parâmetros:

    Retorna:

    """

    def __init__(self, arg_strNomeProcesso:str, arg_strEmailServerSmtp:str, arg_intEmailPortaSmtp:int, arg_strUsuario:str, arg_strSenha:str, arg_clssMaestro:T2CMaestro):
        """
        Inicializa a classe T2CSendEmail.

        Parâmetros:
        - arg_strNomeProcesso (str): nome do processo.
        - arg_strEmailServerSmtp (str): endereço do servidor SMTP.
        - arg_intEmailPortaSmtp (int): porta do servidor SMTP.
        - arg_strUsuario (str): nome de usuário para autenticação.
        - arg_strSenha (str): senha para autenticação.
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.

        Retorna:

        """
        self.var_strEmailServerSmtp = arg_strEmailServerSmtp
        self.var_intEmailPortaSmtp = arg_intEmailPortaSmtp
        self.var_strUsuario = arg_strUsuario
        self.var_strSenha = arg_strSenha
        self.var_clssMaestro = arg_clssMaestro
        self.var_strNomeProcesso = arg_strNomeProcesso

    
    def send_email_inicial(self, arg_strEnvioPara:str, arg_strCC:str=None, arg_strBCC:str=None):
        """
        Envia o email inicial do robô, apenas precisando informar quem deve receber (separado por ;) e o nome do robô

        Parâmetros:
        - arg_strEnvioPara (str): destinatários separados por ';'.
        - arg_strCC (str): destinatários em cópia separados por ';'. (opcional, default=None)
        - arg_strBCC (str): destinatários em cópia oculta separados por ';'. (opcional, default=None)

        Retorna:

        """

        #Lendo template
        var_fileTemplate = open(ROOT_DIR + "\\resources\\templates\\Email_Inicio.txt", "r")
        var_strEmailTexto = var_fileTemplate.read()
        var_fileTemplate.close()

        var_strEmailTexto = var_strEmailTexto.replace("*NOME_ROBO*", self.var_strNomeProcesso)
        var_strEmailAssunto = "Inicio execução: " + self.var_strNomeProcesso
        
        var_listEnvioPara = arg_strEnvioPara.split(";") if(arg_strEnvioPara is not None) else []
        var_listCC = arg_strCC.split(";") if(arg_strCC is not None) else []
        var_listBCC = arg_strBCC.split(";") if(arg_strBCC is not None) else []

        #Configurando classe do email, separado para emitir logs diferentes
        try:
            self.var_clssMaestro.write_log("Configurando classe de email para envio")
            var_clssEmailController = BotEmailPlugin()
            var_clssEmailController.configure_smtp(self.var_strEmailServerSmtp, self.var_intEmailPortaSmtp)
            var_clssEmailController.login(self.var_strUsuario, self.var_strSenha)
            self.var_clssMaestro.write_log("Email configurado")
        except Exception:
            self.var_clssMaestro.write_log(arg_strMensagemLog="Erro Configurando email: " + str(Exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
            raise

        #Envia o email inicial
        try:
            self.var_clssMaestro.write_log("Enviando email inicial")
            var_clssEmailController.send_message(text_content=var_strEmailTexto, 
                                                 to_addrs=var_listEnvioPara, 
                                                 cc_addrs=var_listCC, 
                                                 bcc_addrs=var_listBCC, 
                                                 use_html=True, 
                                                 subject=var_strEmailAssunto)
            self.var_clssMaestro.write_log("Email enviado com sucesso")
        except Exception:
            self.var_clssMaestro.write_log(arg_strMensagemLog="Erro enviando email inicial: " + str(Exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
            raise
  
    def send_email_final(self, arg_strHorarioInicio:str, arg_strHorarioFim:str, arg_strEnvioPara:str, arg_strCC:str=None, arg_strBCC:str=None, arg_listAnexos:list=None, arg_boolSucesso:bool=True):
        """
        Envio do e-mail de finalização do robô.
        Recebendo o horário do início da execução, o horário final, para quem é necessário enviar (separado por ;) e os relatórios finais
        
        Parâmetros:
        - arg_strHorarioInicio (str): horário de início.
        - arg_strHorarioFim (str): horário de fim.
        - arg_strEnvioPara (str): destinatários separados por ';'.
        - arg_strCC (str): destinatários em cópia separados por ';'. (opcional, default=None)
        - arg_strBCC (str): destinatários em cópia oculta separados por ';'. (opcional, default=None)
        - arg_listAnexos (list): lista de anexos (opcional, default=None).
        - arg_boolSucesso (bool): indica se a execução foi bem-sucedida (opcional, default=True).
        
        Retorna:

        """
        
        #Lendo template
        var_fileTemplate = open(ROOT_DIR + "\\resources\\templates\\Email_Final.txt", "r")
        var_strEmailTexto = var_fileTemplate.read()
        var_fileTemplate.close()

        var_strStatusFinalizacao = "com sucesso" if arg_boolSucesso else "com erros"
        var_strEmailTexto = var_strEmailTexto.replace("*NOME_ROBO*", self.var_strNomeProcesso).replace("*DATAHORA_INI*", arg_strHorarioInicio).replace("*DATAHORA_FIM*", arg_strHorarioFim).replace("*FINALIZACAO*", var_strStatusFinalizacao)
        var_strEmailTexto.replace("*NOME_ROBO*", self.var_strNomeProcesso)
        var_strEmailAssunto = "Finalização da execução: " + self.var_strNomeProcesso

        var_listEnvioPara = arg_strEnvioPara.split(";") if(arg_strEnvioPara is not None) else []
        var_listCC = arg_strCC.split(";") if(arg_strCC is not None) else []
        var_listBCC = arg_strBCC.split(";") if(arg_strBCC is not None) else []

        #Configurando classe do email, separado para emitir logs diferentes
        try:
            self.var_clssMaestro.write_log("Configurando classe de email para envio")
            var_clssEmailController = BotEmailPlugin()
            var_clssEmailController.configure_smtp(self.var_strEmailServerSmtp, self.var_intEmailPortaSmtp)
            var_clssEmailController.login(self.var_strUsuario, self.var_strSenha)
            self.var_clssMaestro.write_log("Email configurado")
        except Exception:
            self.var_clssMaestro.write_log(arg_strMensagemLog="Erro Configurando email: " + str(Exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
            raise
        
        #Envia o email de finalização
        try:
            self.var_clssMaestro.write_log("Enviando email de finalização")
            var_clssEmailController.send_message(text_content=var_strEmailTexto, 
                                                 to_addrs=var_listEnvioPara, 
                                                 cc_addrs=var_listCC, 
                                                 bcc_addrs=var_listBCC, 
                                                 attachments=arg_listAnexos, 
                                                 use_html=True, 
                                                 subject=var_strEmailAssunto)
            self.var_clssMaestro.write_log("Email enviado com sucesso")
        except Exception:
            self.var_clssMaestro.write_log(arg_strMensagemLog="Erro enviando email de finalização: " + str(Exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
            raise

    def send_email_erro(self, arg_strEnvioPara:str, arg_listAnexos:list, arg_strDetalhesErro:str, arg_boolBusiness:bool=False, arg_strCC:str=None, arg_strBCC:str=None):
        """
        Envio do e-mail em casos de erro durante a execução do robô.

        Parâmetros:
        - arg_strEnvioPara (str): destinatários separados por ';'.
        - arg_listAnexos (list): lista de anexos.
        - arg_strDetalhesErro (str): detalhes do erro.
        - arg_boolBusiness (bool): indica se o erro é de regra de negócio. (opcional, default=False)
        - arg_strCC (str): destinatários em cópia separados por ';'. (opcional, default=None)
        - arg_strBCC (str): destinatários em cópia oculta separados por ';'. (opcional, default=None)

        Retorna:

        """
        
        #Lendo template
        var_fileTemplate = open(ROOT_DIR + "\\resources\\templates\\Email_ErroEncontrado.txt", "r")
        var_strEmailTexto = var_fileTemplate.read()
        var_fileTemplate.close()

        var_strEmailTexto = var_strEmailTexto.replace("*NOME_ROBO*", self.var_strNomeProcesso).replace("*ERRO_DETALHES*", arg_strDetalhesErro)
        var_strEmailTexto = var_strEmailTexto.replace("*ERRO_TIPO*", "ERRO DE REGRA DE NEGÓCIO") if arg_boolBusiness else var_strEmailTexto.replace("*ERRO_TIPO*", "ERRO INESPERADO")
        var_strEmailAssunto = "Erro durante a execução: " + self.var_strNomeProcesso
        
        var_listEnvioPara = arg_strEnvioPara.split(";") if(arg_strEnvioPara is not None) else []
        var_listCC = arg_strCC.split(";") if(arg_strCC is not None) else []
        var_listBCC = arg_strBCC.split(";") if(arg_strBCC is not None) else []

        #Configurando classe do email, separado para emitir logs diferentes
        try:
            self.var_clssMaestro.write_log("Configurando classe de email para envio")
            var_clssEmailController = BotEmailPlugin()
            var_clssEmailController.configure_smtp(self.var_strEmailServerSmtp, self.var_intEmailPortaSmtp)
            var_clssEmailController.login(self.var_strUsuario, self.var_strSenha)
            self.var_clssMaestro.write_log("Email configurado")
        except Exception:
            self.var_clssMaestro.write_log("Erro Configurando email:")
            self.var_clssMaestro.write_log(str(Exception))
            raise

        #Envia o email inicial
        try:
            self.var_clssMaestro.write_log("Enviando email de erro")
            var_clssEmailController.send_message(text_content=var_strEmailTexto, 
                                                 to_addrs=var_listEnvioPara, 
                                                 cc_addrs=var_listCC, 
                                                 bcc_addrs=var_listBCC, 
                                                 use_html=True, 
                                                 subject=var_strEmailAssunto,
                                                 attachments=arg_listAnexos)
            self.var_clssMaestro.write_log("Email enviado com sucesso")
        except Exception:
            self.var_clssMaestro.write_log(arg_strMensagemLog="Erro enviando email de erro: " + str(Exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
            raise
     
    def send_email(self, arg_strCorpoEmail:str, arg_strEnvioPara:str, arg_strCC:str, arg_strBCC:str, arg_strAssunto:str, arg_listAnexos:list=None, arg_boolHtml:bool=False):        
        """
        Simplesmente envia um email normal. Pode ser usado em vários lugares no código, porém é necessário informar um corpo para o email 

        Parâmetros:
        - arg_strCorpoEmail (str): corpo do e-mail.
        - arg_strEnvioPara (str): destinatários separados por ';'.
        - arg_strCC (str): destinatários em cópia separados por ';'.
        - arg_strBCC (str): destinatários em cópia oculta separados por ';'
        - arg_strAssunto (str): assunto do e-mail.
        - arg_listAnexos (list): lista de anexos. (opcional, default=None)
        - arg_boolHtml (bool): indica se o corpo do e-mail é HTML. (default=False)

        Retorna:

        """
        var_listEnvioPara = arg_strEnvioPara.split(";") if(arg_strEnvioPara is not None) else []
        var_listCC = arg_strCC.split(";") if(arg_strCC is not None) else []
        var_listBCC = arg_strBCC.split(";") if(arg_strBCC is not None) else []

        #Configurando classe do email, separado para emitir logs diferentes
        try:
            self.var_clssMaestro.write_log("Configurando classe de email para envio")
            var_clssEmailController = BotEmailPlugin()
            var_clssEmailController.configure_smtp(self.var_strEmailServerSmtp, self.var_intEmailPortaSmtp)
            var_clssEmailController.login(self.var_strUsuario, self.var_strSenha)
            self.var_clssMaestro.write_log("Email configurado")
        except Exception:
            self.var_clssMaestro.write_log(arg_strMensagemLog="Erro Configurando email: " + str(Exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
            raise

        #Envia o email customizado
        try:
            self.var_clssMaestro.write_log("Enviando email customizado")
            var_clssEmailController.send_message(text_content=arg_strCorpoEmail, 
                                                 to_addrs=var_listEnvioPara, 
                                                 attachments=arg_listAnexos, 
                                                 use_html=arg_boolHtml, 
                                                 subject=arg_strAssunto)
            self.var_clssMaestro.write_log("Email enviado com sucesso")
        except Exception:
            self.var_clssMaestro.write_log(arg_strMensagemLog="Erro enviando email customizado", arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)
            raise
        

