##############################    ESTRUTURA DO PROJETO     ##############################    


EducMais/                     # Diretório principal do projeto
│
├── EducMais/                 # Aplicação principal do projeto
│   ├── __pycache__/          # Diretório gerado automaticamente com os arquivos compilados do Python
│   ├── migrations/           # Migrations do banco de dados
│   ├── static/               # Arquivos estáticos (CSS, imagens)
│   │   ├── css/
│   │   │   └── style.css     # Arquivo CSS principal
│   │   ├── img/              # Imagens usadas no sistema
│   │   │   ├── avatar-1.png
│   │   │   ├── Caderneta.png
│   │   │   ├── home.png
│   │   │   ├── Menu.png
│   │   │   ├── planlab_logo_branco_p.png
│   │   │   └── planlab_logo_principal_p.png
│   │   └── Plano.png
│   ├── templates/            # Templates HTML do projeto
│   │   ├── caderneta.html    # Template para visualização das cadernetas
│   │   ├── form_aula.html    # Formulário para criação/edição de planos de aula
│   │   ├── form_caderneta.html # Formulário para criação/edição de cadernetas
│   │   ├── form_editar_aula.html # Formulário para edição de plano de aula
│   │   ├── form_editar_caderneta.html # Formulário para edição de cadernetas
│   │   ├── home.html         # Página inicial
│   │   ├── login.html        # Tela de login
│   │   ├── pag_cadernetas.html # Página que lista as cadernetas
│   │   ├── pag_planos_de_aula.html # Página que lista os planos de aula
│   │   └── plano.html        # Página para visualização dos planos de aula
│   ├── __init__.py           # Arquivo para indicar que este diretório é um pacote Python
│   ├── admin.py              # Configurações do admin do Django
│   ├── apps.py               # Configurações do aplicativo
│   ├── backends.py           # Lógica customizada de backends
│   ├── forms.py              # Formulários utilizados nas views
│   ├── models.py             # Definições das entidades e relações do banco de dados
│   ├── tests.py              # Testes do aplicativo
│   ├── urls.py               # Definições de URLs para o aplicativo
│   └── views.py              # Views que controlam a lógica de negócios
│
├── EducMaisRevolution/       # Diretório com as configurações do projeto
│   ├── __pycache__/          # Arquivo compilado
│   ├── __init__.py           # Indica que o diretório é um pacote Python
│   ├── asgi.py               # Arquivo de configuração ASGI
│   ├── settings.py           # Configurações principais do Django
│   ├── urls.py               # URLs principais do projeto
│   └── wsgi.py               # Arquivo de configuração WSGI
│
├── venv/                     # Ambiente virtual do Python
│   ├── .gitignore            # Arquivo para ignorar arquivos do Git
│   ├── manage.py             # Script para gerenciar o projeto
│   └── requirements.txt      # Arquivo com dependências do projeto


##############################    MODELS     ##############################    

Disciplina
    + Descrição: Este modelo representa uma disciplina acadêmica.
    + Campos:
        * nome: Nome da disciplina (máximo de 100 caracteres).

                ┌──────────────────────────────────────────────────┐
                │ python                                           |
                │                                                  |
                │ class Disciplina(models.Model):                  |
                │   nome = models.CharField(max_length=100)        |
                └──────────────────────────────────────────────────┘

Turma
    + Descrição: Representa uma turma de alunos.
    + Campos:
        * nome: Nome da turma (máximo de 100 caracteres).

                ┌──────────────────────────────────────────────────┐
                | python                                           |
                |                                                  |
                |class Turma(models.Model):                        |
                |   nome = models.CharField(max_length=100)        |
                └──────────────────────────────────────────────────┘

Semestre
    + Descrição: Este modelo representa o semestre acadêmico.
    + Campos:
        * descricao: Descrição do semestre (máximo de 50 caracteres).

                ┌──────────────────────────────────────────────────┐
                | python                                           |
                |                                                  |
                |class Semestre(models.Model):                     |
                |   descricao = models.CharField(max_length=50)    |
                └──────────────────────────────────────────────────┘

Aula
    + Descrição: Representa uma aula de uma disciplina em um semestre específico, dada em uma turma por um usuário (professor).
    + Relacionamentos:
        * disciplina: Relacionamento com a disciplina da aula.
        * turma: Relacionamento com a turma da aula.
        * semestre: Relacionamento com o semestre da aula.
        * usuario: Relacionamento com o usuário (professor).
    + Campos:
        * data_aula: Data da aula.
        * titulo: Título da aula (máximo de 200 caracteres).
        * eventos_extraordinarios: Eventos extraordinários ocorridos durante a aula.
        * conteudo_programatico: Conteúdo programático da aula.
        * metodologia: Metodologia de ensino utilizada.
        * recursos_necessarios: Recursos necessários para a aula.
        * avaliacao_observacoes: Avaliação e observações feitas sobre a aula.
        * observacoes: Outras observações relacionadas à aula.

        ┌───────────────────────────────────────────────────────────────────────────────────────┐
        | class Aula(models.Model):                                                             |
        |  disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)                 |
        |  turma = models.ForeignKey(Turma, on_delete=models.CASCADE)                           |
        |  semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)                     |
        |  usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')  |
        |  data_aula = models.DateField(verbose_name='Data da Aula')                            |
        |  titulo = models.CharField(max_length=200, verbose_name='Título')                     |
        |  eventos_extraordinarios = models.CharField(                                          |
        |    max_length=255, blank=True, null=True, verbose_name='Eventos Extraordinários'      |
        |  )                                                                                    |
        |  conteudo_programatico = models.TextField(verbose_name='Conteúdo Programático')       |
        |  metodologia = models.TextField(verbose_name='Metodologia')                           |
        |  recursos_necessarios = models.TextField(verbose_name='Recursos Necessários')         |
        |  avaliacao_observacoes = models.TextField(                                            |
        |    blank=True, null=True, verbose_name='Avaliação e Observações'                      |
        |  )                                                                                    |
        |  observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')    |
        └───────────────────────────────────────────────────────────────────────────────────────┘

        