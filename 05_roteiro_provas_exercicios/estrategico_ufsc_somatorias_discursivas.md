# GUIA ESTRATÉGICO UFSC: MECÂNICA DE SOMATÓRIAS, QUESTÕES ABERTAS (00-99) E PADRÃO DISCURSIVO COPERVE

**Documento:** `05_roteiro_provas_exercicios/estrategico_ufsc_somatorias_discursivas.md`  
**Núcleo:** 05 — Roteiro Estratégico de Exercícios e Provas ENEM/UFSC  
**Banca Examinadora:** COPERVE / Universidade Federal de Santa Catarina (UFSC)  
**Público-Alvo:** Autodidatas em preparação para aprovação com excelência acadêmica

---

## 1. VISÃO GERAL E PERFIL AVALIATIVO DA COPERVE/UFSC

A Comissão Permanente do Vestibular da Universidade Federal de Santa Catarina (**COPERVE/UFSC**) é reconhecida nacionalmente por administrar um dos exames seletivos mais exigentes, analíticos e intelectualmente sofisticados do ensino superior brasileiro.

Diferentemente da abordagem prioritariamente fenomenológica e interdisciplinar do ENEM, a prova de Química da UFSC caracteriza-se por:
1. **Elevado Rigor Formal e Conceitual:** Exigência de definições canônicas estritas, reconhecimento das regras sistemáticas e atualizadas da IUPAC, distinção milimétrica entre conceitos correlatos (ex.: ligação covalente intramolecular versus força intermolecular) e cobrança de exceções periódicas e particularidades de orbitais e reatividade.
2. **Exatidão Algébrica e Estequiométrica:** Os enunciados trazem dados quantitativos reais e experimentais. Não há espaço para estimativas vagas ou arredondamentos grosseiros: as contas devem ser executadas com precisão decimal para atingir valores que definam a veracidade de proposições ou o preenchimento de questões abertas numéricas.
3. **Mecânica Avaliativa Binária e Aberta:** A COPERVE não adota testes tradicionais de múltipla escolha simples de 5 opções (A-E). O vestibular da UFSC estrutura-se em **Questões Somatórias de Proposições Múltiplas (01 a 64)**, **Questões Abertas Numéricas (00 a 99)** e **Questões Discursivas Interdisciplinares** com espelhos analíticos de correção.

Neste modelo, o desconhecimento das regras matemáticas do edital pode anular o desempenho de um estudante que domina a teoria. Este guia estabelece a engenharia tática e matemática completa para dominar o Vestibular da UFSC.

---

## 2. A MECÂNICA DAS QUESTÕES SOMATÓRIAS (PROPOSIÇÕES 01 A 64)

### 2.1 A Estrutura de Numeração Binária

Nas questões de proposições múltiplas da COPERVE, cada proposição afirmativa é indexada por uma potência de base 2:

$$\{2^0, 2^1, 2^2, 2^3, 2^4, 2^5, 2^6\} = \{\mathbf{01}, \mathbf{02}, \mathbf{04}, \mathbf{08}, \mathbf{16}, \mathbf{32}, \mathbf{64}\}$$

O candidato deve analisar independentemente a veracidade ou falsidade de cada uma das proposições apresentadas (habitualmente 6 ou 7 proposições por questão). A resposta oficial que o candidato transcreve para a Folha de Respostas é um **número inteiro compreendido entre 01 e 99** (ou até 127 quando há 7 proposições), resultante da **soma aritmética exclusiva das proposições consideradas verdadeiras**.

#### Propriedade da Unicidade da Representação Binária:
Graças ao Teorema Fundamental da Representação Numérica em Base Binária, para qualquer subconjunto de proposições corretas, a sua soma resulta em um número inteiro estritamente único. Não existem duas combinações distintas de proposições que produzam a mesma soma. 
* Exemplo: Uma soma `21` decompõe-se matematicamente apenas como $16 + 4 + 1$ (proposições 01, 04 e 16). O sistema leitor óptico decodifica de forma inequívoca quais proposições o candidato marcou.

---

### 2.2 A Fórmula Matemática Oficial de Cálculo da Pontuação ($P$)

O edital oficial da COPERVE/UFSC define a atribuição de pontuação por uma **função matemática por partes**, governada por uma **cláusula de barreira eliminatória**:

$$P = \begin{cases} \left\{ \frac{NP - [NTPC - (NPC - NPI)]}{NP} \right\} \times VQ & \text{se } NPC > NPI \\ 0,00 & \text{se } NPC \le NPI \end{cases}$$

Onde:
* **$P$:** Pontuação líquida final obtida pelo candidato na questão (arredondada para duas casas decimais).
* **$NP$:** Número total de proposições que integram a questão (geralmente $NP = 7$ se as opções vão de 01 a 64; ou $NP = 6$ se vão de 01 a 32).
* **$NTPC$:** Número Total de Proposições Corretas (verdadeiras) da questão, segundo o gabarito oficial definitivo da COPERVE.
* **$NPC$:** Número de Proposições Corretas consideradas/marcadas pelo candidato em sua resposta.
* **$NPI$:** Número de Proposições Incorretas (falsas) que o candidato marcou erroneamente como verdadeiras.
* **$VQ$:** Valor nominal (peso) da questão na escala da prova (habitualmente $VQ = 1,00$).

---

### 2.3 Análise Algébrica e Dedução das Penalidades

Para compreender a fundo a dinâmica da fórmula quando a condição $NPC > NPI$ é atendida, podemos expandir algebricamente o numerador da fração:

$$\text{Numerador} = NP - NTPC + NPC - NPI = (NP - NTPC) + NPC - NPI$$

Lembrando que $(NP - NTPC)$ é exatamente o **Número Total de Proposições Incorretas ($NTPI$)** da questão:

$$P = \left\{ \frac{NTPI + NPC - NPI}{NP} \right\} \times VQ$$

Dessa equivalência matemática decorrem três conclusões fundamentais sobre o impacto das decisões do candidato:
1. **Impacto da Omissão de uma Proposição Correta:** Se o candidato deixa de assinalar uma proposição que era verdadeira, $NPC$ diminui em $1$ unidade. A perda de pontuação é de:
   $$\Delta P_{\text{omissão}} = -\frac{1}{NP} \times VQ$$
   Em uma questão de 7 proposições ($NP = 7, VQ = 1,00$), a omissão custa $-\frac{1}{7} \approx -0,143$ pontos.
2. **Impacto da Marcação de uma Proposição Falsa:** Se o candidato assinala uma proposição que era falsa, $NPI$ aumenta em $1$ unidade. A penalização direta na fórmula é:
   $$\Delta P_{\text{erro}} = -\frac{1}{NP} \times VQ$$
   Ou seja, o desconto matemático imediato no cálculo parcial é idêntico ao da omissão ($-\frac{1}{7} \approx -0,143$ pontos).
3. **O Risco Catastrófico da Barreira Eliminatória ($NPC \le NPI$):**
   Embora o desconto marginal de errar ou omitir pareça igual na fração interna, assinalar uma incorreta aproxima perigosamente o candidato da barreira de anulação $NPC \le NPI$. Se o número de proposições falsas marcadas igualar ou superar o de verdadeiras, a questão inteira é sumariamente **ZERADA ($P = 0,00$)**, incinerando todos os acertos legítimos conquistados!

---

### 2.4 Simulações Numéricas Passo a Passo da Fórmula COPERVE

Considere uma questão típica de Química da UFSC com **$NP = 7$ proposições (01, 02, 04, 08, 16, 32, 64)** e valor $VQ = 1,00$.  
Suponha que o gabarito oficial homologue como verdadeiras as proposições **01, 04 e 16** (Soma Oficial = $01 + 04 + 16 = \mathbf{21}$).  
Temos:
* $NP = 7$
* $NTPC = 3$ (proposições 01, 04, 16)
* $NTPI = 7 - 3 = 4$ (proposições 02, 08, 32, 64 são falsas)

