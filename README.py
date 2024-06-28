#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `unrar` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `unrar` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/using the `unrar` on `Linux Ubuntu`._

# ## Revisão(ões)/Versão(ões)

# | Revisão número | Data da revisão | Descrição da revisão                                    | Autor da revisão                                |
# |:--------------:|:---------------:|:--------------------------------------------------------|:------------------------------------------------|
# | 0              | 02/04/2024      | <ul><li>Revisão inicial/criação do documento.</li></ul> | <ul><li>Eden Denis F. da S. L. Santos</li></ul> |
# 

# ## Descrição [2]
# 
# ### `unrar`
# 
# O UnRAR é uma ferramenta de linha de comando usada para extrair e descompactar arquivos no formato RAR. Ele permite aos usuários extrair arquivos de arquivos RAR, bem como visualizar e listar o conteúdo desses arquivos. O UnRAR é uma versão gratuita e de código aberto do utilitário de descompactação para o formato proprietário RAR, permitindo que os usuários acessem o conteúdo desses arquivos sem depender de software comercial. É amplamente utilizado em sistemas Unix e Linux devido à sua facilidade de uso e eficiência na extração de arquivos RAR.
# 

# ## 1. Como configurar/instalar/usar o `unrar` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `unrar` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# Para extrair um arquivo `.rar` no `Linux Ubuntu`, você pode usar o `unrar`, que é uma ferramenta disponível através do terminal. Se o `unrar` não estiver instalado no seu sistema, você precisará instalá-lo primeiro. Siga os passos abaixo:
# 
# 3. **Instale o `unrar` com o comando:** `sudo apt install unrar -y`
# 
# 4. **Após a instalação, você pode extrair o arquivo `.rar` usando:** `unrar x caminho/para/seu/arquivo.rar`
# 
#     Substitua `caminho/para/seu/arquivo.rar` pelo caminho real do seu arquivo `.rar`.
# 
# O comando `unrar x` extrai os arquivos mantendo a estrutura de diretórios completa. Existem outras opções que você pode usar com `unrar`, como:
# 
# - **`unrar l caminho/para/seu/arquivo.rar:`** Lista o conteúdo de um arquivo `.rar` sem extrair.
# 
# - **`unrar e caminho/para/seu/arquivo.rar:`** Extrai os arquivos sem manter a estrutura de diretórios.
# 
# Selecione a opção que melhor atende às suas necessidades.

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `unrar` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean -y
#     sudo apt autoremove -y
#     sudo apt update -y
#     sudo apt uptoremove -y
#     sudo apt autoclean -y
#     sudo apt install unrar -y
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Extrair arquivo .rar Linux.*** Disponível em: <https://chat.openai.com/c/b315251f-5bf4-48bb-8c0b-d306db412439> (texto adaptado). Acessado em: 02/04/2023 17:11.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 02/04/2024 17:10.
# 
