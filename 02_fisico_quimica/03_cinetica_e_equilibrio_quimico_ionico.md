# Módulo 03: Cinética Química, Equilíbrio Químico e Equilíbrio Iônico

---

## 1. Cinética Química: A Velocidade das Transformações

Enquanto a Termodinâmica Química prevê se uma reação química é termodinamicamente possível ou espontânea ($\Delta G < 0$), a **Cinética Química** estuda a **rapidez (velocidade)** com que os reagentes são convertidos em produtos e os **mecanismos moleculares** através dos quais essas transformações ocorrem.

*Exemplo Didático:* A transformação do diamante em grafite ($C_{\text{diamante}} \to C_{\text{grafite}}$) é termodinamicamente espontânea sob condições ambientes ($\Delta G < 0$), porém sua velocidade cinética é tão infinitesimalmente lenta que o diamante permanece inalterado por milhões de anos (metaestabilidade cinética).

```
                      CINÉTICA vs. TERMODINÂMICA
         TERMODINÂMICA                                CINÉTICA
  ┌───────────────────────────┐             ┌───────────────────────────┐
  │ Prevê a ESPONTANEIDADE    │             │ Mede a VELOCIDADE e o     │
  │ e o RENDIMENTO MÁXIMO     │             │ TEMPO para a reação       │
  │ (ΔH, ΔS, ΔG, K_eq)        │             │ (v, Ea, k, Mecanismos)    │
  └───────────────────────────┘             └───────────────────────────┘
```

---

### 1.1. Velocidade Média de Reação

Dada a reação hipotética genérica:

$$a\ A + b\ B \longrightarrow c\ C + d\ D$$

- **Velocidade Média de Consumo de um Reagente:**
  $$v_m(A) = -\frac{\Delta [A]}{\Delta t} = -\frac{[A]_{\text{final}} - [A]_{\text{inicial}}}{t_{\text{final}} - t_{\text{inicial}}} > 0$$
  *(O sinal negativo é inserido por convenção porque a concentração de reagente decresce ao longo do tempo, garantindo velocidade positiva).*
- **Velocidade Média de Formação de um Produto:**
  $$v_m(C) = +\frac{\Delta [C]}{\Delta t} = \frac{[C]_{\text{final}} - [C]_{\text{inicial}}}{t_{\text{final}} - t_{\text{inicial}}}$$
- **Velocidade Média da Reação Global ($v_{\text{reação}}$):**
  Para que a velocidade da reação seja um valor único e independente da espécie química monitorada no laboratório, divide-se a velocidade de cada componente pelo seu respectivo coeficiente estequiométrico:

$$v_{\text{reação}} = \frac{v_m(A)}{a} = \frac{v_m(B)}{b} = \frac{v_m(C)}{c} = \frac{v_m(D)}{d}$$

---

### 1.2. Teoria das Colisões e Complexo Ativado

Formulada por Max Trautz e William Lewis (1916-1918), a **Teoria das Colisões** postula que, para que ocorra uma reação química entre partículas:
1. **Choque Intermolecular:** As partículas reagentes devem colidir fisicamente no espaço.
2. **Orientação Espacial Geométrica Favorável (Choque Efetivo / Eficaz):** A colisão deve ocorrer em um ângulo que aproxime os centros reativos e permita a quebra e formação simultânea de ligações.
3. **Energia Cinética Suficiente (Energia de Ativação - $E_a$):** A soma da energia cinética das partículas no instante da colisão deve ser igual ou superior à barreira energética mínima exigida para a reação.

```
                      MECANISMO DO COMPLEXO ATIVADO
      A-A   +   B-B  ────────►  [ A ••• A ]  ────────►  2 A-B
                                [ •   • ]
     Reagentes Isolados         [ B ••• B ]           Produtos Estáveis
    (Ligações intactas)       Complexo Ativado       (Novas ligações formadas)
                            (Máxima Energia/Instável)
```

