# Módulo 04: Reações Orgânicas Fundamentais, Polímeros Sintéticos e Biomoléculas

---

## 1. Mecânica e Espécies Reacionais em Química Orgânica

As reações orgânicas fundamentam-se na ruptura e formação de ligações covalentes, sendo regidas pela estabilidade termodinâmica dos intermediários reacionais e pela distribuição de densidade eletrônica entre os reagentes:

```
                         CISÃO DE LIGAÇÕES COVALENTES
                                      │
         ┌────────────────────────────┴────────────────────────────┐
         ▼                                                         ▼
  CISÃO HOMOLÍTICA (HOMÓLISE)                               CISÃO HETEROLÍTICA (HETERÓLISE)
  • Quebra simétrica do par eletrônico                      • Quebra assimétrica do par eletrônico
  • Ocorre sob luz (hν), calor ou peróxidos                 • Ocorre em meio polar com solventes ionizantes
  • Gera RADICAIS LIVRES neutros (R•)                       • Gera ÍONS: Carbocátions (R⁺) ou Carbânions (R⁻)
```

### 1.1. Eletrófilos vs. Nucleófilos
- **Eletrófilos ($E^+$):** Espécies químicas deficientes em elétrons (ácidos de Lewis) que buscam centros de alta densidade eletrônica para receber pares de elétrons. Exemplos: $H^+, Br^+, NO_2^+, R_3C^+$ (carbocátions), $AlCl_3, BF_3$.
- **Nucleófilos ($Nu^-$):** Espécies químicas ricas em elétrons (bases de Lewis), que possuem pares de elétrons isolados disponíveis para doar e atacar núcleos atômicos positivos. Exemplos: $OH^-, CN^-, Cl^-, Br^-, I^-, NH_3, H_2O, R-O^-$.

---

## 2. As Quatro Grandes Famílias de Reações Orgânicas

```
                    AS GRANDES FAMÍLIAS REACIONAIS ORGÂNICAS
                                       │
     ┌──────────────────┬──────────────┴──────────────┬──────────────────┐
     ▼                  ▼                             ▼                  ▼
 1. ADIÇÃO          2. SUBSTITUIÇÃO               3. ELIMINAÇÃO      4. OXIDAÇÃO /
 • Alcenos          • Alcanos (Radicalar)         • Desidratação        REDUÇÃO
 • Alcinos          • Aromáticos (Eletrofílica)     de Álcoois       • Branda (Baeyer)
 • Regra de         • Haletos (SN1 / SN2)         • Regra de         • Enérgica
   Markovnikov                                      Saytzeff         • Ozonólise
```

---

### 2.1. Reações de Adição em Alcenos e Alcinos

Ocorrem tipicamente em moléculas insaturadas dotadas de ligações $\pi$. A ligação fraca $\pi$ é rompida e seus elétrons são utilizados para estabelecer duas novas ligações covalentes $\sigma$, mais fortes e estáveis.

#### A. Hidrogenação Catalítica (Reação de Sabatier-Senderens)
Adição de hidrogênio gasoso ($H_2$) na presença de catalisadores metálicos finamente divididos ($Ni, Pt, Pd$):
- **Alcenos $\to$ Alcanos:**
  $$\text{H}_2\text{C}=\text{CH}_2 + \text{H}_2 \xrightarrow{\quad\text{Ni / }\Delta\quad} \text{H}_3\text{C}-\text{CH}_3$$
- **Aplicação Industrial:** Fabricação de margarinas a partir da hidrogenação parcial de óleos vegetais insaturados.

#### B. Halogenação de Alcenos
Adição de halogênios moleculares ($Cl_2$ ou $Br_2$) dissolvidos em solvente inerte ($CCl_4$):
- Ocorre sem necessidade de catalisador através do intermediário íon halônio cíclico.
- **Teste de Bromo no Laboratório:** Uma solução de bromo em tetracloreto de carbono ($Br_2 / CCl_4$) possui coloração castanha avermelhada intensa. Ao ser gotejada em um alceno ou alcino, a cor castanha desaparece instantaneamente pela formação de um di-haleto vicinal incolor. É o teste confirmatório padrão de insaturação em amostras desconhecidas.

#### C. Hidro-halogenação e a Regra de Markovnikov
Adição de haletos de hidrogênio ($HCl, HBr, HI$) a alcenos:
- Quando o alceno é **assimétrico** (como o propeno), surge a possibilidade de formação de dois produtos isoméricos distintos. A reação é governada pela **Regra de Vladimir Markovnikov (1869)**:

> **REGRA DE MARKOVNIKOV:**  
> *"Na adição de haletos de hidrogênio ($H-X$) a alcenos assimétricos, o hidrogênio do reagente liga-se preferencialmente ao átomo de carbono mais hidrogenado da ligação dupla."*

```
          ADIÇÃO DE HBr AO PROPENO SEGUNDO MARKOVNIKOV:
          
               HBr  +  H₂C ════ CH ── CH₃
                       (Mais)  (Menos)
                      Hidrogenado
                          │
                          ▼
               H₃C ── CH(Br) ── CH₃   (2-Bromopropano / > 90% Produto Principal)
               H₂C(Br) ── CH₂ ── CH₃  (1-Bromopropano / < 10% Produto Marginal)
```

- **Mecanismo e Fundamento Quântico:** O próton $H^+$ ataca a ligação $\pi$. A adição do $H^+$ ao carbono terminal gera um **carbocátion secundário** [$CH_3-CH^+-CH_3$], estabilizado pelo efeito indutivo doador ($+I$) e hiperconjugação de dois grupos metila vizinhos. Se o hidrogênio se ligasse ao carbono central, formaria um carbocátion primário [$CH_3-CH_2-CH_2^+$], termodinamicamente muito menos estável:

$$\text{Estabilidade de Carbocátions: } \mathbf{\text{Terciário } (3^\circ)} > \mathbf{\text{Secundário } (2^\circ)} > \mathbf{\text{Primário } (1^\circ)} > \text{Metila } (CH_3^+)$$

