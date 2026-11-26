# Módulo 02: Tabela Periódica Moderna, Carga Nuclear Efetiva e Propriedades Periódicas

---

## 1. Introdução Histórica e a Lei Periódica

A **Tabela Periódica dos Elementos Químicos** é o mapa fundamental da Química moderna. Ela organiza a totalidade da matéria conhecida no universo observável segundo padrões lógicos, correlacionando a arquitetura eletrônica submicroscópica com as propriedades físicas e químicas macroscópicas.

### 1.1. A Construção Histórica do Sistema Periódico

A busca por uma ordenação dos elementos percorreu marcos pioneiros ao longo do século XIX:
1. **Tríades de Döbereiner (1829):** Johann Döbereiner agrupou elementos com propriedades análogas em trios nos quais a massa atômica do elemento central era aproximadamente a média aritmética dos extremos (ex.: $Li \approx 7$, $Na \approx 23$, $K \approx 39 \implies \frac{7+39}{2} = 23$).
2. **Parafuso Telúrico de Chancourtois (1862):** Alexandre de Chancourtois organizou os elementos em ordem crescente de massa atômica sobre uma hélice cilíndrica traçada a $45^\circ$, observando que elementos situados na mesma geratriz vertical compartilhavam propriedades químicas.
3. **Lei das Oitavas de Newlands (1865):** John Newlands observou que, ordenando os elementos por massa atômica, cada oitavo elemento apresentava propriedades semelhantes ao primeiro, em analogia às oitavas musicais (falhava para elementos além do Cálcio).
4. **A Tabela de Dmitri Mendeleev (1869) e Julius Lothar Meyer:**
   - Mendeleev organizou os $63$ elementos então conhecidos em cartões, dispondo-os em ordem crescente de massas atômicas e agrupando-os por propriedades químicas semelhantes.
   - **O Triunfo Epistemológico de Mendeleev:** Teve a audácia científica de **deixar espaços vazios** em sua tabela para elementos ainda não descobertos pela humanidade, prevendo com exatidão matemática impressionante suas massas atômicas e propriedades físico-químicas. Exemplos históricos: o *Eka-Alumínio* (descoberto em 1875 como Gálio, $Ga$), o *Eka-Boro* (descoberto em 1879 como Escândio, $Sc$) e o *Eka-Silício* (descoberto em 1886 como Germânio, $Ge$).

```
        COMPARAÇÃO HISTÓRICA: A PREVISÃO DO EKA-SILÍCIO POR MENDELEEV
┌─────────────────────────────┬───────────────────────────┬──────────────────────────┐
│ Propriedade                 │ Previsão de Mendeleev     │ Dado Real Experimental   │
│                             │ (Eka-Silício, 1871)       │ (Germânio, 1886)         │
├─────────────────────────────┼───────────────────────────┼──────────────────────────┤
│ Massa Atômica               │ ~ 72 u                    │ 72,6 u                   │
│ Densidade                   │ 5,5 g/cm³                 │ 5,35 g/cm³               │
│ Ponto de Fusão              │ Elevado                   │ 937 °C                   │
│ Fórmula do Óxido            │ EsO₂ (densidade 4,7 g/cm³)│ GeO₂ (densidade 4,2 g/cm³)│
│ Fórmula do Cloreto          │ EsCl₄ (PE ~ 100 °C)       │ GeCl₄ (PE = 84 °C)       │
└─────────────────────────────┴───────────────────────────┴──────────────────────────┘
```

---

### 1.2. A Lei Periódica Moderna de Moseley (1913)

Mendeleev ordenou os elementos por **massa atômica**, o que gerava anomalias incômodas na tabela (ex.: o Telúrio, com massa $127,6$, vinha antes do Iodo, com massa $126,9$, para respeitar o agrupamento químico).

Em 1913, o jovem físico britânico **Henry Moseley**, ao bombardear diversos metais com raios catódicos de alta energia e analisar as frequências dos raios X característicos emitidos, descobriu que a raiz quadrada da frequência ($\sqrt{\nu}$) correlacionava-se linearmente com uma grandeza atômica fundamental: o **número de cargas positivas do núcleo (Número Atômico, $Z$)**:

$$\sqrt{\nu} = a \cdot (Z - b)$$