- **Complexo Ativado:** É uma estrutura intermediária transitória e de altíssima energia potencial, na qual as ligações químicas dos reagentes estão parcialmente enfraquecidas e as novas ligações dos produtos estão parcialmente constituídas.
- **Energia de Ativação ($E_a$):** É a barreira energética que os reagentes devem transpor para atingir o topo da colina de energia potencial e formar o complexo ativado:
  $$E_a = H_{\text{complexo ativado}} - H_{\text{reagentes}} > 0$$

```
               PERFIL DE ENERGIA POTENCIAL DE UMA REAÇÃO
    Energia (E)
        ▲
        │                Complexo Ativado (Topo)
        │                       ╭─●─╮
        │                      ╭╯   ╰╮
        │       Ea (direta)   ╭╯     ╰╮  Ea (inversa)
        │      ┌─────────────╭╯       ╰╮
        │      ▼            ╭╯         ╰╮
   H_R ─┼──────●────────────╯           ╰╮
        │   Reagentes                    ╰╮
        │                                 ╰─────────●─ H_P
        │           │◄─────── ΔH < 0 ───────────────►│  Produtos
        └───────────┴────────────────────────────────┴──► Coordenada de Reação
```

---

### 1.3. Fatores que Alteram a Velocidade da Reação

A rapidez de uma reação química pode ser manipulada alterando-se quatro fatores fundamentais:

1. **Temperatura:**
   - O aumento de temperatura eleva a energia cinética média das partículas ($\overline{E}_c = \frac{3}{2} k_B T$).
   - Conforme a **Distribuição de Maxwell-Boltzmann**, um aumento mesmo modesto de temperatura expande exponencialmente a fração de moléculas cuja energia cinética é igual ou superior à energia de ativação ($E \ge E_a$).
   - Regra empírica de Van 't Hoff: para muitas reações à temperatura ambiente, um aumento de $10^\circ C$ dobra a velocidade da reação.

2. **Superfície de Contato (Sistemas Heterogêneos):**
   - Em reações entre um sólido e um fluido (líquido ou gás), a reação só pode ocorrer na interface de contato. Ao triturar ou pulverizar um sólido, sua área superficial total aumenta exponencialmente, elevando a frequência de choques efetivos por segundo (ex.: comprimido efervescente em pó dissolve muito mais rápido que em pastilha inteira; poeira de carvão em minas é explosiva).

3. **Concentração dos Reagentes e Pressão de Gases:**
   - O aumento da concentração de solutos em solução ou da pressão em sistemas gasosos eleva o número de partículas por unidade de volume, intensificando a frequência de colisões entre os reagentes.

4. **Ação de Catalisadores:**
   - Um catalisador é uma substância que **aumenta a velocidade de uma reação química sem ser consumida permanentemente** no processo global.
   - **Mecanismo de Ação:** O catalisador cria uma rota reacional alternativa (novo mecanismo) que apresenta uma **MENOR ENERGIA DE ATIVAÇÃO ($E_{a,\text{cat}} < E_{a,\text{livre}}$)**.

> ⚠️ **O QUE O CATALISADOR NÃO FAZ (ARMADILHA CLÁSSICA DE VESTIBULAR):**  
> 1. O catalisador **NÃO altera a variação de entalpia ($\Delta H$)** da reação (os patamares de reagentes e produtos são rigorosamente os mesmos).  
> 2. O catalisador **NÃO altera o rendimento termodinâmico** da reação nem desloca a posição de equilíbrio químico ($K_c$ permanece idêntico). Ele apenas faz com que o equilíbrio seja atingido em menor tempo!

- **Tipos de Catálise:**
  - *Catálise Homogênea:* O catalisador e os reagentes encontram-se na mesma fase física (ex.: decomposição do $H_2O_2$ aquoso catalisada por íons $I^-$ aquosos).
  - *Catálise Heterogênea:* O catalisador forma uma fase física distinta dos reagentes, atuando por adsorção superficial (ex.: metais sólidos $Pt, Pd, Rh$ nos conversores catalíticos de escapamentos automotivos).
  - *Biocatálise:* Enzimas proteicas que aceleram reações bioquímicas em fatores de até $10^6$ a $10^{12}$ vezes sob temperatura fisiológica de $37^\circ C$.

