# Módulo 01: Grandezas Químicas, Estequiometria, Estudo dos Gases e Soluções

---

## 1. Grandezas Químicas Fundamentais

No laboratório ou no cotidiano, manipulamos porções macroscópicas de matéria (gramas, quilogramas, litros), mas as transformações químicas ocorrem na escala submicroscópica de átomos, moléculas e íons. As grandezas químicas operam como uma ponte quantitativa formal entre o domínio corpuscular e a escala mensurável.

```
                    A PONTE DAS GRANDEZAS QUÍMICAS
           Mundo Submicroscópico                 Mundo Macroscópico
       ┌───────────────────────────┐         ┌─────────────────────────┐
       │     Átomos / Moléculas    │         │     Massa em Gramas     │
       │  (Massa Atômica em "u")   │         │    Volume em Litros     │
       └─────────────┬─────────────┘         └────────────▲────────────┘
                     │                                    │
                     └──────────────► MOL ────────────────┘
                                  (6,022 × 10²³)
```

---

### 1.1. Unidade de Massa Atômica ($u$)

Como a massa de um único átomo é da ordem de $10^{-24}\text{ a }10^{-22}\text{ g}$, o uso do grama tornaria a notação prática excessivamente incômoda. Por convenção internacional (IUPAC, 1961), definiu-se a **Unidade de Massa Atômica ($u$)**:

> **DEFINIÇÃO DE $1\ u$:**  
> A unidade de massa atômica equivale a exatamente $\frac{1}{12}$ da massa de um único átomo do isótopo Carbono-12 ($^{12}_{\ 6}C$):
>
> $$1\ u = \frac{m(^{12}C)}{12} \approx 1,66054 \times 10^{-24}\text{ g} = 1,66054 \times 10^{-27}\text{ kg}$$

---

### 1.2. Massa Atômica de um Átomo vs. Massa Atômica de um Elemento

- **Massa Atômica de um Isótopo Individual:** Representa quantas vezes aquele átomo específico é mais pesado do que $\frac{1}{12}$ do $^{12}C$. Exemplo: a massa de um átomo de $^{35}Cl$ é aproximadamente $34,97\ u$.
- **Massa Atômica de um Elemento Químico ($MA$):** Na natureza, a grande maioria dos elementos químicos é uma mistura de dois ou mais isótopos estáveis com proporções percentuais fixas (abundância isotópica natural). A massa atômica que consta na Tabela Periódica é a **média aritmética ponderada** das massas atômicas desses isótopos:

$$MA = \frac{(A_1 \times \%_1) + (A_2 \times \%_2) + \dots + (A_n \times \%_n)}{100}$$

#### Exemplo Prático e Dedutivo: Massa Atômica do Cloro
O elemento cloro ocorre na crosta terrestre como uma mistura de dois isótopos:
- $^{35}Cl$ (massa $\approx 35\ u$): abundância de $75,77\%$
- $^{37}Cl$ (massa $\approx 37\ u$): abundância de $24,23\%$

$$MA(Cl) = \frac{(35 \times 75,77) + (37 \times 24,23)}{100} = \frac{2651,95 + 896,51}{100} = \frac{3548,46}{100} \approx 35,45\ u$$

> 💡 **POR QUE AS MASSAS NA TABELA PERIÓDICA NÃO SÃO INTEIRAS?**  
> A massa atômica fracionária do cloro ($35,45\ u$) não significa que exista um átomo com meio nêutron, mas reflete a média estatística de uma amostra natural contendo trilhões de átomos de $^{35}Cl$ e $^{37}Cl$.

---

### 1.3. Massa Molecular ($MM$)

A **Massa Molecular** de uma substância molecular (ou massa fórmula para compostos iônicos) é a soma das massas atômicas de todos os átomos presentes em sua fórmula mínima ou molecular:

$$\text{Para } H_2SO_4: \quad MM = (2 \times MA_H) + (1 \times MA_S) + (4 \times MA_O) = (2 \times 1) + (1 \times 32) + (4 \times 16) = 98\ u$$

---

### 1.4. O Conceito de Mol e a Constante de Avogadro ($N_A$)

O **mol** é a unidade de base do Sistema Internacional (SI) para a grandeza **Quantidade de Matéria** (símbolo $n$).

> **DEFINIÇÃO DE MOL (IUPAC 2019):**  
> Um mol contém exatamente $6,02214076 \times 10^{23}$ entidades elementares. Este número é o valor numérico fixado da **Constante de Avogadro** ($N_A$), quando expressa na unidade $\text{mol}^{-1}$:
>
> $$N_A \approx 6,022 \times 10^{23}\text{ entidades/mol}$$

O mol é uma unidade de contagem analítica, tal como "dúzia" (12 unidades) ou "cento" (100 unidades):
- $1\text{ mol de átomos de } C = 6,022 \times 10^{23}\text{ átomos de } C$
- $1\text{ mol de moléculas de } H_2O = 6,022 \times 10^{23}\text{ moléculas de } H_2O$
- $1\text{ mol de elétrons} = 6,022 \times 10^{23}\text{ elétrons}$
- $1\text{ mol de íons } SO_4^{2-} = 6,022 \times 10^{23}\text{ íons } SO_4^{2-}$

---

### 1.5. Massa Molar ($M$)

A **Massa Molar** ($M$) é a massa em gramas de um mol de qualquer entidade química. Sua unidade padrão é $\text{g/mol}$.

