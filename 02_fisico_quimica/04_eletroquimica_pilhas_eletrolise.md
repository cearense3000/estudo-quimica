# Módulo 04: Eletroquímica — Oxirredução, Pilhas Galvânicas e Eletrólise

---

## 1. Introdução à Eletroquímica e Fenômenos de Oxirredução

A **Eletroquímica** é o ramo da físico-química que investiga a interconversão entre a **energia química** armazenada nas ligações moleculares e a **energia elétrica** gerada pelo fluxo ordenado de elétrons.

As transformações eletroquímicas dividem-se em dois grandes domínios complementares:
1. **Células Galvânicas (Pilhas e Baterias):** Reações químicas redox **espontâneas** ($\Delta G < 0$) geram corrente elétrica contínua aproveitável.
2. **Células Eletrolíticas (Eletrólise):** Uma corrente elétrica externa fornecida por um gerador força a ocorrência de reações químicas **não-espontâneas** ($\Delta G > 0$).

```
                      O MAPA DA ELETROQUÍMICA
       Célula Galvânica (Pilha)             Célula Eletrolítica (Eletrólise)
  ┌───────────────────────────────────┐   ┌───────────────────────────────────┐
  │ Energia Química ──► Energia Elétr.│   │ Energia Elétr. ──► Energia Química│
  │ Processo ESPONTÂNEO (ΔG < 0)      │   │ Processo NÃO-ESPONTÂNEO (ΔG > 0)  │
  │ ΔE° > 0                           │   │ Forçado por gerador externo       │
  │ Ânodo (-) │ Cátodo (+)            │   │ Ânodo (+) │ Cátodo (-)            │
  └───────────────────────────────────┘   └───────────────────────────────────┘
```

---

### 1.1. Oxidação, Redução e o Número de Oxidação (Nox)

Toda reação eletroquímica fundamenta-se na **transferência de elétrons** entre espécies químicas:

> **CONCEITOS FUNDAMENTAIS:**  
> - **Oxidação:** É a **perda de elétrons**. O átomo que oxida tem seu Número de Oxidação (Nox) **aumentado**. A espécie química que sofre oxidação atua como **AGENTE REDUTOR** (porque fornece elétrons para reduzir outra espécie).  
> - **Redução:** É o **ganho de elétrons**. O átomo que reduz tem seu Número de Oxidação (Nox) **diminuído**. A espécie química que sofre redução atua como **AGENTE OXIDANTE** (porque captura elétrons, oxidando a outra espécie).

```
                      MNEMÔNICO INFALÍVEL
               OXIDAÇÃO                        REDUÇÃO
       ┌────────────────────────┐      ┌────────────────────────┐
       │ PERDA de elétrons      │      │ GANHO de elétrons      │
       │ AUMENTA o Nox          │      │ DIMINUI o Nox          │
       │ É o AGENTE REDUTOR     │      │ É o AGENTE OXIDANTE    │
       └────────────────────────┘      └────────────────────────┘
```

---

### 1.2. Regras Formais para Determinação do Número de Oxidação (Nox)

O Nox expressa a carga elétrica real (em compostos iônicos) ou a carga aparente/formal (em compostos moleculares polares, caso a ligação fosse rompida heteroliticamente atribuindo os elétrons ao átomo mais eletronegativo):

1. **Substância Simples no Estado Fundamental:** O Nox de qualquer átomo em substância simples é rigorosamente **ZERO** ($Fe^0, O_2^0, H_2^0, P_4^0, S_8^0$).
2. **Íons Monoatômicos:** O Nox é igual à própria carga do íon ($Na^+ \to +1$; $Ca^{2+} \to +2$; $Al^{3+} \to +3$; $Cl^- \to -1$; $S^{2-} \to -2$).
3. **Metais com Nox Fixo em Compostos:**
   - Metais Alcalinos (Grupo 1) e Prata ($Ag$): **$+1$**
   - Metais Alcalinoterrosos (Grupo 2) e Zinco ($Zn$): **$+2$**
   - Alumínio ($Al$): **$+3$**
4. **Hidrogênio ($H$):**
   - Na maioria esmagadora dos compostos: **$+1$** ($HCl, H_2O, NH_3$).
   - Exceção canônica: em hidretos metálicos (ligado a metais menos eletronegativos que ele, como $NaH, CaH_2$): **$-1$**.