---

### 1.4. A Lei da Velocidade (Guldberg-Waage / Ação das Massas)

Formulada experimentalmente por Cato Guldberg e Peter Waage (1864):

> **LEI DA VELOCIDADE:**  
> A velocidade instantânea de uma reação química é diretamente proporcional ao produto das concentrações molares dos reagentes, elevadas a potências experimentais denominadas ordens de reação:
>
> $$v = k \cdot [A]^\alpha \cdot [B]^\beta$$

Onde:
- $k$: Constante cinética de velocidade (depende exclusivamente da reação química e da **temperatura**).
- $\alpha$: Ordem parcial da reação em relação ao reagente $A$.
- $\beta$: Ordem parcial da reação em relação ao reagente $B$.
- $\alpha + \beta$: **Ordem Global** da reação.

#### Reações Elementares vs. Não-Elementares:
- **Reação Elementar:** Ocorre em uma única etapa microscópica direta. Os expoentes $\alpha$ e $\beta$ são **iguais aos próprios coeficientes estequiométricos**:
  $$2\ NO_{2(g)} \longrightarrow 2\ NO_{(g)} + O_{2(g)} \implies v = k \cdot [NO_2]^2 \quad (\text{Ordem 2})$$
- **Reação Não-Elementar (em Múltiplas Etapas):** Ocorre através de uma sequência de etapas elementares consecutivas (mecanismo de reação). A velocidade da reação global é **governada exclusivamente pela ETAPA MAIS LENTA**:
  - Etapa 1 (Lenta): $NO_{2(g)} + F_{2(g)} \longrightarrow NO_2F_{(g)} + F_{(g)}$
  - Etapa 2 (Rápida): $NO_{2(g)} + F_{(g)} \longrightarrow NO_2F_{(g)}$
  - Global: $2\ NO_2 + F_2 \longrightarrow 2\ NO_2F$
  - A lei de velocidade é ditada pela Etapa 1: $\mathbf{v = k \cdot [NO_2]^1 \cdot [F_2]^1}$ (e não ao quadrado de $NO_2$!).

#### Determinação Experimental de Ordens de Reação:
Considere os seguintes dados cinéticos para a reação $2\ A + B \to C$:

| Experimento | $[A]$ ($mol/L$) | $[B]$ ($mol/L$) | Velocidade Inicial ($mol\cdot L^{-1}\cdot s^{-1}$) |
|---|---|---|---|
| 1 | $0,10$ | $0,10$ | $2,0 \times 10^{-3}$ |
| 2 | $0,20$ | $0,10$ | $8,0 \times 10^{-3}$ |
| 3 | $0,10$ | $0,30$ | $6,0 \times 10^{-3}$ |

1. **Determinação de $\alpha$ (ordem de A):** Compare experimentos 1 e 2 (onde $[B]$ é mantida constante em $0,10\ M$):
   - $[A]$ dobra ($0,10 \to 0,20$, fator $2$).
   - A velocidade quadruplica ($2,0 \times 10^{-3} \to 8,0 \times 10^{-3}$, fator $4 = 2^2$).
   - Portanto: $2^\alpha = 4 \implies \mathbf{\alpha = 2}$ (Reação de 2ª ordem em relação a $A$).
2. **Determinação de $\beta$ (ordem de B):** Compare experimentos 1 e 3 (onde $[A]$ é mantida constante em $0,10\ M$):
   - $[B]$ triplica ($0,10 \to 0,30$, fator $3$).
   - A velocidade triplica ($2,0 \times 10^{-3} \to 6,0 \times 10^{-3}$, fator $3 = 3^1$).
   - Portanto: $3^\beta = 3 \implies \mathbf{\beta = 1}$ (Reação de 1ª ordem em relação a $B$).
