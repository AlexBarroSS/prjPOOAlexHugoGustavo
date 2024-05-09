from botcity.core import DesktopBot
from ExemploWorkshop.classes_t2c.utils.T2CMaestro import T2CMaestro
from botcity.plugins.recorder import BotRecorderPlugin
import time

class T2CScreenRecorder(DesktopBot):
    """
    Classe responsável por gravar a tela do processo.
    """
    def __init__(self, arg_strNomeProcesso, arg_clssMaestro:T2CMaestro, arg_dictConfig:dict):
        """
        Inicializa a classe T2CScreenRecorder.

        Parâmetros:
             - arg_strNomeProcesso(str): Nome do projeto setado no arquivo config.
             - arg_dictConfig(dict): Dicionário de configuração do framework.
             - arg_clssMaestro(T2CMaestro): Instância de T2CMaestro.
        
        Retorna:
        """
        self.var_clssMaestro = arg_clssMaestro
        self.var_strCaminhoCompleto = arg_dictConfig["CaminhoSalvarVideo"] + arg_strNomeProcesso + ".avi"
        self.var_brpGravador = BotRecorderPlugin(self, self.var_strCaminhoCompleto)
    
    def iniciar_gravacao(self):
        """
        Inicia a gravação de tela do processo.

        Parâmetros:
    
        Retorna:
        """
        self.var_clssMaestro.write_log("Iniciando Gravador de Tela...")
        self.var_brpGravador.start()
        time.sleep(5)

    def finalizar_gravacao(self):
        """
        Finaliza a gravação de tela do processo.
        
        Parâmetros:
    
        Retorna:        
        """
        self.var_clssMaestro.write_log("Finalizando Gravador de Tela...")
        self.var_brpGravador.stop()
        time.sleep(5)