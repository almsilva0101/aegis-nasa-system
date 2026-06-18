import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import lightkurve as lk
import pandas as pd
import numpy as np
import time

# Configuração Completa do Centro de Comando Aeroespacial
st.set_page_config(page_title="AEGIS - Strategic Space Defense", layout="wide", initial_sidebar_state="expanded")

# --- SISTEMA DE SEGURANÇA (AUTENTICAÇÃO ZERO TRUST) ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def login_page():
    st.markdown("<h1 style='text-align: center; color: #FF2E93;'>🛡️ A.E.G.I.S.</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>Advanced Planetary Defense & Galactic Intelligence System</h3>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("aegis_login"):
            st.markdown("### **Acesso de Segurança de Alto Nível - NORAD / NASA**")
            user = st.text_input("ID do Operador (Username)", "nasa_operator_01")
            password = st.text_input("Chave Criptográfica (Password)", type="password")
            submitted = st.form_submit_button("AUTENTICAR NO SISTEMA INTEGRADO")
            
            if submitted:
                if user == "nasa_operator_01" and password == "artemis2026":
                    st.session_state['authenticated'] = True
                    st.success("Acesso Concedido. Inicializando módulos globais...")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Falha na autenticação.")

def main_dashboard():
    st.markdown("<p style='color: #FF2E93; font-size: 14px; margin-bottom: 0;'>🚨 COMMAND CENTER ACTIVE // INTEGRATED EXPLORATION & MITIGATION PLATFORM</p>", unsafe_allow_html=True)
    st.title("🛰️ AEGIS - Plataforma Unificada de Defesa e Exploração Espacial")
    st.markdown("---")

    # --- MENU PRINCIPAL EM ABAS ---
    tab_exoplanetas, tab_telescopios, tab_defesa_ativa = st.tabs([
        "🌌 1. Triagem de Exoplanetas & Anomalias", 
        "🛰️ 2. Status da Frota de Telescópios", 
        "☄️ 3. Centro de Defesa Planetária (Radar & Contra-Medidas)"
    ])

    # ==========================================
    # ABA 1: EXOPLANETAS E ANOMALIAS
    # ==========================================
    with tab_exoplanetas:
        st.markdown("### 🔬 Pipeline de Inteligência em Sinais de Órbita Profunda")
        
        with st.expander("📘 O que estamos fazendo aqui? (Explicação Científica)"):
            st.write("""
            **Objetivo:** Identificar planetas fora do nosso sistema solar ou anomalias cósmicas.
            * **O que é a Fila de Triagem?** É uma tabela gerada por algoritmos de Machine Learning. Ela varre estrelas e isola apenas aquelas onde o brilho mudou de forma suspeita.
            * **O que é o Desvio Padrão (σ)?** Mede o quão 'estranho' é o sinal. Quanto maior o Sigma (σ), mais anômalo é o comportamento da estrela.
            * **O que é o Gráfico de Espectro/Fluxo?** É a curva de luz da estrela. Se uma linha tiver uma queda simétrica, significa que um exoplaneta passou na frente dela bloqueando a luz (Método do Trânsito). Se a linha for caótica e cheia de picos, isolamos uma **Anomalia Não Identificada**.
            """)

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
                cor = '#FF2E93'
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
        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            st.markdown("#### **TESS (Transiting Exoplanet Survey)**")
            st.metric("Status Operacional", "ONLINE", delta="Estável")
            st.progress(0.74, text="Combustível Hidrazina: 74%")
        with col_t2:
            st.markdown("#### **James Webb (JWST)**")
            st.metric("Status Operacional", "COLETANDO DADOS", delta="Carga Alta", delta_color="inverse")
            st.progress(0.89, text="Combustível de Órbita: 89%")
        with col_t3:
            st.markdown("#### **Kepler Telescope**")
            st.metric("Status Operacional", "APOSENTADO / ARQUIVO", delta="Inativo", delta_color="off")

    # ==========================================
    # ABA 3: CENTRO DE DEFESA PLANETÁRIA (UNIFICADO)
    # ==========================================
    with tab_defesa_ativa:
        st.markdown("### ☄️ Monitoramento de Objetos Próximos à Terra (NEOs) e Mitigação Ativa")
        
        with st.expander("📘 Entendendo o Módulo Unificado de Defesa Planetária"):
            st.write("""
            **O que esta seção faz?** Ela junta a **Identificação Visual por Radar** com a **Ação de Interceptação**.
            * **Radar Orbital:** Mostra a posição macro de todas as ameaças circulando a Terra.
            * **Console de Deflexão:** Permite simular um impacto cinético direto em um objeto selecionado para alterar matematicamente a sua trajetória, fazendo-o errar o nosso planeta.
            """)

        # Base de dados unificada de ameaças reais e simuladas
        meteoros_data = {
            "Nome do Objeto": ["Asteroide Apophis 99942", "Corpo Hiperbólico PHA-2026", "Fragmento de Meteoro M-102", "Meteoro de Entrada Rápida BEN-10"],
            "Diâmetro Est. (Metros)": [370, 850, 45, 3],
            "Velocidade (km/h)": [110000, 145000, 48000, 82000],
            "Distância Mínima (LD)": [0.12, 0.04, 2.5, 0.01],
            "Escala de Torino": [2, 8, 1, 0],
            "Risco de Impacto": ["Atenção (Monitoramento Kinetico)", "Ameaça de Extinção Regional", "Baixo Risco", "Nulo (Queima na Atmosfera)"]
        }
        df_meteoros = pd.DataFrame(meteoros_data)
        st.dataframe(df_meteoros, use_container_width=True)

        st.markdown("---")

        # DIVISÃO VISUAL EM DUAS COLUNAS: RADAR À ESQUERDA E SIMULADOR À DIREITA
        col_radar_macro, col_simulador_micro = st.columns([1, 1])

        with col_radar_macro:
            st.subheader("🌐 1. Radar de Aproximação de Trajetórias (Visão Geral)")
            st.write("Posicionamento em tempo real dos corpos em rota de aproximação relativa à Terra.")
            
            fig_radar = go.Figure()
            # Desenha a Terra no centro
            fig_radar.add_trace(go.Scatter(x=[0], y=[0], mode='markers+text', marker=dict(size=30, color='#00E5FF'), text=["TERRA"], textposition="top center", name="Terra"))
            # Plota os objetos ao redor
            fig_radar.add_trace(go.Scatter(
                x=[1.2, -0.09, -2.2, 0.4], y=[0.7, 0.08, 1.8, -0.1], mode='markers+text',
                marker=dict(size=df_meteoros["Diâmetro Est. (Metros)"]/15 + 12, color=df_meteoros["Escala de Torino"], colorscale='Reds', showscale=True),
                text=df_meteoros["Nome do Objeto"], textposition="bottom center", name="Objetos Monitorados"
            ))
            fig_radar.update_layout(
                paper_bgcolor='black', plot_bgcolor='black', font_color='white', margin=dict(l=0, r=0, b=0, t=30),
                xaxis=dict(showgrid=True, zeroline=True, range=[-4, 4]), yaxis=dict(showgrid=True, zeroline=True, range=[-3, 3])
            )
            st.plotly_chart(fig_radar, use_container_width=True)

        with col_simulador_micro:
            st.subheader("💥 2. Simulador Interativo de Deflexão Cinética")
            st.write("Selecione um alvo crítico do radar para testar deflexões de órbita.")
            
            alvo_defesa = st.selectbox("Escolha a rocha para simular impacto tático:", df_meteoros["Nome do Objeto"])
            arma = st.radio("Selecione o Tipo de Contra-Medida:", ["🚀 Sonda de Impacto Cinético (Estilo NASA DART)", "🛰️ Laser Térmico de Superfície Estacionário", "💥 Dispositivo de Pulso Nuclear"])
            potencia = st.slider("Massa / Potência de Energia do Vetor:", 10, 500, 150)
            
            simular_impacto = st.button("💥 EXECUTAR CÁLCULO DE INTERCEPTAÇÃO")
            
            # Gráfico do Desvio
            tempo_trajetoria = np.linspace(-5, 5, 200)
            y_original = (tempo_trajetoria ** 2) * 0.15 - 0.2
            fig_trajetoria = go.Figure()
            
            # Alvo Terra no ponto zero do simulador
            fig_trajetoria.add_trace(go.Scatter(x=[0], y=[0], mode="markers+text", marker=dict(size=35, color="#00E5FF"), text=["TERRA"], textposition="top center", name="Terra"))
            fig_trajetoria.add_trace(go.Scatter(x=tempo_trajetoria, y=y_original, mode="lines", name="Rota de Impacto Original", line=dict(color="#FF2E93", dash="dash")))
            
            if simular_impacto:
                fator_desvio = (potencia / 100) * 0.4
                if "Nuclear" in arma:
                    fator_desvio *= 1.8
                y_desviada = y_original + fator_desvio
                
                fig_trajetoria.add_trace(go.Scatter(x=tempo_trajetoria, y=y_desviada, mode="lines", name="Nova Rota Calculada", line=dict(color="#00FF66", width=4)))
                fig_trajetoria.add_trace(go.Scatter(x=[-2], y=[0.4], mode="markers+text", marker=dict(size=12, color="#FFFF00", symbol="star"), text=["💥 PONTO DE INTERCEPTAÇÃO"], textposition="top right"))
                st.success(f"✅ SUCESSO: {alvo_defesa} desviado com segurança em {fator_desvio*100:,.2f} mil km da Terra.")
            
            fig_trajetoria.update_layout(
                paper_bgcolor='black', plot_bgcolor='black', font_color='white', margin=dict(l=0, r=0, b=0, t=30),
                xaxis=dict(range=[-5, 5], showgrid=True), yaxis=dict(range=[-2, 3], showgrid=True)
            )
            st.plotly_chart(fig_trajetoria, use_container_width=True)

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #555;'>SISTEMA MILITAR INTEGRADO AEGIS - CENTRO DE INTELIGÊNCIA ESPACIAL DA NASA © 2026</p>", unsafe_allow_html=True)

if not st.session_state['authenticated']:
    login_page()
else:
    main_dashboard()