3. **Lei de Velocidade e Ordem Global:**
   $$\mathbf{v = k \cdot [A]^2 \cdot [B]^1} \quad \text{Ordem Global} = 2 + 1 = \mathbf{3}$$

---

## 2. Equilíbrio Químico

Muitas transformações químicas não caminham até o consumo total dos reagentes; ao contrário, chegam a um estado de estagnação macroscópica aparente no qual reagentes e produtos coexistem permanentemente.

### 2.1. O Conceito Dinâmico de Equilíbrio
Em um sistema fechado sob temperatura constante, à medida que a reação direta progride, os reagentes são consumidos e a velocidade direta ($v_d$) decresce. Simultaneamente, os produtos formados colidem e regeneram os reagentes, fazendo a velocidade inversa ($v_i$) crescer a partir de zero.

> **ESTADO DE EQUILÍBRIO QUÍMICO:**  
> O equilíbrio químico é atingido no instante exato em que a **velocidade da reação direta torna-se rigorosamente igual à velocidade da reação inversa**:
>
> $$\mathbf{v_{\text{direta}} = v_{\text{inversa}} \neq 0}$$
>
> A partir desse momento, as **concentrações molares de todas as espécies químicas permanecem constantes** no tempo.

```
                  EVOLUÇÃO TEMPORAL ATÉ O EQUILÍBRIO
    Velocidade (v)                            Concentração ([ ])
       ▲                                          ▲
  v_d ─┼──╮                                       │  [Reagentes]
       │   ╰╮                                [R] ─┼──╮
       │     ╰╮                                   │   ╰╮
       │       ╰─────────── v_d = v_i             │     ╰──────────────── Constante
       │       ╭─────────── (Equilíbrio Dinâmico) │     ╭──────────────── Constante
       │     ╭╯                              [P] ─┼───╭╯  [Produtos]
  v_i ─┼───╭╯                                     │ ╭╯
       └──────────────────► Tempo                 └──────────────────► Tempo
               │                                          │
               t_eq                                       t_eq
```

---

### 2.2. A Constante de Equilíbrio em Concentração ($K_c$) e Pressão ($K_p$)

Dada a reação reversível genérica:

$$a\ A_{(g)} + b\ B_{(aq)} \rightleftharpoons c\ C_{(g)} + d\ D_{(aq)}$$

A **Constante de Equilíbrio em Função das Concentrações ($K_c$)** é:

$$\mathbf{K_c = \frac{[C]^c \cdot [D]^d}{[A]^a \cdot [B]^b}}$$

Para sistemas gasosos, expressa-se a constante em termos das **Pressões Parciais ($K_p$)**:

$$\mathbf{K_p = \frac{(P_C)^c \cdot (P_D)^d}{(P_A)^a \cdot (P_B)^b}}$$

#### Regra Fundamental das Fases Omitidas:
- **Sólidos puros ($s$) e solventes líquidos puros ($l$) NÃO ENTRAM na expressão de $K_c$ ou $K_p$!** Suas atividades ou concentrações são consideradas constantes por definição.
- *Exemplo clássico:* Decomposição do calcário:
  $$CaCO_{3(s)} \rightleftharpoons CaO_{(s)} + CO_{2(g)} \implies \mathbf{K_c = [CO_2]} \quad \text{e} \quad \mathbf{K_p = P_{CO_2}}$$

#### Relação entre $K_p$ e $K_c$:
Pela equação de Clapeyron ($P = \frac{n}{V} RT = [ ] RT$), deduz-se:

$$\mathbf{K_p = K_c \cdot (R \cdot T)^{\Delta n_{\text{gasoso}}}}$$

Onde $\Delta n_{\text{gasoso}} = \sum \text{coeficientes gasosos dos produtos} - \sum \text{coeficientes gasosos dos reagentes}$.
Se $\Delta n = 0$ (ex.: $H_{2(g)} + I_{2(g)} \rightleftharpoons 2\ HI_{(g)}$), então $(RT)^0 = 1 \implies \mathbf{K_p = K_c}$.