5. **Oxigênio ($O$):**
   - Na imensa maioria dos óxidos, ácidos e sais: **$-2$** ($H_2O, CO_2, H_2SO_4$).
   - Exceção 1 (Peróxidos, contendo a ligação $-O-O-$, como $H_2O_2, Na_2O_2$): **$-1$**.
   - Exceção 2 (Superóxidos, como $KO_2$): **$-1/2$**.
   - Exceção 3 (Fluoretos de oxigênio, como $OF_2$, onde o flúor é mais eletronegativo): **$+2$**.
6. **Halogênios (Grupo 17 - $F, Cl, Br, I$):**
   - Quando localizados na extremidade mais à direita da fórmula (sem oxigênio): **$-1$** ($NaCl, CCl_4$).
   - Quando combinados com oxigênio, podem assumir nox positivo $+1, +3, +5, +7$ (ex.: no $HClO_4$, o $Cl$ tem nox $+7$).
7. **Soma Algébrica das Cargas:**
   - Em qualquer molécula ou composto eletricamente neutro: $\mathbf{\sum Nox = 0}$.
   - Em qualquer íon poliatômico: $\mathbf{\sum Nox = \text{carga do íon}}$.

#### Exemplo Prático de Determinação: Permanganato de Potássio ($KMnO_4$)
$$Nox(K) + Nox(Mn) + 4 \times Nox(O) = 0 \implies (+1) + x + 4(-2) = 0 \implies 1 + x - 8 = 0 \implies x = \mathbf{+7}$$
O manganês possui Nox $+7$, seu estado de oxidação máximo.

---

### 1.3. Balanceamento de Reações de Oxirredução

#### A. Método das Variações de Nox ($\Delta$)
1. Identifique os elementos que sofrem oxidação e redução calculando o Nox de cada átomo.
2. Calcule a variação total do Nox ($\Delta$) para cada espécie:
   $$\Delta = |\text{Nox final} - \text{Nox inicial}| \times \text{maior atomicidade do elemento}$$
3. Iguale a quantidade de elétrons trocados: inverta os valores de $\Delta$, atribuindo o $\Delta$ da oxidação como coeficiente do agente redutor e o $\Delta$ da redução como coeficiente do agente oxidante.
4. Ajuste os demais átomos pelo método das tentativas (ordem clássica MACHO: Metais, Ametais, Carbono, Hidrogênio, Oxigênio).

#### B. Método das Semirreações (Íon-Elétron) em Meio Ácido e Básico
Essencial para reações iônicas complexas em solução:

1. **Separação:** Desdobre a reação em duas semirreações (uma de oxidação e uma de redução).
2. **Balanceamento Material:**
   - Balanceie todos os átomos diferentes de $H$ e $O$.
   - Balanceie os átomos de **Oxigênio** adicionando moléculas de **$H_2O$** no lado deficitário.
   - Balanceie os átomos de **Hidrogênio** adicionando íons **$H^+$** no lado deficitário.
3. **Balanceamento Elétrico:** Adicione elétrons ($e^-$) no lado de maior carga positiva para equalizar a carga elétrica total dos dois lados da semirreação.
4. **Equalização de Elétrons e Soma:** Multiplique as semirreações por fatores inteiros para cancelar os elétrons e some-as.
5. *(Para Meio Básico):* Após obter a equação final, adicione íons $OH^-$ a ambos os lados em quantidade suficiente para neutralizar os íons $H^+$ formando $H_2O$, simplificando as moléculas de água repetidas.

---

## 2. Células Galvânicas (Pilhas)

Uma pilha é um dispositivo no qual uma reação de oxirredução espontânea é separada fisicamente em duas semicélulas, forçando os elétrons a trafegar por um fio condutor externo.

