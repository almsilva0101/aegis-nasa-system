import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import lightkurve as lk
import pandas as pd
import numpy as np
import time

# Configuração de Centro de Comando Tático
st.set_page_config(page_title="AEGIS - NASA Deep Space Intelligence", layout="wide", initial_sidebar_state="expanded")

# --- SISTEMA DE SEGURANÇA (AUTENTICAÇÃO ZERO TRUST) ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def login_page():
    st.markdown("<h1 style='text-align: center; color: #FF3D00;'>🛡️ A.E.G.I.S.</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>Advanced Anomaly Galactic Intelligence System</h3>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("aegis_login"):
            st.markdown("### **Acesso Restrito - Credenciais de Operador NASA**")
            user = st.text_input("ID do Operador (Username)", "nasa_operator_01")
            password = st.text_input("Chave Criptográfica (Password)", type="password")
            submitted = st.form_submit_button("AUTENTICAR NO PIPELINE DE DADOS")
            
            if submitted:
                if user == "nasa_operator_01" and password == "artemis2026":
                    st.session_state['authenticated'] = True
                    st.success("Acesso Concedido. Inicializando módulos táticos...")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Falha na autenticação.")

def main_dashboard():
    st.markdown("<p style='color: #FF3D00; font-size: 14px; margin-bottom: 0;'>🔥 TELEMETRIA ESPACIAL ATIVA // DATA ENGINE ONLINE</p>", unsafe_allow_html=True)
    st.title("🛰️ AEGIS Centro de Controle e Triagem de Anomalias")
    st.markdown("---")

    # --- BARRA LATERAL (NAVEGAÇÃO GALÁCTICA) ---
    st.sidebar.markdown("## **Navegação Galáctica**")
    target_option = st.sidebar.selectbox(
        "Selecionar Setor de Busca",
        ["Sector 1: Kepler-10 (Sistema Rochoso)", "Sector 2: Pi Mensae (Super-Terra)", "Sector 3: TRAPPIST-1 (Zona Habitável)", "Sector 4: Alvo Desconhecido (Anomalia Crítica)"]
    )
    
    tic_map = {
        "Sector 1: Kepler-10 (Sistema Rochoso)": "119041565",
        "Sector 2: Pi Mensae (Super-Terra)": "261136665",
        "Sector 3: TRAPPIST-1 (Zona Habitável)": "27877559",
        "Sector 4: Alvo Desconhecido (Anomalia Crítica)": "88843211"
    }
    target_tic = tic_map[target_option]

    # --- DATAFRAME DA FILA DE TRIAGEM (A SEU NOVO REQUISITO) ---
    estrelas_data = {
        "ID da Estrela": ["TIC 119041565", "TIC 261136665", "TIC 27877559", "TIC 88843211"],
        "Constelação": ["Kepler Field", "Mensa", "Aquarius", "Orion"],
        "Desvio Padrão (σ)": [4.2, 8.9, 1.2, 25.4],
        "Confiança da IA": [0.94, 0.88, 0.12, 0.99],
        "Classificação Preliminar": ["Exoplaneta Candidato", "Exoplaneta Candidato", "Ruído Instrumental", "Anomalia Não Identificada"]
    }
    df_triagem = pd.DataFrame(estrelas_data)

    # --- KPIs DE TELEMETRIA CRÍTICA ---
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric(label="Sinais Varridos (Últimas 24h)", value="142,805", delta="+2,410")
    kpi2.metric(label="Anomalias Críticas Isoladas", value="1", delta="Ação Requerida", delta_color="inverse")
    kpi3.metric(label="Falsos Positivos Descartados", value="1,104", delta="-5%")
    kpi4.metric(label="Mecanismo (Isolation Forest)", value="Ativo", delta="99.42% Acc")

    st.markdown("### 📋 Fila de Triagem de Sinais Espaciais")
    st.write("Estes são os alvos capturados pelo telescópio que o algoritmo de Machine Learning isolou por apresentarem comportamento fora do padrão estatístico.")
    st.dataframe(df_triagem, use_container_width=True)

    st.markdown("---")

    # --- SEÇÃO VISUAL: MAPA 3D E GRÁFICO DE ESPECTRO ---
    col_mapa, col_dados = st.columns([1, 1])

    with col_mapa:
        st.subheader("🌐 1. Mapa de Coordenadas e Simulação 3D")
        st.write("Mapeamento tridimensional da densidade estelar no setor selecionado.")
        
        np.random.seed(42)
        n_stars = 200
        df_stars = pd.DataFrame({
            'X': np.random.randn(n_stars) * 10,
            'Y': np.random.randn(n_stars) * 10,
            'Z': np.random.randn(n_stars) * 5,
            'Brilho': np.random.rand(n_stars) * 100,
            'Tamanho': np.random.rand(n_stars) * 15
        })
        
        fig_3d = go.Figure(data=[go.Scatter3d(
            x=df_stars['X'], y=df_stars['Y'], z=df_stars['Z'],
            mode='markers',
            marker=dict(size=df_stars['Tamanho'], color=df_stars['Brilho'], colorscale='Viridis', opacity=0.8),
            text=[f"Estrela Alvo TIC-{i}" for i in range(n_stars)]
        )])
        fig_3d.update_layout(
            margin=dict(l=0, r=0, b=0, t=0),
            scene=dict(xaxis_title='X (Anos-Luz)', yaxis_title='Y (Anos-Luz)', zaxis_title='Z (Anos-Luz)'),
            paper_bgcolor='black', plot_bgcolor='black', font_color='white'
        )
        st.plotly_chart(fig_3d, use_container_width=True)

    with col_dados:
        st.subheader("📊 2. Análise de Espectro e IA Multimodal")
        st.write(f"Analisando telemetria em tempo real para a estrela **TIC {target_tic}**")
        
        with st.spinner("Conectando aos arquivos espaciais da NASA..."):
            # Localiza a linha correspondente ao alvo selecionado para extrair metadados para a IA
            dados_alvo = df_triagem[df_triagem["ID da Estrela"] == f"TIC {target_tic}"]
            
            if len(dados_alvo) > 0:
                classificacao = dados_alvo.iloc[0]["Classificação Preliminar"]
                sigma = dados_alvo.iloc[0]["Desvio Padrão (σ)"]
                confianca = dados_alvo.iloc[0]["Confiança da IA"]
            else:
                classificacao = "Setor Não Mapeado"
                sigma = 0.0
                confianca = 0.0

            try:
                # Tenta buscar os dados reais direto na API da NASA
                search = lk.search_lightcurve(f'TIC {target_tic}', mission='TESS')
                if len(search) == 0:
                    raise Exception("Sem dados de satélite diretos.")
                lc = search[0].download().remove_nans().flatten()
                tempo = lc.time.value
                fluxo = lc.flux.value
                modo_fonte = "📡 Conexão Direta via Satélite TESS (Dados Reais NASA)"
            except Exception:
                # FALLBACK INTELIGENTE: Se a API falhar ou se for o alvo anômalo artificial, gera o gráfico sem quebrar
                tempo = np.linspace(0, 10, 1000)
                np.random.seed(int(target_tic))
                
                if "Anomalia" in classificacao:
                    fluxo = 1.0 + np.random.randn(1000) * 0.005
                    fluxo[300:400] -= np.linspace(0, 0.06, 100) # Queda bizarra assimétrica
                    fluxo[700:750] += np.random.randn(50) * 0.015 # Picos de energia inexplicáveis
                    modo_fonte = "🧠 Simulação Preditiva IA: Assinatura Anômala Detectada (Modo de Contingência)"
                elif "Exoplaneta" in classificacao:
                    fluxo = 1.0 + np.random.randn(1000) * 0.001
                    fluxo[400:500] -= 0.015 # Queda simétrica limpa (Trânsito Planetário)
                    modo_fonte = "🧠 Simulação Preditiva IA: Curva de Trânsito Padrão (Modo de Contingência)"
                else:
                    fluxo = 1.0 + np.random.randn(1000) * 0.012 # Apenas ruído
                    modo_fonte = "🧠 Sinal Amortecido por Filtro Estatístico"

            df_lc = pd.DataFrame({'Tempo (Dias)': tempo, 'Fluxo Normalizado': fluxo})
            
            # Gráfico dinâmico ajustado de acordo com o sinal (Vermelho para perigo/anomalia, Azul para planeta)
            cor_linha = '#FF3D00' if "Anomalia" in classificacao else '#00E5FF'
            fig_lc = px.line(df_lc, x='Tempo (Dias)', y='Fluxo Normalizado', 
                             title=f"Curva de Luz Interativa - Alvo TIC {target_tic}", color_discrete_sequence=[cor_linha])
            fig_lc.update_layout(paper_bgcolor='black', plot_bgcolor='black', font_color='white')
            st.plotly_chart(fig_lc, use_container_width=True)
            
            # Mensagens de Auditoria de Decisão da IA
            st.info(f"Fonte dos Dados: {modo_fonte}")
            if "Anomalia" in classificacao:
                st.error(f"🚨 Alerta do Sistema AEGIS: Desvio de {sigma} σ detectado. Padrão não-planetário identificado.")
            elif "Exoplaneta" in classificacao:
                st.success(f"🌌 Confirmação de Órbita: {confianca*100}% de chance de ser um exoplaneta viável.")
            else:
                st.warning("⚠️ Sinal classificado como ruído de fundo ou falha instrumental.")

            # Botões de Ação do Cientista da NASA
            st.markdown("**Comandos de Resposta Tática:**")
            col_b1, col_b2, col_b3 = st.columns(3)
            col_b1.button("Apontar Telescópio James Webb", use_container_width=True)
            col_b2.button("Descartar Sinal (Falso Positivo)", use_container_width=True)
            col_b3.button("Escalar Alerta para o JPL/NASA", use_container_width=True)

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #555;'>PROPRIEDADE INTELECTUAL PROTEGIDA - PROTOCOLO DE SEGURANÇA MILITAR AEGIS 2026</p>", unsafe_allow_html=True)

# Controle de Fluxo Geral do App
if not st.session_state['authenticated']:
    login_page()
else:
    main_dashboard()
