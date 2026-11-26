# Project: Plano Completo de Estudos e Guia de Aprendizagem de Química (Zero ao Avançado / ENEM & UFSC)

## Architecture

O projeto estrutura uma plataforma autodidata de aprendizagem integral de Química organizada em 6 núcleos temáticos modulares e 1 esteira de validação E2E. A progressão respeita rigorosamente o Triângulo de Johnstone (Macroscópico $\to$ Submicroscópico $\to$ Simbólico/Representacional), sem saltos conceituais ("zero absoluto"), integrando o perfil interdisciplinar e contextualizado do ENEM (com modelagem TRI ML3P) ao elevado rigor acadêmico formal e analítico das Universidades Federais (com foco no modelo de somatórias 01-64 e questões discursivas da COPERVE/UFSC).

### Diretórios e Layout de Entrega
```
C:\Users\guistumpf\teamwork_projects\quimica_estudos\
├── README.md                                         # Apresentação do projeto e manual de navegação
├── PLANO_DE_ESTUDOS_MESTRE.md                        # Trilha integrada progressiva e cronograma
├── 00_fundamentos/                                   # Nível Fundamental / Zero Absoluto
│   ├── 01_materia_estados_misturas.md
│   ├── 02_atomo_particulas_subatomicas.md
│   ├── 03_isotoppia_e_tabela_introdutoria.md
│   └── exercicios_resolvidos_fundamentos.md
├── 01_quimica_geral_inorganica/                      # Química Geral e Funções Inorgânicas
│   ├── 01_modelos_atomicos_distribuicao_eletronica.md
│   ├── 02_tabela_periodica_e_propriedades.md
│   ├── 03_ligacoes_geometria_polaridade_intermolecular.md
│   ├── 04_funcoes_inorganicas_e_reacoes.md
│   └── exercicios_resolvidos_geral_inorganica.md
├── 02_fisico_quimica/                                # Físico-Química Completa
│   ├── 01_estequiometria_gases_solucoes.md
│   ├── 02_propriedades_coligativas_e_termoquimica.md
│   ├── 03_cinetica_e_equilibrio_quimico_ionico.md
│   ├── 04_eletroquimica_pilhas_eletrolise.md
│   └── exercicios_resolvidos_fisico_quimica.md
├── 03_quimica_organica/                              # Química Orgânica Completa
│   ├── 01_estrutura_carbono_hibridizacao_cadeias.md
│   ├── 02_funcoes_organicas_e_nomenclatura.md
│   ├── 03_isomeria_plana_e_espacial.md
│   ├── 04_reacoes_organicas_polimeros_biomoleculas.md
│   └── exercicios_resolvidos_quimica_organica.md
├── 04_recursos_e_metodologia/                        # Bibliografia, Digital e Metacognição
│   ├── bibliografia_livros_didaticos.md
│   ├── ecossistema_digital_e_simuladores.md
│   └── metodologia_estudo_ativo_e_caderno_de_erros.md
├── 05_roteiro_provas_exercicios/                     # Tática de Provas e Resolução Estratégica
│   ├── estrategico_enem_tri.md
│   ├── estrategico_ufsc_somatorias_discursivas.md
│   ├── simulados_provas_anteriores_e_cronograma.md
│   └── banco_exercicios_comentados_vestibulares.md
└── tests/                                            # Testes E2E e Scripts de Validação
    ├── test_curriculum_coverage.py
    └── test_rubric_validation.py
```

---

## Feature Inventory

| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Fundamentos da Matéria e Estados Físicos | Conceito de matéria, massa, volume, densidade, estados físicos, curvas de aquecimento/resfriamento, substâncias puras e misturas, métodos de separação | M1 | ORIGINAL_REQUEST R1, Survey Pedagogy M0.1-M0.3 |
| 2 | Estrutura Atômica Elementar | Prótons, nêutrons, elétrons, número atômico (Z), número de massa (A), íons (cátions e ânions), isótopos, isóbaros, isótonos | M1 | ORIGINAL_REQUEST R1, Survey Pedagogy M0.4-M0.6 |
| 3 | Introdução à Tabela Periódica | Organização em períodos e famílias, metais, ametais, semimetais, gases nobres e identificação elementar | M1 | ORIGINAL_REQUEST R1, Survey Pedagogy M0.7 |
| 4 | Exercícios Resolvidos de Fundamentos | Questões resolvidas passo a passo, conceituais e de cálculo básico (densidade, partículas) | M1 | ORIGINAL_REQUEST R3, Survey Specs §5 |
| 5 | Modelos Atômicos e Distribuição Eletrônica | Dalton, Thomson, Rutherford, Bohr, modelo de orbitais e distribuição pelo Diagrama de Linus Pauling | M2 | ORIGINAL_REQUEST R1, Survey Pedagogy M1.1-M1.2 |
| 6 | Tabela Periódica Avançada e Propriedades | Raio atômico, energia de ionização, eletronegatividade, eletropositividade, afinidade eletrônica, densidade e PF/PE | M2 | ORIGINAL_REQUEST R1, Survey Pedagogy M1.3 |
| 7 | Ligações Químicas, Geometria e Interações | Ligação iônica, covalente (simples, múltipla, dativa), metálica; geometria molecular VSEPR; polaridade e forças intermoleculares (London, dipolo-dipolo, ligação de hidrogênio) | M2 | ORIGINAL_REQUEST R1, Survey Pedagogy M1.4-M1.7 |
| 8 | Funções Inorgânicas e Reações | Teoria de Arrhenius, ácidos, bases, sais e óxidos; nomenclatura IUPAC/usual; solubilidade; reações de neutralização, síntese, decomposição e simples/dupla troca | M2 | ORIGINAL_REQUEST R1, Survey Pedagogy M1.8-M1.9 |
| 9 | Exercícios Resolvidos de Geral e Inorgânica | Questões conceituais, de geometria, polaridade e reações com gabarito analítico detalhado | M2 | ORIGINAL_REQUEST R3, Survey Specs §5 |
| 10 | Grandezas Químicas, Estequiometria e Gases | Mol, Avogadro, massa molar, fórmulas centesimal/mínima/molecular, leis ponderais, estequiometria simples e com reagente limitante/excesso/pureza/rendimento; leis dos gases, PV=nRT e misturas gasosas | M3 | ORIGINAL_REQUEST R1, Survey Pedagogy M2.1-M2.4 |
| 11 | Soluções e Propriedades Coligativas | Curvas de solubilidade, unidades de concentração (g/L, mol/L, título, ppm), diluição e mistura de soluções; tonoscopia, ebulioscopia, crioscopia, osmoscopia e fator de Van 't Hoff | M3 | ORIGINAL_REQUEST R1, Survey Pedagogy M2.5-M2.6 |
| 12 | Termoquímica e Cinética Química | Entalpia, gráficos exo/endotérmicos, calores de formação e combustão, energia de ligação, Lei de Hess; velocidade média, teoria das colisões, energia de ativação, catalisadores e lei da velocidade | M3 | ORIGINAL_REQUEST R1, Survey Pedagogy M2.7-M2.8 |
| 13 | Equilíbrio Químico e Iônico | Kc, Kp, princípio de Le Chatelier; equilíbrio iônico da água, Ka, Kb, pH e pOH, hidrólise salina, tampões e Kps | M3 | ORIGINAL_REQUEST R1, Survey Pedagogy M2.9-M2.12 |
| 14 | Eletroquímica | Número de oxidação (Nox), balanceamento redox, células galvânicas/pilhas (Danyell, ddp, espontaneidade) e eletrólise ígnea e aquosa com leis de Faraday | M3 | ORIGINAL_REQUEST R1, Survey Pedagogy M2.13-M2.14 |
| 15 | Exercícios Resolvidos de Físico-Química | Problemas numéricos e conceituais passo a passo com conversão de unidades e justificativa de cálculos | M3 | ORIGINAL_REQUEST R3, Survey Specs §5 |
| 16 | Estrutura do Carbono e Nomenclatura | Postulados de Kekulé, hibridização (sp3, sp2, sp), tipos de ligação, classificação de carbonos e cadeias; regras sistemáticas IUPAC | M4 | ORIGINAL_REQUEST R1, Survey Pedagogy M3.1-M3.3 |
| 17 | Funções Orgânicas e Propriedades Físicas | Hidrocarbonetos, álcoois, fenóis, aldeídos, cetonas, ácidos carboxílicos, ésteres, éteres, aminas, amidas, nitrilas, haletos; pontos de ebulição, solubilidade e acidez/basicidade | M4 | ORIGINAL_REQUEST R1, Survey Pedagogy M3.4-M3.6 |
| 18 | Isomeria Plana e Espacial | Isomeria constitucional (função, cadeia, posição, metameria, tautomeria); estereoisomeria geométrica (cis-trans / E-Z) e óptica (carbono quiral, enantiômeros, diastereoisômeros, compostos meso) | M4 | ORIGINAL_REQUEST R1, Survey Pedagogy M3.7-M3.8 |
| 19 | Reações Orgânicas, Polímeros e Biomoléculas | Adição, substituição, eliminação, oxidação/redução, esterificação/saponificação; polímeros de adição e condensação; carboidratos, lipídios, aminoácidos e proteínas | M4 | ORIGINAL_REQUEST R1, Survey Pedagogy M3.9-M3.11 |
| 20 | Exercícios Resolvidos de Orgânica | Resolução comentada de identificação funcional, estereoisomeria e rotas sintéticas | M4 | ORIGINAL_REQUEST R3, Survey Specs §5 |
| 21 | Bibliografia de Referência Clássica | Mapeamento analítico de Ricardo Feltre, Martha Reis, Usberco & Salvador, Tito & Canto e obras universitárias (Brown, Atkins, Russell) com roteiro de uso | M5 | ORIGINAL_REQUEST R2, Survey Resources §1 |
| 22 | Ecossistema Digital e Ferramentas Interativas | Canais do YouTube (Prof. Michel, Ferretto/Igor Química, Paulo Valim, etc.), PhET Simulations mapeadas por tópico, MolView e ChemTube3D | M5 | ORIGINAL_REQUEST R2, Survey Resources §2 |
| 23 | Metodologia Ativa e Caderno de Erros | Active recall, repetição espaçada com Anki (cartões e taxonomias), protocolo do Caderno de Erros (5 causas raiz: LC, EM, ET, RV, IU) e ciclo de reteste cego em 48h | M5 | ORIGINAL_REQUEST R2, R3, Survey Resources §3-§5 |
| 24 | Roteiro Estratégico ENEM | Análise de incidência, competências/habilidades da Matriz de Referência, teoria da TRI (ML3P, coerência pedagógica) e estratégia de prova em 3 passagens | M6 | ORIGINAL_REQUEST R3, Survey Specs §2 |
| 25 | Roteiro Estratégico UFSC (Somatórias e Discursivas) | Mecânica somatória COPERVE (01-64), fórmula exata de pontuação, penalidade de itens incorretos e matriz de decisão "a dúvida dita a abstenção"; padrão ouro de resposta discursiva 10.0 | M6 | ORIGINAL_REQUEST R3, Survey Specs §3 |
| 26 | Cronograma de Provas Anteriores e Simulações | Plano de resolução de provas oficiais ENEM (2015-presente) e UFSC (2015-presente), métricas de desempenho e diagnóstico evolutivo | M6 | ORIGINAL_REQUEST R3, Survey Resources §6 |
| 27 | Banco de Exercícios Comentados ENEM/UFSC | Ampla seleção de exercícios representativos reais do ENEM e vestibulares federais (UFSC, UFRGS, UnB, UFPR) com resolução passo a passo e gabarito justificado | M6 | ORIGINAL_REQUEST R3, Survey Specs §4-§5 |
| 28 | Guia Integrado Mestre e Manual de Navegação | `README.md` e `PLANO_DE_ESTUDOS_MESTRE.md` com visão holística, links para os 6 núcleos e plano semanal | M7 | ORIGINAL_REQUEST R1, R2, R3 |
| 29 | E2E Testing Suite & Quality Audit | Scripts de teste em Python para validar cobertura de todos os tópicos, integridade de arquivos, presença de gabaritos comentados e conformidade das fórmulas | M7 | ORIGINAL_REQUEST Acceptance Criteria |