Vamos analisar cinco cenários reais de conduta do vestibulando:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                           SIMULAÇÃO NUMÉRICA DE CENÁRIOS DA SOMATÓRIA                           │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Cenário 1: Acerto Pleno (Perfeição Técnica)                                                     │
│ - Candidato marca: 21 (01 + 04 + 16).                                                           │
│ - NPC = 3, NPI = 0.                                                                             │
│ - Checagem da Barreira: NPC > NPI (3 > 0) -> VÁLIDO.                                            │
│ - Cálculo: P = { (7 - [3 - (3 - 0)]) / 7 } x 1,00 = { (7 - [3 - 3]) / 7 } = 7/7 = 1,00 PONTO.    │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Cenário 2: Acerto Parcial Conservador (Omissão Estratégica / Abstenção na Dúvida)               │
│ - Candidato tem certeza de 01 e 16, tem dúvida sobre 04 e não marca. Resposta: 17 (01 + 16).    │
│ - NPC = 2, NPI = 0.                                                                             │
│ - Checagem da Barreira: NPC > NPI (2 > 0) -> VÁLIDO.                                            │
│ - Cálculo: P = { (7 - [3 - (2 - 0)]) / 7 } x 1,00 = { (7 - [3 - 2]) / 7 } = (7 - 1) / 7        │
│   P = 6/7 ≈ 0,86 PONTOS (Preserva 86% da pontuação total da questão!).                          │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Cenário 3: Acerto Parcial com Erro por Excesso (Arriscou e Errou uma Falsa)                     │
│ - Candidato marca as corretas 01, 04, 16, mas arrisca e inclui a falsa 08. Resposta: 29.       │
│ - NPC = 3, NPI = 1.                                                                             │
│ - Checagem da Barreira: NPC > NPI (3 > 1) -> VÁLIDO.                                            │
│ - Cálculo: P = { (7 - [3 - (3 - 1)]) / 7 } x 1,00 = { (7 - [3 - 2]) / 7 } = (7 - 1) / 7        │
│   P = 6/7 ≈ 0,86 PONTOS.                                                                        │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Cenário 4: Desastre por Cláusula Eliminatória (Dois Acertos e Dois Erros)                       │
│ - Candidato marca as corretas 01 e 04, mas marca também as falsas 02 e 08. Resposta: 15.        │
│ - NPC = 2, NPI = 2.                                                                             │
│ - Checagem da Barreira: NPC <= NPI (2 <= 2) -> CONDIÇÃO DE BARREIRA ATIVADA!                    │
│   PONTUAÇÃO ATRIBUÍDA: P = 0,00 PONTO (A questão é integralmente anulada e zerada).             │
│   Se o candidato tivesse omitido as duas em que tinha dúvida, teria NPC=2, NPI=0 e nota 0,86!  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Cenário 5: O "Chute Cego" em Todas as Proposições (Soma 127)                                    │
│ - Candidato não sabe nada e assinala todas as 7 proposições (01 + 02 + 04 + 08 + 16 + 32 + 64).│
│ - NPC = 3 (acertou todas as verdadeiras), mas NPI = 4 (marcou todas as falsas).                 │
│ - Checagem da Barreira: NPC <= NPI (3 <= 4) -> BARREIRA ATIVADA.                                │
│   PONTUAÇÃO ATRIBUÍDA: P = 0,00 PONTO.                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. A MATRIZ DE DECISÃO TÁTICA: "A DÚVIDA DITA A ABSTENÇÃO"

A demonstração matemática dos cenários acima fundamenta a regra de sobrevivência mais importante do Vestibular da UFSC: **A Dúvida Dita a Abstenção**.

### 3.1 Teoria dos Jogos e Esperança Matemática da Abstenção
Suponha que você já identificou com 100% de certeza duas proposições verdadeiras ($NPC = 2, NPI = 0$).  
Sua pontuação garantida até o momento é:
$$P = \frac{7 - [NTPC - 2]}{7}$$
Se você se depara com uma terceira proposição ambígua e sua dúvida é total ($50\%$ de chance de ser verdadeira e $50\%$ de ser falsa), qual é o valor esperado se você arriscar versus se você se abstiver?
* **Se você se abstiver:** Você não corre risco algum. Sua nota permanece em $0,86$ (se $NTPC=3$) ou $0,71$ (se $NTPC=4$).
* **Se você arriscar e ela for verdadeira:** Você ganha $+0,14$ pontos (subindo de $0,86$ para $1,00$).
* **Se você arriscar e ela for falsa:** Você perde $-0,14$ pontos (descendo para $0,71$) e, caso você tenha apenas um acerto anterior ($NPC = 1$), assinalar uma falsa ($NPI = 1$) faz com que $NPC \le NPI$, **reduzindo sua pontuação de 0,86 para ZERO ABSOLUTO** (perda líquida de $-0,86$ pontos).

A assimetria de risco é esmagadora: você arrisca perder $0,86$ pontos em troca de um ganho potencial de apenas $0,14$ pontos. A relação risco/retorno é de **6 para 1 contra o estudante**!