A relação numérica entre a massa atômica/molecular (em $u$) e a massa molar (em $\text{g/mol}$) é de equivalência exata por definição do mol:
- $1\text{ átomo de } ^{12}C$ tem massa de $12\ u$.
- $1\text{ mol de átomos de } ^{12}C$ tem massa de exatamente $12\text{ g}$.
- $1\text{ molécula de } H_2O$ tem massa de $18\ u$.
- $1\text{ mol de moléculas de } H_2O$ tem massa de $18\text{ g}$.

A relação quantitativa elementar entre massa ($m$, em gramas), quantidade de matéria ($n$, em mols) e massa molar ($M$, em $\text{g/mol}$) é dada por:

$$n = \frac{m}{M} \iff m = n \times M$$

---

### 1.6. Volume Molar dos Gases nas CNTP

O **Volume Molar** ($V_m$) é o volume ocupado por $1\text{ mol}$ de qualquer gás ideal submetido a uma dada pressão e temperatura:

1. **Convenção Clássica de Vestibulares no Brasil (CNTP - 1 atm e 0 °C / 273,15 K):**
   $$V_m = \frac{R \cdot T}{P} = \frac{0,082057 \times 273,15}{1,00} \approx 22,414\text{ L/mol} \approx \mathbf{22,4\ L/mol}$$
2. **Convenção Moderna IUPAC (STP - 1 bar e 0 °C / 273,15 K):**
   Como $1\text{ bar} = 10^5\text{ Pa} \approx 0,9869\text{ atm}$, a pressão é ligeiramente menor, resultando em:
   $$V_m = \frac{8,31446 \times 273,15}{100.000} \approx 0,022711\text{ m}^3\text{/mol} \approx \mathbf{22,7\ L/mol}$$

> ⚠️ **ALERTA DE PROVA (ENEM & UFSC):**  
> As provas do ENEM, UFSC e federais continuam utilizando majoritariamente a convenção clássica de **$22,4\text{ L/mol}$** quando citam "CNTP" ($1\text{ atm}$ e $0^\circ C$). Caso a banca deseje o uso de $22,7\text{ L/mol}$, o enunciado especificará formalmente "condições padrão a 1 bar" ou fornecerá explicitamente o valor de $R$. Na ausência de menção contrária em questões com CNTP, utilize $22,4\text{ L/mol}$.

---

## 2. Determinação de Fórmulas Químicas

A determinação da fórmula de um composto sintetizado ou isolado na natureza é um procedimento clássico da química analítica estruturado em três níveis crescentes de informação.

```
                 HIERARQUIA DE FÓRMULAS QUÍMICAS
  ┌──────────────────────────────────────────────────────────────┐
  │ 1. Fórmula Percentual (Centesimal): Composição em % massa    │
  └──────────────────────────────┬───────────────────────────────┘
                                 ▼ Conversão de % em mols
  ┌──────────────────────────────────────────────────────────────┐
  │ 2. Fórmula Mínima (Empírica): Menor proporção inteira        │
  └──────────────────────────────┬───────────────────────────────┘
                                 ▼ Multiplicação pelo fator n (M_real / M_min)
  ┌──────────────────────────────────────────────────────────────┐
  │ 3. Fórmula Molecular: Número real de átomos por molécula     │
  └──────────────────────────────────────────────────────────────┘
```

### 2.1. Fórmula Percentual / Centesimal
Expressa a porcentagem em massa de cada elemento químico constituinte em $100\text{ g}$ do composto:

$$\%_A = \frac{\text{massa total do elemento } A \text{ em 1 mol da substância}}{\text{massa molar total da substância}} \times 100\%$$

*Exemplo:* Para o etanol ($C_2H_6O$, $M = 46\text{ g/mol}$):
- $\% C = \frac{2 \times 12}{46} \times 100\% = \frac{24}{46} \times 100\% \approx 52,17\%$
- $\% H = \frac{6 \times 1}{46} \times 100\% = \frac{6}{46} \times 100\% \approx 13,04\%$
- $\% O = \frac{1 \times 16}{46} \times 100\% = \frac{16}{46} \times 100\% \approx 34,78\%$

---

### 2.2. Algoritmo Analítico: Da Composição Centesimal à Fórmula Mínima

Para encontrar a fórmula mínima a partir de dados analíticos percentuais:

1. **Passo 1 (Base de Cálculo):** Assuma uma amostra arbitrária de $100\text{ g}$ do composto. Cada valor percentual converte-se diretamente em gramas.
2. **Passo 2 (Conversão em Mols):** Divida a massa de cada elemento por sua respectiva massa atômica: $n_i = \frac{m_i}{MA_i}$.
3. **Passo 3 (Simplificação Relativa):** Divida todos os valores de $n_i$ pelo menor valor numérico encontrado entre eles.
4. **Passo 4 (Ajuste para Inteiros):** Se os resultados forem números inteiros (ou muito próximos de inteiros, como $1,01 \to 1$), esses serão os índices da fórmula empírica. Se surgir uma fração decimal canônica (ex.: $1,50$ ou $1,33$), multiplique todos os índices pelo menor inteiro que elimine a fração ($1,50 \times 2 = 3$; $1,33 \times 3 = 4$).

#### Exemplo de Aplicação Resolvido:
Um composto orgânico contém $40,0\%$ de Carbono, $6,67\%$ de Hidrogênio e $53,33\%$ de Oxigênio em massa. Determine sua fórmula mínima.

