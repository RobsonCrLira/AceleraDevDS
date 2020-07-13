import pandas as pd
import streamlit as st

'''

https://raw.githubusercontent.com/codenation-dev/Data-Science-Online/master/Semana%203/houses_to_rent_v2.csv
url PARA SER ANALIZADA
'''
def Analisafile(file):
    if file is not None:
        dffile = Analisafile(file)
        st.markdown("Numero de linhas e Colunas")
        st.markdown(f"Quantidade de linhas e {dffile.shape[-1]}, e quatiadade de colunas e {dffile.shape[1]}")
        st.markdown("***Visualizacao das colunas***")
    st.subheader("Analizando os dados")
    arq = pd.read_csv(file)
    return arq


def main():
    st.title('Vamos comecar')
    url = st.text_input('Digite a URL')

    if st.button("Analisar"):
        st.subheader("Analizando os dados")
        dfurl = pd.read_csv(url)
        st.markdown("Numero de linhas e Colunas")
        st.markdown(f"Quantidade de linhas e {dfurl.shape[0]}, e quatiadade de colunas e {dfurl.shape[1]}")
        st.markdown("***Visualizacao das colunas***")
        qnt_linhas2 = st.slider("Escolha a quantidade de linhas que deseja ver", min_value=1, max_value=20)
        st.dataframe(dfurl.head(qnt_linhas2))


if __name__ == "__main__":
    main()