---

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Fundamentos de Ciências & Química Elementar | Diretório `00_fundamentos/`: Teoria de matéria/estados/misturas, átomo/partículas, isótopos/tabela introdutória + lista de exercícios comentados | none | PLANNED |
| M2 | Química Geral e Inorgânica | Diretório `01_quimica_geral_inorganica/`: Modelos atômicos, Pauling, tabela periódica, ligações/geometria/polaridade, funções inorgânicas + lista comentada | M1 | PLANNED |
| M3 | Físico-Química | Diretório `02_fisico_quimica/`: Grandezas/estequiometria/gases/soluções, coligativas/termoquímica, cinética/equilíbrio, eletroquímica + lista comentada | M1, M2 | PLANNED |
| M4 | Química Orgânica | Diretório `03_quimica_organica/`: Estrutura do carbono/hibridização, funções/nomenclatura, isomeria plana e espacial, reações/polímeros/biomoléculas + lista comentada | M1, M2 | PLANNED |
| M5 | Bibliografia & Recursos Didáticos Digitais | Diretório `04_recursos_e_metodologia/`: Livros clássicos, canais YouTube, 9 PhETs mapeadas, MolView, ChemTube3D, Anki decks e Caderno de Erros | none | PLANNED |
| M6 | Roteiro Estratégico de Exercícios e Provas ENEM/UFSC | Diretório `05_roteiro_provas_exercicios/`: Estratégia ENEM TRI, mecânica somatória UFSC, cronograma de provas oficiais e banco comentado de vestibulares | M1, M2, M3, M4, M5 | PLANNED |
| M7 | E2E Integration, Complete Review & Verification | `README.md`, `PLANO_DE_ESTUDOS_MESTRE.md`, suite de testes automatizados (`tests/`), revisão integral e auditoria forense de integridade | M1, M2, M3, M4, M5, M6 | PLANNED |