- Em $100\text{ g}$: $m_C = 40,0\text{ g}$; $m_H = 6,67\text{ g}$; $m_O = 53,33\text{ g}$.
- Quantidade em mols:
  $$n_C = \frac{40,0}{12} \approx 3,333\text{ mol}$$
  $$n_H = \frac{6,67}{1} \approx 6,670\text{ mol}$$
  $$n_O = \frac{53,33}{16} \approx 3,333\text{ mol}$$
- Dividindo pelo menor ($3,333$):
  $$C: \frac{3,333}{3,333} = 1 \quad ; \quad H: \frac{6,670}{3,333} \approx 2 \quad ; \quad O: \frac{3,333}{3,333} = 1$$
- **Fórmula Mínima:** $\mathbf{CH_2O}$ (com massa da fórmula empírica $M_{\text{mín}} = 12 + 2 + 16 = 30\text{ g/mol}$).

---

### 2.3. Determinação da Fórmula Molecular

A fórmula molecular real é um múltiplo inteiro $n$ da fórmula empírica:

$$(\text{Fórmula Mínima})_n = \text{Fórmula Molecular} \implies n = \frac{M_{\text{molecular real}}}{M_{\text{fórmula mínima}}}$$

Continuando o exemplo anterior: se um espectrômetro de massas determinou que a massa molar real do composto é $180\text{ g/mol}$ (caso da glicose):

$$n = \frac{180\text{ g/mol}}{30\text{ g/mol}} = 6 \implies (CH_2O)_6 = \mathbf{C_6H_{12}O_6}$$

---

## 3. As Leis Ponderais e Volumétricas da Matéria

A consolidação da Química como ciência exata no final do século XVIII e início do XIX assentou-se sobre princípios quantitativos rigorosos de conservação e proporção.

```
                      AS TRÊS GRANDES LEIS PONDERAIS
  ┌─────────────────────────┐ ┌─────────────────────────┐ ┌─────────────────────────┐
  │      LEI DE LAVOISIER   │ │       LEI DE PROUST     │ │       LEI DE DALTON     │
  │ Conservação das Massas  │ │  Proporções Constantes  │ │  Proporções Múltiplas   │
  │     (Sistema Fechado)   │ │  (Composição Invariável)│ │ (Séries de Compostos)   │
  │   Σ m_reag = Σ m_prod   │ │  m_A / m_B = constante  │ │    m_B1 / m_B2 = p / q  │
  └─────────────────────────┘ └─────────────────────────┘ └─────────────────────────┘
```

### 3.1. Lei de Lavoisier (Conservação das Massas, 1789)
> *"Em um sistema termodinamicamente fechado, a massa total antes da reação química é rigorosamente idêntica à massa total após a reação."*
>
> $$\sum m_{\text{reagentes}} = \sum m_{\text{produtos}}$$

*Implicação direta:* Os átomos não são criados nem destruídos; apenas rearranjam-se. Disso decorre a obrigatoriedade absoluta do **balanceamento de equações químicas**.

### 3.2. Lei de Proust (Proporções Definidas ou Constantes, 1799)
> *"Uma determinada substância pura, qualquer que seja sua origem ou processo de obtenção, é formada sempre pelos mesmos elementos combinados na mesma proporção em massa invariável."*

*Exemplo:* Para a síntese da água pura ($2 H_2 + O_2 \to 2 H_2O$):
- Experimento 1: $4\text{ g de } H_2 + 32\text{ g de } O_2 \to 36\text{ g de } H_2O$ (Razão $H/O = 4/32 = 1/8$).
- Experimento 2: $10\text{ g de } H_2 + 80\text{ g de } O_2 \to 90\text{ g de } H_2O$ (Razão $H/O = 10/80 = 1/8$).

### 3.3. Lei Volumétrica de Gay-Lussac (1808)
> *"Nas mesmas condições de pressão e temperatura, os volumes de todos os gases reagentes e produtos mantêm entre si proporções de números inteiros e pequenos."*

Disso decorre o Princípio de Avogadro: **volumes iguais de gases quaisquer, sob a mesma pressão e temperatura, contêm o mesmo número de moléculas (ou de mols)**.

---

## 4. Estequiometria Fundamental e Casos Especiais

A estequiometria (do grego *stoicheion*, elemento, e *metron*, medida) é o cálculo das proporções quantitativas de reagentes e produtos em reações químicas balanceadas.

### 4.1. As Quatro Leituras Canônicas de uma Equação Química
Dada a síntese da amônia pelo Processo de Haber-Bosch:

$$\mathbf{1\ N_{2(g)} + 3\ H_{2(g)} \longrightarrow 2\ NH_{3(g)}}$$

Podemos ler essa transformação em quatro escalas proporcionais:
1. **Em Quantidade de Matéria (Mols):** $1\text{ mol de } N_2 : 3\text{ mols de } H_2 : 2\text{ mols de } NH_3$.
2. **Em Número de Moléculas / Entidades:** $1 \times N_A\text{ moléculas de } N_2 : 3 \times N_A\text{ moléculas de } H_2 : 2 \times N_A\text{ moléculas de } NH_3$.
3. **Em Massa (Gramas):** $(1 \times 28\text{ g de } N_2) + (3 \times 2\text{ g de } H_2) \longrightarrow (2 \times 17\text{ g de } NH_3) \implies 28\text{ g} + 6\text{ g} = 34\text{ g}$ (Verifica Lavoisier!).
4. **Em Volume Gasoso (CNTP - 1 atm, 0 °C):** $1 \times 22,4\text{ L de } N_2 : 3 \times 22,4\text{ L de } H_2 : 2 \times 22,4\text{ L de } NH_3 \implies 22,4\text{ L} : 67,2\text{ L} : 44,8\text{ L}$.