> **A LEI PERIÓDICA MODERNA:**  
> *"Muitas propriedades físicas e químicas dos elementos químicos são funções periódicas de seus **NÚMEROS ATÔMICOS ($Z$)**."*

Quando os elementos foram reordenados em ordem estrita de $Z$, todas as inversões históricas desapareceram: Telúrio ($Z = 52$) precede naturalmente o Iodo ($Z = 53$).

---

## 2. Arquitetura Sistemática da Tabela Periódica Moderna

A Tabela Periódica moderna é composta por **118 elementos químicos confirmados pela IUPAC** (do Hidrogênio $_{1}H$ ao Oganessônio $_{118}Og$), dispostos em uma grade bidimensional de **7 linhas horizontais (Períodos)** e **18 colunas verticais (Grupos ou Famílias)**:

```
                            A MATRIZ DA TABELA PERIÓDICA MODERNA
      1                                                                    18
   ┌────┐                                                                ┌────┐
 1 │ 1s │ 2                                           13  14  15  16  17 │ 1s │
   ├────┼────┐                                       ┌───┬───┬───┬───┬───┼────┤
 2 │ 2s │ 2s │                                       │2p │2p │2p │2p │2p │ 2p │
   ├────┼────┤                                       ├───┼───┼───┼───┼───┼────┤
 3 │ 3s │ 3s │  3   4   5   6   7   8   9  10  11  12│3p │3p │3p │3p │3p │ 3p │
   ├────┼────┼───┬───┬───┬───┬───┬───┬───┬───┬───┬───┼───┼───┼───┼───┼───┼────┤
 4 │ 4s │ 4s │3d │3d │3d │3d │3d │3d │3d │3d │3d │3d │4p │4p │4p │4p │4p │ 4p │
   ├────┼────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼────┤
 5 │ 5s │ 5s │4d │4d │4d │4d │4d │4d │4d │4d │4d │4d │5p │5p │5p │5p │5p │ 5p │
   ├────┼────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼────┤
 6 │ 6s │ 6s │*5d│5d │5d │5d │5d │5d │5d │5d │5d │5d │6p │6p │6p │6p │6p │ 6p │
   ├────┼────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼────┤
 7 │ 7s │ 7s │#6d│6d │6d │6d │6d │6d │6d │6d │6d │6d │7p │7p │7p │7p │7p │ 7p │
   └────┴────┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴────┘
             *Lantanídeos: │4f │4f │4f │4f │4f │4f │4f │4f │4f │4f │4f │4f │4f │4f │
             #Actinídeos:  │5f │5f │5f │5f │5f │5f │5f │5f │5f │5f │5f │5f │5f │5f │
```

### 2.1. Os 7 Períodos (Linhas Horizontais)
- O número do período indica o **número total de camadas/níveis eletrônicos ($n$)** preenchidos ou parcialmente ocupados por elétrons no átomo no estado fundamental:
  * 1º Período: $n = 1$ (2 elementos: $H, He$).
  * 2º Período: $n = 2$ (8 elementos: do $Li$ ao $Ne$).
  * 3º Período: $n = 3$ (8 elementos: do $Na$ ao $Ar$).
  * 4º Período: $n = 4$ (18 elementos: do $K$ ao $Kr$).
  * 5º Período: $n = 5$ (18 elementos: do $Rb$ ao $Xe$).
  * 6º Período: $n = 6$ (32 elementos: do $Cs$ ao $Rn$, incluindo os Lantanídeos).
  * 7º Período: $n = 7$ (32 elementos: do $Fr$ ao $Og$, incluindo os Actinídeos).

---

### 2.2. Os 18 Grupos / Famílias (Colunas Verticais)
Os elementos situados em uma mesma coluna vertical possuem **a mesma configuração eletrônica na camada de valência**, o que lhes confere **propriedades químicas semelhantes e reatividades análogas**.

A IUPAC recomenda a numeração arábica contínua de **1 a 18** (substituindo a antiga notação americana e europeia $A/B$):

