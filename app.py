
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Painel de Debêntures Incentivadas e de Infraestrutura",
    page_icon="📈",
    layout="wide"
)

# 🔹 Cabeçalho com Logo + Título
# =========================
# Criar duas colunas
col1, col2 = st.columns([4, 1])

with col1:
    st.image("IMAGEM_SRE.jpeg", width=400)

with col2:
    st.image("image_MF.jpeg", width=100)

# Centralizar título e subtítulo
st.markdown(
    """
    <div style="text-align: center;">
        <h3>📊 Painel de Monitoramento de Debêntures Incentivadas e de Infraestrutura</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Menu lateral para navegação
menu = st.sidebar.radio(
    "📑 Selecione a página",
    [
        "ℹ️ Informações sobre o Painel",
        "🏗️ Debêntures Incentivadas e de Infraestrutura",
        "📊 Dados",
        "📈 Análise",
        "🌱 Debêntures Sustentáveis"
    ]
)

# ------------------
# Página: Informações sobre o Painel
# ------------------
if menu == "ℹ️ Informações sobre o Painel":
    st.subheader("ℹ️ Sobre este Painel")
    st.markdown(
        """
        **Objetivo central:** aumentar a **transparência**, o **acesso à informação** e a **compreensão pública**
        sobre **Debêntures Incentivadas** e **Debêntures de Infraestrutura** — acompanhando **emissões**,
        **valores captados**, **prazos** e **setores**, além de oferecer **indicadores** e **análises** sobre
        **custo de captação** e outras variáveis.
        """
    )

    # Blocos de valor
    c1, c2, c3 = st.columns(3)
    with c1:
        st.success("🎯 **Para que serve**")
        st.markdown(
            "- Acompanhar **novas emissões** \n"
            "- Verificar informações como **valores captados**, **custos**, **prazos**, **setores**\n"
            "- Entender **benefícios** e **regras** do instrumento"
        )
    with c2:
        st.info("👥 **Para quem**")
        st.markdown(
            "- **Sociedade** (transparência)\n"
            "- **Formuladores de políticas** (evidências)\n"
            "- **Mercado** (emitentes, investidores, bancos)"
        )
    with c3:
        st.warning("🧭 **O que você encontra**")
        st.markdown(
            "- Conteúdos **explicativos**\n"
            "- **Dados** atualizados de emissões\n"
            "- **Indicadores** e **comparações** de informações relevantes"
        )

    

# ------------------
# Página: Debêntures Incentivadas e de Infraestrutura
# ------------------
elif menu == "🏗️ Debêntures Incentivadas e de Infraestrutura":
    import pandas as pd
    import streamlit as st

    st.subheader("🏗️ Debêntures Incentivadas e de Infraestrutura")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📚 Evolução histórica",
        "⚖️ Comparativo dos instrumentos",
        "🗺️ Setores e atividades elegíveis",
        "📜 Portarias setoriais"
    ])

    # -------------------------------
    # 📚 Evolução histórica
    # -------------------------------

    with tab1:
        st.markdown("""
    ### Evolução Histórica das Debêntures Incentivadas e Integração da Sustentabilidade
    
    A história das debêntures no Brasil tem suas raízes na **Lei nº 6.404/1976** (Lei das Sociedades por Ações), 
    que estabeleceu as bases legais para a emissão desses títulos de dívida.  

    O marco que realmente impulsionou o uso de debêntures para financiamento de infraestrutura, com foco em incentivos fiscais, 
    foi a **Lei nº 12.431/2011**, que criou as **Debêntures Incentivadas**.  
    O atrativo principal foi o **incentivo fiscal direto ao investidor**:  
    - Pessoas físicas com **isenção de IR**  
    - Investidores institucionais com **alíquotas reduzidas**.  

    A integração explícita da **sustentabilidade** ganhou força com o **Decreto nº 10.387/2020**, 
    que definiu critérios de sustentabilidade para os projetos habilitados sob a Lei de Debêntures Incentivadas, 
    marcando um avanço para um financiamento mais consciente e alinhado a objetivos ambientais e sociais.  

    A evolução mais significativa ocorreu com a **Lei nº 14.801/2024**, que dispõe sobre as **Debêntures de Infraestrutura**.  
    Nela, o **benefício fiscal foi direcionado ao emissor**, permitindo dedução de juros e exclusão parcial da base de cálculo 
    do **IRPJ** e da **CSLL**, criando um vetor de estímulo ao investimento em infraestrutura.  

    O **Decreto nº 11.964/2024**, que regulamenta essa lei, reforçou o compromisso com o financiamento sustentável, 
    priorizando setores estratégicos. Nesse contexto, **investimentos ligados à cadeia de petróleo e derivados foram excluídos** 
    dos incentivos, permanecendo elegíveis projetos como os de **gás natural (vetor de transição energética)** e de 
    **infraestrutura de combustíveis de baixo carbono**.  

    **Síntese:** Essa progressão legislativa mostra a clareza crescente sobre a importância de vincular o financiamento da 
    infraestrutura a **práticas sustentáveis**, usando incentivos fiscais como alavanca para atrair capital privado 
    com integridade socioambiental.
    """)

        st.markdown("""
    ### Linha do tempo e integração com sustentabilidade
    - **Lei nº 6.404/1976 (Lei das S.As.)** — estabelece as bases para emissão de debêntures no Brasil.  
    - **Lei nº 12.431/2011** — cria as **Debêntures Incentivadas** para financiar **projetos prioritários de infraestrutura**, 
      com **incentivo fiscal ao investidor** (PF isenta; PJ com alíquota reduzida).  
    - **Decreto nº 10.387/2020** — introduz **critérios de sustentabilidade** para projetos enquadrados na 12.431, 
      elevando a exigência ambiental/social.  
    - **Lei nº 14.801/2024** — cria as **Debêntures de Infraestrutura**, redirecionando o **benefício fiscal ao emissor** 
      (dedução de juros e exclusões na base de IRPJ/CSLL).  
    - **Decreto nº 11.964/2024** — regulamento **unificado** das Leis 12.431 e 14.801, com **priorização setorial** e foco em
      **financiamento sustentável**. Exclui incentivos à **cadeia do petróleo e derivados**; mantém **gás natural** como vetor 
      de transição e permite infraestrutura de transporte de **combustíveis de baixo carbono**.
    """)
    
    # -------------------------------
    # ⚖️ Comparativo dos instrumentos
    # -------------------------------
    with tab2:
        st.markdown("### Debêntures Incentivadas × Debêntures de Infraestrutura")
        comp = pd.DataFrame([
            ["Objeto", "Instrumento de captação de recursos voltado ao financiamento de projetos prioritários de infraestrutura ou de produção econômica intensiva em pesquisa, desenvolvimento e inovação.", "Instrumento de captação de recursos voltado ao financiamento de projetos prioritários de infraestrutura ou de produção econômica intensiva em pesquisa, desenvolvimento e inovação."],
            ["Uso dos recursos", "Projetos considerados prioritários pelo governo federal", "Projetos considerados prioritários pelo governo federal"],
            ["Setores elegíveis", "Transporte, energia, saneamento, mobilidade, telecom, logística, irrigação, etc.", "Transporte, energia, saneamento, mobilidade, telecom, logística, irrigação, etc."],
            ["Beneficiário do incentivo fiscal", "Investidor", "Empresa emissora"],
            ["Benefícios fiscais (IR/CSLL)", "PF: 0% IR | PJ: 15% IR | CSLL: regras gerais", "IR/CSLL: dedução dos juros e exclusão de 30% dos juros no lucro real"],
            ["IR – investidor estrangeiro", "Isento (condições da legislação)", "Tributado conforme regras gerais de renda fixa"],
            ["Prazo mínimo", "Sim — 4 anos", "Sim — 4 anos"],
        ], columns=["Aspecto", "Debênture Incentivada (Lei nº 12.431/2011)", "Debênture de Infraestrutura (Lei nº 14.801/2024)"])
        # Ajusta para ocupar toda a largura
        st.table(comp)



        st.caption("Ambas buscam fomentar infraestrutura; a diferença central está **em quem recebe o benefício fiscal** (investidor vs. emissor) e nas condições associadas. Enquanto as debêntures incentivadas estimulam a demanda do lado do investidor com isenção fiscal, as debêntures de infraestrutura oferecem vantagens fiscais diretas para as empresas que buscam levantar capital, o que pode simplificar o processo e reduzir os custos de captação para o emissor. ")

    # -------------------------------
    # 🗺️ Setores elegíveis (Setores e atividades elegíveis)
    # -------------------------------
# 🗺️ Setores elegíveis (tabela com quebra automática de linhas)
    with tab3:
        # Introdução solicitada
        st.markdown("""
        Tanto as **debêntures incentivadas** quanto as **debêntures de infraestrutura** são destinadas a financiar projetos
        de infraestrutura considerados **prioritários** para o desenvolvimento nacional. Esses projetos devem aderir aos
        critérios estabelecidos pelas leis específicas e, crucialmente, pelo **Decreto nº 11.964/2024**, que detalha os
        procedimentos de enquadramento ministerial.
    
        **São elegíveis os projetos** que estejam inseridos em **setores prioritários**, conforme quadro abaixo:
        """)
    
        import pandas as pd
    
        setores_tbl = pd.DataFrame([
            ["I. Logística e Transportes",
         "a) Rodovias\n"
         "b) Ferrovias (inclusive locomotivas e vagões)\n"
         "c) Hidrovias\n"
         "d) Portos organizados e instalações portuárias\n"
         "   (terminais privados, estações de transbordo e turismo)\n"
         "e) Aeródromos e instalações aeroportuárias de apoio\n"
         "   (exceto aeródromos privados de uso privativo)"],
    
            ["II. Mobilidade Urbana",
             "a) Infraestruturas de transporte público coletivo urbano ou de caráter urbano\n"
             "b) Aquisição de trens, barcas, aeromóveis e teleféricos\n"
             "c) Aquisição de ônibus elétricos (inclusive por célula de combustível) e híbridos a biocombustível ou biogás"],
    
            ["III. Energia",
             "a) Geração por fontes renováveis, transmissão e distribuição de energia elétrica\n"
             "b) Gás natural\n"
             "c) Produção de biocombustíveis e biogás (exceto fase agrícola)\n"
             "d) Combustíveis sintéticos com baixa intensidade de carbono\n"
             "e) Hidrogênio de baixo carbono\n"
             "f) Captura, estocagem, movimentação e uso de CO₂ (CCUS)\n"
             "g) Dutovias para transporte de combustíveis, incluindo biocombustíveis e sintéticos de baixo carbono"],
    
            ["IV. Telecomunicações e Radiodifusão",
             "Projetos de expansão e modernização da infraestrutura de telecomunicações e radiodifusão"],
    
            ["V. Saneamento Básico",
             "Projetos de abastecimento de água, esgotamento sanitário, manejo de resíduos sólidos e drenagem urbana"],
    
            ["VI. Irrigação",
             "Sistemas de irrigação com eficiência hídrica e energética"],
    
            ["VII. Educação Pública e Gratuita",
             "Infraestrutura educacional vinculada ao ensino público e gratuito"],
    
            ["VIII. Saúde Pública e Gratuita",
             "Infraestrutura de saúde para atendimento universal e gratuito"],
    
            ["IX. Segurança Pública e Sistema Prisional",
             "Construção, ampliação ou modernização de instalações de segurança pública e do sistema prisional"],
    
            ["X. Parques Urbanos e Unidades de Conservação",
             "Implantação e requalificação de espaços públicos de lazer e áreas protegidas"],
    
            ["XI. Equipamentos Culturais e Esportivos Públicos",
             "Construção ou reforma de teatros, centros culturais, ginásios e estádios públicos"],
    
            ["XII. Habitação Social",
             "Projetos habitacionais voltados à população de baixa renda, implementados via parcerias público-privadas"],
    
            ["XIII. Requalificação Urbana",
             "Intervenções para melhoria de áreas urbanas degradadas"],
    
            ["XIV. Transformação de Minerais Estratégicos",
             "Projetos voltados à industrialização e transformação de minerais críticos para a transição energética"],
    
            ["XV. Iluminação Pública",
             "Modernização e expansão de sistemas de iluminação com eficiência energética"]
        ], columns=["Setor", "Atividades Elegíveis"])
    
        # Renderização que quebra linhas automaticamente e cabe na página
        st.table(setores_tbl)
    
        # (Opcional) Botão para exportar a tabela
        csv_setores = setores_tbl.to_csv(index=False).encode("utf-8-sig")
        st.download_button("📥 Baixar tabela (CSV)", data=csv_setores,
                           file_name="setores_atividades_elegiveis.csv", mime="text/csv")
    

    # -------------------------------
    # 📜 Portarias setoriais
    # -------------------------------
    with tab4:
        st.markdown("### Portarias setoriais — status até **jun/2025**")
        portarias = pd.DataFrame([
    ["Rodoviário e Ferroviário", "Portaria nº 689, de 17/07/2024", "17/07/2024", "18/07/2024", "Em vigor"],
    ["Hidroviário, Portuário e Aeroportuário", "Portaria nº 419, de 29/08/2024", "29/08/2024", "30/08/2024", "Em vigor"],
    ["Mobilidade Urbana", "Portaria MCID nº 266, de 20/03/2025", "20/03/2025", "27/03/2025", "Em vigor"],
    ["Energia (energia elétrica)", "—", "—", "—", "Pendente"],
    ["Energia (gás natural, biocomb., biogás, sintéticos de baixo carbono, CO₂ e dutovias)", "Portaria Normativa GM/MME nº 93, de 10/12/2024", "10/12/2024", "11/12/2024", "Em vigor"],
    ["Telecomunicações e Radiodifusão", "—", "—", "—", "Pendente"],
    ["Saneamento Básico", "Portaria MCID nº 1.411, de 18/12/2024", "18/12/2024", "23/12/2024", "Em vigor"],
    ["Irrigação", "Portaria MIDR nº 128, de 20/01/2025", "20/01/2025", "22/01/2025", "Em vigor"],
    ["Educação Pública e Gratuita", "—", "—", "—", "Pendente"],
    ["Saúde Pública e Gratuita", "—", "—", "—", "Pendente"],
    ["Segurança Pública e Sistema Prisional", "—", "—", "—", "Pendente"],
    ["Parques Urbanos", "—", "—", "—", "Pendente"],
    ["Unidades de Conservação", "Portaria GM/MMA nº 1.298, de 24/01/2025", "24/01/2025", "28/01/2025", "Em vigor"],
    ["Equipamentos Públicos Culturais", "—", "—", "—", "Pendente"],
    ["Equipamentos Públicos Esportivos", "—", "—", "—", "Pendente"],
    ["Habitação Social", "—", "—", "—", "Pendente"],
    ["Requalificação Urbana", "—", "—", "—", "Pendente"],
    ["Transformação de minerais estratégicos para a transição energética", "Minuta de Portaria", "—", "—", "Em consulta pública"],
    ["Iluminação Pública", "Portaria MCID nº 359, de 09/04/2025", "09/04/2025", "25/04/2025", "Em vigor"],
    ["Transição Energética", "—", "—", "—", "Pendente"],
    ["Transformação Ecológica", "—", "—", "—", "Pendente"],
    ["Transformação Digital", "—", "—", "—", "Pendente"],
    ["Complexo Industrial da Saúde", "—", "—", "—", "Pendente"],
    ["Complexo Industrial Aeroespacial e de Defesa", "—", "—", "—", "Pendente"],
], columns=[
    "Setor", "Portaria", "Data Assinatura", "Data Publicação", "Situação"
])


        st.dataframe(portarias, use_container_width=True, hide_index=True)

        csv = portarias.to_csv(index=False).encode("utf-8-sig")
        st.download_button("📥 Baixar tabela de portarias (CSV)", data=csv, file_name="portarias_setoriais_jun2025.csv", mime="text/csv")

# ------------------
# Página: Dados
# ------------------
elif menu == "📊 Dados":
    st.subheader("📊 Base de dados (exemplo fictício) - PRECISAMOS DEFINIR QUAIS COLUNAS COLOCAR NA TABELA----MOSTRAR ULTIMAS EMISSÕES? EMISSOES DA ULTIMA SEMANA?")
    df = pd.DataFrame({
        "Código": ["DBINFRA-001","DBINC-2024A","DBSUST-EL-15"],
        "Emissor": ["Rodovias BR S.A.","Saneamento Sul S.A.","Energia Limpa S.A."],
        "Setor": ["Rodovias","Saneamento","Energia (Renovável)"],
        "Taxa (%)": [6.2, 12.1, 5.8],
        "Data Vencimento": ["2033-02-20","2030-09-10","2032-03-15"],
        "Valor de Mercado (R$ mi)": [850, 420, 560],
        "Rating": ["AA-","A+","AA"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

    # Exportar CSV
    csv = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button("📥 Baixar CSV", data=csv, file_name="debentures_exemplo.csv", mime="text/csv")

# ------------------
# Página: Análise
# ------------------
elif menu == "📈 Análise":
    st.subheader("📈 Análise gráfica (exemplo)")
    df = pd.DataFrame({
        "Código": ["DBINFRA-001","DBINC-2024A","DBSUST-EL-15"],
        "Emissor": ["Rodovias BR S.A.","Saneamento Sul S.A.","Energia Limpa S.A."],
        "Setor": ["Rodovias","Saneamento","Energia (Renovável)"],
        "Valor de Mercado (R$ mi)": [850, 420, 560],
        "Rating": ["AA-","A+","AA"]
    })

    # gráfico de barras
    fig = px.bar(df, x="Emissor", y="Valor de Mercado (R$ mi)", color="Setor",
                 title="Valor de Mercado por Emissor")
    st.plotly_chart(fig, use_container_width=True)

    # gráfico de pizza
    fig2 = px.pie(df, names="Rating", values="Valor de Mercado (R$ mi)", title="Distribuição por Rating")
    st.plotly_chart(fig2, use_container_width=True)

elif menu == "🌱 Debêntures Sustentáveis":
    st.subheader("🌱 Debêntures Sustentáveis")

    # =========================
    # Texto explicativo
    # =========================
    st.markdown("""
    ### A Retomada da Agenda de Sustentabilidade e o Mercado de Capitais

    No Brasil, a priorização da agenda de clima e sustentabilidade foi retomada a partir de 2023. 
    No Ministério da Fazenda (MF), a criação do **Plano de Transformação Ecológica (PTE)** tem promovido 
    o financiamento climático, sobretudo por meio da mobilização de capital privado.  

    No eixo das **finanças sustentáveis**, o PTE tem promovido iniciativas como:  
    - emissões de **Títulos Soberanos Sustentáveis**  
    - a **Taxonomia Sustentável Brasileira**  
    - o **EcoInvest**  
    - o **Sistema Brasileiro de Comércio de Emissões**, entre outras.  

    Nesse cenário dinâmico, o mercado de capitais desempenha um papel fundamental. 
    A regulamentação da **Lei nº 14.801/2024**, por exemplo, foi um passo estratégico 
    para estimular o uso de debêntures no financiamento de projetos de infraestrutura considerados prioritários.  

    O **Decreto nº 11.964/2024** estabeleceu um regulamento unificado para as Leis 12.431/2011 e 14.801/2024, 
    aprimorando o uso de instrumentos econômicos orientados para a sustentabilidade, com destaque para 
    o financiamento de infraestrutura por meio de títulos de dívida.  
    """)

    st.markdown("""
    ### Regras e Conformidade ESG

    As **debêntures sustentáveis** representam um segmento crescente no mercado brasileiro, 
    refletindo a demanda por investimentos alinhados aos princípios de **ESG (Ambiental, Social e Governança)**.  

    - Um título é considerado sustentável, conforme o **Código de Ofertas Públicas da ANBIMA**, 
      se possuir estrutura que o qualifique como **verde, social, de sustentabilidade ou vinculado a metas**.  
    - A estruturação exige observância à **Resolução CVM nº 160/2022** e ao **Código da ANBIMA**, 
      com a apresentação de um **framework de finanças sustentáveis**.  
    - Esse framework deve detalhar: critérios de elegibilidade, metodologia de seleção, 
      controle da alocação dos recursos e mensuração dos impactos.  
    - A **Second Party Opinion (SPO)** é recomendada para reforçar credibilidade.  

    Complementarmente, a publicidade e materiais promocionais devem estar alinhados aos documentos oficiais da oferta. 
    O descumprimento pode gerar sanções e danos reputacionais.  

    A harmonização entre **CVM, ANBIMA e padrões internacionais** fortalece a posição do Brasil na 
    **economia de baixo carbono**, enquanto a futura **Taxonomia Sustentável Brasileira (TSB)** 
    trará ainda mais clareza e integridade à classificação de ativos.  
    """)

    st.markdown("""
    ---
    ## 📊 Visualização Interativa de Debêntures Sustentáveis
    """)

    # =========================
    # Base de dados fictícia
    # =========================
    df_sust = pd.DataFrame({
        "Código": ["DBSUST-EL-15", "DBSUST-SAN-09", "DBSUST-MOB-07", "DBSUST-EDU-03"],
        "Emissor": ["Energia Limpa S.A.", "Saneamento Verde S.A.", "Mobilidade Sustentável Ltda.", "Educação Futuro"],
        "Setor": ["Energia Renovável", "Saneamento Básico", "Mobilidade Urbana", "Educação Pública"],
        "Valor de Mercado (R$ mi)": [560, 310, 220, 150],
        "ODS Relacionado": [
            "ODS 7 - Energia Limpa",
            "ODS 6 - Água Potável e Saneamento",
            "ODS 11 - Cidades Sustentáveis",
            "ODS 4 - Educação de Qualidade"
        ]
    })

    # =========================
    # Filtros interativos
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        setor_sel = st.multiselect(
            "🔍 Filtrar por Setor",
            options=df_sust["Setor"].unique(),
            default=df_sust["Setor"].unique()
        )

    with col2:
        ods_sel = st.multiselect(
            "🌍 Filtrar por ODS",
            options=df_sust["ODS Relacionado"].unique(),
            default=df_sust["ODS Relacionado"].unique()
        )

    df_filtrado = df_sust[
        (df_sust["Setor"].isin(setor_sel)) & 
        (df_sust["ODS Relacionado"].isin(ods_sel))
    ]

    # =========================
    # Tabela filtrada
    # =========================
    st.markdown("### 📋 Tabela de Debêntures Sustentáveis (filtrada)")
    st.dataframe(df_filtrado, use_container_width=True, hide_index=True)

    # =========================
    # Gráficos
    # =========================
    st.markdown("### 📈 Análises gráficas")

    fig_bar = px.bar(
        df_filtrado, 
        x="Emissor", 
        y="Valor de Mercado (R$ mi)", 
        color="Setor",
        title="Valor de Mercado por Emissor (Filtrado)"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    fig_pie = px.pie(
        df_filtrado, 
        names="ODS Relacionado", 
        values="Valor de Mercado (R$ mi)", 
        title="Distribuição por ODS"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    # =========================
    # Download CSV
    # =========================
    csv = df_filtrado.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "📥 Baixar tabela filtrada (CSV)", 
        data=csv, 
        file_name="debentures_sustentaveis_filtradas.csv", 
        mime="text/csv"
    )
