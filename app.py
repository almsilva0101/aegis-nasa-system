import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import time

# ==========================================
# 1. CONFIGURAÇÃO INTERNA E ESTILIZAÇÃO (CSS COGNITIVO)
# ==========================================
st.set_page_config(
    page_title="AEGIS | NASA Deep Space & Planetary Defense",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Injeção de CSS customizado para transformar o Streamlit em um painel militar/científico
st.markdown("""
    <style>
        /* Ajustes de espaçamento globais */
        .reportview-container .main .block-container { padding-top: 2rem; }
        h1, h2, h3, h4 { font-family: 'Space Grotesk', 'Segoe UI', sans-serif; font-weight: 700; }
        
        /* Customização dos blocos nativos de métricas */
        div[data-testid="stMetricValue"] { font-size: 30px !important; font-weight: bold; color: #00E5FF; }
        div[data-testid="stMetricDelta"] { font-size: 13px !important; }
        
        /* Container de Cartão Premium para Controles e Status */
        .card-painel {
            background-color: #0E1117;
            border: 1px solid #1E293B;
            padding: 22px;
            border-radius: 8px;
            margin-bottom: 15px;
        }
        
        /* Destaque para logs do sistema */
        .system-log {
            font-family: 'Courier New', Courier, monospace;
            font-size: 12px;
            color: #38BDF8;
            background-color: #020617;
            padding: 10px;
            border-left: 3px solid #38BDF8;
            border-radius: 4px;
        }
    </style>
""", unsafe_allow_html=True)

# --- CONTROLE DE SESSÃO / SEGURANÇA ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def login_page():
    st.markdown("<h1 style='text-align: center; color: #FF2E93; margin-bottom: 0;'>🛡️ A.E.G.I.S.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 16px;'>Advanced Planetary Defense & Galactic Intelligence System</p>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2, col3 = st.columns([1, 1.4, 1])
    with col2:
        st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
        with st.form("aegis_login"):
            st.markdown("### **Autenticação de Operador // Nível de Acesso 5**")
            user = st.text_input("ID do Operador (Username)", "nasa_operator_01")
            password = st.text_input("Chave Criptográfica (Password)", type="password")
            submitted = st.form_submit_button("VALIDAR CREDENCIAIS DE DEFESA")
            
            if submitted:
                if user == "nasa_operator_01" and password == "artemis2026":
                    st.session_state['authenticated'] = True
                    st.success("🔒 Chave de encriptação validada. Conectando aos clusters Deep Space...")
                    time.sleep(0.6)
                    st.rerun()
                else:
                    st.error("❌ Falha crítica de autenticação. Acesso negado e registrado.")
        st.markdown("</div>", unsafe_allow_html=True)

def main_dashboard():
    # --- CABEÇALHO TÉCNICO ---
    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.markdown("<p style='color: #FF2E93; font-size: 13px; font-weight: bold; letter-spacing: 2px; margin-bottom: 0;'>🚨 SECURE COMMAND NODE // DATA STREAM ACTIVE</p>", unsafe_allow_html=True)
        st.title("🛰️ AEGIS Operational Command Center")
    with header_col2:
        st.write("")
        st.write("")
        st.markdown("<div style='text-align: right; color: #64748B; font-size: 12px;'>SISTEMA DE DEFESA INTEGRADO<br>VERSÃO 4.9.0 // TOTAL UPGRADE</div>", unsafe_allow_html=True)
    
    st.markdown("---")

    # --- BARRA LATERAL (SIDEBAR TÁTICA) ---
    st.sidebar.markdown("### 🌌 Escopo de Varredura")
    st.sidebar.markdown("Filtros operacionais aplicados à ingestão de dados de satélite:")
    
    target_option = st.sidebar.selectbox(
        "Estrela Alvo Ativa (Aba 1):",
        ["Sector 1: Kepler-10 (Telescópio Kepler)", "Sector 2: Pi Mensae (Telescópio TESS)", "Sector 3: TRAPPIST-1 (Telescópio JWST)", "Sector 4: Alvo Desconhecido (Anomalia Crítica)"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📡 Status de Conectividade")
    st.sidebar.success("● Link de Satélite Deep Space: ONLINE")
    st.sidebar.success("● Pipeline de IA (Lightkurve V4): OPERACIONAL")
    st.sidebar.info("● Ingestão de Dados Real: 4.2 TB/s")

    # Mapeamento interno do alvo da Sidebar
    tic_map = {
        "Sector 1: Kepler-10 (Telescópio Kepler)": "119041565",
        "Sector 2: Pi Mensae (Telescópio TESS)": "261136665",
        "Sector 3: TRAPPIST-1 (Telescópio JWST)": "27877559",
        "Sector 4: Alvo Desconhecido (Anomalia Crítica)": "88843211"
    }
    target_tic = tic_map[target_option]

    # --- MONTAGEM DAS ABAS DA PLATAFORMA ---
    tab_exoplanetas, tab_telescopios, tab_defesa = st.tabs([
        "🌌 1. Triagem de Exoplanetas & Anomalias",
        "🛰️ 2. Monitoramento de Saúde da Frota",
        "☄️ 3. Central de Defesa Planetária Avançada"
    ])

    # ==========================================
    # ABA 1: TRIAGEM DE EXOPLANETAS
    # ==========================================
    with tab_exoplanetas:
        st.markdown("### 🔬 Pipeline de Inteligência em Sinais de Órbita Profunda")
        
        with st.expander("📘 Manual de Operação e Glossário Técnico (Clique para expandir)"):
            st.markdown("""
            * **Fila de Triagem:** Centraliza alvos onde os algoritmos estatísticos da IA detectaram flutuações anormais de fluxo luminoso.
            * **Desvio Padrão (σ):** Mede a variabilidade estatística da luz. Um $\sigma$ muito alto isola mudanças agressivas na emissão de energia (potencial trânsito ou anomalia estrutural).
            * **Curva de Luz:** Gráfico do fluxo de fótons ao longo do tempo. Quedas em formato côncavo periódico revelam corpos planetários obstruindo a luz da estrela mãe.
            """)
        
        # Grid de Métricas Superiores
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Fluxo de Dados Analisados", "4.2 TB/s", "+12% vs ontem")
        m2.metric("Sinais Varridos (Ciclo)", "142.805", "Fase Concluída")
        m3.metric("Anomalias Críticas Isoladas", "3", "Atenção")
        m4.metric("Precisão Geral do Modelo", "99.42%", "Deep Learning V4")
        
        # DataFrame de Triagem Estelar
        estrelas_data = {
            "ID da Estrela": ["TIC 119041565", "TIC 261136665", "TIC 27877559", "TIC 88843211"],
            "Telescópio": ["Kepler (NASA)", "TESS (NASA)", "James Webb (NASA)", "TESS (NASA)"],
            "Desvio Padrão (σ)": [4.2, 8.9, 1.2, 25.4],
            "Confiança IA": ["94.2%", "88.0%", "12.5%", "99.8%"],
            "Status": ["Exoplaneta Candidato", "Exoplaneta Candidato", "Ruído Instrumental", "Anomalia Não Identificada"]
        }
        df_triagem = pd.DataFrame(estrelas_data)
        
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
            dados_alvo = df_triagem[df_triagem["ID da Estrela"] == f"TIC {target_tic}"].iloc[0]
            
            if "Anomalia" in dados_alvo["Status"]:
                fluxo = 1.0 + np.random.randn(800) * 0.004
                fluxo[250:350] -= np.linspace(0, 0.08, 100)
                fluxo[600:650] += np.random.randn(50) * 0.02
                cor_grafico = '#FF2E93'
            elif "Exoplaneta" in dados_alvo["Status"]:
                fluxo = 1.0 + np.random.randn(800) * 0.001
                fluxo[350:450] -= 0.018
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
            * **Temperatura Criogênica:** Sensores infravermelhos exigem resfriamento absoluto (perto de 0 Kelvin). Qualquer pico térmico gera ruído destrutivo nos dados estelares.
            * **Combustível Restante:** Crucial para acionamento de propulsores RCS para estabilização de órbita e desvios contra lixo espacial.
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
    # ABA 3: DEFESA PLANETÁRIA (VERSÃO COMPLETA MASSIVA)
    # ==========================================
    with tab_defesa:
        st.markdown("### ☄️ Centro de Monitoramento de NEOs (Near-Earth Objects) & Deflexão Proativa")
        
        with st.expander("📘 Fundamentos Técnicos e Variáveis Astronômicas Avançadas"):
            st.markdown("""
            * **Distância Mínima (LD - Lunar Distance):** Medida em Unidades Lunares. $1 \\text{ LD} \\approx 384.400 \\text{ km}$.
            * **Escala de Torino:** Classificação de perigo de 0 a 10. Valores acima de 5 indicam riscos graves de destruição em massa.
            * **Magnitude Absoluta (H):** O brilho intrínseco de um corpo celeste. Quanto menor o valor de H, maior é a rocha espacial.
            * **Física de Deflexão Cinética:** Simula a transferência de momentum (Missão NASA DART). Um impacto cirúrgico a milhões de quilômetros altera a velocidade orbital em milímetros por segundo, criando desvios massivos ao longo do tempo.
            """)

        # --- A MAIOR E MAIS REALISTA MATRIZ DE RASTREAMENTO NEO ---
        meteoros_expandidos = {
            "Designação NEO": [
                "99942 Apophis (2004 MN4)", "101955 Bennu (1999 RQ36)", "4179 Toutatis", "(2026 PHA-2) Crítico", 
                "162173 Ryugu", "2023 NT1", "Meteoro-X M-102", "Fragmento 2026-XC4", 
                "Meteoro Rápido BEN-10", "C/2026 A1 (Cometa Siding)", "2024 BX1", "1950 DA (Ameaça Seg)"
            ],
            "Diâmetro Est. (m)": [370, 492, 5400, 850, 900, 30, 45, 145, 3, 1200, 12, 1100],
            "Velocidade Relativa (km/h)": [110200, 101000, 39600, 145000, 78000, 86000, 48000, 67000, 82000, 212000, 45000, 61000],
            "Distância Mínima (LD)": [0.12, 0.54, 1.80, 0.04, 3.10, 0.25, 2.50, 4.50, 0.01, 5.20, 1.40, 0.85],
            "Mag. Absoluta (H)": [19.2, 20.8, 15.3, 17.1, 18.1, 24.5, 23.1, 21.4, 29.1, 14.2, 26.8, 16.9],
            "Período Orbital (Dias)": [323, 436, 1450, 620, 474, 390, 280, 510, 120, 4500, 310, 792],
            "Próxima Aproximação": ["13/04/2029", "24/09/2037", "05/11/2032", "18/07/2026", "12/12/2027", "14/07/2028", "22/08/2026", "30/10/2026", "Imediata", "04/02/2027", "Concluída", "16/03/2880"],
            "Escala Torino": [2, 1, 0, 8, 0, 1, 1, 1, 0, 4, 0, 3],
            "Estação de Varredura Terrestre": ["Goldstone Radar", "Pan-STARRS 1", "Arecibo Node", "AEGIS DeepSpace", "NEOWISE Space", "Mount Lemmon", "Zwicky Transient", "Pan-STARRS 2", "Siding Spring", "Hubble Core", "Catalina Sky", "AEGIS DeepSpace"],
            "Classificação de Risco": ["Atenção Orbital", "Baixo Risco", "Nulo (Seguro)", "Ameaça Crítica Regional", "Nulo (Seguro)", "Monitoramento", "Baixo Risco", "Baixo Risco", "Queima Atmosférica", "Risco em Potencial", "Nulo (Passou)", "Atenção de Longo Prazo"]
        }
        df_meteoros = pd.DataFrame(meteoros_expandidos)
        
        st.markdown("#### 📊 Matriz Global de Rastreamento Activa (NEO Advanced Ledger)")
        # Exibição nativa moderna em alta densidade, interativa e paginada
        st.dataframe(df_meteoros, use_container_width=True, hide_index=True)
        
        st.markdown("---")

        # CONFIGURAÇÃO DE LAYOUT EM DUAS COLUNAS EQUILIBRADAS
        col_radar, col_simulador = st.columns([1.1, 1])
        
        with col_radar:
            st.markdown("#### 🌐 1. Radar de Aproximação de Trajetórias (Visão Macro)")
            st.caption("Mapeamento espacial radial relativo à órbita geoestacionária terrestre em Unidades Lunares (LD).")
            
            # Puxamos os 6 objetos mais importantes para evitar sobreposição poluída no Radar
            df_plot_radar = df_meteoros.head(6)
            
            fig_radar = go.Figure()
            # Ponto Central: A Terra
            fig_radar.add_trace(go.Scatter(
                x=[0], y=[0], mode='markers+text', 
                marker=dict(size=35, color='#00E5FF', line=dict(width=2, color='white')), 
                text=["TERRA"], textposition="top center", name="Ponto Zero (Terra)"
            ))
            # Coordenadas polares projetadas em plano bidimensional cartesiano para visualização limpa
            x_coords = [1.1, -0.3, -2.1, 0.05, 2.8, -0.6]
            y_coords = [0.7, 0.45, 1.3, -0.03, -1.2, -0.2]
            
            fig_radar.add_trace(go.Scatter(
                x=x_coords, y=y_coords, mode='markers+text',
                marker=dict(
                    size=df_plot_radar["Diâmetro Est. (m)"]/20 + 15, 
                    color=df_plot_radar["Escala Torino"], 
                    colorscale='Reds', 
                    showscale=True, 
                    colorbar=dict(title="Torino")
                ),
                text=df_plot_radar["Designação NEO"], textposition="bottom center", name="Objetos Críticos"
            ))
            fig_radar.update_layout(
                paper_bgcolor='#0E1117', plot_bgcolor='#0E1117', font_color='white',
                margin=dict(l=10, r=10, b=10, t=20), height=440,
                xaxis=dict(showgrid=True, gridcolor='#1E293B', zeroline=True, zerolinecolor='#334155', range=[-4, 4]),
                yaxis=dict(showgrid=True, gridcolor='#1E293B', zeroline=True, zerolinecolor='#334155', range=[-3, 3])
            )
            st.plotly_chart(fig_radar, use_container_width=True)
            
        with col_simulador:
            st.markdown("#### 💥 2. Terminal Interativo de Mitigação e Deflexão")
            st.caption("Calcule dinamicamente a energia cinética necessária para deflexão mecânica.")
            
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            alvo_defesa = st.selectbox("Selecione o Vetor de Ameaça Ativo:", df_meteoros["Designação NEO"])
            arma = st.radio("Vetor de Contra-Medida Proposto:", [
                "🚀 Sonda Impactor Cinemático (Estilo NASA DART)", 
                "🛰️ Array de Laser Térmico Estacionário Orbital", 
                "💥 Dispositivo de Pulso Nuclear de Desvio"
            ])
            potencia = st.slider("Massa do Vetor / Output de Energia (Toneladas/MW):", 10, 500, 180)
            
            simular_impacto = st.button("💥 INICIAR CÁLCULO DE INTERCEPTAÇÃO")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Construção do gráfico balístico de vetores orbitais
            tempo_trajetoria = np.linspace(-5, 5, 200)
            y_original = (tempo_trajetoria ** 2) * 0.15 - 0.25
            
            fig_trajetoria = go.Figure()
            fig_trajetoria.add_trace(go.Scatter(x=[0], y=[0], mode="markers+text", marker=dict(size=35, color="#00E5FF"), text=["TERRA"], textposition="top center", name="Terra"))
            fig_trajetoria.add_trace(go.Scatter(x=tempo_trajetoria, y=y_original, mode="lines", name="Trajetória Original", line=dict(color="#FF2E93", width=2, dash="dash")))
            
            if simular_impacto:
                # Lógica de cálculo matemático do desvio com base na potência escolhida
                fator_desvio = (potencia / 100) * 0.45
                if "Nuclear" in arma:
                    fator_desvio *= 1.75
                elif "Laser" in arma:
                    fator_desvio *= 1.10
                    
                y_desviada = y_original + fator_desvio
                
                fig_trajetoria.add_trace(go.Scatter(x=tempo_trajetoria, y=y_desviada, mode="lines", name="Nova Rota Calculada", line=dict(color="#00FF66", width=4)))
                fig_trajetoria.add_trace(go.Scatter(x=[-2], y=[0.35], mode="markers+text", marker=dict(size=14, color="#FFFF00", symbol="star"), text=["💥 INTERCEPTAÇÃO"], textposition="top right"))
                
                st.success(f"✅ OPERAÇÃO CONCLUÍDA: O objeto '{alvo_defesa}' teve o seu vetor modificado em +{(fator_desvio*100):,.1f} mil km de distância radial da Terra.")
            
            fig_trajetoria.update_layout(
                paper_bgcolor='#0E1117', plot_bgcolor='#0E1117', font_color='white',
                margin=dict(l=10, r=10, b=10, t=20), height=240,
                xaxis=dict(range=[-5, 5], showgrid=True, gridcolor='#1E293B'), 
                yaxis=dict(range=[-1.5, 2.5], showgrid=True, gridcolor='#1E293B')
            )
            st.plotly_chart(fig_trajetoria, use_container_width=True)

    # --- RODAPÉ REGULAMENTAR ---
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #475569; font-size: 11px; letter-spacing: 1px;'>SISTEMA MILITAR INTEGRADO AEGIS - CENTRO DE DEFESA PLANETÁRIA INTERNACIONAL © 2026 // ACESSO RESTRITO</p>", unsafe_allow_html=True)

# Inicializador Root controlado pelo fluxo de login
if not st.session_state['authenticated']:
    login_page()
else:
    main_dashboard()