#### O Quociente de Reação ($Q_c$):
Calculado com a mesma fórmula de $K_c$, porém com concentrações medidas em um instante qualquer fora do equilíbrio:
- $Q_c < K_c$: O sistema possui menos produtos que o equilíbrio $\implies$ desloca-se para a **DIREITA** (formação de produtos).
- $Q_c = K_c$: O sistema encontra-se em **EQUILÍBRIO**.
- $Q_c > K_c$: O sistema possui excesso de produtos $\implies$ desloca-se para a **ESQUERDA** (regeneração de reagentes).

---

### 2.3. Deslocamento de Equilíbrio: Princípio de Le Chatelier

Formulado por Henri Louis Le Chatelier (1884):

> **O PRINCÍPIO DE LE CHATELIER:**  
> *"Quando um sistema em equilíbrio químico é submetido a uma perturbação externa (variação de concentração, pressão ou temperatura), ele se desloca espontaneamente no sentido que tende a contrabalançar, minimizar ou anular o efeito dessa perturbação."*

```
              AÇÃO EXTERNA vs. RESPOSTA DE LE CHATELIER
      Perturbação Imposta                Resposta do Sistema
  ┌─────────────────────────────┐    ┌─────────────────────────────┐
  │ Adicionar espécie química   │───►│ Desloca para o LADO OPOSTO  │
  │ Remover espécie química     │───►│ Desloca para o MESMO LADO   │
  │ Aumentar Pressão (Diminui V)│───►│ Desloca para MENOR VOL GÁS  │
  │ Reduzir Pressão (Aumenta V) │───►│ Desloca para MAIOR VOL GÁS  │
  │ Aumentar Temperatura        │───►│ Favorece sentido ENDOTÉRMICO│
  │ Diminuir Temperatura        │───►│ Favorece sentido EXOTÉRMICO │
  └─────────────────────────────┘    └─────────────────────────────┘
```

1. **Efeito da Variação de Concentração:**
   - Adicionar uma espécie química: o sistema desloca-se consumindo-a (para o lado oposto).
   - Remover uma espécie química: o sistema desloca-se repondo-a (para o mesmo lado).
   - *Nota:* A adição ou remoção de espécies químicas **NÃO altera o valor numérico da constante $K_c$**.

2. **Efeito da Variação de Pressão e Volume (Gases):**
   - **Aumento da Pressão Externa (ou redução de volume):** O sistema comprime as partículas gasosas; para aliviar a pressão, o equilíbrio desloca-se no sentido que apresenta o **menor número de mols de substâncias gasosas** ($\sum n_{\text{gás}}$ menor).
   - **Diminuição da Pressão Externa (ou expansão de volume):** Desloca-se no sentido do **maior volume gasoso**.
   - Se o número de mols gasosos for idêntico dos dois lados ($\Delta n = 0$), a pressão **não provoca deslocamento de equilíbrio**.

3. **Efeito da Variação de Temperatura:**
   - **Aumento de Temperatura:** Fornece calor ao sistema; para absorver essa energia térmica excedente, o equilíbrio desloca-se no sentido da **reação endotérmica ($\Delta H > 0$)**.
   - **Diminuição de Temperatura (Resfriamento):** O sistema desloca-se no sentido da **reação exotérmica ($\Delta H < 0$)**, liberando calor.
   - 🚨 **ATENÇÃO MÁXIMA:** A temperatura é a **ÚNICA variável termodinâmica capaz de alterar o valor numérico da constante de equilíbrio ($K$)**!
     - Em reações endotérmicas: aumentar $T$ aumenta $K$.
     - Em reações exotérmicas: aumentar $T$ diminui $K$.

#### Estudo de Caso Tecnológico: O Processo Haber-Bosch
Síntese industrial da amônia para fertilizantes:

$$N_{2(g)} + 3\ H_{2(g)} \rightleftharpoons 2\ NH_{3(g)} \quad \Delta H = -92,2\text{ kJ}$$