---

## Interface Contracts

### 00_fundamentos $\to$ 01_quimica_geral_inorganica
- Fornece: definições de matéria, elemento químico, átomo, prótons ($p$), nêutrons ($n$), elétrons ($e$), número atômico ($Z$), número de massa ($A$), íons (cátion/ânion), isótopos, e organização elementar em períodos e grupos.
- Exige: nenhum pré-requisito químico (apenas aritmética elementar).

### 01_quimica_geral_inorganica $\to$ 02_fisico_quimica
- Fornece: estrutura de valência, distribuição de Linus Pauling, eletronegatividade, tipos de ligações (iônica, covalente, metálica), geometria molecular (VSEPR), polaridade, forças intermoleculares, formulação e nomenclatura de ácidos, bases, sais e óxidos, e reações inorgânicas clássicas.
- Exige: fundamentos de átomo e tabela periódica.

### 01_quimica_geral_inorganica $\to$ 03_quimica_organica
- Fornece: geometria molecular (linear, trigonal plana, tetraédrica), polaridade de ligação e molecular, forças intermoleculares (London, dipolo, pontes de H) e ácidos/bases de Lewis e Arrhenius.
- Exige: modelos de ligação covalente e compartilhamento eletrônico.

### 02_fisico_quimica $\to$ 03_quimica_organica (Conexão Físico-Orgânica)
- Fornece: termoquímica (estabilidade de intermediários), cinética (efeito indutivo e velocidades relativas de substituição/adição), equilíbrios químicos e acidez/basicidade ($Ka, pKa$) de ácidos carboxílicos, fenóis, álcoois e aminas.

### 04_recursos_e_metodologia $\leftrightarrow$ Todos os Módulos Teóricos e de Exercícios
- Fornece: mapeamento de capítulos nos livros de Feltre e Martha Reis para cada tópico teórico; links para simulações PhET e ferramentas 3D; diretrizes do Caderno de Erros para categorização de falhas.

### 05_roteiro_provas_exercicios $\leftrightarrow$ Módulos Curriculares M1 a M4
- Fornece: roteiro prático e banco de questões reais graduadas de vestibulares federais e ENEM que consolidam a teoria desenvolvida em cada módulo.

---

## Code Layout

Os arquivos de conteúdo devem ser gerados em Markdown estruturado, com fórmulas em notação LaTeX/MathJax compatível ($\Delta H$, $K_c$, $pH$, fórmulas estruturais em texto/ASCII/SMILES descritivos quando apropriado), tabelas comparativas, exemplos resolvidos com passo a passo e caixas de destaque didático para ENEM e UFSC:
- Alerta ENEM: Contextualização cotidiana, ambiental ou tecnológica e impacto na TRI.
- Alerta UFSC: Proposições somatórias típicas, pegadinhas de nomenclatura IUPAC estrita e critérios de avaliação da COPERVE.
