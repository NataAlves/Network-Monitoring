# Network Monitor 

Sistema de monitoramento de rede desenvolvido em Python para detecção e comparação de dispositivos conectados em uma rede local, com armazenamento de dados em banco de dados (MariaDB/MySQL) e análise de mudanças entre varreduras.

---

## Visão Geral

O **Network Monitor** realiza varreduras na rede local, identifica dispositivos conectados e registra essas informações em um banco de dados. O sistema também compara varreduras anteriores e atuais para detectar:

- Novos dispositivos conectados
- Dispositivos removidos
- Mudanças no ambiente de rede

Ideal para estudos de **DevOps, redes e automação com Python**.

---

##  Funcionalidades

-  Varredura de dispositivos na rede local
-  Armazenamento de dados em banco de dados (MariaDB/MySQL)
-  Comparação entre estados da rede (current vs new)
-  Persistência de dados em arquivos JSON
-  Estrutura modular para fácil manutenção e expansão
-  Uso de variáveis de ambiente (.env) para segurança

---

## Tecnologias Utilizadas

- Python 3.x
- MariaDB / MySQL
- Nmap (ou biblioteca equivalente, se utilizada)
- JSON para armazenamento local
- dotenv (.env)
- SQL para persistência de dados

---

## Como Executar o Projeto: 

1. Clone o repositório
git clone https://github.com/seu-usuario/network_monitor.git
cd network_monitor

2. Crie e Ative um Ambiente Virtual
python -m venv venv
venv\Scripts\activate

3. Instale dependencias
pip install -r requirements.txt


4. Configure as variáveis de ambiente
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=network_monitor

5. Execute o arquivo main.py


Como Funciona
O sistema realiza uma varredura na rede local
Os dispositivos encontrados são armazenados em JSON e no banco de dados
O sistema compara a varredura atual com a anterior
Diferenças são identificadas (novos ou removidos dispositivos)
Os dados são atualizados para a próxima execução


Objetivo do Projeto

Este projeto foi desenvolvido com foco em aprendizado prático nas áreas de:

-Redes de computadores
-Automação com Python
-Integração com banco de dados
-Boas práticas de organização de projetos
-Conceitos de DevOps iniciais

Segurança
-Credenciais de banco são armazenadas em .env
-Arquivos sensíveis são ignorados via .gitignore


POSSIVEIS MELHORIAS FUTURAS

-Interface web para visualização dos dispositivos
-Dashboard com gráficos
-Notificações (email/telegram) ao detectar novos dispositivos
-API REST com FastAPI
-Dockerização do sistema
-Execução agendada (cron / scheduler)