- **Análise dos Mols Gasosos:** Reagentes = $1 + 3 = 4\text{ mols gasosos}$; Produtos = $2\text{ mols gasosos}$.
- **Para maximizar a produção de $NH_3$:**
  1. *Pressão Elevadíssima (~200 atm):* Favorece o lado de menor volume gasoso ($4\text{ mols} \to 2\text{ mols}$).
  2. *Remoção Contínua de $NH_3$ Líquida:* Ao resfriar o reator seletivamente para liquefazer a amônia e retirá-la, o sistema desloca-se permanentemente para a direita.
  3. *O Dilema da Temperatura de Compromisso (~450 °C):* Como a reação é exotérmica, temperaturas baixas aumentariam o rendimento de equilíbrio ($K$ maior). Porém, a baixas temperaturas as colisões moleculares são muito lentas e a reação levaria semanas. Adota-se uma **temperatura de compromisso** intermediária associada a um **catalisador de ferro ativado com óxidos ($Fe/Al_2O_3/K_2O$)**, garantindo velocidade aceitável e alto rendimento contínuo.

---

## 3. Equilíbrio Iônico em Solução Aquosa

O equilíbrio iônico estuda reações reversíveis que envolvem a ionização ou dissociação de eletrólitos fracos em água.

### 3.1. Constante de Ionização ($K_a$ e $K_b$) e Lei de Ostwald
Para um monoácido fraco ($HA$):

$$HA_{(aq)} + H_2O_{(l)} \rightleftharpoons H_3O^+_{(aq)} + A^-_{(aq)} \implies \mathbf{K_a = \frac{[H^+][A^-]}{[HA]}}$$

- Quanto maior o valor de $K_a$, maior a ionização e mais forte é o ácido.
- $pK_a = -\log K_a$ (quanto menor o $pK_a$, mais forte o ácido).

Analogamente, para uma base fraca ($BOH$ ou $B$):

$$B_{(aq)} + H_2O_{(l)} \rightleftharpoons BH^+_{(aq)} + OH^-_{(aq)} \implies \mathbf{K_b = \frac{[BH^+][OH^-]}{[B]}}$$

Para qualquer par ácido-base conjugado de Brønsted-Lowry:
$$\mathbf{K_a \cdot K_b = K_w = 1,0 \times 10^{-14}\text{ (a } 25^\circ C)} \iff pK_a + pK_b = 14$$

#### Lei da Diluição de Ostwald:
Relaciona a constante de ionização ($K$), a molaridade da solução ($M$) e o grau de ionização ($\alpha$):

$$K = \frac{\alpha^2 \cdot M}{1 - \alpha}$$

Para eletrólitos muito fracos ($\alpha \le 5\% = 0,05$), $1 - \alpha \approx 1$, simplificando para:

$$\mathbf{K \approx \alpha^2 \cdot M} \implies \alpha \approx \sqrt{\frac{K}{M}} \quad \text{e} \quad [H^+] = \alpha \cdot M = \sqrt{K_a \cdot M}$$

---

### 3.2. Autoionização da Água e Escalas de pH e pOH

A água pura sofre uma autoionização extremamente discreta:

$$H_2O_{(l)} + H_2O_{(l)} \rightleftharpoons H_3O^+_{(aq)} + OH^-_{(aq)}$$

A **Constante do Produto Iônico da Água ($K_w$)** a $25^\circ C$ é:

$$\mathbf{K_w = [H^+][OH^-] = 1,0 \times 10^{-14}}$$

Como na água pura cada dissociação gera um $H^+$ e um $OH^-$:
$$[H^+] = [OH^-] = \sqrt{10^{-14}} = 1,0 \times 10^{-7}\text{ mol/L}$$

#### Definições Logarítmicas de Peter Sørensen (1909):
$$pH = -\log[H^+] \iff [H^+] = 10^{-pH}$$
$$pOH = -\log[OH^-] \iff [OH^-] = 10^{-pOH}$$

Aplicando $-\log$ sobre a expressão de $K_w$:

$$\mathbf{pH + pOH = 14\text{ (a } 25^\circ C)}$$