#### D. O Efeito Kharasch (Adição Anti-Markovnikov)
Descoberto por Morris Kharasch em 1933. Quando a adição de **$HBr$** (exclusivamente com $HBr$!) é conduzida na presença de **peróxidos orgânicos** ($R-O-O-R$) sob aquecimento ou luz, o mecanismo deixa de ser iônico e torna-se **radicalar em cadeia**:
- O radical de bromo ($\cdot Br$) ataca primeiro o carbono mais hidrogenado da dupla, gerando o radical livre secundário mais estável. Em seguida, o carbono captura o hidrogênio.
- **Resultado:** Ocorre a inversão estrita da orientação:

$$\text{H}_2\text{C}=\text{CH}-\text{CH}_3 + \text{HBr} \xrightarrow{\quad\text{Peróxido}\quad} \text{H}_2\text{C}(\text{Br})-\text{CH}_2-\text{CH}_3\ (\mathbf{1-\text{Bromopropano / Anti-Markovnikov}})$$

#### E. Hidratação Ácida de Alcenos
Adição de água ($H-OH$) catalisada por ácido sulfúrico diluído ($H_2SO_4$):
- Obedece à Regra de Markovnikov: o hidrogênio ($H^+$) liga-se ao carbono mais hidrogenado e a hidroxila ($-OH$) liga-se ao carbono menos hidrogenado, sintetizando **álcoois**:

$$\text{H}_2\text{C}=\text{CH}-\text{CH}_3 + \text{H}_2\text{O} \xrightarrow{\quad\text{H}^+\quad} \text{H}_3\text{C}-\text{CH}(\text{OH})-\text{CH}_3\ (\mathbf{\text{Propan-2-ol / Álcool Secundário}})$$

---

### 2.2. Reações de Substituição

Consistem na substituição de um átomo ou grupo de átomos da molécula orgânica por outro grupo químico, mantendo intacto o grau de saturação do esqueleto carbônico.

#### A. Halogenação Radicalar de Alcanos
Ocorre por mecanismo de radicais livres na presença de luz ultravioleta ($h\nu$) ou calor intenso ($250-400\ ^\circ C$):
- Facilidade de substituição dos átomos de hidrogênio (regida pela estabilidade do radical formado):

$$\mathbf{\text{Hidrogênio Terciário } (3^\circ)} > \mathbf{\text{Hidrogênio Secundário } (2^\circ)} > \mathbf{\text{Hidrogênio Primário } (1^\circ)}$$

- Na cloração do metilpropano, o 2-cloro-2-metilpropano é o produto predominante em relação ao 1-cloro-2-metilpropano.

#### B. Substituição Eletrofílica Aromática (SEA) no Benzeno
Devido à extraordinária estabilidade de ressonância ($150\text{ kJ/mol}$), o anel benzênico **não sofre adição**, reagindo preferencialmente por **substituição eletrofílica**, na qual um hidrogênio do anel é substituído por um eletrófilo, restaurando a aromaticidade:

1. **Halogenação Aromática:** Reação com $Cl_2$ ou $Br_2$ catalisada por ácido de Lewis ($FeCl_3, AlCl_3$):
   $$\text{C}_6\text{H}_6 + \text{Cl}_2 \xrightarrow{\quad\text{FeCl}_3\quad} \text{C}_6\text{H}_5\text{Cl}\ (\text{Clorobenzeno}) + \text{HCl}$$
2. **Nitração Aromática:** Reação com mistura sulfonítrica concentrada ($HNO_3 + H_2SO_4$). O ácido sulfúrico protona o ácido nítrico, gerando o poderoso eletrófilo **íon nitrônio ($NO_2^+$)**:
   $$\text{C}_6\text{H}_6 + \text{HNO}_3 \xrightarrow{\quad\text{H}_2\text{SO}_4\quad} \text{C}_6\text{H}_5\text{NO}_2\ (\text{Nitrobenzeno}) + \text{H}_2\text{O}$$
3. **Sulfonação Aromática:** Reação com ácido sulfúrico fumegante contendo trióxido de enxofre ($H_2SO_4 / SO_3$):
   $$\text{C}_6\text{H}_6 + \text{SO}_3 \xrightarrow{\quad\text{H}_2\text{SO}_4\quad} \text{C}_6\text{H}_5\text{SO}_3\text{H}\ (\text{Ácido Benzenossulfônico})$$
4. **Alquilação de Friedel-Crafts:** Introdução de radical alquila via haleto de alquila com $AlCl_3$:
   $$\text{C}_6\text{H}_6 + \text{CH}_3\text{Cl} \xrightarrow{\quad\text{AlCl}_3\quad} \text{C}_6\text{H}_5\text{CH}_3\ (\text{Tolueno}) + \text{HCl}$$
5. **Acilação de Friedel-Crafts:** Introdução de grupo acila via cloreto de acila com $AlCl_3$:
   $$\text{C}_6\text{H}_6 + \text{CH}_3\text{COCl} \xrightarrow{\quad\text{AlCl}_3\quad} \text{C}_6\text{H}_5\text{COCH}_3\ (\text{Acetofenona}) + \text{HCl}$$

#### C. Regras de Orientação no Anel Benzênico Substituído
Quando o anel benzênico já possui um substituinte prévio (anel monossustituído), esse grupo orienta a posição em que o segundo eletrófilo se ligará:

```
                  REGRAS DE ORIENTAÇÃO AROMÁTICA
                                 │
         ┌───────────────────────┴───────────────────────┐
         ▼                                               ▼
  GRUPOS ATIVANTES (ORTO / PARA-DIRIGENTES)       GRUPOS DESATIVANTES (META-DIRIGENTES)
  • Doam elétrons para o anel (ressonância/indução) • Retiram elétrons do anel (indução/ressonância)
  • Aumentam a densidade eletrônica em orto/para  • Diminuem a densidade do anel (especialmente o/p)
  • Aceleram a velocidade de reação               • Desaceleram a reação (menos reativos que benzeno)
  • Exemplos: ─OH, ─NH₂, ─OCH₃, ─CH₃, alquilas    • Exemplos: ─NO₂, ─COOH, ─SO₃H, ─CHO, ─CN
  
  [EXCEÇÃO HALOGÊNIOS: ─Cl, ─Br, ─I são DESATIVANTES FRACOS, mas orientam em ORTO / PARA!]
```