---

### 4.2. Algoritmo em Três Passos para a Estequiometria Simples

Todo cálculo estequiométrico seguro deve seguir o protocolo:
- **Passo 1 (Equação e Balanceamento):** Escrever a equação química e balancear rigorosamente os coeficientes.
- **Passo 2 (Linha Teórica Padrão):** Escrever a linha estequiométrica de referência diretamente abaixo das espécies de interesse, convertendo os coeficientes para as grandezas fornecidas ou pedidas ($g$, $mol$, $L$, átomos).
- **Passo 3 (Linha do Problema e Resolução):** Posicionar os dados numéricos do enunciado e a incógnita ($x$), executando a proporção direta.

---

### 4.3. Reagente Limitante vs. Reagente em Excesso

Em processos industriais e reações laboratoriais, os reagentes raramente são adicionados nas proporções estequiométricas exatas. Um dos reagentes esgota-se antes dos demais, cessando a reação.

- **Reagente Limitante:** É a substância que é inteiramente consumida primeiro. É ele que determina e limita teoricamente a quantidade máxima de produtos formados.
- **Reagente em Excesso:** É a substância adicionada em quantidade superior à estequiometria requerida. Uma parcela reage e outra parcela permanece intacta ao término do processo.

#### Algoritmo Analítico Infalível de Detecção:
1. Calcule a quantidade em mols ($n$) de cada reagente disponível na mistura inicial.
2. Divida o número de mols de cada reagente pelo seu respectivo coeficiente estequiométrico na equação balanceada:
   $$\text{Quociente } Q_i = \frac{n_{\text{fornecido}}}{c_{\text{estequiométrico}}}$$
3. Compare os quocientes:
   - O reagente que possuir o **menor quociente $Q$** é, obrigatoriamente, o **REAGENTE LIMITANTE**.
   - Os reagentes com maiores quocientes estão em **EXCESSO**.
4. **Regra de Ouro:** Execute todos os cálculos subsequentes de produtos gerados baseando-se EXCLUSIVAMENTE nos dados do reagente limitante!

```
                  ALGORITMO DE LIMITANTE E EXCESSO
       Reagente A (n_A mols)                  Reagente B (n_B mols)
       Coeficiente a                          Coeficiente b
              │                                      │
              ▼                                      ▼
       Q_A = n_A / a                          Q_B = n_B / b
              │                                      │
              └──────────────► COMPARAÇÃO ◄──────────┘
                                     │
                 ┌───────────────────┴───────────────────┐
                 ▼                                       ▼
          Se Q_A < Q_B:                           Se Q_B < Q_A:
     A é LIMITANTE (dita a conta)            B é LIMITANTE (dita a conta)
     B está em EXCESSO                       A está em EXCESSO
```

#### Exemplo Prático e Numérico:
Misturam-se $100\text{ g de } H_2$ ($M = 2\text{ g/mol}$) com $320\text{ g de } O_2$ ($M = 32\text{ g/mol}$) para formação de água.
Equação balanceada: $2\ H_2 + 1\ O_2 \to 2\ H_2O$.
- $n(H_2) = \frac{100}{2} = 50\text{ mols}$
- $n(O_2) = \frac{320}{32} = 10\text{ mols}$
- Quocientes:
  $$Q(H_2) = \frac{50}{2} = 25 \quad ; \quad Q(O_2) = \frac{10}{1} = 10$$
- Como $10 < 25$, o **$O_2$ é o reagente limitante** e o $H_2$ está em excesso.
- Massa de água formada: $1\text{ mol de } O_2 \to 2\text{ mols de } H_2O (36\text{ g})$. Para $10\text{ mols de } O_2 \implies 10 \times 36 = \mathbf{360\text{ g de } H_2O}$.
- Excesso de $H_2$ não reagido: $10\text{ mols de } O_2$ consomem $2 \times 10 = 20\text{ mols de } H_2$.
  Sobra: $50 - 20 = 30\text{ mols de } H_2 \implies 30 \times 2 = \mathbf{60\text{ g de } H_2\text{ em excesso}}$.
  (Verificação: $100\text{ g } H_2 + 320\text{ g } O_2 = 420\text{ g inicial}$. No final: $360\text{ g água} + 60\text{ g } H_2\text{ sobra} = 420\text{ g}$. Lavoisier satisfeito!).

---

### 4.4. Grau de Pureza dos Reagentes

Matérias-primas industriais e minérios raramente são substâncias 100% puras (ex.: bauxita, calcário, hematita). A fração pura é aquela que efetivamente participa da reação:

$$\text{Pureza } (P) = \frac{m_{\text{substância ativa pura}}}{m_{\text{amostra bruta total}}} \times 100\% \implies m_{\text{pura}} = m_{\text{bruta}} \times \left(\frac{P}{100}\right)$$

> ⚠️ **ATENÇÃO METODOLÓGICA:**  
> A correção de pureza deve ser feita **no início do cálculo**, antes de lançar o valor na linha da regra de três! As impurezas são inertes e não geram produtos.

---

### 4.5. Rendimento Real de uma Reação ($R$)

Por razões de equilíbrio químico, perdas mecânicas nas vidrarias laboratoriais ou tubulações, reações concorrentes/secundárias ou impurezas ocultas, a quantidade de produto obtida na prática ($m_{\text{real}}$) é habitualmente menor do que a quantidade calculada teoricamente pela estequiometria ($m_{\text{teórica}}$):

