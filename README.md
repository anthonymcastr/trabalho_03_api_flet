
# CK Informática – Sistema de Controle de Estoque

Sistema completo de controle de estoque para uma loja de informática, com API e interface visual desenvolvida em Flet e backend em Python. O projeto permite o cadastro de produtos, geração de gráficos de marca e preço, além de interface amigável para usuários.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x  
- Flet  
- JSON Server (API fake)  
- Matplotlib  
- Git  

---

## 📦 Estrutura do Projeto

```
ck_informatica/
  - ck_informatica.py                  # Interface principal da aplicação
  - telas/
    - cad_produtos.py                  # Tela de cadastro de produtos
    - graf_caros.py                    # Gráfico dos produtos mais caros
    - graf_marcas.py                   # Gráfico de quantidade por marca

api_loja_ck/
  - db.json                            # Banco de dados fake (JSON Server)
  - server.py                          # Código da API (mock)
  - README.md                          # Documentação original
```

---

## 🧪 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/ck-informatica.git
cd ck-informatica
```

### 2. (Opcional) Criar ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Instalar dependências
```bash
pip install flet matplotlib
```

### 4. Iniciar a API local 
```
npx json-server db.json
```

### 5. Executar a aplicação
```
python ck_informatica/ck_informatica.py
```

---

## 📊 Funcionalidades

- Cadastro de produtos com nome, marca, preço, modelo, etc.  
- Geração de gráficos por marca e por produtos mais caros  
- API simulada com JSON Server  
- Interface gráfica com Flet  

---

## ⚠️ Observações

Este projeto é demonstrativo e utiliza uma API fake via JSON Server. Pode ser facilmente adaptado para usar um banco de dados real, como SQLite ou PostgreSQL.

---

## 👨‍💻 Autor

Desenvolvido por Anthony Martins de Castro  
Atividade 03 (Algoritmos e Estruturas de Dados 1) UNISENAC – Sistema de Controle de Estoque