### 3.2 O Fluxograma de Decisão em Prova

```
                        ┌──────────────────────────────────────────────┐
                        │   ESTOU LENDO UMA PROPOSIÇÃO NA PROVA UFSC   │
                        └──────────────────────┬───────────────────────┘
                                               │
             ┌─────────────────────────────────┼─────────────────────────────────┐
             ▼                                 ▼                                 ▼
┌───────────────────────────┐    ┌───────────────────────────┐    ┌───────────────────────────┐
│     CERTEZA ABSOLUTA      │    │     DÚVIDA METÓDICA       │    │     CERTEZA ABSOLUTA      │
│      QUE É VERDADEIRA     │    │  (Não sei demonstrar 100%)│    │       QUE É FALSA         │
└────────────┬──────────────┘    └─────────────┬─────────────┘    └─────────────┬─────────────┘
             │                                 │                                │
             ▼                                 ▼                                ▼
┌───────────────────────────┐    ┌───────────────────────────┐    ┌───────────────────────────┐
│   SOMAR AO MEU GABARITO   │    │    ABSTENÇÃO IMEDIATA     │    │  DESCARTAR / NÃO SOMAR    │
│   (Garante fração NP)     │    │   (NÃO ARRISCAR JAMAIS)   │    │  (Evita elevação de NPI)  │
└───────────────────────────┘    └───────────────────────────┘    └───────────────────────────┘
```

---

## 4. A REGRA ESTRITA DAS QUESTÕES OBJETIVAS ABERTAS (00 A 99)

Em todas as edições do vestibular, a COPERVE inclui questões objetivas que **não são somatórias**, denominadas **Questões Abertas Numéricas**:

### 4.1 Características Operacionais das Abertas
1. O enunciado propõe um problema quantitativo analítico cujo desfecho numérico é rigorosamente um **número inteiro compreendido entre 00 e 99**.
2. Não há proposições para julgar e não há pontuação parcial: ou o candidato encontra exatamente o valor numérico inteiro ou o escore é zero.

### 4.2 A Regra Mandatória do Preenchimento do Zero à Esquerda
O Cartão-Resposta da UFSC possui duas colunas de preenchimento óptico para cada questão aberta: a coluna das **Dezenas ($D$)** e a coluna das **Unidades ($U$)**.

```
    CARTÃO DE RESPOSTAS (LEITURA ÓPTICA)
    Questão Aberta: Resultado obtido pelo candidato = 7

         DEZENAS (D)        UNIDADES (U)
            [ 0 ] ◄── MARCADO   [ 0 ]
            [ 1 ]               [ 1 ]
            [ 2 ]               [ 2 ]
            [ 3 ]               [ 3 ]
            [ 4 ]               [ 4 ]
            [ 5 ]               [ 5 ]
            [ 6 ]               [ 6 ]
            [ 7 ]               [ 7 ] ◄── MARCADO
            [ 8 ]               [ 8 ]
            [ 9 ]               [ 9 ]
    
    PREENCHIMENTO CORRETO: "07"
    PREENCHIMENTO COM FALHA (ZERADO): Deixar Dezenas em branco e marcar apenas 7 na Unidade!
```

> **ADVERTÊNCIA OFICIAL DA COPERVE:**  
> Se o resultado do seu cálculo for um número de 0 a 9, é **obrigatório preencher o dígito zero na coluna da esquerda** (ex.: `00`, `01`, `02`, `04`, `07`, `09`).  
> O leitor óptico computadorizado rejeita como nula a questão que contiver apenas um dígito marcado na coluna de unidades com a coluna de dezenas em branco. Se o cálculo resultar em zero absoluto, marque obrigatoriamente `00`.

---

## 5. O PADRÃO-OURO PARA QUESTÕES DISCURSIVAS DA UFSC (RUBRICA NOTA 10.0)

A COPERVE aplica, no primeiro dia do Vestibular Unificado, questões discursivas interdisciplinares que frequentemente envolvem conceitos profundos de Química articulados com Biologia e Física.

### 5.1 Os Quatro Pilares da Rubrica de Correção 10.0 da Banca Examinadora

