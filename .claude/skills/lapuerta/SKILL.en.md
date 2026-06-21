# lapuerta · Synthetic insurance users (Peru) — English guide

> Invoke with `/lapuerta`. English mirror of `SKILL.md`. Claude Code loads `SKILL.md`
> (Spanish) as the active skill; this file is a reference for English-speaking users.

Self-contained skill to **generate synthetic populations** of Peruvian insurance
consumers and **simulate their answers**. Distributions are calibrated with real data
and validated (model marginals ≈ reality).

## When to use it
- "Generate N synthetic insurance personas (Peru)."
- "Ask a question to a simulated group / a segment (NSE A, Gen Z…)."
- "I need a sample for prototyping, class balancing, or message testing."
- "What share distrusts / has insurance / would pay more in segment X?"

## Generate users

Standard-library only Python (nothing to install).

```bash
# N profiles to console (CSV)
python scripts/generate_synthetic_users.py --n 20 --seed 42

# N profiles to a reproducible file
python scripts/generate_synthetic_users.py --n 1000 --out users.csv --seed 42
```

Flags: `--n` (count), `--out` (CSV path; prints if omitted), `--seed`
(reproducibility), `--schema` (alternate schema). **Same seed → same people.**

### Filter a segment
Generate a large batch and filter by field (`generacion`, `nse`, `region`,
`canal_preferido`, …) — see the Spanish `SKILL.md` for the snippet.

## Simulate answers (two engines)
1. **Rule-based** — ready to use:
   ```bash
   python scripts/simulate_rules.py --list
   python scripts/simulate_rules.py --question confianza --n 1000 --seed 42
   python scripts/simulate_rules.py --question marca --brand "RIMAC" --filter nse=A --by generacion
   ```
   Each trait adds or subtracts to decide the stance; supports `--filter` and `--by`
   (segment breakdown). Questions: `confianza`, `contratar`, `tenencia`, `marca`, `datos_ia`.
2. **LLM-based (Claude)** — give the model each profile + the codebook and ask it to
   answer in first person, returning `quote` + `sentiment` (favorable/neutral/unfavorable).

## The 16 variables
generación · nse · región · educación financiera · present bias · preferred channel ·
**situación laboral · tenencia de vehículo · acceso digital · bancarizado** · seismic exposure ·
openness to data/AI · trust in insurers · insurance tenure · disaster cover · WTP (fraction of
the fair price). Full table in `SKILL.md` / `references/`.

## Where each parameter comes from
Trust → **SBS 2023** · tenure & penetration → **APESEG** · NSE segments → **APEIM** ·
present bias & WTP → **behavioral economics** · macro penetration (% GDP) → **MAPFRE / OECD**.

## Validation
Re-sample n=5,000: simulated marginals ≈ real → has-insurance 43% vs 40%,
distrust 45% vs 48%, disaster cover 2.9% vs 3.3%.

## Files
- `scripts/generate_synthetic_users.py` — generator (stdlib).
- `scripts/simulate_rules.py` — rule-based answer engine (stdlib).
- `scripts/synthetic_user_schema.json` — calibrated distributions (editable).
- `references/matriz_usuarios_sinteticos.md` — full matrix, dependency graph, archetypes.

## Limits
Synthetic data: not real people. For prototyping, hypothesis exploration and message
design; **not** a substitute for a market survey, and not causal evidence.

## Install (to share)
Copy the `lapuerta/` folder into `.claude/skills/` (project) or `~/.claude/skills/`
(personal), then restart the session. Invoke with **`/lapuerta`**.