| Grupo Atual (IUPAC) | Notação Clássica | Denominação Canônica | Configuração de Valência | Elementos Notáveis |
|---|---|---|---|---|
| **Grupo 1** | Família IA | **Metais Alcalinos** | $n s^1$ | $Li, Na, K, Rb, Cs, Fr$ |
| **Grupo 2** | Família IIA | **Metais Alcalinoterrosos** | $n s^2$ | $Be, Mg, Ca, Sr, Ba, Ra$ |
| **Grupos 3 a 12** | Famílias B | **Metais de Transição Externa** | $(n-1)d^{1 \text{ a } 10}\ n s^{1 \text{ a } 2}$ | $Fe, Cu, Au, Ag, Pt, Zn, Ti$ |
| *Série destacada* | Bloco $f$ | **Metais de Transição Interna** | $(n-2)f^{1 \text{ a } 14}\ (n-1)d^{0 \text{ ou } 1}\ n s^2$ | Lantanídeos ($Z=57\text{-}71$) e Actinídeos ($Z=89\text{-}103$) |
| **Grupo 13** | Família IIIA | **Família do Boro** | $n s^2\ n p^1$ | $B, Al, Ga, In, Tl$ |
| **Grupo 14** | Família IVA | **Família do Carbono** | $n s^2\ n p^2$ | $C, Si, Ge, Sn, Pb$ |
| **Grupo 15** | Família VA | **Família do Nitrogênio** | $n s^2\ n p^3$ | $N, P, As, Sb, Bi$ |
| **Grupo 16** | Família VIA | **Calcogênios** (formadores de minérios) | $n s^2\ n p^4$ | $O, S, Se, Te, Po$ |
| **Grupo 17** | Família VIIA | **Halogênios** (formadores de sais) | $n s^2\ n p^5$ | $F, Cl, Br, I, At$ |
| **Grupo 18** | Família 0 / VIIIA | **Gases Nobres** (Inertes / Raros) | $n s^2\ n p^6$ ($He: 1s^2$) | $He, Ne, Ar, Kr, Xe, Rn$ |

> **O Caso Singular do Hidrogênio ($_{1}H$):**  
> Embora figure graficamente sobre o Grupo 1 por possuir $1s^1$, **o Hidrogênio NÃO é um metal alcalino**. Trata-se de um ametal singular: não conduz eletricidade, possui elevado potencial de ionização e liga-se covalentemente para compartilhar elétrons ou recebe um elétron para formar o ânion hidreto ($H^-$).

---

### 2.3. Divisão em Blocos Eletrônicos ($s, p, d, f$)
- **Elementos Representativos (Blocos $s$ e $p$):** O elétron de diferenciação (mais energético) localiza-se nos subníveis $s$ ou $p$ da camada de valência.
- **Metais de Transição Externa (Bloco $d$):** O elétron mais energético entra no subnível $d$ da penúltima camada ($(n-1)d$).
- **Metais de Transição Interna (Bloco $f$):** O elétron mais energético entra no subnível $f$ da antepenúltima camada ($(n-2)f$).

---

## 3. Carga Nuclear Efetiva ($Z_{ef}$) e Efeito de Blindagem

Para compreender fisicamente por que o raio atômico, a energia de ionização e a eletronegatividade variam ao longo da tabela, é mandatório dominar o conceito de **Carga Nuclear Efetiva ($Z_{ef}$)**.

Em átomos polieletrônicos, um elétron periférico da camada de valência não sente a atração total da carga nuclear ($+Z$). Ele é repelido pelos elétrons das camadas internas, que formam uma "nuvem de blindagem eletrostática" entre o núcleo positivo e a periferia:

$$Z_{ef} = Z - S$$

Onde:
- $Z$: Carga nuclear real (número atômico / número de prótons).
- $S$: Constante de blindagem (estimada pelas Regras de Slater, representando a densidade de carga dos elétrons das camadas internas).
- $Z_{ef}$: Carga positiva líquida efetivamente experimentada pelo elétron de valência.

```
                    O EFEITO DE BLINDAGEM ELETRÔNICA
                             Camada Interna
                                (Blindagem S)
                  Núcleo (+)        (e-)
                     ╭───╮          ╭───╮          (e-) Elétron de Valência
                     │ Z │◄─────────│ S │           │   Sente apenas:
                     ╰───╯          ╰───╯           ▼   Z_ef = Z - S
                       ▲              │
                       └──────────────┴─────────────┘
                             Atração líquida reduzida
```