- **Exemplo Prático:** A nitração do tolueno (que tem a metila $+I$ ativante) gera a mistura de **$o$-nitrotolueno** e **$p$-nitrotolueno**. Já a nitração do nitrobenzeno (que tem o grupo $-NO_2$ desativante) gera exclusivamente o **$m$-dinitrobenzeno**.

#### D. Substituição Nucleofílica em Haletos de Alquila ($S_N1$ vs. $S_N2$)
Reação fundamental na qual um nucleófilo ($Nu^-$) substitui o átomo de halogênio (grupo abandonador):

```
       MECANISMO SN1 (Unimolecular)           vs.       MECANISMO SN2 (Bimolecular)
       
  • Ocorre em DUAS ETAPAS.                             • Ocorre em ETAPA ÚNICA CONCERTADA.
  • 1ª Etapa (Lenta): Saída do halogênio               • Ataque do nucleófilo por trás
    formando um CARBOCÁTION PLANAR (sp²).                simultâneo à saída do halogênio.
  • 2ª Etapa (Rápida): Ataque do nucleófilo.           • Estado de transição pentacoordenado.
  • Cinética de 1ª Ordem: v = k [R-X]                  • Cinética de 2ª Ordem: v = k [R-X] [Nu⁻]
  • Estereoquímica: RACEMIZAÇÃO parcial                • Estereoquímica: INVERSÃO DE WALDEN
    (ataque por cima ou por baixo do plano).             (inversão 3D como guarda-chuva ao vento).
  • Favorecido por: Haletos Terciários (3°)            • Favorecido por: Haletos Primários (1°)
    e solventes polares próticos (H₂O, álcool).          e solventes polares apróticos (acetona, DMSO).
```

---

### 2.3. Reações de Eliminação

Processos inversos às reações de adição: dois átomos ou grupos são retirados de carbonos vizinhos sem substituição, gerando uma nova ligação múltipla ($\pi$) ou anel.

#### A. Desidratação de Álcoois e a Regra de Saytzeff
Aquecimento de álcoois na presença de catalisador desidratante concentrado ($H_2SO_4$):
1. **Desidratação Intramolecular (Aquecimento Enérgico a $\approx 170\ ^\circ C$):** Ocorre dentro da própria molécula de álcool, com eliminação de uma molécula de água e **formação de um alceno**.
   - Quando o álcool é assimétrico, a eliminação obedece à **Regra de Alexander Saytzeff (Zaitsev - 1875)**:

> **REGRA DE SAYTZEFF (ZAITSEV):**  
> *"Na desidratação intramolecular de álcoois, o hidrogênio é eliminado preferencialmente do átomo de carbono vizinho que for MENOS HIDROGENADO (mais substituído), formando o alceno termodinamicamente mais estável."*

```
       DESIDRATAÇÃO INTRAMOLECULAR DO BUTAN-2-OL:
       
                 H    OH   H
                 │    │    │
       H₃C ──── CH ─ CH ─ CH ──── H    ───►  H₃C ── CH ═ CH ── CH₃  (But-2-eno / 80% Saytzeff)
                (C₃)  (C₂) (C₁)
               (Menos)    (Mais)        ───►  H₃C ── CH₂ ── CH ═ CH₂ (But-1-eno / 20%)
              Hidrogenado Hidrogenado
```

2. **Desidratação Intermolecular (Aquecimento Moderado a $\approx 140\ ^\circ C$):** Ocorre entre duas moléculas distintas de álcool, com eliminação de uma molécula de água entre elas e **formação de um éter**:

$$2\ \text{CH}_3\text{CH}_2\text{OH} \xrightarrow{\quad\text{H}_2\text{SO}_4\ /\ 140\ ^\circ C\quad} \text{CH}_3\text{CH}_2-\text{O}-\text{CH}_2\text{CH}_3\ (\text{Éter Dietílico}) + \text{H}_2\text{O}$$

---

### 2.4. Reações de Oxidação e Redução

#### A. Oxidação de Alcenos
1. **Oxidação Branda (Reagente de Baeyer):** Solução aquosa diluída de permanganato de potássio ($KMnO_4$) em meio neutro ou fracamente básico a frio. Rompe apenas a ligação $\pi$, inserindo duas hidroxilas e gerando um **diol vicinal (glicol)**:
   $$\text{H}_2\text{C}=\text{CH}_2 + [\text{O}] + \text{H}_2\text{O} \xrightarrow{\quad\text{KMnO}_4\ /\ \text{frio}\quad} \text{CH}_2(\text{OH})-\text{CH}_2(\text{OH})\ (\text{Etano-1,2-diol})$$
2. **Oxidação Enérgica:** Solução de $KMnO_4$ ou $K_2Cr_2O_7$ concentrada em **meio ácido ($H_2SO_4$) e a quente ($\Delta$)**. Provoca a **clivagem total e quebra da dupla ligação**, oxidando intensamente os fragmentos:
   - Carbono terminal da dupla ($=CH_2$) $\longrightarrow \mathbf{CO_2\uparrow + H_2O}$
   - Carbono monossubstituído ($=CH-R$) $\longrightarrow \mathbf{R-COOH}$ (Ácido Carboxílico)
   - Carbono dissubstituído [$=C(R_1)(R_2)$] $\longrightarrow \mathbf{R_1-CO-R_2}$ (Cetona)

```
       EXEMPLO DE OXIDAÇÃO ENÉRGICA DO 2-METILBUT-2-ENO:
       
             CH₃
              │
       H₃C ── C ════ CH ── CH₃   +  3 [O]  ───►  H₃C ── C ═ O   +   HO ── C ═ O
                                                        │                 │
                                                       CH₃               CH₃
       (Carbono Dissubstituído) (Carbono Monossubstituído)  (Acetona)     (Ácido Acético)
```