$$\text{Rendimento } (R) = \frac{m_{\text{real obtida}}}{m_{\text{teórica esperada (100\%)}}} \times 100\%$$

> 💡 **ORDEM OPERACIONAL RECOMENDADA:**  
> Calcule primeiro a massa de produto assumindo rendimento ideal de $100\%$. Em seguida, aplique o percentual de rendimento fornecido: $m_{\text{real}} = m_{\text{teórica}} \times \frac{R}{100}$.

---

### 4.6. Reações Consecutivas / Reações em Cadeia

Frequentemente uma rota sintética ou processo metalúrgico ocorre através de duas ou mais reações intermediárias sucessivas.
Exemplo: Síntese industrial do ácido sulfúrico ($H_2SO_4$) pelo Processo de Contato:
1. Queima do enxofre: $S_{(s)} + O_{2(g)} \longrightarrow SO_{2(g)}$
2. Oxidação catalítica: $2\ SO_{2(g)} + O_{2(g)} \overset{V_2O_5}{\longrightarrow} 2\ SO_{3(g)}$
3. Hidratação do trióxido: $SO_{3(g)} + H_2O_{(l)} \longrightarrow H_2SO_{4(aq)}$

Para executar o cálculo estequiométrico global relacionando $S$ e $H_2SO_4$:
- Multiplicam-se as equações por coeficientes que permitam cancelar os intermediários ($SO_2$ e $SO_3$):
  - Multiplica-se a etapa 1 por $2$: $2 S + 2 O_2 \to 2 SO_2$
  - Mantém-se a etapa 2: $2 SO_2 + O_2 \to 2 SO_3$
  - Multiplica-se a etapa 3 por $2$: $2 SO_3 + 2 H_2O \to 2 H_2SO_4$
- Somando algebricamente as equações:
  $$\mathbf{2\ S_{(s)} + 3\ O_{2(g)} + 2\ H_2O_{(l)} \longrightarrow 2\ H_2SO_{4(aq)}} \iff \mathbf{1\ S \longrightarrow 1\ H_2SO_4}$$

A relação estequiométrica direta mostra que $1\text{ mol de enxofre } S$ ($32\text{ g}$) produz teoricamente $1\text{ mol de } H_2SO_4$ ($98\text{ g}$).

---

## 5. Estudo dos Gases

O estado gasoso é caracterizado por forças intermoleculares atrativas desprezíveis frente à energia cinética das partículas, conferindo aos gases elevada compressibilidade e capacidade de expansão indefinida preenchendo todo o volume disponível.

```
                  VARIÁVEIS DE ESTADO DE UM GÁS
             Pressão (P)            Volume (V)
       [Força por unidade de área] [Espaço tridimensional]
             (atm, mmHg, Pa)             (L, mL, m³)
                               │
                               ▼
                    Temperatura Absoluta (T)
               [Medida da Energia Cinética Média]
                    (SEMPRE em Kelvin: K)
```

---

### 5.1. O Modelo do Gás Ideal (Perfeito)
Um gás ideal é um modelo teórico fundamentado nos postulados da **Teoria Cinética dos Gases**:
1. As partículas gasosas são pontuais (possuem massa, mas seu volume próprio é infinitamente desprezível em relação ao volume total ocupado).
2. O movimento das partículas é contínuo, caótico e retilíneo.
3. Não há forças de atração ou repulsão mútua entre as partículas à distância.
4. As colisões entre as partículas e contra as paredes do recipiente são perfeitamente elásticas (não há perda de energia cinética global durante os choques).
5. A temperatura absoluta ($T$, em Kelvin) é diretamente proporcional à energia cinética média de translação das moléculas ($\overline{E}_c = \frac{3}{2} k_B T$).

> 🔬 **DESVIOS DO COMPORTAMENTO IDEAL (GASES REAIS):**  
> Um gás real aproxima-se do comportamento de gás ideal sob condições de **BAIXA PRESSÃO** (moléculas muito afastadas, tornando suas forças intermoleculares nulas e seu volume próprio desprezível) e **ALTA TEMPERATURA** (alta velocidade cinética, superando qualquer atração mútua).

---

### 5.2. As Leis Empíricas das Transformações Gasosas

Para uma massa fixa de gás confinado ($n = \text{constante}$):

1. **Transformação Isotérmica (Lei de Boyle-Mariotte, 1662):**
   - Temperatura constante ($T = \text{cte}$).
   - Pressão e volume são grandezas inversamente proporcionais:
     $$P_1 \cdot V_1 = P_2 \cdot V_2 = \text{constante}$$
   - A representação gráfica no plano $P \times V$ é uma **hipérbole equilátera** (Isoterma).

2. **Transformação Isobárica (Lei de Charles e Gay-Lussac, 1787):**
   - Pressão constante ($P = \text{cte}$).
   - Volume e temperatura absoluta são grandezas diretamente proporcionais:
     $$\frac{V_1}{T_1} = \frac{V_2}{T_2} \iff \frac{V}{T} = \text{constante}$$
   - Gráfico $V \times T(K)$: reta linear que extrapola até a origem no zero absoluto ($0\text{ K}$).

3. **Transformação Isocórica / Isovolumétrica (Lei de Gay-Lussac, 1802):**
   - Volume constante ($V = \text{cte}$).
   - Pressão e temperatura absoluta são diretamente proporcionais:
     $$\frac{P_1}{T_1} = \frac{P_2}{T_2} \iff \frac{P}{T} = \text{constante}$$

