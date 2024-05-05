# código de geração do gráfico 
import pandas as pd
import seaborn as sns

dados = pd.read_csv('gasolina.csv')

with sns.axes_style('ticks'):
  grafico = sns.lineplot(data=dados, x='dia', y='venda')
  grafico.set(title='Vendas da gasolina na cidade de São Paulo',xlabel='Dia', ylabel='Preço (médio)')* Insights:

* Insight:
  
Com a visualização do gráfico, podemos analisar que nesta temporada, entre os dias 2 e 9, não há muitas vendas, provavelmente por não ser dia de pagamento na maioria das empresas. Já nos dias 4, 5, 6, 7 e 8 as vendas já começam a aumentar, sendo o dia 4 o melhor dia de vendas.


