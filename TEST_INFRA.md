# Infraestrutura de Testes e Validação E2E (Dual Track Test Architecture)
## Projeto: Plano Completo de Estudos e Guia de Aprendizagem de Química (Zero ao Avançado / ENEM & UFSC)

---

## 1. Filosofia e Arquitetura de Testes

O projeto adota uma arquitetura de testes **Dual Track (Trilha Dupla)** focada na garantia da qualidade pedagógica, estrutural e técnica do material educacional. Como o produto final consiste em guias textuais, conceituais e matemáticos em Markdown destinados a estudantes autodidatas em preparação para exames de altíssima concorrência (ENEM e Vestibulares Federais, notadamente UFSC), os testes operam segundo princípios de **caixa-preta opaca (opaque-box)**, estritamente orientados pelos requisitos de aceitação (`ORIGINAL_REQUEST.md`), escopo mestre (`PROJECT.md`) e especificações de exames (`survey_specs.md`, `survey_pedagogy.md`, `survey_resources.md`).

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        DUAL TRACK TEST ARCHITECTURE (QUÍMICA)                          │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│ TRACK 1: AUTOMATED AUDIT SUITES           │ TRACK 2: FORENSIC RUBRIC VALIDATION        │
│ (Execução Contínua em Python)             │ (Conformidade Pedagógica e Metacognitiva)  │
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│ • test_curriculum_coverage.py             │ • test_rubric_validation.py                │
│ • Presença física dos 28 arquivos mestre   │ • Transição "Zero ao Avançado" (p, n, e-)  │
│ • Auditoria de 35 módulos curriculares    │ • Bibliografia clássica completa e autores │
│ • Métrica volumétrica (> 1.000 chars)     │ • 9 Simulações PhET e canais YouTube       │
│ • Tolerância zero a placeholders (TODO...) │ • Exercícios com resolução passo a passo   │
│ • Validação de cabeçalhos e seções-chave   │ • Mecânica Somatória UFSC e TRI do ENEM    │
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

### 1.1. Princípios Norteadores
1. **Verificação Baseada em Requisitos (Requirement-Driven):** Cada asserção de teste é diretamente rastreável a um critério de aceitação de `ORIGINAL_REQUEST.md` ou diretriz de `PROJECT.md`.
2. **Integridade de Conteúdo e Anti-Facade:** É expressamente vedado o uso de testes que passem com conteúdo superficial ou simulado. Cada guia curricular deve conter substância conceitual densa, definições formais, equações balanceadas e exemplos aplicados.
3. **Progressão Pedagógica Estrita:** Validação de que não existem "saltos conceituais" inexplicados, assegurando a ancoragem epistemológica do Triângulo de Johnstone (Macroscópico $\to$ Submicroscópico $\to$ Simbólico).
4. **Semântica Limpa de Exit Codes:** Os executores de teste em Python emitem código `0` em caso de sucesso pleno e código `1` em caso de falha de cobertura ou violação de rubrica, permitindo integração transparente em pipelines de integração contínua (CI) e auditorias automatizadas.

---

## 2. Inventário Completo de Funcionalidades (Tiers 1 a 4)

O conjunto de entregáveis é mapeado em quatro camadas de criticidade (Tiers 1 a 4), cobrindo desde os fundamentos elementares até o refinamento tático de prova:

| Tier | Componente / Funcionalidade | Arquivos Abrangidos | Critérios de Sucesso e Validação |
| :---: | :--- | :--- | :--- |
| **Tier 1** | **Fundamentos de Ciências & Nivelamento Zero** | `00_fundamentos/01_materia_estados_misturas.md`<br>`00_fundamentos/02_atomo_particulas_subatomicas.md`<br>`00_fundamentos/03_isotoppia_e_tabela_introdutoria.md`<br>`00_fundamentos/exercicios_resolvidos_fundamentos.md`<br>`PLANO_DE_ESTUDOS_MESTRE.md`<br>`README.md` | • Conceito claro de matéria, densidade ($d=m/V$), curvas de aquecimento e separação de misturas.<br>• Estrutura atômica elementar: prótons, nêutrons, elétrons, $Z$, $A$, cátions e ânions.<br>• Tabela periódica introdutória (metais, ametais, famílias).<br>• Exercícios de fixação com resolução comentada passo a passo. |
| **Tier 2** | **Química Geral, Inorgânica, Físico-Química e Orgânica** | `01_quimica_geral_inorganica/*.md`<br>`02_fisico_quimica/*.md`<br>`03_quimica_organica/*.md` | • Modelos atômicos (Dalton a Bohr/quântico), diagrama de Linus Pauling, VSEPR e polaridade.<br>• Funções inorgânicas de Arrhenius e reações balanceadas.<br>• Estequiometria (mol, pureza, rendimento, limitante), gases ideais e soluções.<br>• Termoquímica (Hess), Cinética, Equilíbrio ($K_c, K_p, pH, K_{ps}$) e Eletroquímica.<br>• Carbono, hibridização, funções orgânicas, isomeria (plana, geométrica, óptica), reações e polímeros.<br>• Listas resolvidas em cada um dos três grandes núcleos. |
| **Tier 3** | **Recursos Didáticos, Ferramentas Digitais e Metodologia Ativa** | `04_recursos_e_metodologia/bibliografia_livros_didaticos.md`<br>`04_recursos_e_metodologia/ecossistema_digital_e_simuladores.md`<br>`04_recursos_e_metodologia/metodologia_estudo_ativo_e_caderno_de_erros.md` | • Análise crítica detalhada de Feltre, Martha Reis, Usberco & Salvador, Tito & Canto.<br>• Obras de consulta universitária (Brown, Atkins, Russell).<br>• Canais YouTube (Michel, Igor, Valim, Marcelão, Kuadro, Khan).<br>• 9 simulações interativas PhET mapeadas tópico a tópico; MolView e ChemTube3D.<br>• Metodologia ativa: Active Recall, Feynman, Dual Coding.<br>• Protocolo Anki com cloze deletions e Caderno de Erros com as 5 causas-raiz (LC, EM, ET, RV, IU) e reteste em 48h. |
| **Tier 4** | **Engenharia de Provas, Simulados e Resolução Estratégica ENEM/UFSC** | `05_roteiro_provas_exercicios/estrategico_enem_tri.md`<br>`05_roteiro_provas_exercicios/estrategico_ufsc_somatorias_discursivas.md`<br>`05_roteiro_provas_exercicios/simulados_provas_anteriores_e_cronograma.md`<br>`05_roteiro_provas_exercicios/banco_exercicios_comentados_vestibulares.md` | • ENEM: Modelo TRI 3PL, matriz de habilidades C7 (H24-H27) e tática dos Três Ciclos.<br>• UFSC: Fórmula oficial da somatória $P = \frac{NP - [NTPC - (NPC - NPI)]}{NP} \times VQ$, barreira $NPC > NPI$, questões abertas 00-99 (com zero à esquerda) e padrão 10.0 para discursivas.<br>• Cronograma de provas oficiais 2015-presente e banco de questões reais comentadas com gabarito justificado proposição por proposição. |

---

## 3. Especificação dos Runners de Teste Automatizados

A suíte automatizada reside no diretório `tests/` e utiliza exclusivamente a biblioteca padrão do Python (`unittest`, `pathlib`, `re`, `sys`), prescindindo de dependências externas pesadas:

### 3.1. `tests/test_curriculum_coverage.py`
Executa a auditoria estrutural e de integridade física de todos os módulos do projeto:
- **Testes de Existência de Arquivos:** Confirma se cada um dos 28 arquivos previstos no layout de `PROJECT.md` está presente no disco.
- **Testes de Densidade Volumétrica de Conteúdo:** Exige que cada documento contenha mais de 1.000 caracteres de texto real (assegurando que nenhum arquivo seja um esboço ou rascunho incompleto).
- **Testes de Auditoria de Placeholders (Zero Placeholder Policy):** Varre os arquivos em busca de marcações de incompletude, tais como:
  * `TODO` / `FIXME` / `TBD`
  * `[A preencher]` / `[Inserir aqui]` / `[Em construção]`
  * `lorem ipsum`
  * Trechos inacabados entre colchetes indicativos de rascunho não finalizado.
- **Auditoria dos 35 Módulos Canônicos:** Verifica se todos os 35 tópicos conceituais descritos no mapa curricular de `survey_pedagogy.md` (M0.1 a M0.7, M1.1 a M1.9, M2.1 a M2.14, M3.1 a M3.11, mais Recursos e Roteiros de Provas) encontram-se representados e abordados nos respectivos arquivos.