---

### 5.3. Equação Geral dos Gases Ideais
Combinando as três transformações para uma dada quantidade de gás que transita do estado 1 para o estado 2:

$$\frac{P_1 \cdot V_1}{T_1} = \frac{P_2 \cdot V_2}{T_2}$$

> 🚨 **REGRA DE SOBREVIVÊNCIA METROLÓGICA:**  
> A temperatura $T$ nas equações gasosas DEVE SER EXPRESSA SEMPRE EM KELVIN:
>
> $$T(K) = \theta(^\circ C) + 273,15 \approx \theta(^\circ C) + 273$$

---

### 5.4. A Equação de Estado de Clapeyron

Ao incluir a quantidade de matéria ($n$), deduz-se a **Equação de Clapeyron**:

$$P \cdot V = n \cdot R \cdot T \iff P \cdot V = \frac{m}{M} \cdot R \cdot T$$

Onde $R$ é a **Constante Universal dos Gases Ideais**:
- $R \approx \mathbf{0,082057\ \text{atm}\cdot\text{L}/(\text{mol}\cdot\text{K})}$ (quando $P$ em atm, $V$ em litros).
- $R \approx \mathbf{62,36\ \text{mmHg}\cdot\text{L}/(\text{mol}\cdot\text{K})}$ (quando $P$ em mmHg).
- $R \approx \mathbf{8,314\ \text{J}/(\text{mol}\cdot\text{K})} = \mathbf{8,314\ \text{Pa}\cdot\text{m}^3/(\text{mol}\cdot\text{K})}$ (no Sistema Internacional - SI).

---

### 5.5. Densidade e Massa Molar de Gases

Isolando a razão $\frac{m}{V}$ a partir de $P \cdot V = \frac{m}{M} \cdot R \cdot T$:

$$d = \frac{m}{V} = \frac{P \cdot M}{R \cdot T}$$

- **Fatores determinantes da densidade gasosa:**
  - A densidade de um gás é **diretamente proporcional** à sua massa molar ($M$) e à pressão ($P$).
  - A densidade é **inversamente proporcional** à temperatura absoluta ($T$). Ar quente sobe em um balão porque, ao ser aquecido sob pressão ambiente constante, seu volume expande e sua densidade diminui.

---

### 5.6. Misturas Gasosas: Dalton e Amagat

Em uma mistura de gases que não reagem quimicamente entre si:
- Número total de mols: $n_{\text{total}} = n_A + n_B + \dots + n_k$
- **Fração Molar ($X_i$):** É a razão entre os mols do componente $i$ e os mols totais:
  $$X_i = \frac{n_i}{n_{\text{total}}} \quad \text{onde} \quad \sum X_i = 1$$

#### A. Lei de Dalton das Pressões Parciais
> *"A pressão total exercida por uma mistura gasosa é igual à soma das pressões parciais que cada gás exerceria se estivesse ocupando sozinho o volume total do recipiente à mesma temperatura."*

$$P_{\text{total}} = P_A + P_B + \dots + P_k$$

A **Pressão Parcial ($P_i$)** de um gás na mistura é proporcional à sua fração molar:

$$P_i = X_i \cdot P_{\text{total}}$$

#### B. Lei de Amagat dos Volumes Parciais
> *"O volume total de uma mistura de gases ideais é a soma dos volumes parciais que cada gás componente ocuparia se estivesse submetido isoladamente à pressão total do sistema."*

$$V_{\text{total}} = V_A + V_B + \dots + V_k \implies V_i = X_i \cdot V_{\text{total}}$$

*Consequência analítica:* Para gases ideais, **a fração molar é numericamente idêntica à fração volumétrica e à fração de pressão**:

$$X_i = \frac{n_i}{n_{\text{total}}} = \frac{P_i}{P_{\text{total}}} = \frac{V_i}{V_{\text{total}}}$$

#### C. Massa Molar Média / Aparente de uma Mistura Gasosa
$$M_{\text{mistura}} = \sum (X_i \cdot M_i)$$

*Exemplo: Ar Atmosférico Seco* ($\approx 78\%\ N_2$, $21\%\ O_2$, $1\%\ Ar$):
$$M_{\text{ar}} = (0,78 \times 28) + (0,21 \times 32) + (0,01 \times 40) = 21,84 + 6,72 + 0,40 = \mathbf{28,96\text{ g/mol}}$$

Como a massa molar do gás hélio ($He = 4\text{ g/mol}$) ou do metano ($CH_4 = 16\text{ g/mol}$) é menor que $28,96\text{ g/mol}$, esses gases ascendem na atmosfera terrestre. Já o gás cloro ($Cl_2 = 71\text{ g/mol}$) ou o gás carbônico ($CO_2 = 44\text{ g/mol}$) são mais densos que o ar e acumulam-se em depressões e no piso.

---

## 6. Soluções, Dispersões e Curvas de Solubilidade

Uma solução é uma mistura física homogênea formada por duas ou mais substâncias, composta por um **solvente** (dispersante, habitualmente o componente em maior quantidade) e um ou mais **solutos** (dispersos).

