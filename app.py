import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import time

# =====================================================================
# 1. CONFIGURAÇÃO DE DESIGN E ESTILIZAÇÃO (CSS AVANÇADO)
# =====================================================================
st.set_page_config(
    page_title="AEGIS | NASA Deep Space & Planetary Defense",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
        
        /* Blocos explicativos obrigatórios */
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

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def login_page():
    st.markdown("<h1 style='text-align: center; color: #FF2E93; margin-top: 5rem; margin-bottom: 0;'>🛡️ A.E.G.I.S.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B; font-size: 15px; letter-spacing: 1px;'>Advanced Planetary Defense & Galactic Intelligence System</p>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
        with st.form("aegis_secure_login"):
            st.markdown("### **Autenticação Biométrica / Chave Operacional**")
            user = st.text_input("Identificador do Operador", "nasa_chief_commander")
            password = st.text_input("Token Criptográfico", type="password")
            submitted = st.form_submit_button("DESBLOQUEAR TERMINAL CRÍTICO")
            
            if submitted:
                if user == "nasa_chief_commander" and password == "orion2026":
                    st.session_state['authenticated'] = True
                    st.success("🔒 Acesso autorizado. Inicializando AEGIS Core...")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("❌ Credenciais inválidas.")
        st.markdown("</div>", unsafe_allow_html=True)

def main_dashboard():
    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.markdown("<p style='color: #FF2E93; font-size: 12px; font-weight: bold; letter-spacing: 2px; margin-bottom: 0;'>🚨 SECURE PIPELINE // TRANSMISSÃO COERENTE ATIVA</p>", unsafe_allow_html=True)
        st.title("🛰️ AEGIS Operational Command Center")
    with header_col2:
        st.write("")
        st.markdown("<div style='text-align: right; color: #64748B; font-size: 12px; line-height: 1.4;'>SISTEMA OPERACIONAL DA NASA<br>NÓ CENTRAL DE MISSÃO // V7.0</div>", unsafe_allow_html=True)
    
    st.markdown("---")

    # BARRA LATERAL
    st.sidebar.markdown("### 🌌 Configuração de Escopo")
    target_option = st.sidebar.selectbox(
        "Setor Estelar Ativo (Aba 1):",
        ["Sector 1: Kepler-10", "Sector 2: Pi Mensae", "Sector 3: TRAPPIST-1", "Sector 4: Anomalia KH-2026"]
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📡 Status de Conectividade")
    st.sidebar.success("● Pipeline de Ingestão: 4.2 TB/s")
    st.sidebar.success("● Sensores Criogênicos: ONLINE")

    tic_map = {
        "Sector 1: Kepler-10": "119041565", "Sector 2: Pi Mensae": "261136665",
        "Sector 3: TRAPPIST-1": "27877559", "Sector 4: Anomalia KH-2026": "88843211"
    }
    target_tic = tic_map[target_option]

    tab_exoplanetas, tab_telescopios, tab_satelites, tab_defesa = st.tabs([
        "🌌 1. Triagem de Exoplanetas & Anomalias",
        "🛰️ 2. Telemetria Preditiva & Saúde de Frota",
        "🌍 3. Monitoramento Global de Satélites & APIs",
        "☄️ 4. Central de Defesa Planetária Avançada"
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
                <b>Como funciona:</b> O sistema varre o fluxo luminoso de estrelas distantes. Quedas periódicas na recepção de fótons indicam corpos ocultos obstruindo o brilho (Método do Trânsito).<br>
                <b>Para que serve:</b> Identificar de forma proativa exoplanetas candidatos à colonização ou anomalias estruturais massivas.<br>
                <b>Integração de API Pública:</b> Consome dados diretamente do <b>NASA Portal (JPL)</b> através do endpoint <code>api.nasa.gov/planetary/exoplanet</code>, que disponibiliza os dados consolidados do arquivo de exoplanetas da NASA.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        estrelas_data = {
            "ID da Estrela": ["TIC 119041565", "TIC 261136665", "TIC 27877559", "TIC 88843211"],
            "Telescópio": ["Kepler (NASA)", "TESS (NASA)", "James Webb (NASA)", "TESS (NASA)"],
            "Desvio Padrão (σ)": [4.2, 8.9, 1.2, 25.4],
            "Confiança da IA": ["94.2%", "88.0%", "12.5%", "99.8%"],
            "Classificação do Sinal": ["Exoplaneta Candidato", "Exoplaneta Candidato", "Ruído Instrumental", "Anomalia Não Identificada"]
        }
        df_triagem = pd.DataFrame(estrelas_data)
        st.dataframe(df_triagem, use_container_width=True, hide_index=True)
        
        col_mapa, col_dados = st.columns([1, 1])
        with col_mapa:
            st.markdown("#### 🌐 Localização Tridimensional do Setor Estelar")
            np.random.seed(42)
            n_stars = 50
            df_stars = pd.DataFrame({
                'X': np.random.randn(n_stars) * 15, 'Y': np.random.randn(n_stars) * 15, 'Z': np.random.randn(n_stars) * 8,
                'Luminosidade': np.random.rand(n_stars) * 100, 'Raio': np.random.rand(n_stars) * 12
            })
            fig_3d = go.Figure(data=[go.Scatter3d(
                x=df_stars['X'], y=df_stars['Y'], z=df_stars['Z'], mode='markers',
                marker=dict(size=df_stars['Raio'], color=df_stars['Luminosidade'], colorscale='Plasma', opacity=0.85)
            )])
            fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0), paper_bgcolor='#0B0F17', plot_bgcolor='#0B0F17', font_color='white', height=300)
            st.plotly_chart(fig_3d, use_container_width=True)
            
        with col_dados:
            st.markdown(f"#### 📊 Curva de Luz do Alvo // TIC {target_tic}")
            tempo = np.linspace(0, 10, 300)
            row_alvo = df_triagem[df_triagem["ID da Estrela"] == f"TIC {target_tic}"].iloc[0]
            if "Anomalia" in row_alvo["Classificação do Sinal"]:
                fluxo = 1.0 + np.random.randn(300) * 0.003
                fluxo[100:150] -= np.linspace(0, 0.06, 50)
                cor = '#FF2E93'
            elif "Exoplaneta" in row_alvo["Classificação do Sinal"]:
                fluxo = 1.0 + np.random.randn(300) * 0.001
                fluxo[120:180] -= 0.022
                cor = '#00E5FF'
            else:
                fluxo = 1.0 + np.random.randn(300) * 0.007
                cor = '#64748B'
            df_plot = pd.DataFrame({"Tempo (Dias)": tempo, "Fluxo Relativo": fluxo})
            fig_lc = px.line(df_plot, x='Tempo (Dias)', y='Fluxo Relativo', color_discrete_sequence=[cor])
            fig_lc.update_layout(paper_bgcolor='#0B0F17', plot_bgcolor='#0B0F17', font_color='white', height=270, margin=dict(t=10, b=10))
            st.plotly_chart(fig_lc, use_container_width=True)

    # =====================================================================
    # ABA 2: TELEMETRIA PREDITIVA
    # =====================================================================
    with tab_telescopios:
        st.markdown("### 🛰️ Monitoramento de Saúde da Frota via Gêmeo Digital Preditivo")
        st.markdown("""
        <div class='manual-box'>
            <div class='manual-title'>📘 DIRETRIZ OPERACIONAL - O QUE É, COMO FUNCIONA E PARA QUE SERVE</div>
            <div class='manual-text'>
                <b>O que é:</b> Uma infraestrutura inédita de Gêmeo Digital (Digital Twin) acoplada a modelos preditivos de degradação estrutural e de sistemas.<br>
                <b>Como funciona:</b> Ingere telemetria de condições térmicas e níveis de propelente, rodando algoritmos de análise de sobrevivência para calcular o tempo até a próxima falha.<br>
                <b>Para que serve:</b> Permitir gerenciamento prescritivo, simulando manobras preventivas para estender a vida útil das missões.<br>
                <b>Integração de API Pública:</b> Integra dados de telemetria meteorológica solar e radiação do <b>NOAA (SWPC)</b> via <code>swpc.noaa.gov/json/data</code> para cruzar anomalias térmicas e impactos de ventos cósmicos nos sensores.
            </div>
        </div>
        """, unsafe_allow_html=True)

        t1, t2, t3 = st.columns(3)
        with t1:
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            st.markdown("#### **Observatório TESS**")
            st.metric("Status de Saúde Global", "94% NOMINAL", "Excelente")
            st.progress(0.74, text="Combustível Hidrazina: 74%")
            st.markdown("</div>", unsafe_allow_html=True)
        with t2:
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            st.markdown("#### **James Webb (JWST)**")
            st.metric("Status de Saúde Global", "87% CRÍTICO", "Raios Cósmicos", delta_color="inverse")
            st.progress(0.89, text="Combustível Restante: 89%")
            st.markdown("</div>", unsafe_allow_html=True)
        with t3:
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            st.markdown("#### **Módulo Kepler (Legado)**")
            st.metric("Status de Saúde Global", "0% OFFLINE", "Aposentado", delta_color="off")
            st.progress(0.0, text="Combustível Exaurido")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")
        col_graf_temp, col_graf_comb = st.columns([1, 1])
        with col_graf_temp:
            st.markdown("#### 📈 Projeção Matemática de Degradação de Hardware")
            dias_futuros = np.array(range(1, 60))
            degradacao_tess = 100 - (dias_futuros * 0.05) - (np.sin(dias_futuros) * 0.5)
            degradacao_jwst = 100 - (dias_futuros * 0.22) - (np.cos(dias_futuros) * 1.2)
            fig_deg = go.Figure()
            fig_deg.add_trace(go.Scatter(x=dias_futuros, y=degradacao_tess, name="TESS (Previsão)", line=dict(color="#00E5FF")))
            fig_deg.add_trace(go.Scatter(x=dias_futuros, y=degradacao_jwst, name="JWST (Alerta)", line=dict(color="#FF2E93", width=3)))
            fig_deg.update_layout(paper_bgcolor='#0B0F17', plot_bgcolor='#0B0F17', font_color='white', height=250, margin=dict(t=20))
            st.plotly_chart(fig_deg, use_container_width=True)
        with col_graf_comb:
            st.markdown("#### 🔋 Simulação de Efeitos de Escala Térmica Criogênica")
            horas = np.linspace(0, 24, 100)
            temp_miri = -266.1 + np.sin(horas)*0.15 + np.random.randn(100)*0.02
            fig_temp = px.line(x=horas, y=temp_miri, color_discrete_sequence=['#FFD600'])
            fig_temp.update_layout(paper_bgcolor='#0B0F17', plot_bgcolor='#0B0F17', font_color='white', height=250, margin=dict(t=20))
            st.plotly_chart(fig_temp, use_container_width=True)

    # =====================================================================
    # ABA 3: MONITORAMENTO GLOBAL DE SATÉLITES E MATRIZ DE APIs
    # =====================================================================
    with tab_satelites:
        st.markdown("### 🌍 Monitoramento e Ingestão de Constelações Orbitais e Detritos Espaciais")
        st.markdown("""
        <div class='manual-box'>
            <div class='manual-title'>📘 DIRETRIZ OPERACIONAL - O QUE É, COMO FUNCIONA E PARA QUE SERVE</div>
            <div class='manual-text'>
                <b>O que é:</b> Um hub global interativo de inteligência que compila as posições, altitudes e origens de todos os corpos artificiais na órbita terrestre, mapeando explicitamente suas fontes de dados.<br>
                <b>Como funciona:</b> Consome dados agregados via protocolos TLE e coordenadas geocêntricas, distribuindo os corpos entre Órbita Baixa (LEO), Média (MEO) e Geoestacionária (GEO) no mapa de dispersão tridimensional.<br>
                <b>Para que serve:</b> Mitigar riscos de colisão contra detritos espaciais, auditar frequências de comunicação e mapear as fontes públicas oficiais e APIs governamentais que alimentam nosso ecossistema de dados.
            </div>
        </div>
        """, unsafe_allow_html=True)

        ms1, ms2, ms3, ms4 = st.columns(4)
        ms1.metric("Satélites Ativos Rastreados", "9.418", "Ingestão Contínua")
        ms2.metric("Detritos Catalogados (Lixo)", "27.500+", "Alto Perigo")
        ms3.metric("APIs Conectadas Ativas", "5 Fontes", "Sincronizado")
        ms4.metric("Última Atualização Orbital", "Agora mesmo", "Protocolo TLE")

        col_mapa_sat, col_tabela_api = st.columns([1.2, 1])

        with col_mapa_sat:
            st.markdown("#### 🛰️ Malha Tridimensional da Dispersão de Satélites e Lixo Espacial")
            st.caption("Visualização tridimensional cartesiana com base na altitude orbital relativa em quilômetros.")
            
            np.random.seed(101)
            n_satelites = 250
            altitudes_simuladas = np.concatenate([
                np.random.uniform(300, 2000, 150),
                np.random.uniform(2000, 20000, 60),
                np.random.uniform(35000, 36000, 40)
            ])
            
            df_sat = pd.DataFrame({
                'Eixo X (Posição)': np.random.randn(n_satelites) * altitudes_simuladas / 5000,
                'Eixo Y (Posição)': np.random.randn(n_satelites) * altitudes_simuladas / 5000,
                'Eixo Z (Altitude)': altitudes_simuladas,
                'Categoria': np.concatenate([['Ativo (Comercial)']*100, ['Ativo (Militar)']*50, ['Lixo Espacial (Detrito)']*100])
            })
            
            fig_sat_3d = px.scatter_3d(
                df_sat, x='Eixo X (Posição)', y='Eixo Y (Posição)', z='Eixo Z (Altitude)',
                color='Categoria', color_discrete_map={
                    'Ativo (Comercial)': '#00E5FF', 'Ativo (Militar)': '#FFD600', 'Lixo Espacial (Detrito)': '#FF2E93'
                }, opacity=0.8, size_max=5
            )
            fig_sat_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0), paper_bgcolor='#0B0F17', plot_bgcolor='#0B0F17', font_color='white', height=400)
            st.plotly_chart(fig_sat_3d, use_container_width=True)

        with col_tabela_api:
            st.markdown("#### 🔌 Matriz de Integração de Dados & APIs Públicas Utilizadas")
            st.caption("Detalhamento técnico obrigatório das fontes externas conectadas para fins de auditoria de governança de dados.")

            api_data = {
                "Tipo de Dado": [
                    "Coordenadas e TLE", "Dados de Clima Espacial", "Detritos Espaciais", 
                    "Sondas e Telescópios", "Posições Starlink", "Meteoroide/NEO Core"
                ],
                "Provedor Oficial": [
                    "NORAD / Space-Track", "NOAA (SWPC)", "NASA Orbital Debris", 
                    "NASA Portal (JPL)", "SpaceX Open API", "NASA NeoWs API"
                ],
                "API Endpoint Utilizada": [
                    "space-track.org/api/v1", "swpc.noaa.gov/json/data", "orbitaldebris.jsc.nasa.gov", 
                    "api.nasa.gov/planetary/exoplanet", "api.spacexdata.com/v4", "api.nasa.gov/neo/rest/v1"
                ],
                "Frequência / Protocolo": ["De 2h em 2h // JSON", "Tempo Real // REST", "Semanal // CSV", "Diário // REST", "A cada 12h // JSON", "Contínuo // HASH Link"]
            }
            df_api_ledger = pd.DataFrame(api_data)
            st.dataframe(df_api_ledger, use_container_width=True, hide_index=True)
            st.markdown("<p style='font-size: 12px; color: #64748B;'>* Nota: As camadas de segurança do proxy corporativo realizam o cache preventivo desses endpoints para manter a estabilidade do pipeline interno.</p>", unsafe_allow_html=True)

    # =====================================================================
    # ABA 4: DEFESA PLANETÁRIA
    # =====================================================================
    with tab_defesa:
        st.markdown("### ☄️ Centro de Monitoramento de NEOs (Near-Earth Objects) & Deflexão Proativa")
        st.markdown("""
        <div class='manual-box'>
            <div class='manual-title'>📘 DIRETRIZ OPERACIONAL - O QUE É, COMO FUNCIONA E PARA QUE SERVE</div>
            <div class='manual-text'>
                <b>O que é:</b> A maior matriz integrada de rastreamento e cálculo balístico de deflexão de corpos perigosos do planeta.<br>
                <b>Como funciona:</b> Organiza dados de estações globais de varredura. Havendo perigo real, o simulador à direita calcula vetores diários de impacto.<br>
                <b>Para que serve:</b> Prevenir impactos catastróficos mapeando o desvio orbital exato gerado por contra-medidas.<br>
                <b>Integração de API Pública:</b> Utiliza em tempo real a API <b>NASA NeoWs (Near Earth Object Web Service)</b> através do endpoint <code>api.nasa.gov/neo/rest/v1</code> para extração sistemática de diâmetro, velocidade e aproximação de asteroides de risco.
            </div>
        </div>
        """, unsafe_allow_html=True)

        meteoros_expandidos = {
            "Designação NEO": [
                "99942 Apophis (2004 MN4)", "101955 Bennu (1999 RQ36)", "4179 Toutatis", "Corpo Hiperbólico PHA-2026", 
                "162173 Ryugu", "2023 NT1", "Fragmento de Meteoro M-102", "Fragmento 2026-XC4"
            ],
            "Diâmetro Est. (m)": [370, 492, 5400, 850, 900, 30, 45, 145],
            "Velocidade Relativa (km/h)": [110200, 101000, 39600, 145000, 78000, 86000, 48000, 67000],
            "Distância Mínima (LD)": [0.12, 0.54, 1.80, 0.04, 3.10, 0.25, 2.50, 4.50],
            "Mag. Absoluta (H)": [19.2, 20.8, 15.3, 17.1, 18.1, 24.5, 23.1, 21.4],
            "Escala Torino": [2, 1, 0, 8, 0, 1, 1, 1],
            "Estação de Varredura": ["Goldstone Radar", "Pan-STARRS 1", "Arecibo Node", "AEGIS DeepSpace", "NEOWISE Space", "Mount Lemmon", "Zwicky Transient", "Pan-STARRS 2"],
            "Risco Classificado": ["Atenção Orbital", "Baixo Risco", "Nulo (Seguro)", "Ameaça Crítica Regional", "Nulo (Seguro)", "Monitoramento", "Baixo Risco", "Baixo Risco"]
        }
        df_meteoros = pd.DataFrame(meteoros_expandidos)
        st.dataframe(df_meteoros, use_container_width=True, hide_index=True)
        st.markdown("---")

        col_radar, col_simulador = st.columns([1.1, 1])
        with col_radar:
            st.markdown("#### 🌐 1. Radar de Aproximação de Trajetórias (Visão Geral)")
            df_plot_radar = df_meteoros.head(6)
            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatter(x=[0], y=[0], mode='markers+text', marker=dict(size=35, color='#00E5FF', line=dict(width=2, color='white')), text=["TERRA"], textposition="top center"))
            x_coords = [1.2, -0.4, -2.2, 0.06, 2.9, -0.7]
            y_coords = [0.8, 0.50, 1.4, -0.04, -1.3, -0.3]
            fig_radar.add_trace(go.Scatter(
                x=x_coords, y=y_coords, mode='markers+text',
                marker=dict(size=df_plot_radar["Diâmetro Est. (m)"]/22 + 16, color=df_plot_radar["Escala Torino"], colorscale='Reds', showscale=True),
                text=df_plot_radar["Designação NEO"], textposition="bottom center"
            ))
            fig_radar.update_layout(paper_bgcolor='#0B0F17', plot_bgcolor='#0B0F17', font_color='white', margin=dict(l=10, r=10, b=10, t=20), height=400, xaxis=dict(range=[-4, 4]), yaxis=dict(range=[-3, 3]))
            st.plotly_chart(fig_radar, use_container_width=True)
            
        with col_simulador:
            st.markdown("#### 💥 2. Terminal Interativo de Mitigação e Deflexão")
            st.markdown("<div class='card-painel'>", unsafe_allow_html=True)
            alvo_defesa = st.selectbox("Selecione o Vetor de Ameaça Ativo:", df_meteoros["Designação NEO"])
            arma = st.radio("Selecione a Contra-Medida:", ["🚀 Sonda de Impacto Cinético (NASA DART)", "🛰️ Laser Térmico de Superfície", "💥 Dispositivo de Pulso Nuclear"])
            potencia = st.slider("Potência / Output de Energia do Vetor:", 10, 500, 200)
            simular_impacto = st.button("💥 EXECUTAR CÁLCULO DE DEFLEXÃO")
            st.markdown("</div>", unsafe_allow_html=True)
            
            tempo_trajetoria = np.linspace(-5, 5, 200)
            y_original = (tempo_trajetoria ** 2) * 0.15 - 0.25
            fig_trajetoria = go.Figure()
            fig_trajetoria.add_trace(go.Scatter(x=[0], y=[0], mode="markers+text", marker=dict(size=35, color="#00E5FF"), text=["TERRA"], textposition="top center"))
            fig_trajetoria.add_trace(go.Scatter(x=tempo_trajetoria, y=y_original, mode="lines", name="Rota Original", line=dict(color="#FF2E93", width=2, dash="dash")))
            
            if simular_impacto:
                fator_desvio = (potencia / 100) * 0.48
                if "Nuclear" in arma: fator_desvio *= 1.80
                elif "Laser" in arma: fator_desvio *= 1.15
                y_desviada = y_original + fator_desvio
                fig_trajetoria.add_trace(go.Scatter(x=tempo_trajetoria, y=y_desviada, mode="lines", name="Nova Rota Calculada", line=dict(color="#00FF66", width=4)))
                st.success(f"✅ OPERAÇÃO CONCLUÍDA: O objeto foi desviado com segurança.")
            
            fig_trajetoria.update_layout(paper_bgcolor='#0B0F17', plot_bgcolor='#0B0F17', font_color='white', margin=dict(l=10, r=10, b=10, t=20), height=200, xaxis=dict(range=[-5, 5]), yaxis=dict(range=[-1.5, 2.5]))
            st.plotly_chart(fig_trajetoria, use_container_width=True)

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #334155; font-size: 11px;'>SISTEMA MILITAR INTEGRADO AEGIS - CENTRO DE DEFESA PLANETÁRIA INTERNACIONAL © 2026 // ACESSO RESTRITO</p>", unsafe_allow_html=True)

if not st.session_state['authenticated']:
    login_page()
else:
    main_dashboard()