3. **Ozonólise de Alcenos:** Tratamento com gás ozônio ($O_3$) seguido de hidrólise em presença de **pó de zinco ($Zn / H_2O$)**. O zinco sequestra o peróxido de hidrogênio gerado ($Zn + H_2O_2 \to ZnO + H_2O$), impedindo a oxidação posterior dos aldeídos:
   - Carbonos com hidrogênio ($=CH_2$ ou $=CH-R$) convertem-se em **Aldeídos**.
   - Carbonos dissubstituídos convertem-se em **Cetonas**.

#### B. Oxidação de Álcoois e o Teste do Bafômetro
- **Álcool Primário:** Oxida em duas etapas sucessivas:
  $$\text{R}-\text{CH}_2\text{OH}\ (\text{Álcool 1°}) \xrightarrow{\quad[\text{O}]\quad} \text{R}-\text{CHO}\ (\text{Aldeído}) \xrightarrow{\quad[\text{O}]\quad} \text{R}-\text{COOH}\ (\text{Ácido Carboxílico})$$
- **Álcool Secundário:** Oxida gerando **Cetona** (que resiste a oxidações posteriores sem quebra de cadeia):
  $$\text{R}-\text{CH}(\text{OH})-\text{R}'\ (\text{Álcool 2°}) \xrightarrow{\quad[\text{O}]\quad} \text{R}-\text{CO}-\text{R}'\ (\text{Cetona})$$
- **Álcool Terciário:** **NÃO OXIDA** sob condições habituais, pois o carbono portador da hidroxila não possui nenhum átomo de hidrogênio ligado a ele para ser removido na oxidação.
- **O Teste do Bafômetro Clássico:** O ar alveolar exalado por motoristas embriagados contém vapores de etanol, que reagem com uma mistura ácida de dicromato de potássio ($K_2Cr_2O_7$) impregnada em sílica gel. O íon dicromato alaranjado ($Cr_2O_7^{2-}$, $Nox\ Cr = +6$) é reduzido a sulfato de cromo III ($Cr^{3+}$, $Nox\ Cr = +3$), de **coloração verde**:

$$\text{3 CH}_3\text{CH}_2\text{OH} + \mathbf{2 K_2Cr_2O_7\ (\text{Alaranjado})} + \text{8 H}_2\text{SO}_4 \longrightarrow \text{3 CH}_3\text{COOH} + \mathbf{2 Cr_2(SO_4)_3\ (\text{Verde})} + \text{2 K}_2\text{SO}_4 + \text{11 H}_2\text{O}$$

---

### 2.5. Esterificação, Saponificação e a Síntese do Biodiesel

#### A. Esterificação de Fischer
Reação em equilíbrio químico dinâmico entre um ácido carboxílico e um álcool sob catálise ácida ($H_2SO_4$):

$$\text{R}-\text{COOH} + \text{R}'-\text{OH} \ \underset{\text{Hidrólise}}{\overset{\text{Esterificação}}{\rightleftharpoons}} \ \text{R}-\text{COO}-\text{R}'\ (\text{Éster}) + \text{H}_2\text{O}$$

#### B. Saponificação (Hidrólise Alcalina de Triglicerídeos)
Triglicerídeos (triacilgliceróis) constituintes de óleos vegetais e gorduras animais são triésteres formados pela esterificação do glicerol (propanotriol) com três moléculas de ácidos graxos superiores. 

Ao serem aquecidos com solução concentrada de base forte ($NaOH$ ou $KOH$), sofrem hidrólise básica irreversível, gerando **glicerol** e **sabão** (mistura de sais de sódio de ácidos graxos, como estearato de sódio, $C_{17}H_{35}COO^- Na^+$):

$$\text{Triglicerídeo} + 3\ \text{NaOH} \xrightarrow{\quad\Delta\quad} \mathbf{\text{Glicerol / Glicerina}} + \mathbf{3\ \text{Sabões}\ (\text{R}-\text{COO}^-\text{Na}^+)}$$

```
                        AÇÃO TENSOATIVA E FORMAÇÃO DE MICELAS
                        
        Molécula do Sabão:
           CH₃─CH₂─CH₂─CH₂─CH₂─CH₂─CH₂─CH₂─CH₂─CH₂─CH₂─CH₂─CH₂─CH₂─CH₂ ── COO⁻ Na⁺
           │◄────────────────── Cauda Apolar Lipofílica ──────────────►│  │◄─ Cabeça ─►│
                               (Interage com Gordura)                        Hidrofílica
                                                                           (Interage com H₂O)
        
        Em água, o sabão forma MICELAS ESFÉRICAS:
        • As caudas apolares voltam-se para o CENTRO, dissolvendo a gotícula de gordura.
        • As cabeças polares ficam na SUPERFÍCIE externa, em contato solúvel com a água.
```

- **Água Dura e o Sabão:** Águas ricas em cátions cálcio ($Ca^{2+}$) e magnésio ($Mg^{2+}$) reagem com o sabão formando precipitados insolúveis de carboxilato de cálcio [$(R-COO)_2Ca\downarrow$], cortando a espuma e anulando o poder de limpeza do sabão. Os **detergentes sintéticos à base de sulfonato ($R-SO_3^- Na^+$)** não sofrem esse problema, pois seus sais de cálcio são solúveis em água.
- **Biodegradabilidade:** Detergentes com cadeias carbônicas **lineares** são facilmente digeridos por bactérias do esgoto (**biodegradáveis**). Detergentes com cadeias **ramificadas** resistem à degradação biológica, acumulando-se nos rios e gerando gigantescas espumas tóxicas que bloqueiam a oxigenação hídrica.

#### C. Transesterificação e Produção Sustentável de Biodiesel
O óleo vegetal cru não pode ser injetado diretamente em motores a diesel comuns devido à sua altíssima viscosidade cinemática, que entope bicos injetores e gera queima incompleta com depósitos carbonosos.

O **Biodiesel** é produzido pela reação de **Transesterificação**, na qual o triglicerídeo reage com um álcool de cadeia curta (**metanol** ou **etanol**) na presença de um catalisador alcalino homogêneo ($NaOH$ ou $KOH$ anidro a $\approx 60\ ^\circ C$):

