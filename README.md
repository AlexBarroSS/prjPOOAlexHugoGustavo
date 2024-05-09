# botcity_framework_t2c

Framework used by T2C to help develop automations in BotCity

## PATCH NOTES

### 06/02/2023:
- Adicionado novo método, init_new_task() na classe T2CMaestro, permite iniciar uma nova task no maestro informando a label de uma automação, possibilitando assim chamar outros robôs depois do fim de um primeiro.

### 07/02/2023:
- Consertado bug nos métodos de envio de email de erro, onde os detalhes da exceção não eram inseridos no corpo do email.

### 13/02/2023:
- Envio de email agora respeita o arquivo config.xlsx.
- Movendo contadores de lugar para contar todas as tentativas e exceções no processamento.
- Adicionado parâmetro no config.xlsx para envio do email inicial.

### 14/02/2023:
- Alterado um replace na classe SQLiteQueue para tirar aspas simples antes de updates.
- Trocando ordem de inicialização de classes no começo para iniciar a classe de sqlite antes para casos onde é necessário subir uma fila no init.

### 15/02/2023:
- Alterado nome da máquina para pegar uma propriedade da classe Maestro. Será o nome do runner em casos onde está rodando pelo maestro, ou o nome da máquina quando rodando local.

### 23/02/2023:
- Erro nas classes de email, mais especificamente no send_email_erro consertados. Antes usavam o template errado ou simplesmente erravam o nome do template, resultando erro.

### 06/03/2023:
- Config agora fica em uma pasta separada para evitar que ele fique jogado no meio de várias imagens usadas pelo robô.
- Erros no envio de email (smtp) consertados.
- Bug simples consertado no InitAllSettings, o que fazia com que itens a mais fossem colocados no dicionário.
- bot.py atualizado, limpando algumas coisas.
- __Relatórios sintético e analítico agora acumulam registros.__
  - Para acomodar essa mudança, o Config foi atualizado e agora usuários são obrigados a fornecer uma pasta para salvar os relatórios __fora do projeto__.
  - Antiga pasta de saída foi excluída.

### 17/04/2023:
- Fixes em relatórios, colocando um close() para fechar o arquivo. Segundo a documentação, não era necessário, mas não ta atrapalhando, então deixei lá.
- __Logs modificados:__
  - Campo de datahora removido, porque tinha redundância com o campo já inserido do Maestro.
  - Campo de referência e level do log adicionados, write_log() tem esses parâmetros opcionais.
  - LogLevel é uma classe enum, com INFO, WARN, ERROR, FATAL.
- __Conexão com o Maestro modificada__, agora necessário fornecer server, login e key no arquivo config.xlsx, na aba propriedades. Essa mudança permite acessar features do Maestro mesmo rodando pelo vs code.
- Suporte para credenciais, dependente das mudanças feitas acima. Nova aba de credenciais no config.xlsx.
- Método para subir fila adicionado no InitAllApplications, não conectado por default.

### 18/04/2023:
- O framework usa agora um pacote para instalar a versão mais nova de um webdriver. Linhas comentadas no bot.py.

### 26/04/2023:
- Novo método para pegar credenciais, leva em conta que a label vai ser sempre o nome do projeto, então leve isso em conta ao adicionar credenciais no Maestro.
- __Nova classe para inserir dados no banco RAAS, tabelas analítico e sintético:__
  - Não é obrigatório, controlado por um campo no config.
  - Necessário colocar os dados de conexão do banco no config.xlsx, na aba Constants.
  - Descrição do projeto também adicionado no config.xlsx, campo necessário no banco.
- Fix para ModuleNotFound introduzido na atualização passada.

### 09/05/2023:
- Incluindo Arquivo .github/workflows/push_clone.yaml para ser possível utilizar o GitHub Actions.
  - No Arquivo contém os passos para toda vez que a branch Main sofrer um push, ele automaticamente faça um push no reposítório do Cookiecutter mantendo o mesmo atualizado.
- Inserindo Arquivo .github/workflows/replace.yaml  no reposítório do cookiecutter para ser possível utilizar o GitHub Actions. 
  - No Arquivo contém os passos para fazer todos os replaces necessários para que seja possível utilizar o cookiecutter (que cria uma cópia do nosso reframework com os nomes já configurados para o nome do projeto)

### 19/05/2023:
- Incluindo no T2CProcess.py os comentários das funções

### 15/06/2023
- Novo método para acionar a interrupção da execução pelo Maestro.
- __logs adicionados:__
  - Campo de ErrorType adicionado, write_log() tem esses parâmetros opcionais.
  - ErrorType é uma classe enum, com NONE, APPLICATION e BUSINESS.

### 26/06/2023
- Adicionado lógica MaxConsecutiveExceptions.
  - Editar a quantidade de Exceções Consecutivas no arquivo Config.xlsx, na aba Constants.
- __Nova classe para gravar a execuçao do robô:__
  - Não é obrigatório, controlado por um campo no config.
  - Necessário colocar o caminho onde o video será salvo.

### 06/07/2023
- Incluindo comentários nas classes e métodos.

### 16/08/2023
- Atualizações na classe Maestro, variável indicando se a task foi iniciada marcada como teste (debug).
- Alterações para apenas enviar dados para o SQL Server em casos onde não esteja debugando (vs code ou como task teste).
- Fix no InitAllApplications.
- Fix no .botproj, o que impedia o projeto de abrir pelo BotStudio.

### 31/08/2023
- Atualizações no bot.py, removido inserção duplicada na primeira linha do sintético.
- Alterado onde é realizado a chamada dos prints, businessException e Exception no Process, para que tire o print antes do killprocess.

### 06/09/2023
- Inserido os comentários no padrão que o gerador de SDD é capaz de gerar o documento.

### 09/11/2023
- Inserido configurações para utilizar o clicknium e funcionar no maestro
  - Atualizado informações no setup.py
  - Atualizado informações no bot.py
  - Atualizado informações no Manifest.in
  - Atualizado informações no requirements.txt
  - Atualizado informações no .gitignore