```
                         A PILHA DE DANIELL
                Voltímetro (V = 1,10 V)
             [e⁻] ──────────────────────► [e⁻]
              │                              │
         ┌────┴────┐                    ┌────┴────┐
         │ ÂNODO   │   Ponte Salina     │ CÁTODO  │
         │ Placa Zn│   ┌────────────┐   │ Placa Cu│
         │ (-)     │   │ Na⁺ ──► Cl⁻│   │ (+)     │
         │         │   └────┬───┬───┘   │         │
         │         │        │   │       │         │
         │ ┌─────┐ │        │   │       │ ┌─────┐ │
         │ │Zn²⁺ │ │        │   │       │ │Cu²⁺ │ │
         └─┴─────┴─┘        └───┘       └─┴─────┴─┘
         Solução ZnSO₄ (1 M)            Solução CuSO₄ (1 M)
         (Oxidação: Zn perde e⁻)        (Redução: Cu²⁺ ganha e⁻)
         (Corrosão da placa)            (Deposição sobre a placa)
```

---

### 2.1. Anatomia e Funcionamento da Pilha de Daniell ($Zn / Cu$)

Montada historicamente por John Frederic Daniell (1836):

1. **Semicélula Anódica (Polo Negativo):**
   - Eletrodo de Zinco imerso em solução de $ZnSO_{4(aq)}$ ($1\text{ mol/L}$).
   - O zinco metálico tem maior tendência de oxidar que o cobre:
     $$\mathbf{Zn_{(s)} \longrightarrow Zn^{2+}_{(aq)} + 2\ e^-} \quad (\text{Semirreação de Oxidação})$$
   - **Consequências observáveis:** A placa de zinco sofre **corrosão** (diminui sua massa) e a concentração de cátions $Zn^{2+}$ na solução aquosa aumenta.
   - Como os elétrons partem desse eletrodo, o ânodo é o **Polo Negativo ($-$)**.

2. **Semicélula Catódica (Polo Positivo):**
   - Eletrodo de Cobre imerso em solução de $CuSO_{4(aq)}$ ($1\text{ mol/L}$).
   - Os cátions $Cu^{2+}$ da solução capturam os elétrons que chegam pelo circuito:
     $$\mathbf{Cu^{2+}_{(aq)} + 2\ e^- \longrightarrow Cu_{(s)}} \quad (\text{Semirreação de Redução})$$
   - **Consequências observáveis:** Ocorre **deposição** de cobre metálico sobre a placa (aumenta sua massa) e a solução azulada de $Cu^{2+}$ vai clareando gradativamente.
   - Como atrai os elétrons, o cátodo é o **Polo Positivo ($+$)**.

3. **Reação Global da Pilha de Daniell:**
   $$\mathbf{Zn_{(s)} + Cu^{2+}_{(aq)} \longrightarrow Zn^{2+}_{(aq)} + Cu_{(s)}}$$

4. **A Função Indispensável da Ponte Salina:**
   - Tubo de vidro contendo um gel (ágar-ágar) saturado com um eletrólito inerte (como $KCl$ ou $KNO_3$).
   - Conforme a pilha funciona, o ânodo acumula excesso de cargas positivas ($Zn^{2+}$) e o cátodo acumula excesso de cargas negativas ($SO_4^{2-}$ não compensados). Esse desequilíbrio interromperia o fluxo de elétrons em milissegundos.
   - A ponte salina **fecha o circuito elétrico e mantém a neutralidade eletrostática das duas meias-células**:
     - Os ânions ($Cl^-$ ou $NO_3^-$) migram em direção ao compartimento anódico ($-$).
     - Os cátions ($K^+$ ou $Na^+$) migram em direção ao compartimento catódico ($+$).

5. **Notação Padrão IUPAC para Células Galvânicas:**
   $$\mathbf{Ânodo_{(s)} \mid Solução\ Anódica\ (M_1) \parallel Solução\ Catódica\ (M_2) \mid Cátodo_{(s)}}$$
   $$\text{Para Daniell: } \mathbf{Zn_{(s)} \mid Zn^{2+}_{(aq)} (1\ M) \parallel Cu^{2+}_{(aq)} (1\ M) \mid Cu_{(s)}}$$

---

### 2.2. Potencial Padrão de Redução ($E^\circ$) e Força Eletromotriz ($\Delta E^\circ$)

O potencial de um eletrodo isolado não pode ser medido isoladamente. Por convenção internacional, definiu-se como padrão de referência o **Eletrodo Padrão de Hidrogênio (EPH)**:

$$2\ H^+_{(aq)} (1\text{ mol/L}) + 2\ e^- \rightleftharpoons H_{2(g)} (1\text{ atm}) \quad \mathbf{E^\circ = 0,00\ V\text{ (a } 25^\circ C)}$$

