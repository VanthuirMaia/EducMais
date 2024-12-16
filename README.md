EducMais
EducMais é uma plataforma educacional desenvolvida com o objetivo de gerenciar planos de aula, cadernetas e turmas de forma eficiente e intuitiva. A plataforma visa facilitar o acompanhamento das atividades pedagógicas, oferecendo ferramentas para que professores possam planejar e registrar suas aulas com facilidade, e para administradores gerenciarem os dados do sistema.

Descrição
Este repositório contém o código-fonte do EducMais, uma aplicação web construída com Django, MySQL e tecnologias modernas para garantir um bom desempenho e uma interface intuitiva.

Funcionalidades
Login de Usuários: Sistema de autenticação para professores e administradores.
Gestão de Planos de Aula: Criação, edição, visualização e exclusão de planos de aula.
Gestão de Cadernetas de Aula: Registro de atividades realizadas durante as aulas, observações sobre os alunos e o desempenho.
Controle de Acessos e Permissões: Diferenciação de permissões entre administradores e usuários (professores).
Tecnologias Utilizadas
Django: Framework web de alto nível que facilita o desenvolvimento rápido e seguro.
HTML, CSS e JavaScript: Tecnologias para desenvolvimento da interface do usuário.
MySQL: Sistema de gerenciamento de banco de dados utilizado para armazenar os dados da plataforma.
Python: Linguagem de programação principal usada para o desenvolvimento da lógica do sistema.
Como Executar o Projeto
Pré-requisitos
Python 3.x
Django 4.x
MySQL (ou outro banco de dados compatível)
Passos para Execução
Clone o repositório:


git clone https://github.com/VanthuirMaia/EducMais.git
Acesse o diretório do projeto:


cd EducMais
Instale as dependências:


pip install -r requirements.txt
Configure as variáveis de ambiente para conectar ao banco de dados (MySQL).

Execute as migrações do banco de dados:


python manage.py migrate
Crie um superusuário para acessar a interface administrativa:


python manage.py createsuperuser
Execute o servidor de desenvolvimento:


python manage.py runserver
Acesse o sistema através do endereço http://127.0.0.1:8000/.

Estrutura do Banco de Dados
O sistema é baseado em vários modelos de dados principais, como:

Usuário: Armazena as credenciais e perfis dos usuários.
Plano de Aula: Contém os dados relacionados aos planos de aula, como data, turma, conteúdo, etc.
Caderneta de Aula: Registra informações sobre o desempenho dos alunos durante as aulas.
Turma: Contém as informações sobre as turmas de alunos.
Disciplina: Define as disciplinas associadas às turmas e planos de aula.
Possíveis Melhorias
Expansão do sistema para integração com plataformas externas.
Implementação de relatórios e funcionalidades de análise de dados.
Criação de uma API para integração com outras ferramentas educacionais.
Licença
Este projeto está licenciado sob a MIT License.