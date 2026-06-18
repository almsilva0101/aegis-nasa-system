import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import time

# 1. CONFIGURAÇÃO DA PÁGINA (Layout Amplo e Tema Dark Forçado nativamente)
st.set_page_config(
    page_title="AEGIS | NASA Deep Space & Planetary Defense",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS customizada para dar o visual "Mission Control" profissional
st.markdown("""
    <style>
        /* Ajuste de fontes e espaçamentos globais */
        .reportview-container .main .block-container { padding-top: 2rem; }
        h1, h2, h3 { font-family: 'Space Grotesk', 'Segoe UI', sans-serif; font-weight: 700; }
        
        /* Customização dos blocos de métricas para parecerem cartões de monitoramento */
        div[data-testid="stMetricValue"] { font-size: 28px !important; font-weight: bold; color: #00E5FF; }
        div[data-testid="stMetricDelta"] { font-size: 14px !important; }
        
        /* Bordas e separadores elegantes */
        .card-painel {
            background-color: #0E1117;
            border: 1px solid #1E293B;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# --- GERENCIAMENTO DE ESTADO DE AUTENTICAÇÃO ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def login_page():
    st.markdown("<h1 style='text-align: center; color: #FF2E93; margin-bottom: 0;'>🛡️ A.E.G.I.S.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 16px;'>Advanced Planetary Defense & Galactic Intelligence System</p>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
        with st.form("aegis_login"):
            st.markdown("### **Autenticação de Operador // Nível de Acesso 5**")
            user = st.text_input("ID do Operador (Username)", "nasa_operator_01")
            password = st.text_input("Chave Criptográfica (Password)", type="password")
            submitted = st.form_submit_button("VALIDAR CREDENCIAIS")
            
            if submitted:
                if user == "nasa_operator_01" and password == "artemis2026":
                    st.session_state['authenticated'] = True
                    st.success("🔒 Chave criptográfica aceita. Inicializando terminais...")
                    time.sleep(0.6)
                    st.rerun()
                else:
                    st.error("❌ Falha na autenticação. Acesso negado.")
        st.markdown("</div>", unsafe_allow_html=True)

def main_dashboard():
    # --- CABEÇALHO DA PLATAFORMA ---
    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.markdown("<p style='color: #FF2E93; font-size: 13px; font-weight: bold; letter-spacing: 2px; margin-bottom: 0;'>🚨 SECURE COMMAND NODE // DATA STREAM ACTIVE</p>", unsafe_allow_html=True)
        st.title("🛰️ AEGIS Operational Command Center")
    with header_col2:
        st.write("")
        st.write("")
        st.markdown("<div style='text-align: right; color: #64748B; font-size: 12px;'>SISTEMA DE DEFESA INTEGRADO<br>VERSÃO 4.2.1 // DEPLOY COMPLETO</div>", unsafe_allow_html=True)
    
    st.markdown("---")

    # --- BARRA LATERAL TÁTICA (SIDEBAR) ---
    st.sidebar.markdown("### 🌌 Parâmetros de Varredura")
    st.sidebar.markdown("Configure os filtros globais de captação dos telescópios:")
    
    target_option = st.sidebar.selectbox(
        "Estrela Alvo Ativa (Aba 1)",
        ["Sector 1: Kepler-10 (Telescópio Kepler)", "Sector 2: Pi Mensae (Telescópio TESS)", "Sector 3: TRAPPIST-1 (Telescópio JWST)", "Sector 4: Alvo Desconhecido (Anomalia Crítica)"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📡 Status de Conexão")
    st.sidebar.success("● Link de Satélite Deep Space: ONLINE")
    st.sidebar.success("● Pipeline de IA (Lightkurve V4): OPERACIONAL")

    # Mapeamento do Alvo Selecionado
    tic_map = {
        "Sector 1: Kepler-10 (Telescópio Kepler)": "119041565",
        "Sector 2: Pi Mensae (Telescópio TESS)": "261136665",
        "Sector 3: TRAPPIST-1 (Telescópio JWST)": "27877559",
        "Sector 4: Alvo Desconhecido (Anomalia Crítica)": "88843211"
    }
    target_tic = tic_map[target_option]

    # --- ESTRUTURA METÓDICA DE ABAS COMPLETA ---
    tab_exoplanetas, tab_telescopios, tab_defesa = st.tabs([
        "🌌 1. Triagem de Exoplanetas & Anomalias",
        "🛰️ 2. Monitoramento de Saúde da Frota",
        "☄️ 3. Central de Defesa Planetária Avançada"
    ])

    # Base de dados de triagem estelar
    estrelas_data = {
        "ID da Estrela": ["TIC 119041565", "TIC 261136665", "TIC 27877559", "TIC 88843211"],
        "Telescópio": ["Kepler (NASA)", "TESS (NASA)", "James Webb (NASA)", "TESS (NASA)"],
        "Desvio Padrão (σ)": [4.2, 8.9, 1.2, 25.4],
        "Confiança IA": ["94.2%", "88.0%", "12.5%", "99.8%"],
        "Status": ["Exoplaneta Candidato", "Exoplaneta Candidato", "Ruído Instrumental", "Anomalia Não Identificada"]
    }
    df_triagem = pd.DataFrame(estrelas_data)

    # ==========================================
    # ABA 1: TRIAGEM DE EXOPLANETAS
    # ==========================================
    with tab_exoplanetas:
        st.markdown("### 🔬 Pipeline de Inteligência em Sinais de Órbita Profunda")
        
        with st.expander("📘 Manual de Operação e Glossário Técnico (Clique para expandir)"):
            st.markdown("""
            * **Fila de Triagem:** Centraliza alvos onde os algoritmos estatísticos da IA detectaram flutuações anormais de fluxo luminoso.
            * **Desvio Padrão (σ):** Representa o nível de dispersão estatística da luz da estrela. Um $\sigma$ muito alto indica mudanças agressivas na emissão de energia (potencial trânsito ou anomalia estrutural cósmica).
            * **Curva de Luz:** Gráfico do fluxo de fótons ao longo do tempo. Quedas em formato côncavo periódico revelam a presença de corpos planetários cruzando a órbita da estrela.
            """)
        
        # Grid de Métricas Superiores da Aba 1
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Fluxo de Dados Analisados", "4.2 TB/s", "+12% vs ontem")
        m2.metric("Sinais Varridos (Ciclo)", "142.805", "Fase Concluída")
        m3.metric("Anomalias Críticas Isoladas", "2", "-1 este período")
        m4.metric("Precisão Geral do Modelo", "99.42%", "Deep Learning V4")
        
        st.markdown("#### Fila Ativa de Sinais Isolados para Auditoria")
        st.dataframe(df_triagem, use_container_width=True, hide_index=True)
        
        col_mapa, col_dados = st.columns([1, 1])
        
        with col_mapa:
            st.markdown("#### 🌐 Localização Tridimensional do Setor Estelar")
            np.random.seed(42)
            n_stars = 120
            df_stars = pd.DataFrame({
                'X': np.random.randn(n_stars) * 12, 'Y': np.random.randn(n_stars) * 12, 'Z': np.random.randn(n_stars) * 6,
                'Magnitude': np.random.rand(n_stars) * 100, 'Tamanho': np.random.rand(n_stars) * 12
            })
            fig_3d = go.Figure(data=[go.Scatter3d(
                x=df_stars['X'], y=df_stars['Y'], z=df_stars['Z'], mode='markers',
                marker=dict(size=df_stars['Tamanho'], color=df_stars['Magnitude'], colorscale='Plasma', opacity=0.85)
            )])
            fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0), paper_bgcolor='#0E1117', plot_bgcolor='#0E1117', font_color='white', height=400)
            st.plotly_chart(fig_3d, use_container_width=True)
            
        with col_dados:
            st.markdown(f"#### 📊 Análise Multimodal de Espectro // TIC {target_tic}")
            
            tempo = np.linspace(0, 10, 800)
            # Localiza os dados específicos do alvo escolhido na barra lateral
            dados_alvo = df_triagem[df_triagem["ID da Estrela"] == f"TIC {target_tic}"].iloc[0]
            
            if "Anomalia" in dados_alvo["Status"]:
                fluxo = 1.0 + np.random.randn(800) * 0.004
                fluxo[250:350] -= np.linspace(0, 0.08, 100)
                fluxo[600:650] += np.random.randn(50) * 0.02
                cor_grafico = '#FF2E93'
            elif "Exoplaneta" in dados_alvo["Status"]:
                fluxo = 1.0 + np.random.randn(800) * 0.001
                fluxo[350:450] -= 0.018  # Simulação perfeita de curva de trânsito em U
                cor_grafico = '#00E5FF'
            else:
                fluxo = 1.0 + np.random.randn(800) * 0.009
                cor_grafico = '#94A3B8'
                
            df_plot = pd.DataFrame({"Tempo (Dias)": tempo, "Fluxo Relativo": fluxo})
            fig_lc = px.line(df_plot, x='Tempo (Dias)', y='Fluxo Relativo', color_discrete_sequence=[cor_grafico])
            fig_lc.update_layout(paper_bgcolor='#0E1117', plot_bgcolor='#0E1117', font_color='white', height=370, margin=dict(t=20))
            st.plotly_chart(fig_lc, use_container_width=True)
            st.markdown(f"**Assinatura de Equipamento:** Telemetria gerada pelo observatório *{dados_alvo['Telescópio']}*.")

    # ==========================================
    # ABA 2: MONITORAMENTO DA FROTA (TELESCÓPIOS)
    # ==========================================
    with tab_telescopios:
        st.markdown("### 🛰️ Telemetria de Saúde e Logística dos Observatórios")
        
        with st.expander("📘 Por que monitoramos essas variáveis físicas?"):
            st.markdown("""
            * **Temperatura Criogênica:** Telescópios espaciais infravermelhos operam com sensores refrigerados a hélio líquido ou resfriadores de pulso. Se a temperatura subir acima do limite operacional (ex: -266°C no instrumento MIRI do JWST), os sensores captam radiação térmica do próprio espelho, destruindo a integridade científica da imagem.
            * **Combustível Restante:** Crucial para manter a órbita estável em pontos de Lagrange (L2) e realizar manobras evasivas contra lixo espacial.
            """)
            
        t1, t2, t3 = st.columns(3)
        
        with t1:
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            st.markdown("#### **Observatório TESS**")
            st.caption("Transiting Exoplanet Survey Satellite")
            st.metric("Status Operacional", "ONLINE", delta="Estável // Coleta Ativa")
            st.progress(0.74, text="Nível de Hidrazina: 74%")
            st.metric("Temperatura da Câmera Core", "-80.2 °C", delta="0.0 °C (Nominal)")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with t2:
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            st.markdown("#### **James Webb (JWST)**")
            st.caption("Deep Space Infrared Observatory")
            st.metric("Status Operacional", "CARGA MÁXIMA", delta="Deep Field Scan", delta_color="inverse")
            st.progress(0.89, text="Combustível de Órbita: 89%")
            st.metric("Sensor Criogênico (MIRI)", "-266.1 °C", delta="-0.4 °C (Excelente)")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with t3:
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            st.markdown("#### **Módulo Kepler (Arquivo)**")
            st.caption("Legacy Mission Database")
            st.metric("Status Operacional", "APOSENTADO", delta="Offline Permanente", delta_color="off")
            st.progress(0.0, text="Combustível: 0%")
            st.text("Dados consolidados sincronizados e indexados localmente na infraestrutura AEGIS.")
            st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # ABA 3: DEFESA PLANETÁRIA (RADAR + INTERCEPTAÇÃO)
    # ==========================================
    with tab_defesa:
        st.markdown("### ☄️ Centro de Monitoramento de NEOs (Near-Earth Objects) & Deflexão Proativa")
        
        with st.expander("📘 Fundamentos Técnicos da Defesa Planetária Avançada"):
            st.markdown("""
            * **Distância Mínima (LD - Lunar Distance):** Distância em relação ao centro da Terra mensurada em Unidades Lunares. $1 \\text{ LD} \\approx 384.400 \\text{ km}$.
            * **Escala de Torino:** Classificação de 0 a 10 para perigo de impacto na atmosfera. Valores acima de 5 indicam colisões com poder de devastação regional a global.
            * **Física de Deflexão Cinética:** Inspirado na missão **NASA DART (2022)**, o cálculo simula a transferência de momentum linear. Um impacto mecânico calculado a milhões de quilômetros de distância altera a velocidade do asteroide em milímetros por segundo, o suficiente para fazer a rocha errar completamente a Terra devido ao efeito cumulativo da trajetória orbital.
            """)

        # Base de Dados Unificada de Ameaças Detectadas
        meteoros_data = {
            "Nome do Objeto": ["Asteroide Apophis 99942", "Corpo Hiperbólico PHA-2026", "Fragmento de Meteoro M-102", "Meteoro de Entrada Rápida BEN-10"],
            "Diâmetro (m)": [370, 850, 45, 3],
            "Velocidade (km/h)": [110000, 145000, 48000, 82000],
            "Distância Mínima (LD)": [0.12, 0.04, 2.50, 0.01],
            "Escala de Torino": [2, 8, 1, 0],
            "Risco Estimado": ["Atenção (Monitoramento)", "Ameaça de Extinção Regional", "Baixo Risco", "Nulo (Queima Atmosférica)"]
        }
        df_meteoros = pd.DataFrame(meteoros_data)
        
        st.markdown("#### Matriz de Rastreamento de Objetos Próximos à Terra")
        st.dataframe(df_meteoros, use_container_width=True, hide_index=True)
        st.markdown("---")

        # DISPOSIÇÃO DO LAYOUT EM COLUNAS: RADAR GERAL VS SIMULADOR DE INTERCEPTAÇÃO
        col_radar, col_simulador = st.columns([1.1, 1])
        
        with col_radar:
            st.markdown("#### 🌐 1. Radar de Aproximação de Trajetórias (Visão Macro)")
            st.caption("Posicionamento radial instantâneo relativo à órbita geoestacionária terrestre.")
            
            fig_radar = go.Figure()
            # Ponto Central: A Terra
            fig_radar.add_trace(go.Scatter(
                x=[0], y=[0], mode='markers+text', 
                marker=dict(size=35, color='#00E5FF', line=dict(width=2, color='white')), 
                text=["TERRA"], textposition="top center", name="Ponto Zero (Terra)"
            ))
            # Plot das rochas espaciais baseando-se em suas distâncias aproximadas
            fig_radar.add_trace(go.Scatter(
                x=[1.1, -0.09, -2.1, 0.4], y=[0.7, 0.06, 1.5, -0.1], mode='markers+text',
                marker=dict(size=df_meteoros["Diâmetro (m)"]/15 + 15, color=df_meteoros["Escala de Torino"], colorscale='Reds', showscale=True, colorbar=dict(title="Torino")),
                text=df_meteoros["Nome do Objeto"], textposition="bottom center", name="NEOs Rastreados"
            ))
            fig_radar.update_layout(
                paper_bgcolor='#0E1117', plot_bgcolor='#0E1117', font_color='white',
                margin=dict(l=10, r=10, b=10, t=20), height=420,
                xaxis=dict(showgrid=True, gridcolor='#1E293B', zeroline=True, zerolinecolor='#334155', range=[-3.5, 3.5]),
                yaxis=dict(showgrid=True, gridcolor='#1E293B', zeroline=True, zerolinecolor='#334155', range=[-2.5, 2.5])
            )
            st.plotly_chart(fig_radar, use_container_width=True)
            
        with col_simulador:
            st.markdown("#### 💥 2. Terminal Interativo de Mitigação e Deflexão")
            st.caption("Calcule o impacto cinético simulado para alteração de vetores orbitais.")
            
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            alvo_defesa = st.selectbox("Alvo Crítico Selecionado:", df_meteoros["Nome do Objeto"])
            arma = st.radio("Vetor de Contra-Medida Proposto:", ["🚀 Sonda Impactor Cinemático (Estilo NASA DART)", "🛰️ Array de Laser Térmico Estacionário Orbital", "💥 Dispositivo de Pulso Nuclear de Desvio"])
            potencia = st.slider("Massa do Vetor / Output de Energia (Toneladas/MW):", 10, 500, 160)
            
            simular_impacto = st.button("💥 INICIAR CÁLCULO DE INTERCEPTAÇÃO")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Construção física do Gráfico de Deflexão Vectorial
            tempo_trajetoria = np.linspace(-5, 5, 200)
            y_original = (tempo_trajetoria ** 2) * 0.15 - 0.25
            
            fig_trajetoria = go.Figure()
            # Linha da Terra (Alvo vulnerável no Y=0)
            fig_trajetoria.add_trace(go.Scatter(x=[0], y=[0], mode="markers+text", marker=dict(size=35, color="#00E5FF"), text=["TERRA"], textposition="top center", name="Terra"))
            # Rota de Colisão Padrão
            fig_trajetoria.add_trace(go.Scatter(x=tempo_trajetoria, y=y_original, mode="lines", name="Rota de Colisão Original", line=dict(color="#FF2E93", width=2, dash="dash")))
            
            if simular_impacto:
                # Modelo lógico matemático de deflexão simulada
                fator_desvio = (potencia / 100) * 0.45
                if "Nuclear" in arma:
                    fator_desvio *= 1.75
                elif "Laser" in arma:
                    fator_desvio *= 1.10
                    
                y_desviada = y_original + fator_desvio
                
                # Linha Verde de Salvamento pós-impacto
                fig_trajetoria.add_trace(go.Scatter(x=tempo_trajetoria, y=y_desviada, mode="lines", name="Nova Rota Pós-Mitigação", line=dict(color="#00FF66", width=4)))
                # Marcador do local de impacto
                fig_trajetoria.add_trace(go.Scatter(x=[-2], y=[0.35], mode="markers+text", marker=dict(size=14, color="#FFFF00", symbol="star"), text=["💥 PONTO DE IMPACTO"], textposition="top right", name="Interceptação"))
                
                st.success(f"✅ OPERAÇÃO CONCLUÍDA: O objeto '{alvo_defesa}' foi desviado em {fator_desvio*100:,.1f} mil quilômetros da linha de entrada atmosférica da Terra.")
            
            fig_trajetoria.update_layout(
                paper_bgcolor='#0E1117', plot_bgcolor='#0E1117', font_color='white',
                margin=dict(l=10, r=10, b=10, t=20), height=260,
                xaxis=dict(range=[-5, 5], showgrid=True, gridcolor='#1E293B'), 
                yaxis=dict(range=[-1.5, 2.5], showgrid=True, gridcolor='#1E293B')
            )
            st.plotly_chart(fig_trajetoria, use_container_width=True)

    # --- FOOTER INSTITUCIONAL ---
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #475569; font-size: 11px; letter-spacing: 1px;'>SISTEMA MILITAR INTEGRADO AEGIS - CENTRO DE DEFESA PLANETÁRIA INTERNACIONAL © 2026 // ACESSO RESTRITO</p>", unsafe_allow_html=True)

# Controle de Fluxo Root
if not st.session_state['authenticated']:
    login_page()
else:
    main_dashboard()