A análise dos Relatórios Oficiais de Avaliação da COPERVE revela que os corretores descontam frações decimais preciosas da nota ($0,25$, $0,50$ ou mais) quando o estudante comete falhas formais de comunicação científica. Para obter **Nota Máxima 10.0**, o candidato deve cumprir quatro mandamentos inegociáveis:

#### Pilar 1: Estados de Agregação da Matéria Explícitos
Em qualquer equação química solicitada ou utilizada na memória de cálculo, é mandatória a notação subscrita ou entre parênteses do estado físico de cada espécie química:
- $(s)$ para sólido; $(l)$ para líquido puro; $(g)$ para gás; $(aq)$ para espécies solvatadas em solução aquosa.
- *Exemplo de Falha (Nota Reduzida):* $CaCO_3 + 2 HCl \rightarrow CaCl_2 + H_2O + CO_2$
- *Exemplo Padrão-Ouro (Nota 10.0):*
  $$CaCO_{3(s)} + 2\,HCl_{(aq)} \longrightarrow CaCl_{2(aq)} + H_2O_{(l)} + CO_{2(g)}$$

#### Pilar 2: Equações Rigorosamente Balanceadas pelos Menores Coeficientes Inteiros
A conservação da massa (Lavoisier) e das cargas elétricas deve ser impecável. Em reações redox, o método íon-elétron ou do Nox deve estar demonstrado, eliminando íons espectadores quando solicitada a equação iônica simplificada:
$$2\,Al^0_{(s)} + 6\,H^+_{(aq)} \longrightarrow 2\,Al^{3+}_{(aq)} + 3\,H_{2(g)}$$

#### Pilar 3: Memória de Cálculo Completa com Unidades de Medida em Todas as Etapas
Nunca insira números "jogados" na folha de resposta sem antes declarar a lei física ou fórmula química utilizada. A análise dimensional deve acompanhar cada substituição até o resultado final:
- *Formulação Literal:* $C = \frac{m_1}{V}$ ou $PV = nRT \implies n = \frac{PV}{RT}$
- *Substituição com Unidades:*
  $$n = \frac{1,00\text{ atm} \times 4,10\text{ L}}{0,082\text{ atm}\cdot\text{L}\cdot\text{mol}^{-1}\cdot\text{K}^{-1} \times 300\text{ K}} = \frac{4,10}{24,6}\text{ mol} = 0,167\text{ mol de } CO_2$$
- Omitir unidades como $g/mol$, $mol/L$, $J$, $kJ/mol$ ou $atm$ custa até 30% da pontuação do item discursivo!

#### Pilar 4: Justificativa Teórica com Conexão Causa-Efeito e Vocabulário Preciso
Evite justificativas genéricas ou baseadas em "senso comum". Explicite o mecanismo microscópico fundamental:
- Em vez de dizer: *"O álcool ferve mais alto que o éter porque ele é mais forte."*
- Redija no padrão acadêmico: *"As moléculas do etanol ($CH_3CH_2OH$) interagem entre si por meio de **ligações de hidrogênio**, decorrentes do hidrogênio polarizado ligado ao átomo altamente eletronegativo de oxigênio. Já as moléculas do éter dimetílico ($CH_3OCH_3$), embora polares, interagem por forças dipolo-dipolo permanente de menor intensidade. Como as ligações de hidrogênio exigem maior energia cinética média para serem rompidas na transição de fase líquida para vapor, o etanol apresenta ponto de ebulição significativamente mais elevado."*

---

### 5.2 Estudo de Caso Comparativo: Resposta Nota 3.0 vs. Resposta Padrão-Ouro 10.0

#### Enunciado Discursivo (Modelo COPERVE/UFSC):
> Em um ensaio de controle ambiental, uma alíquota de $100,0\text{ mL}$ de uma solução aquosa de ácido clorídrico ($HCl$) de concentração $0,050\text{ mol/L}$ foi misturada com $100,0\text{ mL}$ de uma solução aquosa de hidróxido de sódio ($NaOH$) de concentração $0,030\text{ mol/L}$, sob temperatura de $25^\circ\text{C}$.  
> a) Escreva a equação química balanceada da reação de neutralização com os estados de agregação.  
> b) Determine a quantidade de matéria (em mol) do reagente em excesso e calcule o pH final da mistura resultante.

---

