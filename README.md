 # Trilha Integral de Aprendizagem em Química: Do Zero Absoluto ao Ensino Médio Completo
## Plataforma de Excelência Autodidata com Foco no ENEM e Vestibulares Federais (Destaque COPERVE/UFSC)

[![Python 3.12 Test Suite](https://img.shields.io/badge/Python%203.12-E2E%20Tested-brightgreen.svg)](#7-guia-de-execução-dos-testes-automatizados)
[![Status do Repositório](https://img.shields.io/badge/Arquivos%20de%20Entrega-28%2F28%20(100%25)-blue.svg)](#2-mapa-de-navegação-e-arquitetura-modular)
[![Cobertura Curricular](https://img.shields.io/badge/Módulos%20Canônicos-35%2F35%20Completos-success.svg)](#4-matriz-curricular-consolidada-dos-35-módulos-canônicos)
[![Metodologia](https://img.shields.io/badge/Metodologia-Active%20Recall%20%7C%20TRI%20%7C%20Somatórias-orange.svg)](#3-guia-do-estudante-autodidata)

---

## 1. Apresentação Executiva do Projeto

Bem-vindo ao **Plano Completo de Estudos e Guia de Aprendizagem de Química**, uma infraestrutura pedagógica concebida para conduzir o estudante autodidata a partir do **zero absoluto** — sem exigir qualquer conhecimento prévio de ciências além de noções elementares de aritmética — até o domínio pleno e analítico de todo o currículo de Química do Ensino Médio brasileiro.

O projeto foi meticulosamente desenhado para atender aos dois padrões avaliativos mais exigentes e distintos do cenário educacional nacional:

1. **O Exame Nacional do Ensino Médio (ENEM):** Pautado pela Matriz de Referência em Ciências da Natureza e suas Tecnologias (com ênfase na Competência de Área 7 e Habilidades H24 a H27), modelado matematicamente pela **Teoria de Resposta ao Item (TRI — Modelo Logístico de Três Parâmetros / ML3P)**. A preparação visa a maximização da coerência pedagógica, o acerto sistemático de itens de sustentação e a rápida decodificação de situações-problema cotidianas, ambientais e industriais.
2. **Vestibulares de Alta Densidade Acadêmica de Universidades Federais (com foco na COPERVE / UFSC):** Caracterizados pelo rigor formal extremo, profundidade teórica, cobrança da nomenclatura IUPAC sistemática estrita, dedução físico-química formal, o temido formato de **Questões de Proposições Múltiplas (Somatórias binárias 01 a 64)** sob a regra eliminatória condicional $NPC > NPI$, questões abertas de 00 a 99 (com exigência estrita de zero à esquerda) e questões discursivas analíticas com rubricas fracionadas de pontuação.

### 1.1. Fundamentação Epistemológica e Desenho Pedagógico

A progressão dos materiais segue três pilares consagrados da ciência da aprendizagem:

* **O Triângulo de Johnstone:** Todo conceito químico desdobra-se progressivamente em três níveis representacionais:
  $$\text{Nível Macroscópico (Fenômeno Visível)} \longrightarrow \text{Nível Submicroscópico (Átomos, Moléculas e Íons)} \longrightarrow \text{Nível Simbólico (Fórmulas e Equações)}$$
  O autodidata nunca é exposto a fórmulas matemáticas abstratas sem antes compreender a fenomenologia concreta e a mecânica das partículas submicroscópicas.
* **Teoria da Aprendizagem Significativa (David Ausubel):** Estruturação por ancoragens conceituais (*subsunçores*). A matéria elementar e a estrutura de partículas do Stage 0 servem de alicerce para a periodicidade e ligações do Stage 1, que por sua vez explicam a termodinâmica do Stage 2 e as rotas de síntese e estereoquímica do Stage 3.
* **Teoria da Carga Cognitiva (John Sweller):** Gestão equilibrada da memória operacional por meio de *chunking* (micro-passos sequenciais), exemplos resolvidos com passo a passo documentado, diagramas estruturais claros e separação estrita entre definições qualitativas e transformações quantitativas.

---

## 2. Mapa de Navegação e Arquitetura Modular

O repositório é composto por **28 arquivos markdown estruturados**, totalizando mais de 1 milhão de caracteres de conteúdo autoral, sem marcações de incompletude ou textos simulados. A organização física obedece à hierarquia abaixo:

```
quimica_estudos/
├── README.md                                             # [ESTE GUIA] Manual mestre de navegação e visão executiva
├── PLANO_DE_ESTUDOS_MESTRE.md                            # Cronograma integrado de 40 semanas e tabela mestre
├── 00_fundamentos/                                       # Nível Fundamental / Zero Absoluto (Stage 0)
│   ├── 01_materia_estados_misturas.md                    # Matéria, densidade, estados e separação de misturas
│   ├── 02_atomo_particulas_subatomicas.md                # Átomo, prótons, nêutrons, elétrons, Z, A, íons
│   ├── 03_isotoppia_e_tabela_introdutoria.md             # Semelhanças atômicas e introdução à Tabela Periódica
│   └── exercicios_resolvidos_fundamentos.md              # 15 questões resolvidas passo a passo com teoria aplicada
├── 01_quimica_geral_inorganica/                          # Química Geral e Funções Inorgânicas (Stage 1)
│   ├── 01_modelos_atomicos_distribuicao_eletronica.md    # Modelos atômicos históricos, quântica e Pauling
│   ├── 02_tabela_periodica_e_propriedades.md             # Propriedades periódicas e carga nuclear efetiva
│   ├── 03_ligacoes_geometria_polaridade_intermolecular.md# Ligações iônica/covalente/metálica, VSEPR e interações
│   ├── 04_funcoes_inorganicas_e_reacoes.md               # Ácidos, bases, sais, óxidos e reações inorgânicas
│   └── exercicios_resolvidos_geral_inorganica.md         # Exercícios graduados com gabarito analítico completo
├── 02_fisico_quimica/                                    # Físico-Química Completa (Stage 2)
│   ├── 01_estequiometria_gases_solucoes.md               # Mol, leis ponderais, estequiometria, gases e soluções
│   ├── 02_propriedades_coligativas_e_termoquimica.md     # Coligativas, Van 't Hoff, entalpias e Lei de Hess
│   ├── 03_cinetica_e_equilibrio_quimico_ionico.md        # Velocidade, Le Chatelier, pH, pOH, tampão e Kps
│   ├── 04_eletroquimica_pilhas_eletrolise.md             # Pilhas galvânicas, corrosão, eletrólise e Faraday
│   └── exercicios_resolvidos_fisico_quimica.md           # Resoluções detalhadas de problemas numéricos densos
├── 03_quimica_organica/                                  # Química Orgânica e Bioquímica (Stage 3)
│   ├── 01_estrutura_carbono_hibridizacao_cadeias.md      # Carbono, hibridização sp3/sp2/sp, ligações sigma/pi
│   ├── 02_funcoes_organicas_e_nomenclatura.md            # Funções oxigenadas, nitrogenadas e nomenclatura IUPAC
│   ├── 03_isomeria_plana_e_espacial.md                   # Isomeria constitucional, geométrica (cis/trans, E/Z) e óptica
│   ├── 04_reacoes_organicas_polimeros_biomoleculas.md    # Reações orgânicas, polímeros sintéticos e bioquímica
│   └── exercicios_resolvidos_quimica_organica.md         # Questões de identificação, rotas e estereoquímica
├── 04_recursos_e_metodologia/                            # Recursos Didáticos e Metacognição
│   ├── bibliografia_livros_didaticos.md                  # Análise crítica de Feltre, Martha Reis, Brown, Atkins
│   ├── ecossistema_digital_e_simuladores.md              # Canais YouTube, 9 PhETs, MolView, ChemTube3D
│   └── metodologia_estudo_ativo_e_caderno_de_erros.md    # Active Recall, Anki, 5 causas-raiz e reteste 48h
├── 05_roteiro_provas_exercicios/                         # Engenharia Tática de Exames Oficiais
│   ├── estrategico_enem_tri.md                           # TRI ML3P, Matriz de Habilidades C7 e Três Ciclos
│   ├── estrategico_ufsc_somatorias_discursivas.md        # Somatórias (01-64), barreira NPC>NPI, abertas e discursivas
│   ├── simulados_provas_anteriores_e_cronograma.md       # Cronograma de provas oficiais ENEM/UFSC 2015-presente
│   └── banco_exercicios_comentados_vestibulares.md       # Banco representativo comentado de questões reais
└── tests/                                                # Suíte Automatizada de Verificação E2E
    ├── test_curriculum_coverage.py                       # Testes de cobertura física, densidade e tópicos
    └── test_rubric_validation.py                         # Testes de conformidade das rubricas pedagógicas
```

---

## 3. Guia do Estudante Autodidata

Aprender Química de forma autônoma exige método, disciplina e ferramentas ativas. Seguir passivamente videoaulas ou ler apostilas sem engajamento cognitivo gera a falsa ilusão de competência (*fluency illusion*). Abaixo está o protocolo operacional definitivo para o seu dia a dia de estudos.

### 3.1. O Roteiro de Estudo Intra-Capítulo (5 Etapas)

Ao abordar qualquer um dos módulos conceituais do projeto, execute as cinco etapas na ordem prescrita:

1. **Leitura Diagnóstica Rápida (15 a 20 minutos):**
   * Examine o sumário, os títulos de seções, os diagramas conceituais e os boxes "Alerta ENEM" e "Alerta UFSC".
   * Não tente memorizar nada nesta fase; o objetivo é criar um mapa mental prévio (*advanced organizer*).
2. **Leitura Ativa e Estruturação de Fórmulas (45 a 60 minutos):**
   * Leia parágrafo a parágrafo com atenção deliberada.
   * Ao encontrar uma lei ou fórmula físico-química, isole: (a) o significado físico de cada variável, (b) as unidades correspondentes no Sistema Internacional (SI) e (c) as condições de contorno de sua validade (ex.: gases ideais, soluções diluídas).
3. **Estudo de Exemplos Resolvidos com Bloqueio de Visão:**
   * Cubra a resolução comentada dos exemplos com uma folha em branco.
   * Tente resolver o problema no caderno de rascunho de forma 100% autônoma.
   * Destampe a resolução do material e compare sua linha de raciocínio passo a passo com a demonstração oficial.
4. **Bateria Imediata de Exercícios de Fixação (30 a 45 minutos):**
   * Resolva imediatamente de 5 a 10 exercícios conceituais diretos. O feedback imediato consolida o traço de memória antes que ocorra a dispersão da atenção.
5. **Consolidação em Exercícios de Provas Reais (60 a 90 minutos):**
   * Resolva questões dos bancos de vestibulares recomendados (ENEM e UFSC). Qualquer erro cometido deve ser registrado imediatamente no seu **Caderno de Erros**.

### 3.2. Os Três Pilares da Metodologia Ativa

* **Active Recall (Evocação Ativa):** Ao terminar a leitura de uma seção, feche o material e escreva em uma folha em branco tudo o que conseguir lembrar: equações, exceções, geometrias e definições. O esforço neurológico de resgatar a informação sem pistas visuais fortalece os caminhos sinápticos a longo prazo.
* **Técnica de Feynman:** Explique em voz alta o conceito estudado (ex.: "Por que o aumento da pressão desloca o equilíbrio no sentido do menor volume gasoso?") como se estivesse ensinando uma pessoa sem conhecimentos científicos prévios. Sempre que você recorrer a jargões inexplicados ou frases circulares, estará diante de uma lacuna conceitual que precisa ser sanada.
* **Dual Coding (Dupla Codificação):** Combine sempre a informação textual/numérica com esquemas visuais espaciais. Em Química Orgânica, desenhe os orbitais e modelos tridimensionais (utilizando o [MolView](https://molview.org/)); em Termoquímica e Cinética, desenhe o gráfico de entalpia ou energia livre correlacionando com a coordenada de reação.

### 3.3. O Protocolo do Caderno de Erros e Quarentena de 48 Horas

Errar um exercício em simulado ou bateria de estudos é um dado diagnóstico inestimável. Não existe "erro bobo por falta de atenção". Todo erro pertence a uma das **5 Causas-Raiz de Falha em Química**:

| Código | Causa-Raiz | Diagnóstico da Falha | Ação Corretiva Imediata |
| :---: | :--- | :--- | :--- |
| **LC** | **Lacuna Conceitual** | Não conhecia a definição, postulado ou regra formal (ex.: confundiu hidrólise salina com neutralização). | Reler o capítulo teórico correspondente no Feltre ou Martha Reis e confeccionar 3 flashcards no Anki. |
| **EM** | **Erro Matemático** | Compreendeu a química, mas falhou em frações, expoentes, potências de dez ou logaritmos de pH. | Refazer a conta inteiramente à mão no papel por 3 vezes sucessivas, sem uso de calculadora. |
| **ET** | **Erro de Enunciado/Texto** | Não observou termos restritivos ("exceto", "incorreto", "rendimento de 75%", "gás a 27 °C"). | Aplicar o "Marca-Texto Cirúrgico": circular a lápis cada dado numérico e operador restritivo antes de iniciar o cálculo. |
| **RV** | **Representação Visual** | Errou contagem de carbonos em fórmula de traços, confundiu isomeria cis/trans ou leu eixos invertidos. | Redesenhar a molécula explicitando todos os átomos ou plotar o modelo em 3D no MolView. |
| **IU** | **Incompatibilidade de Unidades** | Misturou $cm^3$ com litros, usou Celsius na equação geral dos gases ou esqueceu de converter $mg$ em $g$. | Aplicar a técnica de Análise Dimensional de Russell: carregar todas as unidades explicitamente em cada etapa da equação. |

**O Ciclo de Reteste Cego em 48 Horas:**
Toda questão errada vai para uma lista de "quarentena", sem anotações ou gabarito visível. Exatamente **48 horas depois**, o estudante deve resolver a questão do zero. Se acertar com segurança, a questão é arquivada; se travar novamente, ela retorna à quarentena por mais 7 dias.

### 3.4. Repetição Espaçada com Anki (SRS)

Utilize o software livre **Anki** para memorizar as propriedades invariantes da química:
* **O que deve ir para o Anki:** Grupos funcionais orgânicos, sufixos IUPAC, regras gerais de solubilidade de sais, fila de reatividade dos metais, constantes físicas frequentes ($R = 0,082\ \text{atm}\cdot\text{L}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$, $F = 96.500\ \text{C/mol}$ de elétrons, volume molar na CNTP $= 22,4\ \text{L/mol}$), e reativos específicos (Tollens, Fehling, bromo em $CCl_4$).
* **O que NUNCA deve ir para o Anki:** Contas longas de estequiometria, textos literários do ENEM ou resoluções encadeadas de múltiplos passos. O Anki é dedicado a **fatos atômicos** e recuperações mentais rápidas de menos de 10 segundos por cartão.

---

## 4. Matriz Curricular Consolidada dos 35 Módulos Canônicos

A tabela abaixo sintetiza a totalidade dos **35 Módulos Canônicos** que compõem o currículo integral do projeto, cobrindo os quatro estágios de desenvolvimento cognitivo (Stage 0 a Stage 3):

| Módulo | Denominação Canônica | Arquivo do Projeto | Pré-Requisitos | Objetivos Centrais de Aprendizagem |
| :---: | :--- | :--- | :--- | :--- |
| **M0.1** | Matéria, Corpo, Objeto e Propriedades | [00_fundamentos/01_materia...](00_fundamentos/01_materia_estados_misturas.md) | Nenhum (Zero Absoluto) | Diferenciar matéria e corpo; propriedades gerais vs. específicas; cálculo de densidade ($d=m/V$). |
| **M0.2** | Estados Físicos e Curvas de Aquecimento | [00_fundamentos/01_materia...](00_fundamentos/01_materia_estados_misturas.md) | M0.1 | Mudanças de estado de agregação; calor sensível e latente; interpretação de gráficos de aquecimento. |
| **M0.3** | Fenômenos Físicos/Químicos e Misturas | [00_fundamentos/01_materia...](00_fundamentos/01_materia_estados_misturas.md) | M0.1, M0.2 | Diferenciar transformações físicas e químicas; substâncias puras vs. misturas eutéticas/azeotrópicas. |
| **M0.4** | Métodos de Separação de Misturas | [00_fundamentos/01_materia...](00_fundamentos/01_materia_estados_misturas.md) | M0.1 a M0.3 | Processos mecânicos e térmicos de separação de misturas heterogêneas e homogêneas; fluxo de ETA. |
| **M0.5** | Estrutura Atômica e Partículas Subatômicas | [00_fundamentos/02_atomo...](00_fundamentos/02_atomo_particulas_subatomicas.md) | M0.1, M0.3 | Prótons ($p$), nêutrons ($n$) e elétrons ($e$); núcleo e eletrosfera; número atômico ($Z$) e de massa ($A$). |
| **M0.6** | Semelhanças Atômicas e Conceito de Íon | [00_fundamentos/03_isotoppia...](00_fundamentos/03_isotoppia_e_tabela_introdutoria.md) | M0.5 | Cátions, ânions; isótopos, isóbaros, isótonos e espécies isoeletrônicas; cálculo de carga líquida. |
| **M0.7** | Introdução à Tabela Periódica | [00_fundamentos/03_isotoppia...](00_fundamentos/03_isotoppia_e_tabela_introdutoria.md) | M0.5, M0.6 | Organização em períodos e grupos; metais, ametais e gases nobres; famílias canônicas (1, 2, 16, 17, 18). |
| **M1.1** | Evolução dos Modelos Atômicos e Quântica | [01_quimica_geral.../01_modelos...](01_quimica_geral_inorganica/01_modelos_atomicos_distribuicao_eletronica.md) | Stage 0 completo | Dalton, Thomson, Rutherford, Bohr, Sommerfeld, orbitais atômicos e princípio da incerteza. |
| **M1.2** | Distribuição Eletrônica e Pauling | [01_quimica_geral.../01_modelos...](01_quimica_geral_inorganica/01_modelos_atomicos_distribuicao_eletronica.md) | M1.1, M0.6 | Níveis, subníveis ($s, p, d, f$), Diagrama de Pauling, camada de valência e anomalias de transição. |
| **M1.3** | Tabela Periódica e Propriedades Periódicas| [01_quimica_geral.../02_tabela...](01_quimica_geral_inorganica/02_tabela_periodica_e_propriedades.md) | M1.2, M0.7 | Raio atômico/iônico, energia de ionização, eletronegatividade, densidade e afinidade eletrônica. |
| **M1.4** | Ligações Químicas Fundamentais | [01_quimica_geral.../03_ligacoes...](01_quimica_geral_inorganica/03_ligacoes_geometria_polaridade_intermolecular.md) | M1.3 | Ligação iônica (retículo), covalente (estruturas de Lewis, octeto) e metálica (mar de elétrons). |
| **M1.5** | Geometria Molecular (VSEPR) e Hibridização| [01_quimica_geral.../03_ligacoes...](01_quimica_geral_inorganica/03_ligacoes_geometria_polaridade_intermolecular.md) | M1.4 | Modelo VSEPR (linear, angular, trigonal, piramidal, tetraédrica); orbitais híbridos $sp, sp^2, sp^3$. |
| **M1.6** | Polaridade e Forças Intermoleculares | [01_quimica_geral.../03_ligacoes...](01_quimica_geral_inorganica/03_ligacoes_geometria_polaridade_intermolecular.md) | M1.4, M1.5 | Momento dipolar resultante ($\vec{\mu}_R$); London, dipolo-dipolo, pontes de H, íon-dipolo; PE e solubilidade. |
| **M1.7** | Funções Inorgânicas I: Ácidos e Bases | [01_quimica_geral.../04_funcoes...](01_quimica_geral_inorganica/04_funcoes_inorganicas_e_reacoes.md) | M1.4, M1.6 | Teoria de Arrhenius; ionização de ácidos; força ácida; dissociação e solubilidade de hidróxidos. |
| **M1.8** | Funções Inorgânicas II: Sais e Óxidos | [01_quimica_geral.../04_funcoes...](01_quimica_geral_inorganica/04_funcoes_inorganicas_e_reacoes.md) | M1.7 | Nomenclatura sistemática de sais; óxidos básicos, ácidos, neutros, anfóteros e peróxidos. |
| **M1.9** | Reações Inorgânicas e Balanceamento | [01_quimica_geral.../04_funcoes...](01_quimica_geral_inorganica/04_funcoes_inorganicas_e_reacoes.md) | M1.7, M1.8 | Classificação de reações (síntese, análise, simples troca, dupla troca); balanceamento por tentativas. |
| **M2.1** | Grandezas Químicas, Mol e Avogadro | [02_fisico_quimica/01_estequiometria...](02_fisico_quimica/01_estequiometria_gases_solucoes.md) | M0.5, M1.2 | Massa atômica, massa molecular, conceito de mol ($6,02 \times 10^{23}$ entidades) e massa molar ($g/mol$). |
| **M2.2** | Fórmulas Químicas (Centesimal e Mínima) | [02_fisico_quimica/01_estequiometria...](02_fisico_quimica/01_estequiometria_gases_solucoes.md) | M2.1 | Determinação de fórmulas empíricas/mínimas e moleculares a partir de dados percentuais de massa. |
| **M2.3** | Leis Ponderais e Estequiometria Elementar | [02_fisico_quimica/01_estequiometria...](02_fisico_quimica/01_estequiometria_gases_solucoes.md) | M1.9, M2.1 | Leis de Lavoisier e Proust; proporções em mols, massa e volume nas reações químicas. |
| **M2.4** | Estequiometria Avançada | [02_fisico_quimica/01_estequiometria...](02_fisico_quimica/01_estequiometria_gases_solucoes.md) | M2.3 | Reagente limitante e em excesso; grau de pureza de matérias-primas e rendimento percentual ($\eta$). |
| **M2.5** | Teoria Cinética dos Gases e Equação Geral | [02_fisico_quimica/01_estequiometria...](02_fisico_quimica/01_estequiometria_gases_solucoes.md) | M2.1, M0.2 | Leis de Boyle, Charles, Gay-Lussac; equação de Clapeyron ($PV=nRT$); misturas gasosas e pressão parcial. |
| **M2.6** | Soluções e Curvas de Solubilidade | [02_fisico_quimica/01_estequiometria...](02_fisico_quimica/01_estequiometria_gases_solucoes.md) | M1.6, M2.1 | Soluções insaturadas, saturadas e supersaturadas; gráficos de solubilidade térmica; coeficiente ($C_s$). |
| **M2.7** | Unidades de Concentração e Diluições | [02_fisico_quimica/01_estequiometria...](02_fisico_quimica/01_estequiometria_gases_solucoes.md) | M2.6 | Concentração comum ($g/L$), molaridade ($mol/L$), título, ppm, fração molar, diluição e mistura. |
| **M2.8** | Propriedades Coligativas e Van 't Hoff | [02_fisico_quimica/02_propriedades...](02_fisico_quimica/02_propriedades_coligativas_e_termoquimica.md) | M2.5, M2.7 | Tonoscopia, ebulioscopia, crioscopia, pressão osmótica ($\Pi$) e fator de correção $i = 1+\alpha(q-1)$. |
| **M2.9** | Termoquímica e Lei de Hess | [02_fisico_quimica/02_propriedades...](02_fisico_quimica/02_propriedades_coligativas_e_termoquimica.md) | M1.4, M2.3 | Entalpia ($\Delta H$), processos exo/endotérmicos; calores de formação e combustão; Lei de Hess. |
| **M2.10**| Cinética Química e Catalisadores | [02_fisico_quimica/03_cinetica...](02_fisico_quimica/03_cinetica_e_equilibrio_quimico_ionico.md) | M2.5, M2.9 | Velocidade média e instantânea; teoria das colisões; energia de ativação ($E_a$); catalisadores; ordens. |
| **M2.11**| Equilíbrio Químico e Le Chatelier | [02_fisico_quimica/03_cinetica...](02_fisico_quimica/03_cinetica_e_equilibrio_quimico_ionico.md) | M2.10, M2.5 | Constantes $K_c$ e $K_p$; Princípio de Le Chatelier (efeitos de $T$, $P$, concentrações e gás inerte). |
| **M2.12**| Equilíbrio Iônico: pH, Hidrólise e Kps | [02_fisico_quimica/03_cinetica...](02_fisico_quimica/03_cinetica_e_equilibrio_quimico_ionico.md) | M2.11, M1.7 | Autoionização da água ($K_w$); cálculo de pH/pOH; hidrólise salina; tampões; produto de solubilidade ($K_{ps}$). |
| **M2.13**| Eletroquímica I: Redox e Pilhas | [02_fisico_quimica/04_eletroquimica...](02_fisico_quimica/04_eletroquimica_pilhas_eletrolise.md) | M1.2, M1.3 | Número de oxidação (Nox); balanceamento redox; célula de Daniell; ddp ($\Delta E^\circ$); metais de sacrifício. |
| **M2.14**| Eletroquímica II: Eletrólise e Faraday | [02_fisico_quimica/04_eletroquimica...](02_fisico_quimica/04_eletroquimica_pilhas_eletrolise.md) | M2.13, M2.1 | Eletrólise ígnea vs. aquosa (fila de descarga de íons); Leis de Faraday ($Q=i\cdot t$; $m = \frac{M\cdot i\cdot t}{n\cdot F}$). |
| **M3.1** | O Átomo de Carbono e Cadeias Carbônicas | [03_quimica_organica/01_estrutura...](03_quimica_organica/01_estrutura_carbono_hibridizacao_cadeias.md) | M1.4, M1.5 | Postulados de Kekulé; tetravalência; hibridização $sp^3, sp^2, sp$; classificação de carbonos e cadeias. |
| **M3.2** | Nomenclatura Sistemática IUPAC | [03_quimica_organica/02_funcoes...](03_quimica_organica/02_funcoes_organicas_e_nomenclatura.md) | M3.1 | Regras oficiais IUPAC: prefixo (cadeia principal), infixo (saturação) e sufixo (função química). |
| **M3.3** | Hidrocarbonetos e Indústria do Petróleo | [03_quimica_organica/01_estrutura...](03_quimica_organica/01_estrutura_carbono_hibridizacao_cadeias.md) | M3.1, M3.2 | Alcanos, alcenos, alcinos, alcadienos, ciclanos e aromáticos; destilação fracionada e craqueamento. |
| **M3.4** | Funções Oxigenadas | [03_quimica_organica/02_funcoes...](03_quimica_organica/02_funcoes_organicas_e_nomenclatura.md) | M3.2, M1.6 | Álcoois, fenóis, enóis, éteres, aldeídos, cetonas, ácidos carboxílicos e ésteres; propriedades físicas. |
| **M3.5** | Funções Nitrogenadas, Haletos e Outras | [03_quimica_organica/02_funcoes...](03_quimica_organica/02_funcoes_organicas_e_nomenclatura.md) | M3.4 | Aminas, amidas, nitrilas, nitrocompostos e haletos orgânicos; basicidade relativa de aminas. |
| **M3.6** | Propriedades Físicas e Acidez Orgânica | [03_quimica_organica/02_funcoes...](03_quimica_organica/02_funcoes_organicas_e_nomenclatura.md) | M3.4, M3.5 | Ponto de ebulição, solubilidade; efeito indutivo (+I e -I) e ressonância na acidez de carboxílicos e fenóis. |
| **M3.7** | Isomeria Plana (Constitucional) | [03_quimica_organica/03_isomeria...](03_quimica_organica/03_isomeria_plana_e_espacial.md) | M3.2, M3.4 | Isomeria de função, cadeia, posição, compensação (metameria) e dinâmica (tautomeria aldo/ceto-enólica). |
| **M3.8** | Isomeria Espacial (Geométrica e Óptica) | [03_quimica_organica/03_isomeria...](03_quimica_organica/03_isomeria_plana_e_espacial.md) | M3.7, M1.5 | Diastereoisomeria cis/trans e sistema E/Z; quiralidade, enantiômeros, luz polarizada, compostos meso. |
| **M3.9** | Reações Orgânicas Fundamentais | [03_quimica_organica/04_reacoes...](03_quimica_organica/04_reacoes_organicas_polimeros_biomoleculas.md) | M3.3 a M3.6 | Adição (Markovnikov/Kharasch), substituição aromática e alifática ($S_N1, S_N2$), eliminação, oxidação. |
| **M3.10**| Polímeros Sintéticos e Meio Ambiente | [03_quimica_organica/04_reacoes...](03_quimica_organica/04_reacoes_organicas_polimeros_biomoleculas.md) | M3.9 | Polímeros de adição (PE, PP, PVC, PS) e de condensação (PET, Nylon, baquelite); degradação e reciclagem. |
| **M3.11**| Biomoléculas e Bioquímica Fundamental | [03_quimica_organica/04_reacoes...](03_quimica_organica/04_reacoes_organicas_polimeros_biomoleculas.md) | M3.4, M3.9 | Carboidratos (monossacarídeos/polissacarídeos), lipídios (triglicerídeos, saponificação), aminoácidos. |

---

## 5. Síntese dos Recursos Didáticos

O autodidata é orientado a combinar a literatura clássica impressa com recursos digitais interativos gratuitos de alta tecnologia:

### 5.1. Bibliografia Clássica de Apoio
* **Ricardo Feltre — *Química* (3 Volumes, Ed. Moderna):** Livro-base obrigatório para o aprofundamento formal e preparação para vestibulares como a UFSC. Exposição rigorosa, demonstrações matemáticas límpidas e excelente acervo de questões de exames federais.
* **Martha Reis — *Química: Ensino Médio* (3 Volumes, Ed. Ática):** Obras de referência definitiva para contextualização socioambiental e alinhamento com a matriz do ENEM. Ideal para leitura inicial e construção de intuição fenomenológica.
* **Usberco e Salvador — *Química* (Ed. Saraiva):** Síntese teórica densa, tabelas comparativas e esquemas conceituais ideais para revisões rápidas.
* **Tito e Canto — *Química na Abordagem do Cotidiano* (Ed. Moderna):** Pioneira na pedagogia CTS (Ciência, Tecnologia e Sociedade); excelente para interpretação de textos densos.
* **Tratados Universitários para Consulta:** Brown (*Química: A Ciência Central*), Atkins (*Princípios de Química*) e Russell (*Química Geral*).

### 5.2. Ecossistema Digital Aberto e Interativo
* **Canais de YouTube:** Prof. Michel (*Café com Química* - rigor milimétrico de lousa), Prof. Igor Química (especialista em questões discursivas e somatórias da UFSC), Prof. Paulo Valim (*Química em Ação* - didática enérgica e quebra de bloqueios), *Canal Marcelão da Química* e *Khan Academy Brasil*.
* **As 9 Simulações PhET Essenciais:**
  1. *Construa um Átomo (Build an Atom)*: partículas subatômicas, isótopos e estabilidade nuclear.
  2. *Dispersão de Rutherford (Rutherford Scattering)*: modelo atômico planetário vs. modelo de Thomson.
  3. *Balanceamento de Equações Químicas (Balancing Chemical Equations)*: leis ponderais e proporções.
  4. *Propriedades dos Gases (Gas Properties)*: variáveis de estado e leis dos gases ideais.
  5. *Concentração e Molaridade (Concentration & Molarity)*: diluição, soluto e solvente.
  6. *Soluções Ácido-Base (Acid-Base Solutions)*: força de eletrólitos, condutividade e escala de pH.
  7. *Sais e Solubilidade (Salts & Solubility)*: saturação dinâmica, precipitação e $K_{ps}$.
  8. *Polaridade da Molécula (Molecule Polarity)*: vetores dipolares tridimensionais e campo elétrico.
  9. *Laboratório da Lei de Beer (Beer's Law Lab)*: absorbância, transmitância e concentrações.
* **Visualizadores Espaciais 3D:**
  * **[MolView](https://molview.org/):** Conversão 2D para 3D, mapas de potencial eletrostático e visualização de conformações moleculares.
  * **[ChemTube3D](https://www.chemtube3d.com/):** Animações tridimensionais rotacionáveis de mecanismos de reações orgânicas ($S_N1, S_N2, E1, E2$, adições eletrofílicas e conformações de barco/cadeira).

---

## 6. Síntese da Estratégia de Prova

### 6.1. Exame Nacional do Ensino Médio (ENEM)
* **Modelagem TRI (ML3P):** A proficiência $\theta$ é calculada ponderando discriminação ($a_i$), dificuldade ($b_i$) e acerto casual/chute ($c_i$). O estudante que acerta itens difíceis mas erra itens fáceis sofre o achatamento de sua nota por **incoerência pedagógica**.
* **A Técnica dos Três Ciclos de Resolução (Gestão do Relógio):**
  * *1º Ciclo (Minutos 01 a 60):* Varredura Dourada. Resolver exclusivamente questões teóricas, conceituais e de leitura rápida (separação de misturas, funções orgânicas, impactos ambientais). Questões com mais de 2 linhas de conta são marcadas com estrela e puladas.
  * *2º Ciclo (Minutos 60 a 110):* Questões Estratégicas de Cálculo Médio (estequiometria direta, Lei de Hess simples, pilhas eletroquímicas, diluição).
  * *3º Ciclo (Minutos 110 a 135):* Problemas Complexos (equilíbrio iônico denso, estequiometrias múltiplas) e eliminação racional de alternativas absurdas.
* **Protocolo de "Desidratação" de Textos:** Ler primeiro o comando final da questão e as alternativas; só então escanear o texto do enunciado buscando unicamente as variáveis e restrições químicas pertinentes.

### 6.2. Vestibular Unificado UFSC (COPERVE)
* **A Mecânica Somatória e a Fórmula Oficial:** Cada questão objetiva possui proposições numeradas em potências de 2 (**01, 02, 04, 08, 16, 32, 64**). Se o número de corretas marcadas ($NPC$) for superior ao de incorretas marcadas ($NPI$), a pontuação é atribuída por:
  $$P = \left\{ \frac{NP - [NTPC - (NPC - NPI)]}{NP} \right\} \times VQ$$
  Onde $NP$ é o total de itens, $NTPC$ é o total de itens verdadeiros do gabarito oficial e $VQ$ é o valor nominal da questão.
* **A Cláusula de Barreira Eliminatória:** Se o candidato assinalar um número de itens falsos igual ou superior ao de verdadeiros ($NPC \le NPI$), a pontuação cai instantaneamente para **zero absoluto ($P = 0,00$)**.
* **Regra Tática de Ouro:** **"A Dúvida Dita a Abstenção"**. Nunca assinale um item sobre o qual haja incerteza. A omissão de um item verdadeiro perde apenas uma fração ($1/NP$), enquanto a marcação indevida de um item falso desconta fração e ainda pode anular toda a pontuação da questão.
* **Questões Abertas Numéricas (00 a 99):** O resultado é sempre um número inteiro entre 00 e 99. É mandatório preencher com **zero à esquerda** (ex.: `04`, `09`) no cartão óptico. A omissão do zero à esquerda anula a leitura da questão.
* **Questões Discursivas Padrão Ouro 10.0:** A banca da COPERVE exige: (1) dados declarados com conversão explícita de unidades, (2) equações químicas rigorosamente balanceadas com indicação obrigatória dos estados físicos $(s)$, $(l)$, $(g)$, $(aq)$, (3) equações literais expressas antes dos números, (4) desenvolvimento com análise dimensional de unidades e (5) resposta textual conclusiva destacada em caixa.

---

## 7. Guia de Execução dos Testes Automatizados

O projeto conta com uma esteira de testes automatizados desenvolvida em **Python 3.12**, operando com a biblioteca padrão `unittest` e sem necessidade de pacotes externos. A suíte é estruturada sob a arquitetura **Dual Track (Trilha Dupla)**:

* **Track 1 (`test_curriculum_coverage.py`):** Valida a existência física dos 28 arquivos do layout oficial, a densidade de conteúdo (> 1.000 caracteres por guia), a ausência absoluta de marcações de incompletude ou placeholders (Zero Placeholder Policy) e a cobertura temática dos 35 módulos canônicos.
* **Track 2 (`test_rubric_validation.py`):** Valida a conformidade das rubricas pedagógicas, critérios de aceitação, transição do zero absoluto, presença de obras didáticas e autores, canais e 9 PhETs, resoluções comentadas passo a passo, equações da TRI e somatórias UFSC, e protocolos de metacognição.

### Comandos de Execução (PowerShell / Windows Terminal):

```powershell
# 1. Executar a suíte unificada via test discovery (Modo Padrão Verboso):
& "C:\Users\guistumpf\AppData\Local\Programs\Python\Python312\python.exe" -m unittest discover -s "C:\Users\guistumpf\teamwork_projects\quimica_estudos\tests" -v

# 2. Executar a suíte no Modo Estrito E2E (Garante 100% dos 28 arquivos sem skips):
$env:STRICT_E2E="1"; & "C:\Users\guistumpf\AppData\Local\Programs\Python\Python312\python.exe" -m unittest discover -s "C:\Users\guistumpf\teamwork_projects\quimica_estudos\tests" -v

# 3. Gerar o Relatório Forense Visual de Cobertura Curricular:
& "C:\Users\guistumpf\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\guistumpf\teamwork_projects\quimica_estudos\tests\test_curriculum_coverage.py" --report

# 4. Gerar o Scorecard de Rubricas Pedagógicas:
& "C:\Users\guistumpf\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\guistumpf\teamwork_projects\quimica_estudos\tests\test_rubric_validation.py"
```

---

## 8. Como Iniciar sua Jornada

Para dar os primeiros passos nesta trilha:

1. Abra o arquivo mestre de planejamento: [PLANO_DE_ESTUDOS_MESTRE.md](PLANO_DE_ESTUDOS_MESTRE.md).
2. Configure o seu ambiente de estudos e o software Anki conforme as instruções de [04_recursos_e_metodologia/metodologia_estudo_ativo_e_caderno_de_erros.md](04_recursos_e_metodologia/metodologia_estudo_ativo_e_caderno_de_erros.md).
3. Inicie os estudos da **Semana 01** pelo guia [00_fundamentos/01_materia_estados_misturas.md](00_fundamentos/01_materia_estados_misturas.md).
4. Mantenha a disciplina de quarentena do Caderno de Erros e acompanhe sua evolução semana a semana até a aprovação!