$$\text{Triglicerídeo (Óleo/Gordura)} + 3\ \text{CH}_3\text{OH}\ (\text{Metanol}) \xrightarrow{\quad\text{Cat. KOH}\quad} \mathbf{3\ \text{Ésteres Metílicos (Biodiesel)}} + \mathbf{\text{Glicerol}}$$

```
               A EQUAÇÃO MOLECULAR DA TRANSESTERIFICAÇÃO:
               
         H₂C ── O ── CO ── R₁                       H₂C ── OH
         │                                          │
         HC  ── O ── CO ── R₂  +  3 CH₃OH  ───►     HC  ── OH  +  R₁─COO─CH₃  (Biodiesel)
         │                                          │             R₂─COO─CH₃  (Biodiesel)
         H₂C ── O ── CO ── R₃                       H₂C ── OH     R₃─COO─CH₃  (Biodiesel)
            (Triglicerídeo)       (Metanol)         (Glicerol)
```

- **Vantagens Socioambientais do Biodiesel:**
  1. Combustível renovável com balanço de carbono neutro (o $CO_2$ liberado na queima foi previamente absorvido pelas lavouras de soja, palma ou mamona via fotossíntese).
  2. É virtualmente **isento de enxofre**, reduzindo drasticamente a formação de dióxido de enxofre ($SO_2$) e a ocorrência de chuva ácida.
  3. Gera **glicerol** como subproduto de alto valor agregado para as indústrias farmacêutica e cosmética.

---

## 3. Polímeros Sintéticos e Meio Ambiente

Um **polímero** (do grego *poly* = muitos; *meros* = partes) é uma macromolécula de altíssima massa molar ($10^4$ a $10^7\ g/mol$), formada pela união covalente repetitiva de milhares de unidades moleculares fundamentais chamadas **monômeros**. A menor unidade estrutural que se repete ao longo da cadeia polimérica é denominada **mero**.

---

### 3.1. Polímeros de Adição
Formam-se pela abertura sucessiva das ligações $\pi$ de monômeros vinílicos insaturados ($C=C$), **sem eliminação de qualquer subproduto molecular**:

$$n\ (\text{H}_2\text{C}=\text{CH}-\text{X}) \longrightarrow -\left[ -\text{CH}_2-\text{CH}(\text{X})- \right]_n-$$

| Polímero | Monômero de Origem | Unidade de Repetição (Mero) | Propriedades e Aplicações Principais |
| :--- | :--- | :--- | :--- |
| **Polietileno (PE)** | Eteno (Etileno, $H_2C=CH_2$) | $-[CH_2-CH_2]_n-$ | **PEBD:** Baixa densidade, flexível, ramificado (sacolas plásticas, filmes). <br>**PEAD:** Alta densidade, linear, rígido (frascos, engradados, tubulações). |
| **Polipropileno (PP)** | Propeno ($H_2C=CH-CH_3$) | $-[CH_2-CH(CH_3)]_n-$ | Resistência à fadiga por flexão contínua, alto ponto de fusão ($160\ ^\circ C$); usado em seringas autoclaváveis, para-choques e cadeiras. |
| **Policloreto de Vinila (PVC)** | Cloroeteno ($H_2C=CH-Cl$) | $-[CH_2-CH(Cl)]_n-$ | Rígido, resistente à umidade e autoextinguível ao fogo; usado em tubos e conexões hidráulicas, conduítes e pisos vinílicos. |
| **Poliestireno (PS)** | Vinilbenzeno (Estireno, $H_2C=CH-C_6H_5$) | $-[CH_2-CH(C_6H_5)]_n-$ | Transparente, quebradiço (copos descartáveis). Quando expandido com gases, forma o **Isopor (EPS)**, excelente isolante térmico. |
| **Politetrafluoretileno (PTFE / Teflon)** | Tetrafluoreteno ($F_2C=CF_2$) | $-[CF_2-CF_2]_n-$ | Inércia química quase absoluta, coeficiente de atrito baixíssimo, não inflamável; antiaderente em panelas e fitas de vedação. |
| **Borracha Sintética (Buna-S)** | Buta-1,3-dieno + Estireno | Copolímero de Adição | Alta resistência à abrasão mecânica; usada na banda de rodagem de pneus de automóveis. |

#### A Vulcanização da Borracha (Charles Goodyear, 1839)
A borracha natural pura (poli-isopreno) amolece e torna-se pegajosa no verão e quebradiça no inverno. A **vulcanização** consiste no aquecimento da borracha com **enxofre elementar ($S_8$)**, que quebra parte das ligações duplas e estabelece **pontes cruzadas dissulfeto ($-S-S-$)** covalentes entre as cadeias vizinhas. O elastômero adquire estabilidade térmica e extraordinária memória elástica.

---

### 3.2. Polímeros de Condensação
Formam-se pela reação química entre dois monômeros polifuncionais (ou um monômero bifuncional), com **eliminação simultânea de moléculas pequenas (geralmente água, $H_2O$, ou cloreto de hidrogênio, $HCl$)**:

#### A. Poliésteres: PET (Politereftalato de Etileno / Dácron)
Obtido pela policondensação do **ácido tereftálico** (ácido benzeno-1,4-dicarboxílico) com o **etilenoglicol** (etano-1,2-diol):

$$n\ \text{HOOC}-\text{C}_6\text{H}_4-\text{COOH} + n\ \text{HO}-\text{CH}_2\text{CH}_2-\text{OH} \longrightarrow -\left[ -\text{CO}-\text{C}_6\text{H}_4-\text{COO}-\text{CH}_2\text{CH}_2-\text{O}- \right]_n- + 2n\ \text{H}_2\text{O}$$

- **Aplicações e Reciclagem:** Garrafas de refrigerantes e água mineral. Sua reciclagem mecânica produz fios e fibras têxteis poliéster para fabricação de tecidos e cobertores ecológicos.