#### Resposta do Candidato Amador (Nota Atribuída pela Banca: 3,0 / 10,0):
> a) $HCl + NaOH \rightarrow NaCl + H_2O$  
> b) $100 \times 0,05 = 5$  
> $100 \times 0,03 = 3$  
> Sobra $2$.  
> $pH = 2$.
>
> *Parecer do Corretor da COPERVE:* Omitiu os estados de agregação na equação (a). Não declarou fórmulas conceituais, misturou volume em mL gerando milimols sem explicitar unidades, não recalculou a concentração molar no volume final duplicado ($200\text{ mL}$), gerando cálculo errôneo do pH ($pH = -\log[H^+]$). Nota severamente penalizada.

---

#### Resposta Padrão-Ouro (Nota Atribuída pela Banca: 10,0 / 10,0):

**Item a) Equação Química Balanceada com Estados de Agregação:**
$$HCl_{(aq)} + NaOH_{(aq)} \longrightarrow NaCl_{(aq)} + H_2O_{(l)}$$
Equação iônica simplificada de neutralização:
$$H^+_{(aq)} + OH^-_{(aq)} \longrightarrow H_2O_{(l)}$$

**Item b) Quantidade de Matéria em Excesso e Cálculo Rigoroso do pH:**

1. **Cálculo da quantidade de matéria inicial de cada reagente ($n = C \times V$):**
   - Volume das soluções em litros: $V_{HCl} = 100,0\text{ mL} = 0,100\text{ L}$; $V_{NaOH} = 100,0\text{ mL} = 0,100\text{ L}$.
   - $n(HCl) = 0,050\text{ mol/L} \times 0,100\text{ L} = 5,0 \times 10^{-3}\text{ mol de } H^+_{(aq)}$.
   - $n(NaOH) = 0,030\text{ mol/L} \times 0,100\text{ L} = 3,0 \times 10^{-3}\text{ mol de } OH^-_{(aq)}$.

2. **Determinação do Reagente Limitante e do Excesso:**
   - A proporção estequiométrica da reação de neutralização é de $1 : 1$.
   - O $NaOH$ é o reagente limitante ($3,0 \times 10^{-3}\text{ mol}$ consumidos integralmente).
   - O $HCl$ é o reagente em excesso.
   - **Quantidade de matéria em excesso de $HCl$ ($H^+$):**
     $$n_{\text{excesso}}(H^+) = 5,0 \times 10^{-3}\text{ mol} - 3,0 \times 10^{-3}\text{ mol} = \mathbf{2,0 \times 10^{-3}\text{ mol de } H^+_{(aq)}}$$

3. **Cálculo da Concentração Efetiva de Íons $H^+$ na Mistura Resultante:**
   - O volume final da solução após a mistura é aditivo:
     $$V_{\text{final}} = V_{HCl} + V_{NaOH} = 0,100\text{ L} + 0,100\text{ L} = 0,200\text{ L}$$
   - A concentração molar de íons hidrogênio livres em solução aquosa é dada por:
     $$[H^+] = \frac{n_{\text{excesso}}}{V_{\text{final}}} = \frac{2,0 \times 10^{-3}\text{ mol}}{0,200\text{ L}} = 1,0 \times 10^{-2}\text{ mol/L}$$

4. **Cálculo do pH da Mistura a $25^\circ\text{C}$:**
   - Aplicando a definição formal de Sorensen:
     $$pH = -\log[H^+] = -\log(1,0 \times 10^{-2}) = -(-2) = \mathbf{2,00}$$
   - *Conclusão:* A solução final apresenta caráter ácido com $pH = 2,00$ e $2,0 \times 10^{-3}\text{ mol}$ de ácido clorídrico remanescente.

---

## 6. SÍNTESE E CHECKLIST DE COMBATE PARA O VESTIBULANDO UFSC

- [ ] **Nas Somatórias:** Nunca chute proposições duvidosas. Lembre-se que $NPC \le NPI$ zera o item inteiro. Aplique sem hesitar o princípio: "A Dúvida Dita a Abstenção".
- [ ] **Nas Questões Abertas:** Se a resposta for de um único dígito, preencha compulsoriamente com **zero à esquerda** (`00` a `09`) no cartão óptico.
- [ ] **Nas Discursivas:** Indique sempre os **estados de agregação** ($(s), (l), (g), (aq)$), balanceie as equações, exiba as fórmulas literais antes dos valores numéricos e carregue as **unidades de medida** ($mol/L, g, kJ$) até o fim.
