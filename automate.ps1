# Cria um ambiente virtual do Python
python -m venv venv

# Ativa o ambiente virtual
& ".\venv\Scripts\Activate.ps1"

# Instala o Flask no ambiente virtual
pip install flask
pip install bcrypt

Write-Output "Ambiente virtual criado e Flask instalado com sucesso!"