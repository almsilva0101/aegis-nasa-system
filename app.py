import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import lightkurve as lk
import pandas as pd
import numpy as np
import time

# Configuração de Centro de Comando Tático da NASA
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
    st.markdown("<p style='color: #FF3D00; font-size: 14px; margin-bottom: 0;'>🔥 TELEMETRIA ESPACIAL MULTIMODAL ATIVA // PROTOCOLO AEGIS-2026</p>", unsafe_allow_html=True)
    st.title("🛰️ AEGIS - Sistema Integrado de Defesa e Exploração Espacial")
    st.markdown("---")

    # --- MENU PRINCIPAL EM ABAS ---
    tab_exoplanetas, tab_telescopios, tab_meteoros = st.tabs([
        "🌌 1. Triagem de Exoplanetas & Anomalias", 
        "🛰️ 2. Status da Frota de Telescópios", 
        "☄️ 3. Defesa Planetária (Rastreamento de Meteoros)"
    ])

    # ==========================================
    # ABA 1: EXOPLANETAS E ANOMALIAS
    # ==========================================
    with tab_exoplanetas:
        st.markdown("### 🔬 Pipeline de Inteligência em Sinais de Órbita Profunda")
        
        with st.expander("📘 O que estamos fazendo aqui? (Explicação Científica)"):
            st.write("""
            **Objetivo:** Identificar planetas fora do nosso sistema solar ou anomalias cósmicas.
            * **O que é a Fila de Triagem?** É uma tabela gerada por algoritmos de Machine Learning. Ela varre milhões de estrelas e isola apenas aquelas onde o brilho mudou de forma suspeita.
            * **O que é o Desvio Padrão (σ)?** Mede o quão 'estranho' ou ruidoso é o sinal. Quanto maior o Sigma (σ), mais discrepante e anômalo é o comportamento da estrela.
            * **O que é o Mapa 3D?** Mostra a localização espacial exata de cada estrela analisada em relação à Terra em anos-luz.
            * **O que é o Gráfico de Espectro/Fluxo?** É a curva de luz da estrela. Se uma linha tiver uma queda em formato de 'U', significa que um exoplaneta passou na frente dela bloqueando a luz (Método do Trânsito). Se a linha for caótica e cheia de picos, isolamos uma **Anomalia Não Identificada**.
            """)

        # Configuração da barra lateral apenas para esta aba
        st.sidebar.markdown("## **Configurações de Busca**")
        target_option = st.sidebar.selectbox(
            "Selecionar Estrela Alvo",
            ["Sector 1: Kepler-10 (Telescópio Kepler)", "Sector 2: Pi Mensae (Telescópio TESS)", "Sector 3: TRAPPIST-1 (Telescópio JWST)", "Sector 4: Alvo Desconhecido (Anomalia Crítica)"]
        )
        
        tic_map = {
            "Sector 1: Kepler-10 (Telescópio Kepler)": "119041565",
            "Sector 2: Pi Mensae (Telescópio TESS)": "261136665",
            "Sector 3: TRAPPIST-1 (Telescópio JWST)": "27877559",
            "Sector 4: Alvo Desconhecido (Anomalia Crítica)": "88843211"
        }
        target_tic = tic_map[target_option]

        # Tabela de dados
        estrelas_data = {
            "ID da Estrela": ["TIC 119041565", "TIC 261136665", "TIC 27877559", "TIC 88843211"],
            "Telescópio de Origem": ["Kepler (NASA)", "TESS (NASA)", "James Webb (NASA/ESA)", "TESS (NASA)"],
            "Desvio Padrão (σ)": [4.2, 8.9, 1.2, 25.4],
            "Confiança da IA": [0.94, 0.88, 0.12, 0.99],
            "Classificação Preliminar": ["Exoplaneta Candidato", "Exoplaneta Candidato", "Ruído Instrumental", "Anomalia Não Identificada"]
        }
        df_triagem = pd.DataFrame(estrelas_data)
        st.dataframe(df_triagem, use_container_width=True)

        col_mapa, col_dados = st.columns([1, 1])

        with col_mapa:
            st.subheader("🌐 Mapa de Coordenadas Estelares 3D")
            np.random.seed(42)
            n_stars = 200
            df_stars = pd.DataFrame({
                'X': np.random.randn(n_stars) * 10, 'Y': np.random.randn(n_stars) * 10, 'Z': np.random.randn(n_stars) * 5,
                'Brilho': np.random.rand(n_stars) * 100, 'Tamanho': np.random.rand(n_stars) * 15
            })
            fig_3d = go.Figure(data=[go.Scatter3d(
                x=df_stars['X'], y=df_stars['Y'], z=df_stars['Z'], mode='markers',
                marker=dict(size=df_stars['Tamanho'], color=df_stars['Brilho'], colorscale='Viridis', opacity=0.8)
            )])
            fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0), paper_bgcolor='black', plot_bgcolor='black', font_color='white')
            st.plotly_chart(fig_3d, use_container_width=True)

        with col_dados:
            st.subheader("📊 Gráfico de Fluxo de Fótons (Curva de Luz)")
            dados_alvo = df_triagem[df_triagem["ID da Estrela"] == f"TIC {target_tic}"].iloc[0]
            
            tempo = np.linspace(0, 10, 1000)
            if "Anomalia" in dados_alvo["Classificação Preliminar"]:
                fluxo = 1.0 + np.random.randn(1000) * 0.005
                fluxo[300:400] -= np.linspace(0, 0.06, 100)
                fluxo[700:750] += np.random.randn(50) * 0.015
                cor = '#FF3D00'
            elif "Exoplaneta" in dados_alvo["Classificação Preliminar"]:
                fluxo = 1.0 + np.random.randn(1000) * 0.001
                fluxo[400:500] -= 0.015
                cor = '#00E5FF'
            else:
                fluxo = 1.0 + np.random.randn(1000) * 0.012
                cor = '#FFFFFF'

            df_plot = pd.DataFrame({"Tempo (Dias)": tempo, "Brilho Relativo": fluxo})
            fig_lc = px.line(df_plot, x='Tempo (Dias)', y='Brilho Relativo', color_discrete_sequence=[cor])
            fig_lc.update_layout(paper_bgcolor='black', plot_bgcolor='black', font_color='white')
            st.plotly_chart(fig_lc, use_container_width=True)
            st.write(f"**Telescópio Responsável:** {dados_alvo['Telescópio de Origem']}")

    # ==========================================
    # ABA 2: STATUS DA FROTA DE TELESCÓPIOS
    # ==========================================
    with tab_telescopios:
        st.markdown("### 🛰️ Telemetria de Saúde dos Observatórios Espaciais")
        
        with st.expander("📘 O que significa este Dashboard de Telescópios?"):
            st.write("""
            **Objetivo:** Monitorar as condições físicas dos equipamentos na órbita da Terra e no espaço profundo.
            * **Temperatura Criogênica:** Telescópios infravermelhos (como o James Webb) precisam operar em temperaturas extremamente baixas (perto do zero absoluto, -233°C) para não queimar seus sensores de calor. Se a temperatura subir, o dado fica corrompido!
            * **Combustível Restante:** Essencial para manobras de órbita e desvio de detritos espaciais.
            """)

        col_t1, col_t2, col_t3 = st.columns(3)
        
        with col_t1:
            st.markdown("#### **TESS (Transiting Exoplanet Survey)**")
            st.metric("Status Operacional", "ONLINE", delta="Estável")
            st.progress(0.74, text="Combustível Hidrazina: 74%")
            st.metric("Temperatura do Sensor", "-80°C", delta="Ideal")

        with col_t2:
            st.markdown("#### **James Webb (JWST)**")
            st.metric("Status Operacional", "COLETANDO DADOS", delta="Carga Alta", delta_color="inverse")
            st.progress(0.89, text="Combustível de Órbita: 89%")
            st.metric("Temperatura Criogênica (MIRI)", "-266°C", delta="-1°C (Excelente)")

        with col_t3:
            st.markdown("#### **Kepler Telescope**")
            st.metric("Status Operacional", "APOSENTADO / ARQUIVO", delta="Inativo", delta_color="off")
            st.progress(0.0, text="Combustível: 0%")
            st.write("Dados históricos consolidados integrados ao AEGIS database.")

    # ==========================================
    # ABA 3: DEFESA PLANETÁRIA (METEOROS E ASTEROIDES)
    # ==========================================
    with tab_meteoros:
        st.markdown("### ☄️ Rastreamento de Objetos Próximos à Terra (NEOs)")
        
        with st.expander("📘 O que estamos fazendo aqui? (Defesa Planetária)"):
            st.write("""
            **Objetivo:** Evitar um evento de extinção em massa rastreando Meteoroides, Meteoros e Asteroides potencialmente perigosos (PHA).
            * **Distância de Falha (Miss Distance):** A distância mínima que o objeto vai passar da Terra. Medida em 'Distâncias Lunares' (LD) — 1 LD é a distância da Terra até a Lua.
            * **Diâmetro Estimado:** O tamanho da rocha espacial. Objetos maiores que 140 metros são considerados ameaças catastróficas regionais.
            * **Escala de Torino:** Uma métrica de 0 a 10 que avalia o risco de colisão. 0 significa risco nulo; 10 significa colisão global certa.
            """)

        # Simulando base de dados de asteroides e meteoros detectados na semana
        meteoros_data = {
            "Nome do Objeto": ["Meteoróide M-2026_AQ", "Asteroide Apophis 99942", "Asteroide 2026-XC4", "Meteoro de Entrada Rápida BEN-10"],
            "Diâmetro Est. (Metros)": [12, 370, 145, 3],
            "Velocidade (km/h)": [45000, 110000, 67000, 82000],
            "Distância Mínima (LD)": [1.4, 0.12, 4.5, 0.01],
            "Escala de Torino": [0, 2, 1, 0],
            "Risco de Impacto": ["Nulo (Queima na Atmosfera)", "Atenção (Monitoramento Kinetico)", "Baixo Risco", "Nulo (Impacto Balístico Pequeno)"]
        }
        df_meteoros = pd.DataFrame(meteoros_data)
        st.dataframe(df_meteoros, use_container_width=True)

        st.subheader("🌐 Radar de Aproximação de Trajetórias Orbitais")
        
        # Criando um Gráfico de Radar Espacial Orbital (Gráfico de dispersão polar ou circular)
        # Mostra a Terra no centro e a distância dos meteoros vindo em direção ao planeta
        fig_radar = go.Figure()
        
        # Desenha a Terra no centro (Ponto 0)
        fig_radar.add_trace(go.Scatter(x=[0], y=[0], mode='markers+text', marker=dict(size=30, color='#00E5FF'), text=["TERRA"], textposition="top center"))
        
        # Plota os objetos espaciais com base em suas distâncias aproximadas
        fig_radar.add_trace(go.Scatter(
            x=[1.2, -0.09, -3.2, 0.4], 
            y=[0.7, 0.08, 3.1, -0.1], 
            mode='markers+text',
            marker=dict(size=df_meteoros["Diâmetro Est. (Metros)"]/10 + 10, color=df_meteoros["Escala de Torino"], colorscale='Reds', showscale=True),
            text=df_meteoros["Nome do Objeto"],
            textposition="bottom center"
        ))
        
        fig_radar.update_layout(
            title="Posicionamento Relativo de Objetos em Rota de Aproximação (Distância em Unidades Lunares)",
            paper_bgcolor='black', plot_bgcolor='black', font_color='white',
            xaxis=dict(showgrid=True, zeroline=True, range=[-6, 6]),
            yaxis=dict(showgrid=True, zeroline=True, range=[-6, 6])
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    # --- FOOTER DO PRODUTO ---
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #555;'>SISTEMA MILITAR INTEGRADO AEGIS - CENTRO DE INTELIGÊNCIA ESPACIAL DA NASA © 2026</p>", unsafe_allow_html=True)

# Controle de Fluxo Geral
if not st.session_state['authenticated']:
    login_page()
else:
    main_dashboard()
