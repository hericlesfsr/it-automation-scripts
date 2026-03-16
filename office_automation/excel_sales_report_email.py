"""
Excel Sales Report Automation

Reads sales data from Excel, calculates metrics, 
and automatically sends a formatted report via Outlook email.

Technologies:
- Python
- Pandas
- PyWin32 (Outlook integration)
"""

import pandas as pd # pip install pandas
import win32com.client as win32

# --- FUNÇÃO DE FORMATAÇÃO ---
def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
# ----------------------------

print("\n=== RELATÓRIO AUTOMÁTICO DE VENDAS ===\n")

# importar a base de dados
tabela_vendas = pd.read_excel('vendas.xlsx')
print('-' * 50)

# visualizar a base de dados 
pd.set_option('display.max_columns', None) # mostrar o máximo de colunas - não ocultar x,y
print(tabela_vendas)
print('-' * 50)


# faturamento por loja
# filtrar loja e valor final -> tabela_vendas[['ID Loja', 'Valor Final']]
# agrupando e calculando o faturamento por loja -> tabela_vendas.groupby('ID Loja').sum()
# somente a loja e faturamento por loja -> tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja).sum()
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum().reset_index()
print(faturamento)
print('-' * 50)


# quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum().reset_index()
print(quantidade)
print('-' * 50)


# ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
# Insere a coluna ID Loja na primeira posição para não perder a referência
ticket_medio.insert(0, 'ID Loja', faturamento['ID Loja'])
print(ticket_medio)


# enviar um email com o relatório -> pip install pywin32
outlook = win32.Dispatch('outlook.application')     # realiza a conexão do python com o outlook 
mail = outlook.CreateItem(0)        # cria um email
mail.To = 'hericles.silva100@gmail.com'      # inserir o destinatário
mail.Subject = 'Relatório de Vendas por Loja'        # assunto do email

# --- GERAÇÃO DAS TABELAS HTML ---
# index=False remove a coluna de números (0, 1, 2...)
faturamento_table = faturamento.to_html(formatters={'Valor Final': formatar_real}, justify='center', index=False)
quantidade_table = quantidade.to_html(justify='center', index=False)
ticket_table = ticket_medio.to_html(formatters={'Ticket Médio': formatar_real}, justify='center', index=False)

mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada loja.</p>

<p>Faturamento:</p>
{faturamento_table}

<p>Quantidade vendida:</p>
{quantidade_table}

<p>Ticket Médio dos produtos em cada loja:</p>
{ticket_table}

<p>Qualquer dúvida estarei à disposição.</p>

<p>At.te,</p>
<p>Héricles Rozendo.</p>
'''
#mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

# To attach a file to the email (optional):
# attachment  = "Path to the attachment"
# mail.Attachments.Add(attachment)

mail.Send()

print('Email enviado com sucesso')