- **Potencial Padrão de Redução ($E^\circ_{\text{red}}$):** Mede a tendência termodinâmica de uma espécie química em sofrer redução (ganhar elétrons) frente ao hidrogênio nas condições padrão ($25^\circ C$, $1\text{ atm}$, $1\text{ mol/L}$):
  - Quanto **maior** o $E^\circ_{\text{red}}$, **maior a facilidade de reduzir** e mais forte é o agente oxidante (ex.: $F_{2(g)} + 2e^- \to 2F^-$, $E^\circ = +2,87\ V$).
  - Quanto **menor** (mais negativo) o $E^\circ_{\text{red}}$, **maior a facilidade de oxidar** e mais forte é o agente redutor (ex.: $Li^+ + e^- \to Li^0$, $E^\circ = -3,04\ V$).

#### Cálculo da Força Eletromotriz / Diferença de Potencial ($\Delta E^\circ$ ou ddp):
A ddp padrão de uma pilha é calculada diretamente pela diferença entre os potenciais padrão de redução:

$$\mathbf{\Delta E^\circ = E^\circ_{\text{red(cátodo)}} - E^\circ_{\text{red(ânodo)}} = E^\circ_{\text{maior}} - E^\circ_{\text{menor}}}$$

- **Critério de Espontaneidade Termodinâmica:**
  $$\Delta G^\circ = -n \cdot F \cdot \Delta E^\circ$$
  - Uma reação química redox é **ESPONTÂNEA** se, e somente se, **$\mathbf{\Delta E^\circ > 0}$** ($\Delta G^\circ < 0$).
  - Se $\Delta E^\circ < 0$, o processo é não-espontâneo no sentido direto (rege a eletrólise).

*Cálculo para a Pilha de Daniell:*
- $Cu^{2+} + 2e^- \to Cu^0 \quad E^\circ_{\text{red}} = +0,34\ V$ (Maior potencial $\to$ Reduz $\to$ Cátodo)
- $Zn^{2+} + 2e^- \to Zn^0 \quad E^\circ_{\text{red}} = -0,76\ V$ (Menor potencial $\to$ Oxida $\to$ Ânodo)
$$\mathbf{\Delta E^\circ = (+0,34\ V) - (-0,76\ V) = +0,34 + 0,76 = \mathbf{+1,10\ V}}$$

> ⚠️ **PROPRIEDADE INTENSIVA DO POTENCIAL:**  
> O potencial $E^\circ$ é uma propriedade intensiva (voltagem) e **NUNCA é multiplicado pelos coeficientes estequiométricos da reação química**! Se multiplicarmos uma semirreação por 2 ou 3, o seu $E^\circ$ permanece estritamente o mesmo.

---

### 2.3. Baterias Comerciais e Tecnologia de Armazenamento

1. **Bateria de Chumbo-Ácido Automotiva (Gaston Planté, 1859):**
   - Utilizada na partida de veículos a combustão (recarregável, composta por 6 células de $2\ V$ ligadas em série $\to 12\ V$).
   - Ânodo: Chumbo metálico esponjoso ($Pb_{(s)}$).
   - Cátodo: Dióxido de chumbo ($PbO_{2(s)}$).
   - Eletrólito: Solução aquosa concentrada de ácido sulfúrico ($H_2SO_4 \approx 30\%$).
   - *Reação Global de Descarga:*
     $$Pb_{(s)} + PbO_{2(s)} + 2\ H_2SO_{4(aq)} \rightleftharpoons 2\ PbSO_{4(s)} + 2\ H_2O_{(l)} \quad \Delta E^\circ \approx 2,05\ V$$
   - Durante a descarga, consome-se $H_2SO_4$ e forma-se água, reduzindo a densidade do eletrólito (um densímetro afere o estado de carga da bateria).

2. **Baterias de Íon-Lítio (Prêmio Nobel de Química 2019):**
   - Presentes em smartphones, notebooks e veículos elétricos modernos.
   - Não possuem lítio metálico livre (que é pirofórico e perigoso); operam pelo vaivém de cátions $Li^+$ entre as camadas hexagonais de grafite (ânodo $Li_x C_6$) e um óxido lamelar de metal de transição (cátodo $Li_{1-x} CoO_2$).
   - Vantagens revolucionárias: altíssima densidade energética por peso (o lítio é o metal mais leve e com o menor potencial de redução da tabela, gerando tensões de até $3,7\text{ a }4,2\ V$ por célula) e ausência de efeito memória.