- Meio Ácido: $[H^+] > [OH^-] \iff [H^+] > 10^{-7}\text{ M} \iff \mathbf{pH < 7}$
- Meio Neutro: $[H^+] = [OH^-] = 10^{-7}\text{ M} \iff \mathbf{pH = 7}$
- Meio Básico: $[H^+] < [OH^-] \iff [H^+] < 10^{-7}\text{ M} \iff \mathbf{pH > 7}$

---

### 3.3. Hidrólise Salina

Ao dissolver um sal em água, ele dissocia-se completamente em cátions e ânions. Esses íons podem reagir com as moléculas de água (hidrólise), alterando o pH da solução.

```
                      QUADRO GERAL DA HIDRÓLISE SALINA
  ┌─────────────────────┬───────────────────┬──────────────┬───────────────┐
  │ Tipo de Sal         │ Íon que Hidrolisa │ Caráter      │ pH a 25 °C    │
  ├─────────────────────┼───────────────────┼──────────────┼───────────────┤
  │ Ácido Forte +       │ Nenhum (Cátions e │              │               │
  │ Base Forte (NaCl)   │ Ânions neutros)   │ Neutro       │ pH = 7,0      │
  ├─────────────────────┼───────────────────┼──────────────┼───────────────┤
  │ Ácido Fraco +       │ Ânion hidrolisa   │              │               │
  │ Base Forte (CH₃COONa)│ A⁻ + H₂O ⇌ HA + OH⁻│ Básico       │ pH > 7,0      │
  ├─────────────────────┼───────────────────┼──────────────┼───────────────┤
  │ Ácido Forte +       │ Cátion hidrolisa  │              │               │
  │ Base Fraca (NH₄Cl)  │ B⁺ + H₂O ⇌ BOH + H⁺│ Ácido       │ pH < 7,0      │
  ├─────────────────────┼───────────────────┼──────────────┼───────────────┤
  │ Ácido Fraco +       │ Ambos hidrolisam  │ Depende de   │ Se Ka > Kb: <7│
  │ Base Fraca (NH₄Ac)  │ simultaneamente   │ Ka vs. Kb    │ Se Kb > Ka: >7│
  └─────────────────────┴───────────────────┴──────────────┴───────────────┘
```

#### Dedução da Constante de Hidrólise ($K_h$):
Para a hidrólise do ânion acetato ($CH_3COO^-$):
$$CH_3COO^- + H_2O \rightleftharpoons CH_3COOH + OH^- \implies K_h = \frac{[CH_3COOH][OH^-]}{[CH_3COO^-]}$$

Multiplicando o numerador e o denominador por $[H^+]$:
$$K_h = \frac{[CH_3COOH]}{[CH_3COO^-][H^+]} \times [H^+][OH^-] = \frac{1}{K_a} \times K_w \implies \mathbf{K_h = \frac{K_w}{K_a}}$$

---

### 3.4. Soluções-Tampão (Buffers)

Uma **Solução-Tampão** é uma solução que tem a notável capacidade de **resistir a variações bruscas de pH** quando pequenas quantidades de ácidos fortes ($H^+$) ou bases fortes ($OH^-$) são adicionadas a ela, ou quando a solução é diluída.

#### Constituição Típica:
1. **Tampão Ácido:** Mistura de um Ácido Fraco com o seu Sal de Base Forte (ex.: Ácido Acético $CH_3COOH$ e Acetato de Sódio $CH_3COONa$).
2. **Tampão Básico:** Mistura de uma Base Fraca com o seu Sal de Ácido Forte (ex.: Amônia $NH_3$ e Cloreto de Amônio $NH_4Cl$).

#### Equação de Henderson-Hasselbalch:
Dada a ionização do ácido fraco $HA \rightleftharpoons H^+ + A^-$:
$$K_a = \frac{[H^+][A^-]}{[HA]} \implies [H^+] = K_a \cdot \frac{[HA]}{[A^-]}$$

Aplicando o operador logarítmico negativo:
$$\mathbf{pH = pK_a + \log \left( \frac{[\text{base conjugada } A^-]}{[\text{ácido fraco } HA]} \right)}$$

