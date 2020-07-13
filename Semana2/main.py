#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


black_friday.columns


# In[4]:


black_friday.head(10)


# In[5]:


black_friday.isnull().sum()


# In[6]:


black_friday.info()


# In[7]:


aux = pd.DataFrame({'colunas': black_friday.columns,
                    'tipos': black_friday.dtypes,
                    'percentual_faltante': black_friday.isna().sum() / black_friday.shape[0]})
aux


# In[8]:


black_friday[["Product_Category_1","Product_Category_2","Product_Category_3"]].describe()


# In[9]:


valores_null =  black_friday.isna().sum() / len(black_friday)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[10]:


def q1():
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[11]:


def q2():
    mulheres = len(black_friday[(black_friday['Gender'] == 'F') & (black_friday['Age'] == '26-35')])
    return mulheres


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[12]:


def q3():
    return black_friday["User_ID"].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[13]:


def q4():
    dados = black_friday.dtypes.nunique()
    return dados


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[14]:


def q5():
    valores_null = black_friday.isna().any(axis=1).sum() / len(black_friday)
    return valores_null


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[15]:


def q6():
    max_null = black_friday.isna().sum().max()
    return max_null


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[16]:


def q7():
    frequencia =  float(black_friday["Product_Category_3"].mode())
    return frequencia


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[17]:


def q8():
    media = ((black_friday['Purchase'] - black_friday['Purchase'].min())/ 
    (black_friday['Purchase'].max()-black_friday['Purchase'].min())).mean()
    return media


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[18]:


def q9():
    padroniza = black_friday["Purchase"]
    std_padroniza = (padroniza - padroniza.mean()) / (padroniza.std())
    cont = 0
    for valor in range (len(std_padroniza)):
        if (std_padroniza[valor] <= 1) and (std_padroniza[valor] >= -1):
            cont = cont + 1
    return cont


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[19]:


def q10():
    aux = black_friday[black_friday['Product_Category_2'].isnull()]
    return bool(aux['Product_Category_2'].sum() == aux['Product_Category_3'].sum())


# In[20]:


q1()


# In[25]:


q2()


# In[21]:


q4()


# In[22]:


q5()


# In[23]:


q7()


# In[24]:


q9()

