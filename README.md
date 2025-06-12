### 1. Instale o PIP e o VENV

Primeiro, vamos garantir que você tenha o `pip` (gerenciador de pacotes do Python) e o `venv` (para criar ambientes virtuais). Abra seu terminal (Ctrl+Alt+T) e execute o seguinte comando:

```bash
sudo apt update && sudo apt install python3-pip python3-venv -y
```

### 2. Crie a Pasta do Projeto e o Ambiente Virtual

Agora, crie uma pasta para o seu projeto e entre nela. Em seguida, crie um ambiente virtual.

```bash
# Crie e acesse a pasta do seu projeto (substitua 'meuprojeto' pelo nome que desejar)
mkdir meuprojeto
cd meuprojeto

# Crie o ambiente virtual (chamado 'venv' por convenção)
python3 -m venv venv
```

### 3. Ative o Ambiente Virtual

Para que os pacotes que você instalar fiquem isolados neste projeto, você precisa "ativar" o ambiente virtual.

```bash
source venv/bin/activate
```

Você saberá que funcionou, pois o nome do seu terminal mudará para exibir `(venv)` no início da linha.

**(Lembre-se: toda vez que for trabalhar no projeto, você precisará entrar na pasta e executar este comando de ativação.)**

### 4. Instale o Django

Com o ambiente virtual ativo, use o `pip` para instalar o Django.

```bash
pip install django
```

### 5. Crie o Projeto Django

Agora, use o comando do Django para criar a estrutura inicial do seu site.

```bash
# O ponto no final indica para criar na pasta atual
django-admin startproject config .
```

* **Por que `config .`?** Usamos `config` como o nome do diretório principal de configurações (é uma prática comum) e o `.` para dizer ao Django para criar os arquivos na pasta atual (`meuprojeto`), evitando um nível extra de diretórios.

### 6. Rode o Servidor de Teste

Seu projeto já está criado! Vamos testá-lo. Primeiro, aplique as migrações iniciais do banco de dados (o Django já vem com um SQLite pronto para usar).

```bash
python manage.py migrate
```

Agora, inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

### 7. Verifique no Navegador

Abra seu navegador e acesse o endereço `http://127.0.0.1:8000/`.

Você deverá ver a página de boas-vindas do Django. 🚀