#### Mecanismo Fisiológico do Tampão Bicarbonato no Sangue Humano:
O plasma sanguíneo mantém seu pH rigidamente na estreita faixa de **$7,35\text{ a }7,45$**. Variações fora desse intervalo levam à acidose ou alcalose metabólica/respiratória, podendo causar coma e morte.

O sistema tampão primário é o equilíbrio bifásico ácido carbônico/bicarbonato:

$$CO_{2(g)} + H_2O_{(l)} \rightleftharpoons H_2CO_{3(aq)} \rightleftharpoons H^+_{(aq)} + HCO_{3(aq)}^-$$

- **Se houver influxo de ácido ($H^+$):** O excesso de $H^+$ reage com o ânion bicarbonato ($HCO_3^-$), deslocando o equilíbrio para a esquerda e formando $H_2CO_3$, que se decompõe em $CO_2$ e $H_2O$. O organismo reage aumentando a frequência respiratória (**hiperventilação**), eliminando o $CO_2$ pelos pulmões e preservando o pH.
- **Se houver influxo de base ($OH^-$):** Os íons hidróxido neutralizam os prótons $H^+$ formando água. O equilíbrio desloca-se para a direita, consumindo ácido carbônico e liberando novos prótons $H^+$, mantendo o pH estável.

---

### 3.5. Produto de Solubilidade ($K_{ps}$) e Precipitação Seletiva

Para um sal pouco solúvel (precipitado) em contato com sua solução aquosa saturada:

$$A_x B_{y(s)} \rightleftharpoons x\ A^{y+}_{(aq)} + y\ B^{x-}_{(aq)}$$

Como a concentração do sólido puro é constante, define-se o **Produto de Solubilidade ($K_{ps}$)**:

$$\mathbf{K_{ps} = [A^{y+}]^x \cdot [B^{x-}]^y}$$

#### Relação entre Solubilidade Molar ($S$) e $K_{ps}$:
Seja $S$ a solubilidade do sal em $\text{mol/L}$:
- Para sais do tipo $AB$ (ex.: $AgCl$): $[Ag^+] = S, [Cl^-] = S \implies \mathbf{K_{ps} = S^2} \iff S = \sqrt{K_{ps}}$
- Para sais do tipo $AB_2$ (ex.: $PbCl_2, Ca(OH)_2$): $[A^{2+}] = S, [B^-] = 2S \implies K_{ps} = (S)(2S)^2 = \mathbf{4S^3} \iff S = \sqrt[3]{\frac{K_{ps}}{4}}$
- Para sais do tipo $A_2B_3$ (ex.: $Al_2S_3$): $[A^{3+}] = 2S, [B^{2-}] = 3S \implies K_{ps} = (2S)^2(3S)^3 = \mathbf{108S^5}$

#### O Efeito do Íon Comum na Solubilidade:
Se adicionarmos um eletrólito solúvel contendo um íon já presente no equilíbrio (ex.: adicionar $NaCl$ a uma solução saturada de $AgCl$), a concentração de $Cl^-$ aumenta abruptamente. Pelo Princípio de Le Chatelier, o equilíbrio:

$$AgCl_{(s)} \rightleftharpoons Ag^+_{(aq)} + Cl^-_{(aq)}$$

é forçado a deslocar-se para a **ESQUERDA**, provocando a precipitação imediata de mais $AgCl_{(s)}$ e **reduzindo drasticamente a solubilidade molar do sal**.

#### Previsão de Precipitação pelo Quociente de Solubilidade ($Q_{ps}$):
- $Q_{ps} < K_{ps}$: Solução insaturada (não ocorre precipitação).
- $Q_{ps} = K_{ps}$: Solução saturada em equilíbrio dinâmico.
- $Q_{ps} > K_{ps}$: Solução supersaturada $\implies$ **OCORRE PRECIPITAÇÃO** até que o produto das concentrações atinja novamente o valor de $K_{ps}$.