### 3.2. `tests/test_rubric_validation.py`
Executa a auditoria de conformidade das regras de negócio pedagógicas e critérios de aceitação:
- **Rubrica 1 — Transição Conceitual "Zero Absoluto":** Valida se o Stage 0 explicita conceitos basilares (`átomo`, `próton`, `nêutron`, `elétron`, `número atômico`, `número de massa`, `tabela periódica`), garantindo acessibilidade a quem nunca estudou química.
- **Rubrica 2 — Bibliografia Clássica e Autores de Referência:** Valida se o módulo bibliográfico cita formalmente as obras e autores canônicos (`Ricardo Feltre`, `Martha Reis`, `Usberco`, `Tito e Canto`, `Brown`, `Atkins`, `Russell`), com direcionamento didático.
- **Rubrica 3 — Ecossistema Digital Gratuito:** Valida a presença de canais abertos do YouTube (`Michel` / `Café com Química`, `Igor Química`, `Paulo Valim`) e a cobertura das **9 simulações interativas PhET** recomendadas (Construa um Átomo, Rutherford, Balanceamento, Gases, Concentração/Molaridade, Ácido-Base, Sais/Solubilidade, Polaridade, Beer), além de `MolView` e `ChemTube3D`.
- **Rubrica 4 — Rigor dos Exercícios e Resoluções Passo a Passo:** Valida se as listas de exercícios de todos os blocos (`00_fundamentos`, `01_quimica_geral_inorganica`, `02_fisico_quimica`, `03_quimica_organica` e `05_roteiro_provas_exercicios`) contêm resoluções completas e detalhadas, identificando dados do enunciado, raciocínio químico e cálculos matemáticos explícitos.
- **Rubrica 5 — Engenharia de Provas ENEM e UFSC:**
  * Valida a modelagem da **TRI (Teoria de Resposta ao Item)**, modelo logístico 3PL e coerência pedagógica no roteiro do ENEM.
  * Valida a mecânica de **Somatórias da COPERVE/UFSC**, incluindo a fórmula matemática oficial da pontuação ($P$), a cláusula eliminatória de validação ($NPC > NPI$), a regra do zero à esquerda para questões abertas (`00` a `99`), e os critérios formais para respostas discursivas de Química (equacionamento com estados físicos e unidades SI).
- **Rubrica 6 — Metacognição e Caderno de Erros:** Valida o protocolo do Caderno de Erros com a taxonomia das 5 causas-raiz (`LC`, `EM`, `ET`, `RV`, `IU`) e o ciclo de reteste cego de 48 horas.

---

## 4. Matriz de Rastreabilidade dos Critérios de Aceitação

| Critério de Aceitação (`ORIGINAL_REQUEST.md`) | Requisito Formal | Arquivo de Teste Responsável | Método de Teste Específico |
| :--- | :--- | :--- | :--- |
| **Trilha do Zero ao Avançado** | Contemplar explicitamente transição desde átomo, prótons, nêutrons até o conteúdo integral de Geral, Físico-Química e Orgânica. | `test_rubric_validation.py` | `test_zero_to_advanced_progression()`<br>`test_pedagogical_stages_continuity()` |
| **Sequência Lógica de Pré-Requisitos** | Módulos ordenados em sequência lógica e interdependente. | `test_curriculum_coverage.py` | `test_module_dependency_hierarchy()` |
| **Livros Didáticos Clássicos** | Indicação com títulos, autores e orientações para vestibular. | `test_rubric_validation.py` | `test_classic_textbooks_rubric()` |
| **Recursos Gratuitos e Simuladores** | Videoaulas abertas, PhET Simulations e visualizadores 3D. | `test_rubric_validation.py` | `test_free_digital_resources_and_phet()` |
| **Exercícios Passo a Passo** | Resoluções explicadas e comentadas para cada bloco curricular. | `test_rubric_validation.py` | `test_step_by_step_exercise_solutions()` |
| **Roteiro Estratégico ENEM e UFSC** | Provas anteriores, métricas de revisão de erros, TRI e mecânica somatória. | `test_rubric_validation.py` | `test_enem_tri_and_ufsc_somatorias_mechanics()`<br>`test_error_log_and_metacognition_metrics()` |
| **Entregáveis no Diretório Alvo** | Todos os arquivos presentes e sem placeholders em `~/teamwork_projects/quimica_estudos`. | `test_curriculum_coverage.py` | `test_all_expected_files_exist()`<br>`test_files_minimum_character_count()`<br>`test_zero_placeholders_audit()` |

---

## 5. Como Executar os Testes

Para executar os testes a partir da linha de comando (PowerShell ou Bash):

```powershell
# Navegar até o diretório raiz do projeto
cd C:\Users\guistumpf\teamwork_projects\quimica_estudos

# Executar a suíte de cobertura curricular
python tests/test_curriculum_coverage.py

# Executar a suíte de validação de rubricas pedagógicas
python tests/test_rubric_validation.py

# Ou executar ambos simultaneamente via unittest padrão do Python
python -m unittest discover -s tests -p "test_*.py" -v
```
