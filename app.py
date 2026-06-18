import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import time

# =====================================================================
# 1. ORQUESTRAÇÃO DE DESIGN E COMPORTAMENTO VISUAL (CSS AVANÇADO)
# =====================================================================
st.set_page_config(
    page_title="AEGIS | NASA Deep Space & Planetary Defense",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Customização profunda para simular o ambiente escuro e técnico das salas de controle aeroespaciais
st.markdown("""
    <style>
        .reportview-container .main .block-container { padding-top: 1.5rem; }
        h1, h2, h3, h4 { font-family: 'Space Grotesk', 'Segoe UI', sans-serif; font-weight: 700; color: #F8FAFC; }
        
        /* Customização dos cartões táticos de métricas */
        div[data-testid="stMetricValue"] { font-size: 32px !important; font-weight: 800; color: #00E5FF; letter-spacing: -0.5px; }
        div[data-testid="stMetricDelta"] { font-size: 12px !important; }
        
        /* Containers de Alta Densidade (Premium Cards) */
        .card-painel {
            background-color: #0B0F17;
            border: 1px solid #1E293B;
            padding: 24px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        }
        
        /* Blocos explicativos obrigatórios exigidos pela Gestão */
        .manual-box {
            background-color: #0F172A;
            border-left: 4px solid #38BDF8;
            padding: 15px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 20px;
        }
        .manual-title { color: #38BDF8; font-weight: bold; margin-bottom: 5px; font-size: 14px; }
        .manual-text { color: #94A3B8; font-size: 13px; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# --- CONTROLE ESTÁVEL DE SESSÃO ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# =====================================================================
# 2. PROTOTIPAGEM DO NÓ DE SEGURANÇA (BYPASS DE PROXY)
# =====================================================================
def login_page():
    st.markdown("<h1 style='text-align: center; color: #FF2E93; margin-top: 5rem; margin-bottom: 0;'>🛡️ A.E.G.I.S.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B; font-size: 15px; letter-spacing: 1px;'>Advanced Planetary Defense & Galactic Intelligence System</p>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
        with st.form("aegis_secure_login"):
            st.markdown("### **Autenticação Biométrica / Chave Operacional**")
            st.markdown("<p style='color: #94A3B8; font-size: 12px;'>Acesso restrito a engenheiros e cientistas nível 5. Conexão direta via cluster interno criptografado.</p>", unsafe_allow_html=True)
            user = st.text_input("Identificador do Operador", "nasa_chief_commander")
            password = st.text_input("Token Criptográfico", type="password")
            submitted = st.form_submit_button("DESBLOQUEAR TERMINAL CRÍTICO")
            
            if submitted:
                if user == "nasa_chief_commander" and password == "orion2026":
                    st.session_state['authenticated'] = True
                    st.success("🔒 Chave validada com sucesso. Ignorando intermediários de rede. Inicializando AEGIS Core...")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("❌ Credenciais inválidas. Tentativa registrada no Zabbix Central.")
        st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 3. CONSTRUTOR DO ECOSSISTEMA PRINCIPAL (MISSION CONTROL)
# =====================================================================
def main_dashboard():
    # --- CABEÇALHO TÁTICO INSTITUCIONAL ---
    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.markdown("<p style='color: #FF2E93; font-size: 12px; font-weight: bold; letter-spacing: 2px; margin-bottom: 0;'>🚨 SECURE PIPELINE // LIVE DATA LINK COHERENT</p>", unsafe_allow_html=True)
        st.title("🛰️ AEGIS Operational Command Center")
    with header_col2:
        st.write("")
        st.markdown("<div style='text-align: right; color: #64748B; font-size: 12px; line-height: 1.4;'>SISTEMA MILITAR INTEGRADO<br>NÓ DE CONTROLE PLANETÁRIO // V5.0</div>", unsafe_allow_html=True)
    
    st.markdown("---")

    # --- CONTROLADORES DA SIDEBAR LATERAL ---
    st.sidebar.markdown("### 🌌 Configuração de Escopo")
    st.sidebar.markdown("Selecione o setor estelar profundo para direcionar os espelhos coletores infravermelhos:")
    
    target_option = st.sidebar.selectbox(
        "Setor Ativo (Varredura de Sinais):",
        ["Sector 1: Kepler-10", "Sector 2: Pi Mensae", "Sector 3: TRAPPIST-1", "Sector 4: Anomalia KH-2026"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📡 Status de Conectividade")
    st.sidebar.success("● Pipeline de Ingestão: 4.2 TB/s")
    st.sidebar.success("● Sensores Criogênicos: OPERACIONAIS")
    st.sidebar.info("● Firewall Corporal: BYPASS ATIVO")

    # Mapeamento estrito para evitar bugs de chaves vazias ou falta de colunas
    tic_map = {
        "Sector 1: Kepler-10": "119041565",
        "Sector 2: Pi Mensae": "261136665",
        "Sector 3: TRAPPIST-1": "27877559",
        "Sector 4: Anomalia KH-2026": "88843211"
    }
    target_tic = tic_map[target_option]

    # --- INICIALIZAÇÃO DAS NAVES DE INTERFACE (ABAS DE EXPLICABILIDADE) ---
    tab_exoplanetas, tab_telescopios, tab_defesa = st.tabs([
        "🌌 1. Triagem de Exoplanetas & Anomalias",
        "🛰️ 2. Monitoramento de Saúde da Frota",
        "☄️ 3. Central de Defesa Planetária Avançada"
    ])

    # =====================================================================
    # ABA 1: TRIAGEM DE EXOPLANETAS
    # =====================================================================
    with tab_exoplanetas:
        st.markdown("### 🔬 Pipeline de Inteligência em Sinais de Órbita Profunda")
        
        st.markdown("""
        <div class='manual-box'>
            <div class='manual-title'>📘 DIRETRIZ OPERACIONAL - O QUE É, COMO FUNCIONA E PARA QUE SERVE</div>
            <div class='manual-text'>
                <b>O que é:</b> Um analisador estatístico de fotometria profunda automatizado por algoritmos de Machine Learning.<br>
                <b>Como funciona:</b> O sistema varre o fluxo luminoso de estrelas distantes. Quedas periódicas na recepção de fótons indicam corpos ocultos obstruindo o brilho. O gráfico mapeia a estabilidade temporal do fluxo vs desvio padrão térmico.<br>
                <b>Para que serve:</b> Identificar de forma proativa exoplanetas candidatos à colonização ou anomalias estruturais massivas que possam interferir em medições astronômicas.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Grid de Performance
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Fluxo de Dados Analisados", "4.2 TB/s", "+14% vs ontem")
        m2.metric("Sinais Varridos (Ciclo Atual)", "142.805", "Concluído")
        m3.metric("Anomalias Críticas Isoladas", "3", "Atenção Crítica")
        m4.metric("Precisão do Modelo de IA", "99.42%", "Deep Learning V4")
        
        # Banco de Dados Seguro da Fila Ativa
        estrelas_data = {
            "ID da Estrela": ["TIC 119041565", "TIC 261136665", "TIC 27877559", "TIC 88843211"],
            "Telescópio": ["Kepler (NASA)", "TESS (NASA)", "James Webb (NASA)", "TESS (NASA)"],
            "Desvio Padrão (σ)": [4.2, 8.9, 1.2, 25.4],
            "Confiança da IA": ["94.2%", "88.0%", "12.5%", "99.8%"],
            "Classificação do Sinal": ["Exoplaneta Candidato", "Exoplaneta Candidato", "Ruído Instrumental", "Anomalia Não Identificada"]
        }
        df_triagem = pd.DataFrame(estrelas_data)
        
        st.markdown("#### Fila Ativa de Sinais Isolados para Auditoria Humana")
        st.dataframe(df_triagem, use_container_width=True, hide_index=True)
        
        col_mapa, col_dados = st.columns([1, 1])
        
        with col_mapa:
            st.markdown("#### 🌐 Localização Tridimensional do Setor Estelar")
            np.random.seed(42)
            n_stars = 100
            df_stars = pd.DataFrame({
                'Coordenada X': np.random.randn(n_stars) * 15,
                'Coordenada Y': np.random.randn(n_stars) * 15,
                'Coordenada Z': np.random.randn(n_stars) * 8,
                'Luminosidade': np.random.rand(n_stars) * 100,
                'Raio Estelar': np.random.rand(n_stars) * 14
            })
            fig_3d = go.Figure(data=[go.Scatter3d(
                x=df_stars['Coordenada X'], y=df_stars['Coordenada Y'], z=df_stars['Coordenada Z'], mode='markers',
                marker=dict(size=df_stars['Raio Estelar'], color=df_stars['Luminosidade'], colorscale='Plasma', opacity=0.85)
            )])
            fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0), paper_bgcolor='#0B0F17', plot_bgcolor='#0B0F17', font_color='white', height=380)
            st.plotly_chart(fig_3d, use_container_width=True)
            
        with col_dados:
            st.markdown(f"#### 📊 Análise Multimodal de Espectro // TIC {target_tic}")
            
            tempo = np.linspace(0, 10, 500)
            # Busca defensiva baseada no mapeamento da sidebar para eliminar erros em tempo de execução
            row_alvo = df_triagem[df_triagem["ID da Estrela"] == f"TIC {target_tic}"].iloc[0]
            
            if "Anomalia" in row_alvo["Classificação do Sinal"]:
                fluxo = 1.0 + np.random.randn(500) * 0.003
                fluxo[150:280] -= np.linspace(0, 0.06, 130)
                fluxo[400:450] += np.random.randn(50) * 0.015
                cor_grafico = '#FF2E93'
            elif "Exoplaneta" in row_alvo["Classificação do Sinal"]:
                fluxo = 1.0 + np.random.randn(500) * 0.001
                fluxo[200:300] -= 0.022
                cor_grafico = '#00E5FF'
            else:
                fluxo = 1.0 + np.random.randn(500) * 0.007
                cor_grafico = '#64748B'
                
            df_plot = pd.DataFrame({"Tempo (Dias)": tempo, "Fluxo Relativo": fluxo})
            fig_lc = px.line(df_plot, x='Tempo (Dias)', y='Fluxo Relativo', color_discrete_sequence=[cor_grafico])
            fig_lc.update_layout(paper_bgcolor='#0B0F17', plot_bgcolor='#0B0F17', font_color='white', height=350, margin=dict(t=15, b=15))
            st.plotly_chart(fig_lc, use_container_width=True)

    # =====================================================================
    # ABA 2: MONITORAMENTO DA FROTA (TELESCOPIOS)
    # =====================================================================
    with tab_telescopios:
        st.markdown("### 🛰️ Telemetria de Saúde e Logística dos Observatórios Espaciais")
        
        st.markdown("""
        <div class='manual-box'>
            <div class='manual-title'>📘 DIRETRIZ OPERACIONAL - O QUE É, COMO FUNCIONA E PARA QUE SERVE</div>
            <div class='manual-text'>
                <b>O que é:</b> Um hub de telemetria física em tempo real para monitoramento das condições estruturais das nossas sondas orbitais.<br>
                <b>Como funciona:</b> Coleta dados de sensores embarcados de temperatura térmica profunda e nível volumétrico de tanques de hidrazina via link de rádio de banda X.<br>
                <b>Para que serve:</b> Evitar a perda de capacidade de varredura profunda. Picos térmicos em sensores infravermelhos invalidam dados científicos instantaneamente.
            </div>
        </div>
        """, unsafe_allow_html=True)
            
        t1, t2, t3 = st.columns(3)
        
        with t1:
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            st.markdown("#### **Observatório TESS**")
            st.caption("Transiting Exoplanet Survey Satellite")
            st.metric("Status Operacional", "ONLINE", delta="Estável // Coleta Ativa")
            st.progress(0.74, text="Nível de Hidrazina (RCS): 74%")
            st.metric("Temperatura da Câmera Core", "-80.2 °C", delta="Nominal")
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
            st.text("Dados unificados indexados localmente para mitigar problemas com proxies lentos.")
            st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================================
    # ABA 3: DEFESA PLANETÁRIA (A GRANDE INOVAÇÃO CIENTÍFICA)
    # =====================================================================
    with tab_defesa:
        st.markdown("### ☄️ Centro de Monitoramento de NEOs (Near-Earth Objects) & Deflexão Mecânica Ativa")
        
        st.markdown("""
        <div class='manual-box'>
            <div class='manual-title'>📘 DIRETRIZ OPERACIONAL - O QUE É, COMO FUNCIONA E PARA QUE SERVE</div>
            <div class='manual-text'>
                <b>O que é:</b> A maior e mais densa matriz de rastreamento de rochas espaciais e bólidos em rota de aproximação com a Terra, equipada com um simulador computacional balístico.<br>
                <b>Como funciona:</b> A tabela compila variáveis astronômicas fundamentais (Diâmetro, Velocidade Relativa, Distância Mínima em Unidades Lunares, Período Orbital e Magnitude Absoluta H). O simulador dinâmico à direita calcula as leis de transferência de momentum cinético com base em contra-medidas propostas.<br>
                <b>Para que serve:</b> Mitigar catástrofes em escala global. Permite testar armas mecânicas e lasers térmicos antes do bólido atingir o ponto de não-retorno orbital.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # BASE DE DADOS MASSIVA EXPANDIDA - MÚLTIPLOS CORPOS CELESTES REAIS E SIMULADOS
        meteoros_expandidos = {
            "Designação NEO": [
                "99942 Apophis (2004 MN4)", "101955 Bennu (1999 RQ36)", "4179 Toutatis", "Corpo Hiperbólico PHA-2026", 
                "162173 Ryugu", "2023 NT1", "Fragmento de Meteoro M-102", "Fragmento 2026-XC4", 
                "Meteoro Rápido BEN-10", "C/2026 A1 (Cometa Siding)", "2024 BX1", "1950 DA (Alta Massa)"
            ],
            "Diâmetro Est. (m)": [370, 492, 5400, 850, 900, 30, 45, 145, 3, 1200, 12, 1100],
            "Velocidade Relativa (km/h)": [110200, 101000, 39600, 145000, 78000, 86000, 48000, 67000, 82000, 212000, 45000, 61000],
            "Distância Mínima (LD)": [0.12, 0.54, 1.80, 0.04, 3.10, 0.25, 2.50, 4.50, 0.01, 5.20, 1.40, 0.85],
            "Mag. Absoluta (H)": [19.2, 20.8, 15.3, 17.1, 18.1, 24.5, 23.1, 21.4, 29.1, 14.2, 26.8, 16.9],
            "Período Orbital (Dias)": [323, 436, 1450, 620, 474, 390, 280, 510, 120, 4500, 310, 792],
            "Próxima Aproximação": ["13/04/2029", "24/09/2037", "05/11/2032", "18/07/2026", "12/12/2027", "14/07/2028", "22/08/2026", "30/10/2026", "Imediata", "04/02/2027", "Concluída", "16/03/2880"],
            "Escala Torino": [2, 1, 0, 8, 0, 1, 1, 1, 0, 4, 0, 3],
            "Estação de Varredura": ["Goldstone Radar", "Pan-STARRS 1", "Arecibo Node", "AEGIS DeepSpace", "NEOWISE Space", "Mount Lemmon", "Zwicky Transient", "Pan-STARRS 2", "Siding Spring", "Hubble Core", "Catalina Sky", "AEGIS DeepSpace"],
            "Risco Classificado": ["Atenção Orbital", "Baixo Risco", "Nulo (Seguro)", "Ameaça Crítica Regional", "Nulo (Seguro)", "Monitoramento", "Baixo Risco", "Baixo Risco", "Queima Atmosférica", "Risco em Potencial", "Nulo (Passou)", "Atenção de Longo Prazo"]
        }
        df_meteoros = pd.DataFrame(meteoros_expandidos)
        
        st.markdown("#### 📊 Matriz Global de Rastreamento Activa (NEO Advanced Ledger)")
        # Uso do dataframe interativo moderno com paginação automática integrada
        st.dataframe(df_meteoros, use_container_width=True, hide_index=True)
        
        st.markdown("---")

        # CONSTRUÇÃO DO LAYOUT EM COLUNAS EQUILIBRADAS: RADAR VS TERMINAL CIBERNÉTICO
        col_radar, col_simulador = st.columns([1.1, 1])
        
        with col_radar:
            st.markdown("#### 🌐 1. Radar de Aproximação de Trajetórias (Visão Geral)")
            st.caption("Posicionamento em tempo real relativo à órbita geoestacionária terrestre em Unidades Lunares (1 LD ≈ 384.400 km).")
            
            # Puxamos os alvos principais para evitar superpopulação e quebra de renderização no gráfico de espalhamento
            df_plot_radar = df_meteoros.head(6)
            
            fig_radar = go.Figure()
            # Origem estável do plano cartesiano orbital: O planeta Terra
            fig_radar.add_trace(go.Scatter(
                x=[0], y=[0], mode='markers+text', 
                marker=dict(size=36, color='#00E5FF', line=dict(width=2, color='white')), 
                text=["TERRA"], textposition="top center", name="Centro"
            ))
            
            x_coords = [1.2, -0.4, -2.2, 0.06, 2.9, -0.7]
            y_coords = [0.8, 0.50, 1.4, -0.04, -1.3, -0.3]
            
            fig_radar.add_trace(go.Scatter(
                x=x_coords, y=y_coords, mode='markers+text',
                marker=dict(
                    size=df_plot_radar["Diâmetro Est. (m)"]/22 + 16, 
                    color=df_plot_radar["Escala Torino"], 
                    colorscale='Reds', 
                    showscale=True, 
                    colorbar=dict(title="Escala Torino")
                ),
                text=df_plot_radar["Designação NEO"], textposition="bottom center", name="Objetos Monitorados"
            ))
            fig_radar.update_layout(
                paper_bgcolor='#0B0F17', plot_bgcolor='#0B0F17', font_color='white',
                margin=dict(l=10, r=10, b=10, t=20), height=440,
                xaxis=dict(showgrid=True, gridcolor='#1E293B', zeroline=True, zerolinecolor='#334155', range=[-4, 4]),
                yaxis=dict(showgrid=True, gridcolor='#1E293B', zeroline=True, zerolinecolor='#334155', range=[-3, 3])
            )
            st.plotly_chart(fig_radar, use_container_width=True)
            
        with col_simulador:
            st.markdown("#### 💥 2. Simulador Interativo de Deflexão Cinética")
            st.caption("Calcule dinamicamente a energia cinética necessária para deflexão mecânica.")
            
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            alvo_defesa = st.selectbox("Selecione o Vetor de Ameaça Ativo:", df_meteoros["Designação NEO"])
            arma = st.radio("Selecione o Tipo de Contra-Medida Proposta:", [
                "🚀 Sonda de Impacto Cinético (Estilo NASA DART)", 
                "🛰️ Laser Térmico de Superfície Estacionário Orbital", 
                "💥 Dispositivo de Pulso Nuclear de Desvio Coerente"
            ])
            potencia = st.slider("Massa / Potência de Energia do Vetor (Toneladas ou MW):", 10, 500, 200)
            
            simular_impacto = st.button("💥 INICIAR CÁLCULO DE DEFLEXÃO")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Trajetória balística projetada em polinômio quadrático estável
            tempo_trajetoria = np.linspace(-5, 5, 200)
            y_original = (tempo_trajetoria ** 2) * 0.15 - 0.25
            
            fig_trajetoria = go.Figure()
            fig_trajetoria.add_trace(go.Scatter(x=[0], y=[0], mode="markers+text", marker=dict(size=35, color="#00E5FF"), text=["TERRA"], textposition="top center", name="Terra"))
            fig_trajetoria.add_trace(go.Scatter(x=tempo_trajetoria, y=y_original, mode="lines", name="Trajetória Original", line=dict(color="#FF2E93", width=2, dash="dash")))
            
            if simular_impacto:
                # Função de transferência de massa-momentum simulada
                fator_desvio = (potencia / 100) * 0.48
                if "Nuclear" in arma:
                    fator_desvio *= 1.80
                elif "Laser" in arma:
                    fator_desvio *= 1.15
                    
                y_desviada = y_original + fator_desvio
                
                fig_trajetoria.add_trace(go.Scatter(x=tempo_trajetoria, y=y_desviada, mode="lines", name="Nova Rota Calculada", line=dict(color="#00FF66", width=4)))
                fig_trajetoria.add_trace(go.Scatter(x=[-1.8], y=[0.4], mode="markers+text", marker=dict(size=14, color="#FFFF00", symbol="star"), text=["💥 INTERCEPTAÇÃO"], textposition="top right"))
                
                st.success(f"✅ OPERAÇÃO CONCLUÍDA: O desvio cinético modificado afastou o objeto '{alvo_defesa}' em +{(fator_desvio*100):,.1f} mil quilômetros da atmosfera terrestre.")
            
            fig_trajetoria.update_layout(
                paper_bgcolor='#0B0F17', plot_bgcolor='#0B0F17', font_color='white',
                margin=dict(l=10, r=10, b=10, t=20), height=230,
                xaxis=dict(range=[-5, 5], showgrid=True, gridcolor='#1E293B'), 
                yaxis=dict(range=[-1.5, 2.5], showgrid=True, gridcolor='#1E293B')
            )
            st.plotly_chart(fig_trajetoria, use_container_width=True)

    # --- FOOTER CORPORATIVO DE SEGURANÇA ---
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #334155; font-size: 11px; letter-spacing: 1px;'>SISTEMA MILITAR INTEGRADO AEGIS - CENTRO DE DEFESA PLANETÁRIA INTERNACIONAL © 2026 // ACESSO RESTRITO</p>", unsafe_allow_html=True)

# Inicialização segura controlada por estado
if not st.session_state['authenticated']:
    login_page()
else:
    main_dashboard()
