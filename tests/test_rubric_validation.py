#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_rubric_validation.py - Suíte de Validação de Rubricas Pedagógicas e Critérios de Aceitação
Projeto: Plano Completo de Estudos e Guia de Aprendizagem de Química
Público: ENEM e Vestibulares Federais (com foco na UFSC)

Verifica conformidade com todos os Critérios de Aceitação de ORIGINAL_REQUEST.md e PROJECT.md:
1. Transição pedagógica do "zero absoluto" ao avançado (átomo, prótons, nêutrons, elétrons, tabela periódica).
2. Obras didáticas clássicas com títulos e autores (Feltre, Martha Reis, Usberco, Tito & Canto, Brown, Atkins, Russell).
3. Recursos digitais abertos e gratuitos (canais YouTube, 9 simulações interativas PhET, MolView, ChemTube3D).
4. Resolução comentada passo a passo para cada bloco de exercícios curriculares.
5. Roteiro tático ENEM (TRI 3PL) e UFSC (mecânica somatória oficial COPERVE, barreira NPC > NPI, abertas 00-99).
6. Metacognição e métricas de revisão de erros (Caderno de Erros com as 5 causas-raiz e reteste em 48h).
"""

import os
import re
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(r"C:\Users\guistumpf\teamwork_projects\quimica_estudos")


class TestRubricValidation(unittest.TestCase):
    """Validação forense dos critérios pedagógicos, metodológicos e táticos."""

    @classmethod
    def setUpClass(cls):
        cls.root = PROJECT_ROOT
        cls.is_strict = os.environ.get("STRICT_E2E", "0") == "1" or "--strict" in sys.argv

    def _read_file_if_exists(self, rel_path, rubric_name):
        """Lê o arquivo se existir; se não existir, pula o teste no modo progressivo ou falha no estrito."""
        full_path = self.root / rel_path
        if not full_path.exists():
            if self.is_strict:
                self.fail(f"Modo Estrito: Arquivo necessário para a rubrica '{rubric_name}' ausente: {rel_path}")
            else:
                self.skipTest(f"Arquivo '{rel_path}' ainda não implementado (Progressive Testability).")
        return full_path.read_text(encoding="utf-8")

    # -------------------------------------------------------------------------
    # RUBRICA 1: TRANSIÇÃO DO ZERO ABSOLUTO AO AVANÇADO
    # -------------------------------------------------------------------------

    def test_rubric_zero_absolute_foundations(self):
        """Valida que o Stage 0 define rigorosamente átomo, prótons, nêutrons, elétrons, Z, A e tabela periódica."""
        text_atomo = self._read_file_if_exists(
            "00_fundamentos/02_atomo_particulas_subatomicas.md",
            "Fundamentos do Átomo e Partículas Subatômicas",
        )
        text_tabela = self._read_file_if_exists(
            "00_fundamentos/03_isotoppia_e_tabela_introdutoria.md",
            "Isotopia e Introdução à Tabela Periódica",
        )

        # 1. Partículas subatômicas fundamentais com cargas e massas relativas
        self.assertRegex(text_atomo, r"(?i)pr[óo]ton", "Menção obrigatória a próton ausente.")
        self.assertRegex(text_atomo, r"(?i)n[êe]utron", "Menção obrigatória a nêutron ausente.")
        self.assertRegex(text_atomo, r"(?i)el[ée]tron", "Menção obrigatória a elétron ausente.")
        self.assertRegex(text_atomo, r"(?i)n[úu]cleo", "Menção à estrutura do núcleo atômico ausente.")
        self.assertRegex(text_atomo, r"(?i)eletrosfera", "Menção à eletrosfera ausente.")

        # 2. Grandezas fundamentais Z e A
        self.assertRegex(text_atomo, r"(?i)n[úu]mero\s+at[ôo]mico\s*(\([Zz]\))?", "Conceito de Número Atômico (Z) ausente.")
        self.assertRegex(text_atomo, r"(?i)n[úu]mero\s+de\s+massa\s*(\([Aa]\))?", "Conceito de Número de Massa (A) ausente.")
        self.assertRegex(text_atomo, r"(?i)[Cc][áa]tions?|[Ââ]nions?", "Diferenciação de cátions e ânions ausente.")

        # 3. Semelhanças atômicas e introdução à tabela periódica
        self.assertRegex(text_tabela, r"(?i)is[óo]topos?", "Definição de Isótopos ausente.")
        self.assertRegex(text_tabela, r"(?i)is[óo]baros?", "Definição de Isóbaros ausente.")
        self.assertRegex(text_tabela, r"(?i)is[óo]tonos?", "Definição de Isótonos ausente.")
        self.assertRegex(text_tabela, r"(?i)per[íi]odos?", "Estrutura de períodos na tabela periódica ausente.")
        self.assertRegex(text_tabela, r"(?i)fam[íi]lias?|grupos?", "Estrutura de famílias/grupos ausente.")
        self.assertRegex(text_tabela, r"(?i)metais|ametais|n[ãa]o-metais", "Classificação em metais/não-metais ausente.")

    # -------------------------------------------------------------------------
    # RUBRICA 2: BIBLIOGRAFIA CLÁSSICA E TRATADOS UNIVERSITÁRIOS
    # -------------------------------------------------------------------------

    def test_rubric_classic_textbooks_and_authors(self):
        """Valida que o guia bibliográfico detalha Feltre, Martha Reis, Usberco, Tito & Canto e obras de consulta."""
        bib_text = self._read_file_if_exists(
            "04_recursos_e_metodologia/bibliografia_livros_didaticos.md",
            "Bibliografia e Livros Didáticos",
        )

        # 1. Quatro coleções consagradas brasileiras
        self.assertRegex(bib_text, r"(?i)Ricardo\s+Feltre|Feltre", "Referência à coleção de Ricardo Feltre ausente.")
        self.assertRegex(bib_text, r"(?i)Martha\s+Reis", "Referência à coleção de Martha Reis ausente.")
        self.assertRegex(bib_text, r"(?i)Usberco(\s+e\s+Salvador)?", "Referência à coleção de Usberco e Salvador ausente.")
        self.assertRegex(bib_text, r"(?i)Tito\s+e\s+Canto|Peruzzo\s+e\s+Canto", "Referência à coleção de Tito e Canto ausente.")

        # 2. Obras universitárias de consulta de alto nível
        self.assertRegex(bib_text, r"(?i)Brown.*(LeMay|Bursten)|Qu[íi]mica:\s*A\s*Ci[êe]ncia\s*Central", "Referência a Brown ausente.")
        self.assertRegex(bib_text, r"(?i)Atkins|Princ[íi]pios\s+de\s+Qu[íi]mica", "Referência a Atkins ausente.")
        self.assertRegex(bib_text, r"(?i)Russell|Qu[íi]mica\s+Geral", "Referência a John B. Russell ausente.")

        # 3. Roteiro tático de leitura para o autodidata
        self.assertRegex(
            bib_text,
            r"(?i)roteiro|guia|trilha|quando\s+usar|ordem\s+de\s+leitura|manual\s+de\s+navega[çc][ãa]o",
            "Roteiro tático de como e quando o autodidata deve usar cada livro ausente.",
        )

    # -------------------------------------------------------------------------
    # RUBRICA 3: RECURSOS DIGITAIS GRATUITOS E SIMULADORES
    # -------------------------------------------------------------------------

    def test_rubric_free_digital_ecosystem_and_phet(self):
        """Valida a curadoria de canais do YouTube, as 9 simulações PhET mapeadas, MolView e ChemTube3D."""
        dig_text = self._read_file_if_exists(
            "04_recursos_e_metodologia/ecossistema_digital_e_simuladores.md",
            "Ecossistema Digital e Simuladores",
        )

        # 1. Canais abertos de YouTube
        self.assertRegex(dig_text, r"(?i)Michel|Caf[ée]\s+com\s+Qu[íi]mica", "Canal Prof. Michel ausente.")
        self.assertRegex(dig_text, r"(?i)Igor\s+Qu[íi]mica|Ferretto", "Canal Prof. Igor ausente.")
        self.assertRegex(dig_text, r"(?i)Paulo\s+Valim|Qu[íi]mica\s+em\s+A[çc][ãa]o", "Canal Paulo Valim ausente.")

        # 2. PhET Interactive Simulations (9 simulações essenciais)
        phet_simulations = [
            r"(?i)Construa\s+um\s+[Áá]tomo|Build\s+an\s+Atom",
            r"(?i)Rutherford|Dispers[ãa]o\s+de\s+Rutherford",
            r"(?i)Balanceamento\s+de\s+Equa[çc][õo]es|Balancing\s+Chemical\s+Equations",
            r"(?i)Propriedades\s+dos\s+Gases|Gas\s+Properties",
            r"(?i)Concentra[çc][ãa]o|Molaridade|Concentration",
            r"(?i)Solu[çc][õo]es\s+[Áá]cido-Base|Acid-Base\s+Solutions",
            r"(?i)Sais\s+e\s+Solubilidade|Salts\s+&\s+Solubility",
            r"(?i)Polaridade\s+da\s+Mol[ée]cula|Molecule\s+Polarity",
            r"(?i)Lei\s+de\s+Beer|Beer's\s+Law",
        ]
        for sim in phet_simulations:
            self.assertRegex(dig_text, sim, f"Simulação PhET obrigatória não encontrada: {sim}")

        # 3. Visualizadores tridimensionais
        self.assertRegex(dig_text, r"(?i)MolView", "Referência à ferramenta MolView ausente.")
        self.assertRegex(dig_text, r"(?i)ChemTube3D", "Referência à ferramenta ChemTube3D ausente.")

        # 4. Portais oficiais de provas abertas
        self.assertRegex(dig_text, r"(?i)COPERVE|coperve\.ufsc\.br", "Portal oficial COPERVE-UFSC ausente.")
        self.assertRegex(dig_text, r"(?i)INEP", "Portal oficial INEP ausente.")

    # -------------------------------------------------------------------------
    # RUBRICA 4: EXERCÍCIOS RESOLVIDOS PASSO A PASSO
    # -------------------------------------------------------------------------

    def test_rubric_step_by_step_exercise_solutions(self):
        """Valida se as listas de exercícios apresentam gabarito comentado ou resolução passo a passo."""
        exercise_files = [
            "00_fundamentos/exercicios_resolvidos_fundamentos.md",
            "01_quimica_geral_inorganica/exercicios_resolvidos_geral_inorganica.md",
            "02_fisico_quimica/exercicios_resolvidos_fisico_quimica.md",
            "03_quimica_organica/exercicios_resolvidos_quimica_organica.md",
            "05_roteiro_provas_exercicios/banco_exercicios_comentados_vestibulares.md",
        ]

        active_exercise_files = [self.root / f for f in exercise_files if (self.root / f).exists()]

        if not active_exercise_files:
            if self.is_strict:
                self.fail("Modo Estrito: Nenhuma lista de exercícios resolvidos encontrada.")
            else:
                self.skipTest("Listas de exercícios ainda não implementadas (Progressive Testability).")

        solution_markers = [
            r"(?i)resolu[çc][ãa]o\s+(comentada|passo\s+a\s+passo|detalhada)",
            r"(?i)passo\s+\d+|etapa\s+\d+",
            r"(?i)justificativa|an[áa]lise\s+das\s+proposi[çc][õo]es|an[áa]lise\s+dos\s+itens",
            r"(?i)gabarito\s+comentado",
        ]

        for file_path in active_exercise_files:
            content = file_path.read_text(encoding="utf-8")
            has_step_by_step = any(re.search(marker, content) for marker in solution_markers)
            self.assertTrue(
                has_step_by_step,
                f"O arquivo {file_path.name} não apresenta marcações evidentes de resolução comentada passo a passo.",
            )

    # -------------------------------------------------------------------------
    # RUBRICA 5: ESTRATÉGIA ENEM (TRI) E UFSC (SOMATÓRIAS E DISCURSIVAS)
    # -------------------------------------------------------------------------

    def test_rubric_enem_tri_strategic_roadmap(self):
        """Valida que o roteiro do ENEM explica a TRI (ML3P, coerência pedagógica, estratégia de prova)."""
        enem_text = self._read_file_if_exists(
            "05_roteiro_provas_exercicios/estrategico_enem_tri.md",
            "Roteiro Estratégico ENEM",
        )

        # 1. Teoria de Resposta ao Item (TRI) e parâmetros
        self.assertRegex(enem_text, r"(?i)TRI|Teoria\s+de\s+Resposta\s+ao\s+Item", "Menção à TRI ausente.")
        self.assertRegex(enem_text, r"(?i)discrimina[çc][ãa]o|par[âa]metro\s+[Aa]", "Parâmetro de discriminação 'a' ausente.")
        self.assertRegex(enem_text, r"(?i)dificuldade|par[âa]metro\s+[Bb]", "Parâmetro de dificuldade 'b' ausente.")
        self.assertRegex(enem_text, r"(?i)acerto\s+casual|chute|par[âa]metro\s+[Cc]", "Parâmetro de acerto casual 'c' ausente.")
        self.assertRegex(enem_text, r"(?i)coer[êe]ncia\s+pedag[óo]gica", "Princípio da coerência pedagógica ausente.")

        # 2. Competência 7 e habilidades de Química
        self.assertRegex(enem_text, r"(?i)Compet[êe]ncia(\s+de\s+[Áá]rea)?\s+7", "Competência de Área 7 do ENEM ausente.")
        self.assertRegex(enem_text, r"(?i)H24|H25|H26|H27", "Habilidades da Matriz ENEM (H24-H27) ausentes.")

    def test_rubric_ufsc_somatorias_and_discursivas(self):
        """Valida a mecânica oficial da somatória COPERVE, barreira NPC > NPI, abertas 00-99 e discursivas."""
        ufsc_text = self._read_file_if_exists(
            "05_roteiro_provas_exercicios/estrategico_ufsc_somatorias_discursivas.md",
            "Roteiro Estratégico UFSC",
        )

        # 1. Proposições binárias e fórmula de pontuação
        self.assertRegex(ufsc_text, r"(?i)01.*02.*04.*08.*16.*32.*64", "Potências binárias de somatória (01 a 64) ausentes.")
        self.assertRegex(ufsc_text, r"(?i)NPC|NPI|NTPC", "Parâmetros NPC, NPI, NTPC da fórmula oficial ausentes.")
        self.assertRegex(
            ufsc_text,
            r"(?i)NP\s*-\s*\[NTPC\s*-\s*\(NPC\s*-\s*NPI\)\].*NP",
            "Expressão da fórmula oficial de pontuação parcial da UFSC ausente.",
        )

        # 2. Regra eliminatória / barreira de validação
        self.assertRegex(
            ufsc_text,
            r"(?i)NPC\s*>\s*NPI|NPC\s*(?:<=|\\le)\s*NPI|anula|zer",
            "Cláusula eliminatória condicional (NPC > NPI) da COPERVE ausente.",
        )

        # 3. Questões abertas numéricas de 00 a 99
        self.assertRegex(
            ufsc_text,
            r"(?i)zero\s+[àa]\s+esquerda|00\s+[àa]\s+99",
            "Regra obrigatória do preenchimento com zero à esquerda em questões abertas ausente.",
        )

        # 4. Questões discursivas e critérios de correção 10.0
        self.assertRegex(
            ufsc_text,
            r"(?i)estados?\s+f[íi]sicos?|\(s\),?\s*\(l\),?\s*\(g\),?\s*\(aq\)",
            "Critério de estados de agregação em discursivas ausente.",
        )
        self.assertRegex(
            ufsc_text,
            r"(?i)unidades?(\s+de\s+medida)?|SI|g/mol|kJ",
            "Exigência de unidades de medida em discursivas ausente.",
        )

    # -------------------------------------------------------------------------
    # RUBRICA 6: METACOGNIÇÃO E CADERNO DE ERROS
    # -------------------------------------------------------------------------

    def test_rubric_active_learning_and_error_log(self):
        """Valida que o guia metodológico ensina Active Recall, Anki, 5 causas-raiz e reteste em 48h."""
        met_text = self._read_file_if_exists(
            "04_recursos_e_metodologia/metodologia_estudo_ativo_e_caderno_de_erros.md",
            "Metodologia de Estudo Ativo e Caderno de Erros",
        )

        # 1. Três pilares da aprendizagem ativa
        self.assertRegex(met_text, r"(?i)Active\s+Recall|Evoca[çc][ãa]o\s+Ativa", "Princípio do Active Recall ausente.")
        self.assertRegex(met_text, r"(?i)Feynman|T[ée]cnica\s+de\s+Feynman", "Técnica de Feynman ausente.")
        self.assertRegex(met_text, r"(?i)Dual\s+Coding|Dupla\s+Codifica[çc][ãa]o", "Dual Coding ausente.")

        # 2. Anki e cartões atômicos
        self.assertRegex(met_text, r"(?i)Anki|SRS|repeti[çc][ãa]o\s+espa[çc]ada", "Instruções sobre Anki e SRS ausentes.")

        # 3. As 5 Causas-Raiz de Erro em Química
        self.assertRegex(met_text, r"(?i)\bLC\b.*Lacuna\s+Conceitual", "Causa de erro LC (Lacuna Conceitual) ausente.")
        self.assertRegex(met_text, r"(?i)\bEM\b.*Erro\s+Matem[áa]tico", "Causa de erro EM (Erro Matemático) ausente.")
        self.assertRegex(met_text, r"(?i)\bET\b.*(Erro\s+de\s+)?Enunciado|Texto|Pegadinha", "Causa de erro ET ausente.")
        self.assertRegex(met_text, r"(?i)\bRV\b.*(Representa[çc][ãa]o\s+)?Visual", "Causa de erro RV ausente.")
        self.assertRegex(met_text, r"(?i)\bIU\b.*(Incompatibilidade\s+de\s+)?Unidades?", "Causa de erro IU ausente.")

        # 4. Ciclo de Reteste Cego em 48 horas
        self.assertRegex(met_text, r"(?i)48\s*h(oras)?|reteste\s+cego", "Ciclo de reteste cego de 48 horas ausente.")


def print_rubric_scorecard():
    """Imprime um scorecard analítico dos critérios de aceitação e conformidade."""
    root = PROJECT_ROOT
    print("\n" + "=" * 90)
    print("          SCORECARD DE RUBRICAS PEDAGÓGICAS E REQUISITOS (quimica_estudos)")
    print("=" * 90)

    rubrics = [
        ("Rubrica 1: Transição Zero Absoluto ao Avançado", ["00_fundamentos/02_atomo_particulas_subatomicas.md", "00_fundamentos/03_isotoppia_e_tabela_introdutoria.md"]),
        ("Rubrica 2: Bibliografia Clássica e Autores (Feltre, Reis, etc.)", ["04_recursos_e_metodologia/bibliografia_livros_didaticos.md"]),
        ("Rubrica 3: Recursos Digitais Abertos (YouTube, 9 PhETs, MolView)", ["04_recursos_e_metodologia/ecossistema_digital_e_simuladores.md"]),
        ("Rubrica 4: Exercícios com Solução Passo a Passo", ["00_fundamentos/exercicios_resolvidos_fundamentos.md"]),
        ("Rubrica 5A: Roteiro Estratégico ENEM e Modelagem TRI", ["05_roteiro_provas_exercicios/estrategico_enem_tri.md"]),
        ("Rubrica 5B: Roteiro Estratégico UFSC (Somatórias e Discursivas)", ["05_roteiro_provas_exercicios/estrategico_ufsc_somatorias_discursivas.md"]),
        ("Rubrica 6: Metacognição, Anki e Caderno de Erros (5 Causas / 48h)", ["04_recursos_e_metodologia/metodologia_estudo_ativo_e_caderno_de_erros.md"]),
    ]

    for name, req_files in rubrics:
        all_present = all((root / f).exists() for f in req_files)
        any_present = any((root / f).exists() for f in req_files)
        if all_present:
            status = "PRONTO P/ AUDITORIA"
        elif any_present:
            status = "PARCIAL"
        else:
            status = "AGUARDANDO MÓDULO"
        print(f"• {name:<70} | {status}")

    print("=" * 90 + "\n")


if __name__ == "__main__":
    print_rubric_scorecard()
    unittest.main(argv=[sys.argv[0]] + [a for a in sys.argv[1:] if a not in ("--strict",)])