### Comportamento Periódico de $Z_{ef}$:
1. **Ao longo de um mesmo Período (da esquerda para a direita):**
   - O número de camadas eletrônicas ($n$) permanece constante.
   - O número atômico ($Z$) aumenta de $1$ em $1$ unidade a cada elemento.
   - Como os elétrons adicionais entram na **mesma camada de valência**, eles são ineficientes em blindar uns aos outros.
   - **Resultado:** A constante $S$ cresce muito pouco, fazendo com que **$Z_{ef}$ aumente significativamente da esquerda para a direita ao longo do período**. O núcleo atrai os elétrons de valência com força progressivamente maior.

2. **Ao longo de um mesmo Grupo (de cima para baixo):**
   - A cada descida de linha, adiciona-se uma camada interna inteira de elétrons ($n$ cresce).
   - O aumento de $Z$ é quase totalmente compensado pelo acréscimo de elétrons de blindagem em $S$.
   - **Resultado:** $Z_{ef}$ varia relativamente pouco ou cresce sutilmente, mas o **aumento no número de níveis quânticos ($n$) domina amplamente o comportamento físico do raio**.

---

## 4. Estudo Pormenorizado das Propriedades Periódicas

As propriedades atômicas que variam de modo regular e recorrente em função do número atômico crescente são chamadas de **Propriedades Periódicas**.

---

### 4.1. Raio Atômico

O raio atômico define a extensão espacial da nuvem eletrônica de um átomo. Como a densidade de probabilidade de Schrödinger decai assintoticamente sem um término abrupto, o raio atômico é medido operacionalmente por difração de raios X como **metade da distância interatômica internuclear ($d$) entre dois átomos idênticos ligados covalentemente**:

$$r = \frac{d}{2}$$

#### A. Tendência Periódica do Raio Atômico:
- **Nas Famílias (de cima para baixo):** O raio atômico **aumenta**.
  * *Justificativa física:* Adicionam-se novas camadas eletrônicas principais ($n$). Elétrons mais afastados do núcleo geram um volume atômico substancialmente maior.
- **Nos Períodos (da direita para a esquerda):** O raio atômico **aumenta para a esquerda** (ou seja, diminui da esquerda para a direita!).
  * *Justificativa física:* Da esquerda para a direita, como o número de camadas é o mesmo mas a **Carga Nuclear Efetiva ($Z_{ef}$)** aumenta, o núcleo atrai a nuvem eletrônica de valência com força coulombiana crescente, promovendo uma **contração volumétrica** da eletrosfera.

```
                        TENDÊNCIA DO RAIO ATÔMICO
                      ◄────────────────────────────
                      │                         ▲
                      │                         │
                      ▼                         │
                   Cresce                     Cresce
                   para a                     para
                  esquerda                    baixo
```

*Maior átomo da tabela:* Césio ($Cs$) / Frâncio ($Fr$).  
*Menor átomo da tabela:* Hélio ($He$) / Flúor ($F$).

---

### 4.2. Raio Iônico: Cátions, Ânions e Séries Isoeletrônicas

A formação de íons altera de maneira drástica as forças de atração e repulsão na eletrosfera:

#### A. Raio do Cátion vs. Átomo Neutro:
> **Regra:** O raio de um cátion é **SEMPRE MENOR** do que o raio de seu átomo neutro de origem ($r_{\text{cátion}} < r_{\text{neutro}}$).

*Justificativa física:*
1. Ao perder elétrons, a repulsão intereletrônica na camada periférica diminui sensivelmente.
2. O mesmo número de prótons nucleares ($Z$) passa a atrair um número menor de elétrons, aumentando a força atrativa por elétron remanescente e contraindo o raio.
3. Em muitos casos (ex.: metais alcalinos e alcalinoterrosos), a perda dos elétrons de valência **elimina integralmente a camada mais externa**, reduzindo em uma unidade o valor de $n$.
- Exemplo: $_{11}Na\ (1s^2\ 2s^2\ 2p^6\ 3s^1) \to r \approx 186\text{ pm}$ vs. $_{11}Na^+\ (1s^2\ 2s^2\ 2p^6) \to r \approx 99\text{ pm}$.

#### B. Raio do Ânion vs. Átomo Neutro:
> **Regra:** O raio de um ânion é **SEMPRE MAIOR** do que o raio de seu átomo neutro de origem ($r_{\text{ânion}} > r_{\text{neutro}}$).

