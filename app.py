import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="AEGIS - Deep Space Anomaly Detector", layout="wide", initial_sidebar_state="expanded")

# Inicialização do estado de autenticação
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def login_page():
    st.markdown("<h1 style='text-align: center; color: #FF3D00;'>🛡️ A.E.G.I.S.</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>Advanced Anomaly Galactic Intelligence System</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("aegis_login"):
            st.markdown("### **Autenticação de Operador Especialista**")
            user = st.text_input("Username", "nasa_operator_01")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("CONECTAR AO PIPELINE DE DADOS"):
                if user == "nasa_operator_01" and password == "artemis2026":
                    st.session_state['authenticated'] = True
                    st.rerun()
                else:
                    st.error("Credenciais inválidas.")

def main_dashboard():
    st.markdown("<p style='color: #FF3D00; font-size: 14px; margin-bottom: 0;'>🔥 TELEMETRIA ATIVA // ANOMALY DETECTION ENGINE ENFORCED</p>", unsafe_allow_html=True)
    st.title("🛰️ AEGIS Centro de Controle e Triagem de Anomalias")
    st.markdown("---")

    # 1. GERAÇÃO DE DADOS CIENTÍFICOS COM ANOMALIAS REAIS (Simulação Avançada)
    # Criando um dataset de 5 estrelas alvos com telemetria e classificação de IA
    np.random.seed(101)
    estrelas_data = {
        "ID da Estrela": ["TIC 119041565", "TIC 261136665", "TIC 27877559", "TIC 88843211", "TIC 99421102"],
        "Constelação": ["Kepler Field", "Mensa", "Aquarius", "Orion", "Cygnus"],
        "Desvio Padrão do Sinal (σ)": [4.2, 8.9, 1.2, 15.4, 23.1],
        "Score de Confiança da IA": [0.94, 0.88, 0.12, 0.99, 0.76],
        "Classificação Preliminar": ["Exoplaneta Candidato", "Exoplaneta Candidato", "Ruído Instrumental", "Anomalia Não Identificada", "Estrela Binária"]
    }
    df_triagem = pd.DataFrame(estrelas_data)

    # KPIs Dinâmicos focados em Erros e Anomalias
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric(label="Sinais Varridos (Últimas 24h)", value="142,805", delta="+2,410")
    kpi2.metric(label="Anomalias Críticas Isoladas", value="2", delta="Ação Requerida", delta_color="inverse")
    kpi3.metric(label="Falsos Positivos Descartados", value="1,104", delta="-5%")
    kpi4.metric(label="Mecanismo de Detecção (Isolation Forest)", value="Ativo", delta="Online")

    st.markdown("### 📋 Fila de Triagem de Sinais Espaciais")
    st.write("Estes são os alvos capturados pelo telescópio que o algoritmo de Machine Learning isolou por apresentarem comportamento fora do desvio padrão estatístico aceitável.")
    
    # Exibição da tabela com destaque científico
    st.dataframe(df_triagem, use_container_width=True)

    st.markdown("---")
    
    # Seletor interativo para o analista investigar a anomalia a fundo
    st.markdown("### 🔬 Painel de Diagnóstico do Alvo")
    alvo_selecionado = st.selectbox("Escolha um alvo da fila acima para auditar os dados brutos:", df_triagem["ID da Estrela"])
    
    row = df_triagem[df_triagem["ID da Estrela"] == alvo_selecionado].iloc[0]
    
    col_meta, col_grafico = st.columns([1, 2])
    
    with col_meta:
        st.markdown(f"#### Detalhes Técnicos: **{alvo_selecionado}**")
        st.write(f"**Setor Espacial:** {row['Constelação']}")
        st.write(f"**Assinatura de Ruído (Sigma):** {row['Desvio Padrão do Sinal (σ)']} σ")
        st.write(f"**Confiança do Modelo:** {row['Score de Confiança da IA'] * 100}%")
        
        # Alertas visuais baseados no tipo de anomalia
        if "Anomalia" in row["Classification Preliminar"] or row["Desvio Padrão do Sinal (σ)"] > 10:
            st.error(f"⚠️ Alerta Crítico: {row['Classificacao Preliminar']}. Assinatura de energia não condiz com modelos planetários conhecidos.")
        elif "Exoplaneta" in row["Classificacao Preliminar"]:
            st.success(f"🌌 Padrão Periódico Detectado: Compatível com órbita exoplanetária estável.")
        else:
            st.warning(f"🛑 Atenção: Sinal fraco ou possivelmente corrompido por poeira cósmica.")
            
        st.markdown("##### **Ações do Operador da NASA:**")
        st.button("Aprovar e Enviar para o James Webb", key="btn1")
        st.button("Descartar como Falso Positivo (Ruído)", key="btn2")
        st.button("Escalar para Investigação Astrofísica Profunda", key="btn3")

    with col_grafico:
        # Geração da Curva de Luz baseada no tipo selecionado para análise visual do cientista
        tempo = np.linspace(0, 10, 500)
        np.random.seed(42)
        
        if "Anomalia" in row["Classificacao Preliminar"]:
            # Sinal bizarro (Anomalia Estreitamente única - Ex: Esfera de Dyson ou pulso irregular)
            fluxo = 1.0 + np.random.randn(500) * 0.005
            fluxo[150:200] -= np.linspace(0, 0.08, 50) # Queda assimétrica violenta
            fluxo[350:400] += np.random.randn(50) * 0.02 # Picos inexplicáveis de energia
            titulo_grafico = f"CURVA DE LUZ DISRUPTIVA - ALVO HISTÓRICO {alvo_selecionado}"
            cor_linha = "#FF3D00"
        elif "Exoplaneta" in row["Classificacao Preliminar"]:
            # Trânsito limpo e simétrico
            fluxo = 1.0 + np.random.randn(500) * 0.001
            fluxo[200:250] -= 0.02  # Queda quadrada perfeita do planeta passando
            titulo_grafico = f"Trânsito Planetário Periódico Padronizado - {alvo_selecionado}"
            cor_linha = "#00E5FF"
        else:
            # Apenas ruído feio e sem padrão
            fluxo = 1.0 + np.random.randn(500) * 0.015
            titulo_grafico = f"Espectro de Ruído Caótico Amortecido - {alvo_selecionado}"
            cor_linha = "#FFFFFF"

        df_plot = pd.DataFrame({"Tempo de Observação (Dias)": tempo, "Fluxo de Fótons Recebidos": fluxo})
        fig = px.line(df_plot, x="Tempo de Observação (Dias)", y="Fluxo de Fótons Recebidos", title=titulo_grafico)
        fig.update_layout(paper_bgcolor='black', plot_bgcolor='black', font_color='white')
        st.plotly_chart(fig, use_container_width=True)

if not st.session_state['authenticated']:
    login_page()
else:
    main_dashboard()