#### B. Poliamidas: Nylon-6,6 e Kevlar
- **Nylon-6,6:** Formado pela reação entre o **ácido hexanodioico (ácido adípico)** e a **hexano-1,6-diamina**:
  $$n\ \text{HOOC}-(\text{CH}_2)_4-\text{COOH} + n\ \text{H}_2\text{N}-(\text{CH}_2)_6-\text{NH}_2 \longrightarrow -\left[ -\text{CO}-(\text{CH}_2)_4-\text{CONH}-(\text{CH}_2)_6-\text{NH}- \right]_n- + 2n\ \text{H}_2\text{O}$$
  Apresenta as mesmíssimas **ligações amídicas** encontradas nas proteínas. É ultrarresistente e tenaz (usado em meias de náilon, linhas de pesca, cerdas de escova de dentes e engrenagens mecânicas).
- **Kevlar:** Poliamida aromática formada por anéis benzênicos rígidos ligados por pontes de amida. Apresenta resistência à tração cinco vezes superior à do aço para o mesmo peso, sendo empregado em coletes à prova de balas e blindagens aeroespaciais.

#### C. Resinas Termofixas: Baquelite (Fenol-Formaldeído)
Primeiro polímero puramente sintético da história (Leo Baekeland, 1907). Obtido pela condensação de fenol com formaldeído em meio ácido ou básico, gerando uma densa rede tridimensional cruzada inflexível. É duro, insolúvel, isolante elétrico e termorrígido (usado em tomadas elétricas, cabos de panela e bolas de bilhar).

---

### 3.3. Classificação Térmica e Reciclagem de Polímeros

```
                   COMPORTAMENTO TÉRMICO DOS POLÍMEROS
                                    │
       ┌────────────────────────────┼────────────────────────────┐
       ▼                            ▼                            ▼
  TERMOPLÁSTICOS               TERMOFIXOS (TERMORRÍGIDOS)    ELASTÔMEROS (BORRACHAS)
  • Cadeias lineares/ramificadas• Densa rede tridimensional   • Cadeias enoveladas com
  • Interações intermoleculares   cruzada com ligações        poucas pontes de enxofre
    fracas                      covalentes                    • Apresentam altíssima
  • Amolecem e FUNDEM com calor• DEGRADAM antes de fundir     deformação elástica reversível
  • Podem ser REMOLDADOS       • NÃO FUNDEM com aquecimento  • Vulcanização confere
  • 100% RECICLÁVEIS mecanicamente• NÃO SÃO RECICLÁVEIS       memória mecânica
    (Ex.: PE, PP, PVC, PET, PS)  mecanicamente (Baquelite)     (Ex.: Pneus, látex natural)
```

#### O Flagelo Ambiental dos Microplásticos
- A durabilidade dos polímeros petroquímicos torna-os persistentes por séculos na biosfera. Sob ação da radiação solar ultravioleta e atrito mecânico das ondas marinhas, garrafas e redes de pesca fragmentam-se em partículas menores que $5\text{ mm}$ (**microplásticos**).
- Os microplásticos adsorvem pesticidas e poluentes orgânicos persistentes (POPs) do mar e são ingeridos pelo zooplâncton e peixes, bioacumulando-se ao longo da teia alimentar até alcançar o organismo humano.
- **Alternativa Sustentável:** O desenvolvimento de polímeros **biodegradáveis**, como o **Ácido Polilático (PLA)**, sintetizado a partir da fermentação do amido de milho por bactérias e degradado biologicamente em composteiras industriais em poucos meses.

---

## 4. Biomoléculas e Bioquímica Fundamental

A Química da Vida articula os princípios das funções orgânicas na arquitetura dos seres vivos.

---

### 4.1. Carboidratos (Glicídios ou Açúcares)
Definidos quimicamente como **poliidroxialdeídos** (aldoses) ou **poliidroxicetonas** (cetoses), ou substâncias que geram esses compostos por hidrólise:

```
               MONOSSACARÍDEOS CLÁSSICOS (C₆H₁₂O₆)
               
          D-Glicose (Aldohexose):            D-Frutose (Cetohexose):
               CHO                                CH₂OH
               │                                  │
          H ─ C ─ OH                         C ═ O
               │                                  │
         HO ─ C ─ H                         HO ─ C ─ H
               │                                  │
          H ─ C ─ OH                         H ─ C ─ OH
               │                                  │
          H ─ C ─ OH                         H ─ C ─ OH
               │                                  │
               CH₂OH                              CH₂OH
```

#### A. Dissacarídeos e a Ligação Glicosídica
Formam-se pela reação de condensação entre duas unidades monossacarídicas, com saída de uma molécula de água. A ponte de éter covalente formada entre os carbonos é denominada **ligação glicosídica**:
- **Sacarose (Açúcar de cana):** $\alpha$-D-Glicose $+ \beta$-D-Frutose (Ligação glicosídica $\alpha-1,2$).
- **Lactose (Açúcar do leite):** $\beta$-D-Galactose $+ \alpha$-D-Glicose (Ligação $\beta-1,4$). A carência da enzima intestinal **lactase** impede a hidrólise da ligação $\beta$, causando fermentação bacteriana com diarreia e gases (intolerância à lactose).
- **Maltose (Açúcar do malte):** $\alpha$-D-Glicose $+ \alpha$-D-Glicose (Ligação $\alpha-1,4$).

#### B. Polissacarídeos
Macromoléculas formadas pela condensação de centenas ou milhares de monômeros de glicose:
1. **Amido:** Polímero vegetal de reserva energética (formado por amilose linear e amilopectina ramificada com ligações $\alpha-1,4$). Facilmente digerido pela amilase salivar humana.
2. **Glicogênio:** Polímero animal de reserva rápida de glicose, armazenado no fígado e nos músculos esqueléticos. Apresenta estrutura altamente ramificada.
3. **Celulose:** Principal componente estrutural da parede celular vegetal. Formado por cadeias estritamente lineares unidas por **ligações $\beta-1,4$** estabilizadas por feixes maciços de pontes de hidrogênio. O organismo humano **não produz celulase**, sendo incapaz de hidrolisar a celulose (que atua na nossa dieta como fibras alimentares insolúveis).