*Justificativa física:*
1. A entrada de novos elétrons na camada de valência **aumenta a repulsão eletrostática mútua entre os elétrons**.
2. O número de prótons nucleares ($Z$) permanece fixo, tornando a atração nuclear média por elétron ligeiramente menor. A nuvem eletrônica expande-se para minimizar a energia potencial repulsiva.
- Exemplo: $_{17}Cl\ (r \approx 99\text{ pm})$ vs. $_{17}Cl^-\ (r \approx 181\text{ pm})$.

#### C. Comparação em Séries Isoeletrônicas
Espécies químicas isoeletrônicas apresentam rigorosamente o **mesmo número total de elétrons e a mesma configuração eletrônica**.
- Para espécies isoeletrônicas, a repulsão eletrônica é idêntica; portanto, o raio atômico é determinado **exclusivamente pela carga nuclear ($Z$)**:
  $$\text{Quanto maior o número atômico } Z \implies \text{Maior a atração nuclear} \implies \text{MENOR o raio}$$

Considere a célebre série isoeletrônica com $10$ elétrons (configuração $[Ne]: 1s^2\ 2s^2\ 2p^6$):

```
                     ORDEM DECRESCENTE DE RAIO IÔNICO (SÉRIE ISOELETRÔNICA)
       Espécie:    N³⁻   >   O²⁻   >   F⁻   >   Ne   >   Na⁺   >   Mg²⁺   >   Al³⁺
       Prótons (Z): 7         8         9       10       11        12         13
       Elétrons:   10        10        10       10       10        10         10
       Raio (pm): 171       140       133      112       99        72         53
                   ◄────────────────────────────────────────────────────────────
                   Maior Raio (Menor Z)                  Menor Raio (Maior Z)
```

---

### 4.3. Energia ou Potencial de Ionização (EI)

> **Definição Formal:** É a quantidade **mínima de energia absorvida** necessária para remover um elétron de um átomo isolado, no estado fundamental e na fase gasosa:
> $$X_{(g)} + \text{EI} \longrightarrow X^+_{(g)} + e^- \quad (\Delta H > 0, \text{sempre endotérmico})$$

Unidades usuais: elétron-volt por átomo ($eV/\text{átomo}$) ou quilojoules por mol ($kJ/mol$).

#### A. Tendência Periódica da Energia de Ionização:
- **Nos Períodos (da esquerda para a direita):** A energia de ionização **aumenta**.
  * *Justificativa:* Menor raio atômico e maior carga nuclear efetiva ($Z_{ef}$) prendem o elétron periférico com força eletrostática muito maior.
- **Nas Famílias (de baixo para cima):** A energia de ionização **aumenta**.
  * *Justificativa:* Menor número de camadas ($n$); o elétron de valência está mais próximo do núcleo e sofre menor blindagem, exigindo maior energia para ser arrancado.

```
                      TENDÊNCIA DA ENERGIA DE IONIZAÇÃO
                                                   ▲
                                                   │
                      ────────────────────────────►│
                      Cresce para                  Cresce
                      a direita                    para cima
```

*Elemento com maior energia de ionização:* Hélio ($He \approx 2.372\ kJ/mol$).  
*Elemento com menor energia de ionização:* Césio ($Cs \approx 376\ kJ/mol$) e Frâncio.

