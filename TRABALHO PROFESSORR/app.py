import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================
# CONFIGURAÇÃO DA PÁGINA
# ==========================
st.set_page_config(
    page_title="Portfólio - Mineração de Dados",
    page_icon="📊",
    layout="wide"
)

# ==========================
# CARREGAMENTO DOS DADOS
# ==========================
@st.cache_data
def carregar_dados():
    return pd.read_csv("netflix_titles.csv")

df = carregar_dados()

# ==========================
# MENU LATERAL
# ==========================
st.sidebar.title("📊 Menu")

pagina = st.sidebar.radio(
    "Navegação",
    [
        "Início",
        "Visão Geral",
        "Análises",
        "Insights",
        "Sobre"
    ]
)

# ==========================
# INÍCIO
# ==========================
if pagina == "Início":

    st.title("📊 Portfólio de Analista Júnior em Mineração de Dados")

    st.markdown("""
    ### Objetivo

    Este projeto foi desenvolvido para demonstrar competências
    relacionadas à Mineração de Dados através da análise do catálogo
    da Netflix.

    ### Tecnologias Utilizadas

    - Python
    - Pandas
    - Plotly
    - Streamlit
    - Visualização de Dados
    """)

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg",
        width=250
    )

# ==========================
# VISÃO GERAL
# ==========================
elif pagina == "Visão Geral":

    st.title("📈 Visão Geral")

    total_registros = len(df)
    total_colunas = len(df.columns)

    filmes = len(df[df["type"] == "Movie"])
    series = len(df[df["type"] == "TV Show"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Registros", total_registros)
    col2.metric("Colunas", total_colunas)
    col3.metric("Filmes", filmes)
    col4.metric("Séries", series)

    st.divider()

    st.subheader("Prévia da Base")

    st.dataframe(df.head(20))

# ==========================
# ANÁLISES
# ==========================
elif pagina == "Análises":

    st.title("📊 Dashboard Analítico")

    col1, col2 = st.columns(2)

    with col1:

        tipo = df["type"].value_counts()

        fig1 = px.pie(
            values=tipo.values,
            names=tipo.index,
            title="Filmes x Séries",
            hole=0.5
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with col2:

        rating = df["rating"].value_counts().head(10)

        fig2 = px.bar(
            x=rating.index,
            y=rating.values,
            title="Classificação Indicativa"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.divider()

    paises = (
        df["country"]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
    )

    fig3 = px.bar(
        x=paises.index,
        y=paises.values,
        title="Top 10 Países com Mais Produções"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    anos = df["release_year"].value_counts().sort_index()

    fig4 = px.line(
        x=anos.index,
        y=anos.values,
        title="Evolução dos Lançamentos"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# ==========================
# INSIGHTS
# ==========================
elif pagina == "Insights":

    st.title("💡 Principais Insights")

    st.success("""
    Filmes representam a maior parte do catálogo da Netflix.
    """)

    st.success("""
    Os Estados Unidos lideram a produção de conteúdos.
    """)

    st.success("""
    O catálogo apresentou forte crescimento após 2015.
    """)

    st.success("""
    A maior parte do conteúdo é voltada para adolescentes e adultos.
    """)

    st.success("""
    A análise de dados permite identificar padrões e apoiar a tomada de decisões.
    """)

# ==========================
# SOBRE
# ==========================
elif pagina == "Sobre":

    st.title("👨‍💻 Sobre o Projeto")

    st.markdown("""
    ### Projeto Acadêmico

    Desenvolvido como atividade prática da disciplina
    de Análise e Mineração de Dados.

    ### Competências Demonstradas

    ✅ Coleta de Dados

    ✅ Limpeza de Dados

    ✅ Análise Exploratória

    ✅ Visualização de Dados

    ✅ Geração de Insights

    ✅ Python

    ✅ Pandas

    ✅ Streamlit
    """)