---

### 4.2. Lipídios
Compostos biológicos caracterizados por sua **insolubilidade em água e alta solubilidade em solventes orgânicos apolares**:

1. **Óleos vs. Gorduras:** Ambos são triglicerídeos. Os óleos (vegetais) possuem predomínio de **ácidos graxos insaturados com dobras espaciais $cis$**, que impedem o empacotamento compacto e mantêm a substância líquida à temperatura ambiente. As gorduras (animais) possuem predomínio de **ácidos graxos saturados lineares**, que se empacotam densamente e formam sólidos.
2. **Ácidos Graxos Essenciais:** Ácido linolênico (**Ômega-3**, com dupla ligação no 3º carbono a partir da ponta metila) e ácido linoleico (**Ômega-6**), precursores de agentes anti-inflamatórios celulares.
3. **Fosfolipídios:** Moléculas anfipáticas formadas por glicerol ligado a dois ácidos graxos apolares (cauda hidrofóbica) e um grupo fosfato carregado com colina (cabeça polar hidrofílica). Em meio aquoso, auto-organizam-se espontaneamente na **bicamada lipídica fundamental da membrana celular**.

---

### 4.3. Aminoácidos e Proteínas

#### A. Estrutura Canônica de um $\alpha$-Aminoácido
Apresentam um átomo de carbono central ($\alpha$) ligado simultaneamente a quatro grupos distintos:
1. Um grupo **amino básico ($-NH_2$)**.
2. Um grupo **carboxila ácido ($-COOH$)**.
3. Um átomo de **hidrogênio ($-H$)**.
4. Uma **cadeia lateral variável ($-R$)**, que define a identidade dos 20 aminoácidos biológicos.

Com exceção da glicina (onde $-R = -H$), o carbono $\alpha$ de todos os outros 19 aminoácidos é **quiral**, existindo na natureza exclusivamente sob a forma do estereoisômero **L-aminoácido**.

```
                   O ÍON DIPOLAR (ZWITTERION)
                   
          Forma Neutra Não-Ionizada:             Forma Zwitterion (Meio Aquoso):
                    H                                        H
                    │                                        │
             H₂N ── C ── COOH                   H₃N⁺ ──── C ──── COO⁻
                    │                                        │
                    R                                        R
```

- **Caráter Anfótero:** O aminoácido comporta-se tanto como ácido quanto como base de Brønsted. Em meio aquoso neutro, o grupo carboxila ácido cede seu próton para o grupo amino básico intramolecularmente, gerando uma espécie eletricamente neutra dotada de cargas opostas simultâneas: o **Zwitterion** (íon dipolar).
- **Ponto Isoelétrico ($pI$):** O valor específico de $pH$ no qual a carga elétrica líquida total da molécula de aminoácido é rigorosamente zero.

#### B. A Ligação Peptídica
Consiste na união covalente entre o grupo carboxila de um aminoácido e o grupo amino do aminoácido vizinho, com **eliminação de uma molécula de água** (reação de condensação que forma uma função **amida**):

```
                   FORMAÇÃO DA LIGAÇÃO PEPTÍDICA
                   
         H           O           H           O
         │           ║           │           ║
    H₂N─ C ────── C ─ OH  +  H ─ N ─ C ────── C ─ OH
         │                       │   │
         R₁                      H   R₂
                     │
                     ▼  (Eliminação de H₂O)
         H           O       H   H           O
         │           ║       │   │           ║
    H₂N─ C ────── C ─────── N ─ C ────── C ─ OH
         │           ▲           │
         R₁   LIGAÇÃO PEPTÍDICA  R₂
                 (Amida Planar)
```

- **Rigidez Planar:** O par de elétrons do nitrogênio entra em ressonância com o oxigênio da carbonila, conferindo à ligação peptídica um **caráter parcial de ligação dupla ($\approx 40\%$)**, o que impede sua rotação livre e trava os seis átomos em um plano rígido.

#### C. Os Quatro Níveis de Conformação Proteica
1. **Estrutura Primária:** A sequência linear exata de aminoácidos unidos pelas ligações peptídicas covalentes ao longo da cadeia polipeptídica. É ditada pelo código genético.
2. **Estrutura Secundária:** O arranjo espacial local da cadeia principal polipeptídica, estabilizado exclusivamente por **ligações de hidrogênio** regulares entre os grupos $C=O$ e $N-H$ das ligações peptídicas:
   - **$\alpha$-Hélice:** Espiral helicoidal compacta (ex.: queratina do cabelo).
   - **Folha-$\beta$ Pregueada:** Lâminas paralelas ou antiparalelas distendidas (ex.: fibroína da seda).
3. **Estrutura Terciária:** O enovelamento tridimensional global nativo da cadeia proteica sobre si mesma, conferindo atividade biológica ativa (enzimas, anticorpos). Mantida por interações entre as cadeias laterais ($-R$):
   - Forças hidrofóbicas apolares (resíduos alifáticos no centro da proteína).
   - Pontes de hidrogênio e atrações eletrostáticas (pontes salinas).
   - **Pontes Dissulfeto ($-S-S-$):** Ligações covalentes fortes entre dois resíduos do aminoácido cisteína.
4. **Estrutura Quaternária:** A associação espacial coordenada de duas ou mais cadeias polipeptídicas individuais (subunidades) para formar o complexo funcional ativo. Exemplo: A **hemoglobina**, formada por quatro subunidades globulares associadas a um grupo heme com ferro ($Fe^{2+}$).

```
                      NÍVEIS DE ORGANIZAÇÃO PROTEICA
                      
    Primária:       ─[Ala]─[Gly]─[Val]─[Ser]─[Cys]─[Leu]─   (Sequência linear)
                           │
    Secundária:      ╭───╮   ╭───╮   ╭───╮   ╭───╮          (α-Hélice / Pontes H)
                     ╰───╯   ╰───╯   ╰───╯   ╰───╯
                           │
    Terciária:             ╭────────╮                       (Enovelamento 3D ativo:
                          ╭╯  (S-S) ╰╮                      Pontes dissulfeto,
                          ╰──────────╯                      Forças hidrofóbicas)
                           │
    Quaternária:         [ α₁ ] ── [ β₁ ]                   (Associação de
                         [ β₂ ] ── [ α₂ ]                   Múltiplas Subunidades)
```