#### B. Energias de Ionização Sucessivas e o Salto Quântico
Para qualquer átomo polieletrônico, as energias de ionização sucessivas crescem estritamente:
$$\text{EI}_1 < \text{EI}_2 < \text{EI}_3 < \text{EI}_4 < ...$$
*Por quê?* À medida que retiramos elétrons sucessivos, o íon torna-se progressivamente mais positivo, com menos elétrons sentindo a mesma atração nuclear de $Z$ prótons, tornando a remoção subsequente cada vez mais custosa energeticamente.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🔬 ALERTA UFSC: O SALTO QUÂNTICO NA IDENTIFICAÇÃO DE FAMÍLIAS QUÍMICAS       │
├─────────────────────────────────────────────────────────────────────────────┤
│ Quando todos os elétrons da camada de valência são removidos e a ionização │
│ subsequente exige a retirada de um elétron de uma CAMADA INTERNA FECHADA,   │
│ ocorre um SALTO ABRUPTO E DESPROPORCIONAL (da ordem de 5 a 10 vezes) no    │
│ valor da energia de ionização!                                              │
│                                                                             │
│ Observe as energias de ionização sucessivas do Magnésio (Grupo 2, Z=12):    │
│ • EI₁ (1º elétron de 3s):  738 kJ/mol                                       │
│ • EI₂ (2º elétron de 3s): 1.451 kJ/mol (crescimento normal)                │
│ • EI₃ (elétron de 2p⁶):  7.733 kJ/mol (SALTO ABRUPTO DE ~5,3 VEZES!)      │
│                                                                             │
│ Como a quebra abrupta ocorre entre EI₂ e EI₃, deduz-se infalivelmente       │
│ que o elemento possui exatamente 2 elétrons de valência (Grupo 2 / IIA).   │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### C. Anomalias da 1ª Energia de Ionização: Configurações de Máxima Simetria
Embora a tendência geral ao longo de um período seja o aumento de EI da esquerda para a direita, existem duas anomalias célebres frequentemente cobradas na UFSC, Fuvest e ITA:
1. **$Be$ ($Z=4$) vs. $B$ ($Z=5$):**
   - $Be: [He]\ 2s^2 \implies \text{EI}_1 = 899\ kJ/mol$
   - $B: [He]\ 2s^2\ 2p^1 \implies \text{EI}_1 = 801\ kJ/mol$
   - *Explicação:* O subnível $2s$ do berílio está completamente preenchido ($s^2$), conferindo estabilidade especial. No boro, remover o elétron solitário do subnível $2p^1$ (mais energético e menos penetrante) é mais fácil do que desemparelhar a camada fechada $2s^2$ do berílio.
2. **$N$ ($Z=7$) vs. $O$ ($Z=8$):**
   - $N: [He]\ 2s^2\ 2p^3 \implies \text{EI}_1 = 1.402\ kJ/mol$
   - $O: [He]\ 2s^2\ 2p^4 \implies \text{EI}_1 = 1.314\ kJ/mol$
   - *Explicação:* O nitrogênio possui o subnível $2p$ exatamente **semi-preenchido** ($p_x^1 p_y^1 p_z^1$), com três elétrons desemparelhados de spins paralelos (máxima estabilidade pela Regra de Hund). No oxigênio ($p_x^2 p_y^1 p_z^1$), o quarto elétron entra emparelhado no orbital $p_x$, gerando repulsão intereletrônica localizada que facilita sua ejeção.

---

### 4.4. Eletroafinidade ou Afinidade Eletrônica (AE)

> **Definição Formal:** É a quantidade de **energia liberada** (na convenção termodinâmica clássica) quando um átomo neutro, isolado no estado gasoso fundamental, captura um elétron para formar um ânion monovalente:
> $$X_{(g)} + e^- \longrightarrow X^-_{(g)} + \text{Energia Liberada}$$

- **Tendência Periódica:** Aumenta para a **direita nos períodos** e para **cima nas famílias** (idêntica à energia de ionização).
  * Quanto menor o raio atômico e maior a carga nuclear efetiva, com mais avidez o núcleo atrai e acolhe o elétron entrante.
  * **Atenção:** Os **Gases Nobres (Grupo 18)** possuem afinidade eletrônica praticamente nula ou endotérmica, pois já possuem a camada de valência completa ($s^2 p^6$); a entrada de um elétron exigiria a abertura de um novo nível quântico principal de alta energia.

#### A Anomalia Clássica do Cloro vs. Flúor
Teoricamente, por estar acima do cloro e ter menor raio, o flúor deveria ter maior afinidade eletrônica. Contudo, **o elemento de maior afinidade eletrônica de toda a tabela é o Cloro ($Cl$):**
- $\text{AE}_{\text{Cloro}} \approx 349\ kJ/mol$
- $\text{AE}_{\text{Flúor}} \approx 328\ kJ/mol$
*Causa física:* O átomo de flúor é tão diminuto ($n=2$) que seus 7 elétrons de valência estão confinados em um volume espacial extremamente reduzido, gerando uma altíssima densidade de carga. Quando um elétron tenta entrar na nuvem do flúor, sofre **forte repulsão eletrostática intereletrônica**, reduzindo a energia líquida liberada no processo. No cloro ($n=3$), a eletrosfera é mais espaçosa, acomodando o elétron entrante com menor repulsão.