---

### 2.4. Corrosão Metálica e Métodos de Proteção

A corrosão do ferro (ferrugem) é um processo eletroquímico espontâneo provocado pelo contato conjunto do metal com o **oxigênio atmosférico ($O_2$)** e a **umidade ($H_2O$)**:

1. **Mecanismo da Ferrugem:**
   - Ânodo (região da peça de ferro): $2\ Fe_{(s)} \longrightarrow 2\ Fe^{2+}_{(aq)} + 4\ e^-$
   - Cátodo (gotícula de água com oxigênio dissolvido): $O_{2(g)} + 2\ H_2O_{(l)} + 4\ e^- \longrightarrow 4\ OH^-_{(aq)}$
   - Precipitação de hidróxido: $Fe^{2+} + 2\ OH^- \longrightarrow Fe(OH)_{2(s)}$
   - Oxidação subsequente pelo oxigênio do ar:
     $$4\ Fe(OH)_{2(s)} + O_{2(g)} + 2\ H_2O_{(l)} \longrightarrow 2\ Fe_2O_3 \cdot nH_2O_{(s)} \quad (\text{Ferrugem hidratada})$$

2. **Métodos de Proteção Anticorrosiva:**
   - **Proteção Catódica por Metal de Sacrifício (Ânodo de Sacrifício):** Soldam-se blocos de um metal que possua **potencial de redução menor (maior facilidade de oxidar)** que o ferro — tipicamente **Zinco ($Zn$)** ou **Magnésio ($Mg$)** — ao casco de navios, tanques subterrâneos e oleodutos. O metal de sacrifício corrói-se preferencialmente, doando elétrons para a estrutura de ferro e mantendo-a intacta na condição de cátodo.
   - **Galvanização:** Revestimento da superfície do ferro por uma camada de zinco metálico através de imersão a quente ou eletrodeposição. O zinco cria uma barreira física e, mesmo que sofra riscos ou fendas, atua como metal de sacrifício galvânico.

---

## 3. Células Eletrolíticas (Eletrólise)

A **Eletrólise** é o processo forçado e não espontâneo no qual a energia elétrica fornecida por um gerador de corrente contínua provoca uma transformação química redox ($\Delta G > 0$).

```
                      POLARIDADES COMPARATIVAS
       Célula Galvânica (Pilha)             Célula Eletrolítica (Eletrólise)
  ┌───────────────────────────────────┐   ┌───────────────────────────────────┐
  │ ÂNODO: Oxidação  │ Polo NEGATIVO  │   │ ÂNODO: Oxidação  │ Polo POSITIVO  │
  │ CÁTODO: Redução  │ Polo POSITIVO  │   │ CÁTODO: Redução  │ Polo NEGATIVO  │
  └───────────────────────────────────┘   └───────────────────────────────────┘
               ▲                                       ▲
               └──────── REGRA MNEMÔNICA DE OURO ──────┘
                     Vogal com Vogal: ÂNODO = OXIDAÇÃO
                     Consoante com Consoante: CÁTODO = REDUÇÃO
```

---

### 3.1. Eletrólise Ígnea

Ocorre a seco, com o composto iônico no estado líquido **fundido** (liquefeito por aquecimento a altas temperaturas, sem água). Como não há água presente, não existe competição de descarga: os únicos íons disponíveis são os originados do próprio sal fundido.

#### Exemplo Canônico: Eletrólise Ígnea do Cloreto de Sódio ($NaCl$ puro a ~800 °C):
- Fusão iônica: $2\ NaCl_{(s)} \overset{\Delta}{\longrightarrow} 2\ Na^+_{(l)} + 2\ Cl^-_{(l)}$
- **No Cátodo (Polo Negativo - Redução):** Os cátions $Na^+$ migram para o cátodo e recebem elétrons:
  $$2\ Na^+_{(l)} + 2\ e^- \longrightarrow 2\ Na_{(l)}^0 \quad (\text{Obtenção de Sódio Metálico})$$