#### D. Desnaturação Proteica
A **desnaturação** consiste na desorganização e perda irreversível da conformação espacial tridimensional nativa (estruturas secundária, terciária e quaternária) de uma proteína, provocada por agentes desestabilizadores:
- **Calor excessivo (temperatura elevada):** Agitação térmica que rompe as pontes de hidrogênio e atrações hidrofóbicas.
- **Variações extremas de pH:** Protonação ou desprotonação das cadeias laterais, rompendo as atrações iônicas.
- **Metais pesados ($Pb^{2+}, Hg^{2+}$) e solventes orgânicos (álcool 70°).**

> ⚠️ **IMPACTO CONCEITUAL INEGOCIÁVEL (ENEM & UFSC):**
> A desnaturação proteica **NÃO ROMPE AS LIGAÇÕES PEPTÍDICAS**! A **estrutura primária (a sequência de aminoácidos) permanece rigorosamente intacta**! Para romper ligações peptídicas, é necessária uma reação química de **hidrólise ácida, básica ou enzimática** (como na digestão gastrointestinal pela pepsina).

---

### 4.4. Ácidos Nucleicos (DNA e RNA)

São macromoléculas biológicas informacionais poliméricas, formadas pela condensação sequencial de **nucleotídeos**:

```
                       COMPOSIÇÃO DE UM NUCLEOTÍDEO
                       
                       [GRUPO FOSFATO] (PO₄³⁻)
                             │ (Ligação Fosfoéster)
                       [AÇÚCAR PENTOSE] ─── (Ligação N-Glicosídica) ─── [BASE NITROGENADA]
                       • Desoxirribose (DNA)                             • Púricas: A, G
                       • Ribose (RNA)                                    • Pirimídicas: C, T (DNA), U (RNA)
```

#### A. A Ligação Fosfodiéster
Os nucleotídeos unem-se covalentemente através de uma **ligação fosfodiéster**: o grupo fosfato ligado ao carbono $5'$ da pentose de um nucleotídeo reage com a hidroxila do carbono $3'$ da pentose do nucleotídeo seguinte, estabelecendo o esqueleto açúcar-fosfato na direção polarizada orientada **$5' \longrightarrow 3'$**.

#### B. A Dupla Hélice do DNA e o Pareamento de Bases por Pontes de Hidrogênio
A estrutura tridimensional da dupla hélice do DNA (descoberta por James Watson, Francis Crick e Rosalind Franklin em 1953) é mantida pela interação eletrostática específica de **ligações de hidrogênio** entre as bases nitrogenadas complementares das duas fitas antiparalelas:

- **Adenina pareia exclusivamente com Timina ($A = T$)** através de **duas ligações de hidrogênio**:
  $$\text{Adenina} \ \bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet \ \text{Timina} \quad (\mathbf{2\ \text{Pontes de Hidrogênio}})$$
- **Guanina pareia exclusivamente com Citosina ($C \equiv G$)** através de **três ligações de hidrogênio**:
  $$\text{Guanina} \ \bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet\bullet \ \text{Citosina} \quad (\mathbf{3\ \text{Pontes de Hidrogênio}})$$

> 🔬 **ALERTA UFSC — ESTABILIDADE DA DUPLA HÉLICE:**
> O par Guanina-Citosina ($C\equiv G$) é muito mais resistente à desnaturação térmica (possui maior temperatura de desnaturação / *melting temperature* $T_m$) do que o par Adenina-Timina ($A=T$), porque o pareamento $C\equiv G$ envolve **três ligações de hidrogênio**, contra apenas duas do par $A=T$!

---

## 5. Síntese Didática e Boxes Avaliativos

### ⚠️ ALERTA ENEM: Biocombustíveis, Reciclagem e Sustentabilidade
- **Transesterificação do Biodiesel:** É um dos temas de maior incidência histórica no ENEM. Lembre-se de que o reagente é um **triglicerídeo** (óleo de fritura ou óleo vegetal novo), que reage com **etanol ou metanol** gerando **biodiesel (éster monoetílico ou monometílico)** e **glicerol** como subproduto. O sabão só é formado se houver água em excesso ou se for hidrólise alcalina pura.
- **Reciclagem de Plásticos:** O ENEM exige saber que plásticos termoplásticos (PET, PE, PP, PVC) podem ser fundidos e reciclados mecanicamente, enquanto os termofixos (baquelite) não fundem e sofrem pirólise/carbonização ao calor.
- **Ação do Álcool 70°:** Mata bactérias e desativa vírus envelopados (como o coronavírus SARS-CoV-2) por dois mecanismos complementares: a água facilita a penetração do álcool através da membrana e o etanol **desnatura as proteínas vitais** e dissolve a bicamada lipídica externa.

### 🔬 ALERTA UFSC: Previsão de Produtos Reacionais e Somatórias
- **Markovnikov e Saytzeff na Mesma Questão:** Em provas da COPERVE, preste atenção aos comandos: "Adição de $HCl$ ao 2-metilbut-2-eno" $\to$ Markovnikov; "Desidratação de álcool a $170\ ^\circ C$" $\to$ Saytzeff (o hidrogênio sai do carbono menos hidrogenado!).
- **Oxidação Enérgica:** Lembre-se sempre de conferir se a dupla tem hidrogênios: se o carbono for $=CH_2$, o produto é **$CO_2 + H_2O$** (e não ácido!); se tiver 1 hidrogênio, é **ácido carboxílico**; se for dissubstituído sem hidrogênio, o produto é **cetona**.
- **Equações de Condensação:** A formação de PET e Nylon-6,6 libera água como subproduto em proporção estequiométrica ($2n\ H_2O$). Proposições que afirmem que são polímeros de adição sem eliminação de moléculas são **FALSAS**!