---

### 4.5. Eletronegatividade e Eletropositividade

#### A. Eletronegatividade
> **Definição de Linus Pauling:** É a capacidade que um átomo possui de **atrair para si o par de elétrons compartilhado em uma ligação química covalente**.

- **Diferença conceitual essencial:** A Afinidade Eletrônica mede a energia de um átomo **isolado no vácuo**. A Eletronegatividade mede a força atrativa em uma **molécula unida por ligação química**.
- **Os Gases Nobres:** Como em condições normais não formam compostos covalentes estáveis, os gases nobres mais leves ($He, Ne, Ar$) **não possuem valor atribuído na escala padrão de Pauling**.
- **Tendência Periódica:** Aumenta para a **direita e para cima** (o Flúor é o elemento mais eletronegativo, com valor arbitrário $4,0$).

```
                      A ESCALA DE ELETRONEGATIVIDADE DE PAULING
                                 (Ordem Decrescente)
       F > O > N ≈ Cl > Br > I ≈ S ≈ C > P ≈ H > Semimetais > Metais
      (4,0) (3,5) (3,0) (3,0) (2,8) (2,5)(2,5)(2,5) (2,1)(2,1)

      Mnemônico Popular Canônico:
      "Fui Ontem No Clube, Briguei I Saí Correndo Para o Hospital"
```

#### B. Eletropositividade (Caráter Metálico)
É a tendência que um elemento possui de **perder elétrons**, oxidando-se e formando cátions.
- É a propriedade estritamente antagônica à eletronegatividade.
- **Tendência Periódica:** Aumenta para a **esquerda nos períodos** e para **baixo nas famílias** (cresce exatamente no mesmo sentido do raio atômico).
- *Elemento mais eletropositivo:* Frâncio ($Fr$) e Césio ($Cs$).

---

### 4.6. Propriedades Periódicas Físicas: Densidade, Ponto de Fusão e Ponto de Ebulição

Nem todas as propriedades periódicas dependem exclusivamente de atrações eletrônicas simples; algumas refletem a física do estado sólido condensado e o tipo de retículo cristalino:

#### A. Densidade Absoluta ($d = m/V$)
- **Nas Famílias:** Cresce de **cima para baixo**, pois o aumento da massa atômica ($A$) supera amplamente o aumento do volume atômico ($V$).
- **Nos Períodos:** Cresce das **extremidades para o centro**, atingindo o valor máximo nos metais de transição do 6º período.
- **Elementos Mais Densos da Natureza:**
  * **Ósmio ($Os$):** $d \approx 22,59\ g/cm^3$
  * **Irídio ($Ir$):** $d \approx 22,56\ g/cm^3$
  * *(Para efeito de comparação: o chumbo possui $11,3\ g/cm^3$; um tijolo do tamanho de uma caixa de sapatos de Ósmio pesaria cerca de $45\ kg$!).*

```
                           TENDÊNCIA DA DENSIDADE
                           ───────►     ◄───────
                           │      \     /      │
                           ▼       ▼   ▼       ▼
                                  ╭─────╮
                                  │ Os  │ (Centro inferior: máxima densidade)
                                  ╰─────╯
```

#### B. Pontos de Fusão (PF) e Pontos de Ebulição (PE)
- **Nos Grupos 1 e 2 (Metais Alcalinos e Alcalinoterrosos):** O ponto de fusão cresce de **baixo para cima**!
  * *Por quê?* Como possuem retículo metálico, quanto menor o cátion metálico (mais acima na família), mais próxima fica a nuvem eletrônica dos núcleos e mais forte é a ligação metálica.
- **Na maioria dos demais grupos (Metais de Transição e Ametais):** O PF e PE crescem de **cima para baixo**.
- **Recordistas da Tabela Periódica:**
  * **Tungstênio ($W$):** O metal de maior ponto de fusão conhecido ($\text{PF} \approx 3.422\ ^\circ C$ e $\text{PE} \approx 5.555\ ^\circ C$), razão pela qual foi classicamente utilizado em filamentos de lâmpadas incandescentes.
  * **Carbono (forma Diamante):** Substância pura de maior ponto de fusão e sublimação ($\text{PF} > 3.550\ ^\circ C$), sustentado por sua rede tridimensional covalente infinita tetraédrica.
  * **Hélio ($He$):** Menor ponto de ebulição de toda a matéria ($\text{PE} \approx -268,9\ ^\circ C \approx 4,2\text{ K}$).

