#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_curriculum_coverage.py - Suíte de Testes de Cobertura Curricular E2E
Projeto: Plano Completo de Estudos e Guia de Aprendizagem de Química
Público: ENEM e Vestibulares Federais (com foco na UFSC)

Verifica:
1. Existência física de todos os guias e módulos do layout oficial do projeto.
2. Densidade volumétrica de conteúdo (> 1.000 caracteres por guia).
3. Ausência total de marcações de incompletude ou placeholders (Zero Placeholder Policy).
4. Cobertura explícita dos tópicos curriculares canônicos previstos na matriz pedagógica.
"""

import os
import re
import sys
import unittest
from pathlib import Path

# Raiz do projeto de química
PROJECT_ROOT = Path(r"C:\Users\guistumpf\teamwork_projects\quimica_estudos")

# Layout oficial dos 28 arquivos de entrega definidos em PROJECT.md
EXPECTED_GUIDES = {
    "M0_FUNDAMENTOS": [
        "00_fundamentos/01_materia_estados_misturas.md",
        "00_fundamentos/02_atomo_particulas_subatomicas.md",
        "00_fundamentos/03_isotoppia_e_tabela_introdutoria.md",
        "00_fundamentos/exercicios_resolvidos_fundamentos.md",
    ],
    "M1_GERAL_INORGANICA": [
        "01_quimica_geral_inorganica/01_modelos_atomicos_distribuicao_eletronica.md",
        "01_quimica_geral_inorganica/02_tabela_periodica_e_propriedades.md",
        "01_quimica_geral_inorganica/03_ligacoes_geometria_polaridade_intermolecular.md",
        "01_quimica_geral_inorganica/04_funcoes_inorganicas_e_reacoes.md",
        "01_quimica_geral_inorganica/exercicios_resolvidos_geral_inorganica.md",
    ],
    "M2_FISICO_QUIMICA": [
        "02_fisico_quimica/01_estequiometria_gases_solucoes.md",
        "02_fisico_quimica/02_propriedades_coligativas_e_termoquimica.md",
        "02_fisico_quimica/03_cinetica_e_equilibrio_quimico_ionico.md",
        "02_fisico_quimica/04_eletroquimica_pilhas_eletrolise.md",
        "02_fisico_quimica/exercicios_resolvidos_fisico_quimica.md",
    ],
    "M3_ORGANICA": [
        "03_quimica_organica/01_estrutura_carbono_hibridizacao_cadeias.md",
        "03_quimica_organica/02_funcoes_organicas_e_nomenclatura.md",
        "03_quimica_organica/03_isomeria_plana_e_espacial.md",
        "03_quimica_organica/04_reacoes_organicas_polimeros_biomoleculas.md",
        "03_quimica_organica/exercicios_resolvidos_quimica_organica.md",
    ],
    "M4_RECURSOS_METODOLOGIA": [
        "04_recursos_e_metodologia/bibliografia_livros_didaticos.md",
        "04_recursos_e_metodologia/ecossistema_digital_e_simuladores.md",
        "04_recursos_e_metodologia/metodologia_estudo_ativo_e_caderno_de_erros.md",
    ],
    "M5_ROTEIRO_PROVAS_EXERCICIOS": [
        "05_roteiro_provas_exercicios/estrategico_enem_tri.md",
        "05_roteiro_provas_exercicios/estrategico_ufsc_somatorias_discursivas.md",
        "05_roteiro_provas_exercicios/simulados_provas_anteriores_e_cronograma.md",
        "05_roteiro_provas_exercicios/banco_exercicios_comentados_vestibulares.md",
    ],
    "ROOT_OVERVIEW": [
        "README.md",
        "PLANO_DE_ESTUDOS_MESTRE.md",
    ],
}

# Expressões regulares para detecção de placeholders não finalizados
# NOTA: \bTODO\b, \bFIXME\b, \bTBD\b DEVEM ser case-sensitive, pois "todo" é uma palavra comum em português ("todo átomo")!
PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTODO\b"),
    re.compile(r"\bFIXME\b"),
    re.compile(r"\bTBD\b"),
    re.compile(r"\[A\s+preencher\]", re.IGNORECASE),
    re.compile(r"\[Inserir\s+aqui\]", re.IGNORECASE),
    re.compile(r"\[Em\s+constru[çc][ãa]o\]", re.IGNORECASE),
    re.compile(r"lorem\s+ipsum", re.IGNORECASE),
    re.compile(r"conte[úu]do\s+ser[áa]\s+adicionado", re.IGNORECASE),
]

# Tópicos canônicos essenciais que devem ser abordados em cada estágio
CURRICULUM_KEYWORDS = {
    "M0_FUNDAMENTOS": [
        r"densidade",
        r"estados?\s+f[íi]sicos?",
        r"misturas?",
        r"[áa]tomo",
        r"pr[óo]tons?",
        r"n[êe]utrons?",
        r"el[ée]trons?",
        r"n[úu]mero\s+at[ôo]mico",
        r"is[óo]topos?",
        r"tabela\s+peri[óo]dica",
    ],
    "M1_GERAL_INORGANICA": [
        r"modelos?\s+at[ôo]micos?",
        r"distribui[çc][ãa]o\s+eletr[ôo]nica",
        r"tabela\s+peri[óo]dica",
        r"liga[çc][ãa]o\s+i[ôo]nica|covalente|met[áa]lica",
        r"geometria\s+molecular|VSEPR",
        r"polaridade",
        r"for[çc]as?\s+intermoleculares?",
        r"[áa]cidos?|bases?|sais?|[óo]xidos?",
        r"balanceamento",
    ],
    "M2_FISICO_QUIMICA": [
        r"estequiometria",
        r"gases?",
        r"solu[çc][õo]es?",
        r"concentra[çc][ãa]o",
        r"propriedades?\s+coligativas?",
        r"termoqu[íi]mica|entalpia|Hess",
        r"cin[ée]tica|velocidade",
        r"equil[íi]brio\s+qu[íi]mico",
        r"pH|pOH",
        r"eletroqu[íi]mica|pilhas?|eletr[óo]lise",
    ],
    "M3_ORGANICA": [
        r"carbono|tetraval[êe]ncia|hibridiza[çc][ãa]o",
        r"nomenclatura\s+IUPAC",
        r"hidrocarbonetos?",
        r"fun[çc][õo]es?\s+org[âa]nicas?|[áa]lcool|[ée]ster|[ée]ter|cetona|alde[íi]do",
        r"isomeria\s+(plana|espacial|geom[ée]trica|[óo]ptica)",
        r"rea[çc][õo]es?\s+org[âa]nicas?",
        r"pol[íi]meros?",
        r"biomol[ée]culas?",
    ],
    "M4_RECURSOS_METODOLOGIA": [
        r"Feltre",
        r"Martha\s+Reis",
        r"PhET",
        r"Active\s+Recall|Feynman|Dual\s+Coding",
        r"Anki|repeti[çc][ãa]o\s+espa[çc]ada",
        r"Caderno\s+de\s+Erros",
    ],
    "M5_ROTEIRO_PROVAS_EXERCICIOS": [
        r"ENEM|TRI|Teoria\s+de\s+Resposta\s+ao\s+Item",
        r"UFSC|COPERVE|somat[óo]ria",
        r"cronograma|simulados?",
    ],
}


class TestCurriculumCoverage(unittest.TestCase):
    """Suíte de auditoria de cobertura, densidade volumétrica e ausência de placeholders."""

    @classmethod
    def setUpClass(cls):
        """Verifica a presença do diretório raiz do projeto."""
        cls.root = PROJECT_ROOT
        cls.is_strict = os.environ.get("STRICT_E2E", "0") == "1" or "--strict" in sys.argv

    def _get_stage_files(self, stage_key):
        """Retorna os caminhos absolutos dos arquivos de um determinado estágio."""
        return [self.root / rel_path for rel_path in EXPECTED_GUIDES[stage_key]]

    def _check_stage_active_or_skip(self, stage_key, stage_name):
        """No modo progressivo, pula estágios ainda não implementados. No modo estrito, falha se faltarem."""
        files = self._get_stage_files(stage_key)
        existing_files = [f for f in files if f.exists()]

        if not existing_files:
            if self.is_strict:
                self.fail(
                    f"Modo Estrito E2E: Nenhum arquivo encontrado para o estágio {stage_name} ({stage_key}). "
                    f"Esperados: {[str(p.name) for p in files]}"
                )
            else:
                self.skipTest(
                    f"Estágio {stage_name} ({stage_key}) ainda não implementado (Progressive Testability). "
                    f"Nenhum dos {len(files)} arquivos existe ainda."
                )
        return files, existing_files

    # -------------------------------------------------------------------------
    # TESTES DE EXISTÊNCIA E DENSIDADE POR ESTÁGIO
    # -------------------------------------------------------------------------

    def test_stage0_fundamentos_coverage(self):
        """Audita presença e qualidade dos guias do Stage 0 (Nível Fundamental / Zero Absoluto)."""
        files, existing = self._check_stage_active_or_skip("M0_FUNDAMENTOS", "Stage 0 (Fundamentos)")
        for path in files:
            if not path.exists():
                if self.is_strict:
                    self.fail(f"Arquivo obrigatório do Stage 0 ausente: {path}")
                else:
                    continue
            content = path.read_text(encoding="utf-8")
            self.assertGreater(
                len(content),
                1000,
                f"Arquivo {path.name} possui densidade insuficiente ({len(content)} caracteres < 1000).",
            )

    def test_stage1_quimica_geral_coverage(self):
        """Audita presença e qualidade dos guias do Stage 1 (Química Geral e Inorgânica)."""
        files, existing = self._check_stage_active_or_skip("M1_GERAL_INORGANICA", "Stage 1 (Geral e Inorgânica)")
        for path in files:
            if not path.exists():
                if self.is_strict:
                    self.fail(f"Arquivo obrigatório do Stage 1 ausente: {path}")
                else:
                    continue
            content = path.read_text(encoding="utf-8")
            self.assertGreater(
                len(content),
                1000,
                f"Arquivo {path.name} possui densidade insuficiente ({len(content)} caracteres < 1000).",
            )

    def test_stage2_fisico_quimica_coverage(self):
        """Audita presença e qualidade dos guias do Stage 2 (Físico-Química)."""
        files, existing = self._check_stage_active_or_skip("M2_FISICO_QUIMICA", "Stage 2 (Físico-Química)")
        for path in files:
            if not path.exists():
                if self.is_strict:
                    self.fail(f"Arquivo obrigatório do Stage 2 ausente: {path}")
                else:
                    continue
            content = path.read_text(encoding="utf-8")
            self.assertGreater(
                len(content),
                1000,
                f"Arquivo {path.name} possui densidade insuficiente ({len(content)} caracteres < 1000).",
            )

    def test_stage3_quimica_organica_coverage(self):
        """Audita presença e qualidade dos guias do Stage 3 (Química Orgânica)."""
        files, existing = self._check_stage_active_or_skip("M3_ORGANICA", "Stage 3 (Química Orgânica)")
        for path in files:
            if not path.exists():
                if self.is_strict:
                    self.fail(f"Arquivo obrigatório do Stage 3 ausente: {path}")
                else:
                    continue
            content = path.read_text(encoding="utf-8")
            self.assertGreater(
                len(content),
                1000,
                f"Arquivo {path.name} possui densidade insuficiente ({len(content)} caracteres < 1000).",
            )

    def test_stage4_recursos_metodologia_coverage(self):
        """Audita presença e qualidade dos guias do Stage 4 (Recursos Didáticos e Metodologia)."""
        files, existing = self._check_stage_active_or_skip("M4_RECURSOS_METODOLOGIA", "Stage 4 (Recursos e Metodologia)")
        for path in files:
            if not path.exists():
                if self.is_strict:
                    self.fail(f"Arquivo obrigatório do Stage 4 ausente: {path}")
                else:
                    continue
            content = path.read_text(encoding="utf-8")
            self.assertGreater(
                len(content),
                1000,
                f"Arquivo {path.name} possui densidade insuficiente ({len(content)} caracteres < 1000).",
            )

    def test_stage5_roteiro_provas_coverage(self):
        """Audita presença e qualidade dos guias do Stage 5 (Roteiro de Provas e Exercícios)."""
        files, existing = self._check_stage_active_or_skip("M5_ROTEIRO_PROVAS_EXERCICIOS", "Stage 5 (Provas e Exercícios)")
        for path in files:
            if not path.exists():
                if self.is_strict:
                    self.fail(f"Arquivo obrigatório do Stage 5 ausente: {path}")
                else:
                    continue
            content = path.read_text(encoding="utf-8")
            self.assertGreater(
                len(content),
                1000,
                f"Arquivo {path.name} possui densidade insuficiente ({len(content)} caracteres < 1000).",
            )

    def test_master_guides_coverage(self):
        """Audita presença e densidade dos guias mestres: README.md e PLANO_DE_ESTUDOS_MESTRE.md."""
        files, existing = self._check_stage_active_or_skip("ROOT_OVERVIEW", "Guias Mestres Raiz")
        for path in files:
            if not path.exists():
                if self.is_strict:
                    self.fail(f"Arquivo mestre ausente: {path}")
                else:
                    continue
            content = path.read_text(encoding="utf-8")
            self.assertGreater(
                len(content),
                1000,
                f"Arquivo mestre {path.name} possui menos de 1000 caracteres ({len(content)}).",
            )

    # -------------------------------------------------------------------------
    # AUDITORIA DE ZERO PLACEHOLDERS EM TODOS OS ARQUIVOS PRESENTES
    # -------------------------------------------------------------------------

    def test_zero_placeholders_audit(self):
        """Garante que nenhum arquivo markdown existente contenha TODO, FIXME, TBD ou placeholders."""
        all_md_files = list(self.root.rglob("*.md"))
        # Excluir arquivos de infraestrutura de teste e relatórios de auditoria se houver
        target_files = [
            f for f in all_md_files
            if not any(excluded in str(f) for excluded in ["tests", ".agents", "TEST_INFRA", "TEST_READY"])
        ]

        if not target_files:
            self.skipTest("Nenhum arquivo markdown de conteúdo encontrado ainda para auditoria de placeholders.")

        violations = []
        for file_path in target_files:
            content = file_path.read_text(encoding="utf-8")
            lines = content.splitlines()
            for line_no, line in enumerate(lines, start=1):
                for pattern in PLACEHOLDER_PATTERNS:
                    match = pattern.search(line)
                    if match:
                        violations.append(
                            f"{file_path.relative_to(self.root)}:{line_no} -> Encontrado '{match.group(0)}' na linha: {line.strip()}"
                        )

        self.assertEqual(
            violations,
            [],
            f"Violação da Política Zero Placeholders! Encontrados {len(violations)} marcadores não resolvidos:\n"
            + "\n".join(violations[:15]),
        )

    # -------------------------------------------------------------------------
    # AUDITORIA DOS 35 TÓPICOS CURRICULARES CANÔNICOS
    # -------------------------------------------------------------------------

    def test_curriculum_thematic_keywords(self):
        """Audita se os temas canônicos essenciais estão documentados nos estágios já implementados."""
        for stage_key, keywords in CURRICULUM_KEYWORDS.items():
            files = self._get_stage_files(stage_key)
            existing_files = [f for f in files if f.exists()]

            if not existing_files:
                continue

            combined_text = "\n".join(f.read_text(encoding="utf-8") for f in existing_files)

            missing_keywords = []
            for kw in keywords:
                if not re.search(kw, combined_text, re.IGNORECASE):
                    missing_keywords.append(kw)

            self.assertEqual(
                missing_keywords,
                [],
                f"Estágio {stage_key} está incompleto pedagogicamente. Palavras-chave essenciais não encontradas: {missing_keywords}",
            )


def print_curriculum_status_matrix():
    """Gera um relatório visual completo do status de cobertura de todos os 28 arquivos."""
    root = PROJECT_ROOT
    print("\n" + "=" * 90)
    print("           RELATÓRIO FORENSE DE COBERTURA CURRICULAR (PROJECT quimica_estudos)")
    print("=" * 90)
    print(f"{'Arquivo':<70} | {'Status':<10} | {'Tamanho':<10}")
    print("-" * 90)

    total_expected = 0
    total_found = 0
    total_chars = 0

    for stage, guides in EXPECTED_GUIDES.items():
        print(f"\n[{stage}]")
        for rel_path in guides:
            total_expected += 1
            full_path = root / rel_path
            if full_path.exists():
                total_found += 1
                size = full_path.stat().st_size
                total_chars += size
                status = "OK" if size >= 1000 else "CURTO"
                print(f"  {rel_path:<68} | {status:<10} | {size:>7} B")
            else:
                print(f"  {rel_path:<68} | {'PENDENTE':<10} | {'-':>7}")

    print("-" * 90)
    print(f"Total de Arquivos Entregues: {total_found} / {total_expected} ({total_found/total_expected*100:.1f}%)")
    print(f"Volume Total de Conteúdo: {total_chars:,} bytes")
    print("=" * 90 + "\n")


if __name__ == "__main__":
    if "--report" in sys.argv or "-r" in sys.argv:
        print_curriculum_status_matrix()
        sys.exit(0)

    print_curriculum_status_matrix()
    unittest.main(argv=[sys.argv[0]] + [a for a in sys.argv[1:] if a not in ("--strict", "--report", "-r")])