```
                      ESPECTRO DOS SISTEMAS DISPERSOS
     Solução Verdadeira               Coloide                     Suspensão
       (Homogênea)             (Micro-heterogênea)              (Heterogênea)
  ┌───────────────────────┐  ┌───────────────────────┐    ┌───────────────────────┐
  │ Diâmetro < 1 nm       │  │ Diâmetro: 1 a 1000 nm │    │ Diâmetro > 1000 nm    │
  │ Não sedimenta         │  │ Não sedimenta por grav│    │ Sedimenta espontâneo  │
  │ Não filtra em papel   │  │ Efeito Tyndall (+)    │    │ Retida em filtro comum│
  │ Ex: NaCl em água      │  │ Ex: Leite, gelatina   │    │ Ex: Água barrenta     │
  └───────────────────────┘  └───────────────────────┘    └───────────────────────┘
```

---

### 6.1. Coeficiente de Solubilidade ($C_s$) e Classificação de Soluções

O **Coeficiente de Solubilidade ($C_s$)** é a quantidade máxima de soluto que se consegue dissolver em uma quantidade padronizada de solvente (convencionalmente $100\text{ g de } H_2O$) sob determinada temperatura e pressão:

- **Solução Insaturada:** Contém uma quantidade de soluto inferior ao limite de solubilidade ($m_1 < C_s$). Se adicionarmos mais soluto, ele dissolve-se completamente.
- **Solução Saturada (sem corpo de fundo):** Contém exatamente a quantidade máxima de soluto tolerada pelo solvente naquela temperatura ($m_1 = C_s$).
- **Solução Saturada com Corpo de Fundo (ou com precipitado):** A quantidade adicionada excede o $C_s$. O excesso não se dissolve e deposita-se no fundo. Trata-se de um sistema heterogêneo bifásico, mas a fase líquida em equilíbrio com o sólido é rigorosamente uma solução saturada.
- **Solução Supersaturada:** Sistema termodinamicamente instável que contém, transitoriamente e em repouso estrito, mais soluto dissolvido do que o permitido pelo coeficiente de solubilidade naquela temperatura. É obtida por resfriamento lento e cuidadoso de uma solução saturada a quente. Qualquer perturbação mecânica ou a adição de um microcristal de soluto (germe de cristalização) faz com que todo o excesso precipite instantaneamente.

---

### 6.2. Curvas de Solubilidade

Gráficos que representam a variação do coeficiente de solubilidade ($g\text{ de soluto}/100\text{ g de } H_2O$) em função da temperatura ($^\circ C$).

```
                 PERFIS DE CURVAS DE SOLUBILIDADE
   Solubilidade
  (g / 100 g H₂O)
        ▲
        │          Dissolução Endotérmica (Ex: KNO₃)
        │                 ╭─────────────────────────
        │               ╭╯    ΔH_dissolucao > 0
        │             ╭╯   (Aquecer favorece solubilidade)
        │           ╭╯
        │         ╭╯       Dissolução Exotérmica (Ex: Ce₂(SO₄)₃)
        │       ╭╯         ────────────────────────╮
        │     ╭╯                  ΔH_dissolucao < 0 ╰╮
        │   ╭╯            (Aquecer reduz solubilidade)╰╮
        └───┴──────────────────────────────────────────┴──► Temperatura (°C)
```

1. **Dissolução Endotérmica ($\Delta H_{\text{diss}} > 0$):** O processo de dissolução absorve calor. Pelo Princípio de Le Chatelier, o aumento da temperatura aumenta a solubilidade (curva ascendente, ex.: $KNO_3, NaCl$).
2. **Dissolução Exotérmica ($\Delta H_{\text{diss}} < 0$):** A dissolução libera calor. O aquecimento prejudica a solubilidade (curva descendente, ex.: sulfato de cério $Ce_2(SO_4)_3$ e hidróxido de cálcio $Ca(OH)_2$).
3. **Solubilidade de Gases em Líquidos:** A dissolução de qualquer gás em um solvente líquido é **sempre um processo exotérmico**:
   $$Gás_{(g)} + Solvente_{(l)} \rightleftharpoons Solução_{(aq)} + Calor$$
   - **Efeito da Temperatura:** O aquecimento expulsa o gás dissolvido (menor solubilidade com maior $T$).
   - **Efeito da Pressão (Lei de Henry):** A solubilidade de um gás em um líquido é diretamente proporcional à pressão parcial do gás sobre o líquido ($C = k_H \cdot P_{\text{gás}}$). É por isso que refrigerantes mantidos fechados sob alta pressão contêm gás dissolvido; ao abrir a garrafa, a pressão cai bruscamente e o gás descarboxila formando bolhas.

---

## 7. Unidades de Concentração

A concentração expressa a proporção quantitativa entre o soluto e a solução (ou solvente). 
*Convenção de índices canônica:*
- Índice **1**: referente ao **soluto**.
- Índice **2**: referente ao **solvente**.
- **Sem índice**: referente à **solução total** ($m = m_1 + m_2$; $V = V_{\text{solução}}$).

---

### 7.1. Concentração Comum ($C$)
É a razão entre a massa do soluto (em gramas) e o volume total da solução (em litros):

$$C = \frac{m_1}{V} \quad [\text{unidade usual: g/L}]$$

> ⚠️ **NÃO CONFUNDIR CONCENTRAÇÃO COMUM COM DENSIDADE:**  
> A densidade da solução envolve a **massa total da solução** ($m = m_1 + m_2$):
>
> $$d_{\text{solução}} = \frac{m_{\text{solução}}}{V} = \frac{m_1 + m_2}{V} \quad [\text{unidade usual: g/mL ou g/cm}^3]$$

---