- **No Ânodo (Polo Positivo - Oxidação):** Os ânions $Cl^-$ migram para o ânodo e perdem elétrons:
  $$2\ Cl^-_{(l)} \longrightarrow Cl_{2(g)} + 2\ e^- \quad (\text{Obtenção de Gás Cloro})$$
- **Reação Global:**
  $$\mathbf{2\ NaCl_{(l)} \overset{\text{eletrólise}}{\longrightarrow} 2\ Na_{(l)} + Cl_{2(g)}}$$

#### Produção Industrial de Alumínio (Processo Hall-Héroult):
O alumínio não pode ser obtido por redução clássica com carvão devido à sua extraordinária reatividade. A bauxita purificada ($\text{alumina, } Al_2O_3$) é dissolvida em criolita fundida ($Na_3AlF_6$) a cerca de $950^\circ C$ para reduzir o ponto de fusão (a alumina pura funde a $2050^\circ C$). Sob passagem de altíssima corrente elétrica, o cátion $Al^{3+}$ descarrega no cátodo de fundo formando alumínio líquido puro ($Al^{3+} + 3e^- \to Al_{(l)}$), enquanto os ânodos de grafite oxidam os ânions $O^{2-}$ e são lentamente consumidos gerando gás carbônico ($C + 2O^{2-} \to CO_2 + 4e^-$).

---

### 3.2. Eletrólise Aquosa e a Competição de Descarga

Quando um eletrólito está dissolvido em água, além dos íons do soluto, estão presentes em solução os íons provenientes da autoionização da água: os prótons **$H^+$** e as hidroxilas **$OH^-$**.

Estabelece-se uma **competição iônica**: apenas um cátion descarregará no cátodo e apenas um ânion descarregará no ânodo, governados pela **Fila de Prioridade de Descarga**:

```
                   FILA DE PRIORIDADE DE DESCARGA
    NO CÁTODO (Redução de Cátions):
    Metais Alcalinos, Alcalinoterrosos e Al³⁺  <  H⁺ da Água  <  Demais Cátions Metálicos
    (Li⁺, Na⁺, K⁺, Ca²⁺, Mg²⁺, Ba²⁺, Al³⁺)      (2H⁺ + 2e⁻ ──► H₂) (Cu²⁺, Ag⁺, Ni²⁺, Fe²⁺, etc.)
    ──────────────────────────────────────────► FACILIDADE CRESCENTE DE DESCARGA

    NO ÂNODO (Oxidação de Ânions):
    Fluoreto (F⁻) e Ânions Oxigenados  <  OH⁻ da Água  <  Ânions Não-Oxigenados e HSO₄⁻
    (SO₄²⁻, NO₃⁻, CO₃²⁻, PO₄³⁻, F⁻)     (2OH⁻ ──► H₂O + ½O₂ + 2e⁻) (Cl⁻, Br⁻, I⁻, S²⁻)
    ──────────────────────────────────────────► FACILIDADE CRESCENTE DE DESCARGA
```

#### Estudo de Caso Resolvido: Eletrólise Aquosa do $NaCl$ (Salmoura)
Íons presentes em solução aquosa:
- Da dissociação do sal: $2\ NaCl_{(s)} \overset{H_2O}{\longrightarrow} 2\ Na^+_{(aq)} + 2\ Cl^-_{(aq)}$
- Da autoionização da água: $2\ H_2O_{(l)} \rightleftharpoons 2\ H^+_{(aq)} + 2\ OH^-_{(aq)}$

1. **No Cátodo (Polo Negativo):** Disputa entre $Na^+$ e $H^+$.
   - Conforme a fila, o **$H^+$ tem prioridade sobre os metais alcalinos**:
     $$\mathbf{2\ H^+_{(aq)} + 2\ e^- \longrightarrow H_{2(g)}} \quad (\text{Desprende Gás Hidrogênio})$$
2. **No Ânodo (Polo Positivo):** Disputa entre $Cl^-$ e $OH^-$.
   - O **$Cl^-$ (não oxigenado) tem prioridade sobre o $OH^-$**:
     $$\mathbf{2\ Cl^-_{(aq)} \longrightarrow Cl_{2(g)} + 2\ e^-} \quad (\text{Desprende Gás Cloro})$$
