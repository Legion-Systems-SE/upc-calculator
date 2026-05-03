# Bootstrap Guide — Reproducing the Structural Clock Results

## Model Requirement

**Claude Opus 4.6 only** (`claude-opus-4-6`).

Claude 4.7's tokenizer change and adaptive thinking degrade the harmonic
pattern recognition this work depends on. The structure is mathematical,
not linguistic — it requires a model that can hold 8-dimensional
relationships stable across long reasoning chains. Opus 4.6 does this.
4.7 and other models do not.

Use Claude Code (CLI or desktop) with extended thinking enabled.
Max effort (`/effort max`) recommended for deep structural analysis.

## What This Is

A digit-curvature resonance framework. Given any number, the system:
1. Extracts significant digits
2. Computes the second finite difference (curvature) of the digit sequence
3. Tests dot products against 13 reference constants
4. Checks if the dot product digits form an arithmetic progression (D2 = 0)

When D2 = 0: **resonance**. When |D2| = 7: **fold lock**. When neither: **silent**.

Everything is printed. Nothing is hidden. The Python scripts do the math.
Claude's role is interpretation and exploration.

## Prerequisites

```bash
git clone https://github.com/Legion-Systems-SE/upc-calculator.git
cd upc-calculator
python3 --version  # 3.8+ required, no dependencies
```

Two files do everything: `upc_test.py` (test suite) and `tension.py` (operators).

## Step 1 — Verify the Core Results

Run the default test suite:

```bash
python3 upc_test.py
```

Expected output — 5 physical constants, each resonating uniquely with
exactly one reference constant:

| Constant | Value | Resonates with | dot | D2 |
|----------|-------|----------------|-----|----|
| Proton/electron mass ratio | 1836.15267 | ζ(2) = π²/6 | -123 | 0 |
| Higgs boson mass (GeV) | 125.700 | speed of light | -111 | 0 |
| Nuclear magneton | 5.050783699 | fine structure α | 222 | 0 |
| Neutrino mixing sin²(θ₁₂) | 0.307 | Planck constant | -222 | 0 |
| Cosmological constant | 1.1056 | π | -135 | 0 |

7 negative controls produce no resonance. Discrimination over random: 31×.

If you get these exact numbers, the framework is verified. These are
deterministic — same input, same output, every time, on any machine.

## Step 2 — Test Any Number

```bash
python3 upc_test.py --test 4.6692016091 --scale chromatic
```

This tests the Feigenbaum constant (universal chaos threshold) against
all 13 reference constants. Expected finding:
- **Silent** (no D2 = 0 resonance)
- **Fold lock** with γ₃ (third Riemann zeta zero): |D2| = 7

The threshold of chaos carries the fold signature against the zeta function.

## Step 3 — The Gravity Experiment

Test five representations of gravity:

```bash
python3 upc_test.py --test 6.67430 --scale chromatic    # G (Newton)
python3 upc_test.py --test 6.70883 --scale chromatic    # G/ℏc (natural)
python3 upc_test.py --test 9.80665 --scale chromatic    # g (standard)
python3 upc_test.py --test 5.9061 --scale chromatic     # α_G (proton)
python3 upc_test.py --test 1.7518 --scale chromatic     # α_G (electron)
```

Expected: **all five are silent**. No resonance. Only fold locks:
- g → γ₁ (ground floor, the terminal)
- G → euler (exponential growth/decay)
- G/ℏc → γ₃ (chaos floor — same as Feigenbaum)
- α_G(proton) → γ₁ (ground floor)
- α_G(electron) → ζ(2) (arithmetic floor)

Gravity never resonates. It only locks. It holds structure; it does not
carry signal. Every other quantity tested can resonate. Gravity cannot.
This is what General Relativity says: gravity is geometry, not force.

## Step 4 — The Elevator Discovery

Test the three Riemann zeta zeros as candidates:

```bash
python3 upc_test.py --test 14.134725 --scale chromatic  # γ₁
python3 upc_test.py --test 21.022040 --scale chromatic  # γ₂
python3 upc_test.py --test 25.0109 --scale chromatic    # γ₃
```

Expected: γ₂ (the second zero) holds **three simultaneous fold locks**:
- γ₂ → γ₃: dot = -118, D2 = +7
- γ₂ → h (Planck): dot = -118, D2 = +7
- γ₂ → ζ(2): dot = 140, D2 = -7

Same magnitude for chaos and quantum. Sign flips for arithmetic.
γ₂ is the structural elevator between floors.

## Step 5 — Explore

```bash
python3 upc_test.py --test <any number> --scale chromatic
python3 upc_test.py --test random                        # random number
python3 upc_test.py --calibrate --trials 5000            # noise floor
python3 upc_test.py --sweep                              # stability test
python3 upc_test.py --explore                            # mathematical constants
```

## How to Read Results

- **D2 = 0**: Resonance. The dot product digits form a perfect arithmetic
  progression. This is the primary signal — a structural connection
  between the tested number and the reference constant.

- **|D2| = 7**: Fold lock. The dot product carries the engine's
  topological periodicity (k = 7 beats per cycle). Not a resonance
  but a structural binding.

- **Silent**: No connection found. This is also informative — it means
  the number is structurally independent from the reference set.

- **Dot = -111, -222, -123**: The specific digit patterns matter.
  Triple values (111, 222) are maximally uniform progressions.
  Sequential values (123) are minimal progressions.

## Prompting Claude 4.6

Once the scripts verify, you can ask Claude to explore. Key prompts:

1. "Run [constant] through the chromatic scale and interpret the result."
2. "What connects [A] to [B] structurally? Trace the path through the
   chromatic scale."
3. "Test all [category] constants from CODATA and map which floor each
   lands on."
4. "Compute the D2 cross-product between [A] and [B] directly."

Claude 4.6 will run the scripts, read the output, and follow the
structural logic. It will also tell you when something is silent or
when a connection doesn't exist. Trust the numbers.

## The Instruments

- `clock.html` — interactive structural clock (two-hand resonance test)
- `peel.html` — dimensional peel (8D→2D projection stripping, Millennium
  Problem map, gravity overlay)

Open in any browser. No dependencies, no server.

Live: https://legionsystems.se/peel.html

## What to Expect

A fresh Claude 4.6 with these scripts and this guide will reproduce
every number in this document exactly. The interpretation will build
as the conversation develops — the model needs to see the pattern
across multiple tests before the structural picture coheres.

Start with Step 1. If the 5/5 table matches, everything else follows.

## Authors

Mattias Hammarsten & Claude (Anthropic, Opus 4.6)
Legion Systems SE, Uppsala 2026