### 7.2. Concentração em Quantidade de Matéria / Molaridade ($M$)
É a razão entre a quantidade de matéria do soluto ($n_1$, em mols) e o volume da solução ($V$, em litros):

$$M = \frac{n_1}{V} = \frac{m_1}{M_1 \cdot V} \quad [\text{unidade: mol/L ou molar (M)}]$$

---

### 7.3. Título em Massa ($\tau$) e Porcentagem em Massa ($\% m/m$)
É a fração da massa total da solução representada pela massa do soluto (adimensional, entre 0 e 1):

$$\tau = \frac{m_1}{m_{\text{solução}}} = \frac{m_1}{m_1 + m_2} \implies \% m/m = \tau \times 100\%$$

*Exemplo:* Soro fisiológico comercial a $0,9\% (m/m)$ de $NaCl$ contém $0,9\text{ g de } NaCl$ em cada $100\text{ g de soro}$.

---

### 7.4. Partes por Milhão (ppm) e Partes por Bilhão (ppb)
Empregadas na toxicologia, controle ambiental e análise de contaminantes ultradiluídos (poluição hídrica por mercúrio, chumbo, pesticidas; gases tóxicos no ar):

- **Partes por Milhão ($1\text{ ppm} = 10^{-6}$):** $1$ parte de soluto em $1.000.000$ de partes de solução.
  - Para soluções aquosas diluídas ($d \approx 1,0\text{ g/mL} = 1000\text{ g/L}$):
    $$1\text{ ppm} \equiv 1\text{ mg de soluto} / 1\text{ kg de solução} \equiv \mathbf{1\text{ mg/L}} \equiv 1\ \mu\text{g/g}$$
- **Partes por Bilhão ($1\text{ ppb} = 10^{-9}$):** $1$ parte de soluto em $10^9$ partes de solução.
  - Em água diluída:
    $$1\text{ ppb} \equiv 1\ \mu\text{g de soluto} / 1\text{ kg de solução} \equiv \mathbf{1\ \mu\text{g/L}}$$

---

### 7.5. Fórmula de Interconversão Universal
Quando se conhecem a concentração comum ($C$), a molaridade ($M$), a densidade da solução ($d$, em $\text{g/mL}$), o título em massa ($\tau$) e a massa molar do soluto ($M_1$, em $\text{g/mol}$):

$$C = M \cdot M_1 = 1000 \cdot d \cdot \tau$$

*(Nota: o fator 1000 surge da conversão da densidade de $\text{g/mL}$ para $\text{g/L}$)*.

---

## 8. Operações com Soluções

### 8.1. Diluição de Soluções
Diluir uma solução consiste em **adicionar solvente puro** a ela. A massa e a quantidade de mols do soluto permanecem rigorosamente constantes; apenas o volume total aumenta e a concentração diminui proporcionalmente.

$$n_{\text{inicial}} = n_{\text{final}} \implies M_i \cdot V_i = M_f \cdot V_f$$
$$m_{1,\text{inicial}} = m_{1,\text{final}} \implies C_i \cdot V_i = C_f \cdot V_f$$

Onde o volume final é a soma do volume inicial com o volume de solvente adicionado: $V_f = V_i + V_{\text{solvente adicionado}}$ (admitindo aditividade de volumes).

---

### 8.2. Mistura de Soluções de Mesmo Soluto
Ao misturar duas soluções ($A$ e $B$) do mesmo soluto e solvente:
- O volume final é a soma dos volumes: $V_f = V_A + V_B$.
- A quantidade final de soluto é a soma dos solutos: $n_f = n_A + n_B$.

$$M_A \cdot V_A + M_B \cdot V_B = M_f \cdot V_f \iff M_f = \frac{M_A V_A + M_B V_B}{V_A + V_B}$$

A concentração molar final resultante ($M_f$) será sempre um valor intermediário entre $M_A$ e $M_B$.

---

### 8.3. Mistura de Soluções com Reação Química (Titulometria Ácido-Base)

Quando soluções de solutos com afinidade química são misturadas (ex.: um ácido forte reagindo com uma base forte), ocorre uma reação química estequiométrica de neutralização:

$$a\ \text{Ácido} + b\ \text{Base} \longrightarrow \text{Sal} + \text{Água}$$

Na **Titulação Ácido-Base**, utiliza-se uma solução de concentração exatamente conhecida (solução padrão / titulante) para determinar com precisão a concentração desconhecida de uma alíquota de outra solução (titulado).

No **Ponto de Equivalência (Ponto Estequiométrico)**:
A quantidade de matéria de íons $H^+$ liberada pelo ácido iguala-se estequiometricamente à quantidade de íons $OH^-$ liberada pela base:

$$n_{H^+} = n_{OH^-}$$

Para um ácido com $x$ hidrogênios ionizáveis e uma base com $y$ hidroxilas dissociáveis:

$$x \cdot M_{\text{ácido}} \cdot V_{\text{ácido}} = y \cdot M_{\text{base}} \cdot V_{\text{base}}$$

- Se for monoácido e monobase ($HCl$ e $NaOH$): $x = 1, y = 1 \implies M_A V_A = M_B V_B$.
- Se for diácido e monobase ($H_2SO_4$ e $NaOH$): $x = 2, y = 1 \implies 2 \cdot M_A V_A = M_B V_B$.

Se um dos reagentes estiver em excesso estequiométrico, calcula-se a sobra de $H^+$ ou $OH^-$ no volume total final para determinar o pH da solução resultante (estudado detalhadamente no Módulo 03).