3. **Solução Remanescente:**
   - Sobram em solução os íons $Na^+$ e $OH^-$, convertendo o meio em uma solução límpida e concentrada de **Hidróxido de Sódio ($NaOH_{(aq)}$)** de pH altamente alcalino ($pH > 13$).
4. **Equação Global da Eletrólise Aquosa de Salmoura:**
   $$\mathbf{2\ NaCl_{(aq)} + 2\ H_2O_{(l)} \overset{\text{eletrólise}}{\longrightarrow} H_{2(g)} \uparrow + Cl_{2(g)} \uparrow + 2\ NaOH_{(aq)}}$$
   *(Processo cloro-álcali: base da indústria petroquímica e de saneamento básico).*

---

## 4. Aspectos Quantitativos da Eletrólise: As Leis de Faraday

Michael Faraday estabeleceu em 1834 a relação quantitativa entre a carga elétrica que atravessa um circuito e a massa de substância transformada nos eletrodos.

### 4.1. Carga Elétrica e a Constante de Faraday ($F$)
A carga elétrica total ($Q$) conduzida por uma corrente elétrica constante de intensidade $I$ durante um intervalo de tempo $t$ é dada por:

$$Q = I \cdot t$$

Onde:
- $Q$: Carga elétrica expressa em **Coulombs (C)**.
- $I$: Corrente elétrica expressa em **Amperes (A)** ($1\text{ A} = 1\text{ C/s}$).
- $t$: Tempo decorrido expresso **OBRIGATORIAMENTE EM SEGUNDOS (s)**.

A carga elétrica transportada por **$1\text{ mol de elétrons}$** é a **Constante de Faraday ($F$)**:

$$F = N_A \cdot e = (6,022 \times 10^{23}\text{ elétrons}) \times (1,602 \times 10^{-19}\text{ C/elétron}) \approx \mathbf{96.485\text{ C/mol de } e^-}$$
$$(\text{Convenção usual de vestibulares: } \mathbf{1\ F \approx 96.500\text{ C/mol de } e^-})$$

---

### 4.2. Dedução da Equação Fundamental da Eletrólise

Para depositar $1\text{ mol}$ de um metal $M$ cuja valência iônica é $n$ ($M^{n+} + n\ e^- \to M_{(s)}$):
- $n\text{ mols de elétrons}$ correspondem a uma carga de $n \times F\text{ Coulombs}$.
- Essa carga deposita uma massa equivalente à massa molar $M$ do metal.

Estruturando a proporção estequiométrica:

$$\begin{matrix}
M\text{ gramas do metal} & \longleftrightarrow & n \times 96.500\text{ C} \\
m\text{ gramas depositadas} & \longleftrightarrow & Q = (I \cdot t)\text{ C}
\end{matrix}$$

Multiplicando cruzado:

$$\mathbf{m = \frac{M \cdot I \cdot t}{n \cdot F}} = \mathbf{\frac{M \cdot I \cdot t}{n \times 96.500}}$$

Onde:
- $m$: Massa depositada ou liberada no eletrodo (em gramas).
- $M$: Massa molar do elemento (em $\text{g/mol}$).
- $I$: Intensidade da corrente elétrica (em $\text{A}$).
- $t$: Tempo de eletrólise (em $\text{s}$).
- $n$: Número de elétrons trocados na semirreação balanceada (valência do cátion/ânion).
- $F$: Constante de Faraday ($96.500\text{ C/mol de } e^-$).

#### Determinação de Volumes Gasosos nas CNTP:
Se a espécie descarregada for um gás nas CNTP ($22,4\text{ L/mol}$):
- Exemplo: para o gás hidrogênio ($2\ H^+ + 2e^- \to H_{2(g)}$), $2\text{ mols de } e^-$ ($2 \times 96.500\text{ C}$) desprendem $1\text{ mol de } H_2 = 22,4\text{ L}$ nas CNTP.
- Para o gás oxigênio ($4\ OH^- \to 2\ H_2O + O_{2(g)} + 4e^-$), $4\text{ mols de } e^-$ ($4 \times 96.500\text{ C}$) desprendem $1\text{ mol de } O_2 = 22,4\text{ L}$ nas CNTP.
