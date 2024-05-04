# código de geração do gráfico 
import pandas as pd
import seaborn as sns

dados = pd.read_csv('gasolina.csv')

with sns.axes_style('ticks'):
  grafico = sns.lineplot(data=dados, x='dia', y='venda')
  grafico.set(title='Vendas da gasolina na cidade de São Paulo',xlabel='Dia', ylabel='Preço (médio)')