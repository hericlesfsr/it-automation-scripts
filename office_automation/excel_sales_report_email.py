"""
Sales Report Automation

Reads sales data from Excel, calculates store performance metrics,
and automatically sends a formatted report via Outlook email.

Technologies:
- Python
- Pandas
- PyWin32 (Outlook integration)
"""

import pandas as pd
import win32com.client as win32
from datetime import datetime
data = datetime.now().strftime("%d/%m/%Y")

# --- FUNÇÃO DE FORMATAÇÃO (REAL BRASILEIRO) ---
def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
# ---------------------------------------------


print("\n=== RELATÓRIO AUTOMÁTICO DE VENDAS ===\n")

# importar a base de dados
tabela_vendas = pd.read_excel("ARQUIVO_EXCEL.xlsx")

print("-" * 50)

# visualizar a base de dados
pd.set_option("display.max_columns", None)
print(tabela_vendas.head())

print("-" * 50)

# -----------------------------
# FATURAMENTO POR LOJA
# -----------------------------
faturamento = (
    tabela_vendas[["ID Loja", "Valor Final"]]
    .groupby("ID Loja")
    .sum()
    .reset_index()
)

print("Faturamento por loja:")
print(faturamento)

print("-" * 50)

# -----------------------------
# QUANTIDADE DE PRODUTOS VENDIDOS
# -----------------------------
quantidade = (
    tabela_vendas[["ID Loja", "Quantidade"]]
    .groupby("ID Loja")
    .sum()
    .reset_index()
)

print("Quantidade vendida por loja:")
print(quantidade)

print("-" * 50)

# -----------------------------
# TICKET MÉDIO
# -----------------------------
ticket_medio = (faturamento["Valor Final"] / quantidade["Quantidade"]).to_frame()

ticket_medio = ticket_medio.rename(columns={0: "Ticket Médio"})

ticket_medio.insert(0, "ID Loja", faturamento["ID Loja"])

print("Ticket médio por loja:")
print(ticket_medio)

print("-" * 50)

# -----------------------------
# CONEXÃO COM OUTLOOK
# -----------------------------
outlook = win32.Dispatch("outlook.application")

mail = outlook.CreateItem(0)

mail.To = "seu_email@gmail.com"
mail.Subject = f"Relatório de Vendas - {data}"


# -----------------------------
# GERANDO TABELAS HTML
# -----------------------------
faturamento_table = faturamento.to_html(
    formatters={"Valor Final": formatar_real},
    justify="center",
    index=False
)

quantidade_table = quantidade.to_html(
    justify="center",
    index=False
)

ticket_table = ticket_medio.to_html(
    formatters={"Ticket Médio": formatar_real},
    justify="center",
    index=False
)


# -----------------------------
# CORPO DO EMAIL
# -----------------------------
mail.HTMLBody = f"""
<p>Prezados,</p>

<p>Segue o relatório automático de vendas por loja.</p>

<h3>Faturamento por Loja</h3>
{faturamento_table}

<h3>Quantidade de Produtos Vendidos</h3>
{quantidade_table}

<h3>Ticket Médio por Loja</h3>
{ticket_table}

<p>Qualquer dúvida estou à disposição.</p>

<p>At.te,<br>
Héricles Rozendo</p>
"""

# enviar email
mail.Send()

print("Email enviado com sucesso!")