---

## 5. Matriz-Resumo Integrada de Propriedades Periódicas

```
┌───────────────────────────────┬───────────────────────────────┬──────────────────────────────┐
│ Propriedade Periódica         │ Crescimento nos Períodos      │ Crescimento nas Famílias     │
├───────────────────────────────┼───────────────────────────────┼──────────────────────────────┤
│ Raio Atômico                  │ Direita ──► Esquerda (◄──)    │ Cima ──► Baixo (▼)           │
│ Raio do Cátion                │ Menor que o átomo neutro      │ Menor que o átomo neutro     │
│ Raio do Ânion                 │ Maior que o átomo neutro      │ Maior que o átomo neutro     │
│ Energia de Ionização (EI)     │ Esquerda ──► Direita (──►)    │ Baixo ──► Cima (▲)           │
│ Afinidade Eletrônica (AE)     │ Esquerda ──► Direita (──►)    │ Baixo ──► Cima (▲)           │
│ Eletronegatividade            │ Esquerda ──► Direita (──►)    │ Baixo ──► Cima (▲)           │
│ Eletropositividade            │ Direita ──► Esquerda (◄──)    │ Cima ──► Baixo (▼)           │
│ Densidade Absoluta            │ Extremidades ──► Centro       │ Cima ──► Baixo (▼)           │
│ Ponto de Fusão (Geral)        │ Extremidades ──► Centro       │ Cima ──► Baixo (▼)           │
│ Ponto de Fusão (Alcalinos)    │ Extremidades ──► Centro       │ Baixo ──► Cima (▲)           │
└───────────────────────────────┴───────────────────────────────┴──────────────────────────────┘
```

---

## 6. Destaques para Provas Oficiais (ENEM e UFSC)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🌍 ALERTA ENEM: METAIS E A TRANSIÇÃO ENERGÉTICA GLOBAL                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ No ENEM, as propriedades periódicas são cobradas aplicadas à sustentabilidade│
│ e novas tecnologias energéticas:                                            │
│ • Lítio (Li): Metal alcalino de menor raio atômico e menor massa atômica    │
│   do Grupo 1. Possui baixíssima densidade e altíssimo potencial eletro-     │
│   químico de oxidação, permitindo que as baterias de íon-lítio armazenem    │
│   máxima densidade de energia com peso mínimo em veículos elétricos e       │
│   smartphones.                                                              │
│ • Terras Raras (Lantanídeos): Neodímio (Nd) e Disprósio (Dy) são elementos   │
│   de transição interna com múltiplos elétrons desemparelhados em orbitais 4f│
│   usados na fabricação de superímãs permanentes em turbinas eólicas e       │
│   motores de tração elétrica.                                               │
│ • Silício (Si) e Germânio (Ge): Semicondutores do Grupo 14 cuja condutivi-  │
│   dade elétrica intermediária permite a construção de junções p-n em painéis│
│   fotovoltaicos solares e microprocessadores de silício.                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Mapa Conceitual Integrador do Módulo 02

```
                       TABELA PERIÓDICA MODERNA
                                  │
     ┌────────────────────────────┴────────────────────────────┐
     ▼                                                         ▼
ARQUITETURA (Moseley - Z)                             FORÇAS DIRETORAS
• 7 Períodos (n = camadas)                             • Z_ef = Z - S (Carga Efetiva)
• 18 Grupos (configuração da CV)                       • n (Efeito da Distância)
• Blocos s, p, d, f                                    • Blindagem dos e⁻ Internos
     │                                                         │
     └────────────────────────────┬────────────────────────────┘
                                  ▼
                        PROPRIEDADES PERIÓDICAS
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
DIMENSÃO ESPACIAL          ENERGIA & ELETRONS        MACROSCÓPICAS
• Raio Atômico             • Energia de Ionização    • Densidade (Os, Ir)
• Raio Iônico (Cátion<Ânion)• Afinidade Eletrônica   • Ponto de Fusão (W)
• Séries Isoeletrônicas    • Eletronegatividade      • Metais vs Ametais
```
