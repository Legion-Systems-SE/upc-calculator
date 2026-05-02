# UPC — Universal Pocket Calculator

**Experimental.** A digit-curvature resonance test for physical constants.

Given any number, the UPC computes its digit-sequence curvature and compares
it against a set of reference constants.  When the curvature dot product
satisfies a specific arithmetic condition (D2 = 0), the number "resonates"
with that reference — a tonic.

## Quick start

```
python3 upc_test.py
```

No dependencies beyond Python 3.8+.  Two files, no install.

## Method

Every step is printed.  Nothing is hidden.

```
1. ENCODE      value  -->  first 10 significant digits
               1836.15267343  -->  [1, 8, 3, 6, 1, 5, 2, 6, 7, 3]

2. DIFFERENCES  d1[i] = digits[i+1] - digits[i]           (velocity)
                d2[i] = d1[i+1] - d1[i]                   (acceleration)

3. DOT PRODUCT  for each reference constant p:
                dot = sum( d2_candidate[i] * d2_parent[i] )

4. TENSION      if 100 <= |dot| <= 999, extract digits d0 d1 d2:
                D2 = d0 - 2*d1 + d2
                D2 = 0 means the digits form an arithmetic progression

5. VERDICT      exactly one parent with D2=0  -->  unique resonance
                no parent with D2=0           -->  silent
                multiple parents with D2=0    -->  ambiguous
```

## What the default run shows

```
$ python3 upc_test.py
```

**Confirmed resonances** (5/5 unique, correct parent):

| Constant | Value | Resonates with | dot | \|dot\| digits |
|----------|-------|---------------|-----|----------------|
| Proton/electron mass ratio | 1836.15267 | zeta(2) = pi^2/6 | -123 | [1,2,3] D2=0 |
| Higgs boson mass (GeV) | 125.700 | speed of light | -111 | [1,1,1] D2=0 |
| Nuclear magneton | 5.050783699 | fine structure constant | 222 | [2,2,2] D2=0 |
| Neutrino mixing sin^2(th_12) | 0.307 | Planck constant | -222 | [2,2,2] D2=0 |
| Cosmological constant | 1.1056 | pi | -135 | [1,3,5] D2=0 |

**Negative controls** (7/7 silent):
CKM matrix elements, Yukawa couplings, and mixing angles produce
no resonance.

**Noise floor** (1000 random trials):
- 82.5% silent, 15.9% false unique, 3.2% per specific parent
- Claimed resonances: 100% correct = 31x above random baseline

**Stability sweep** (digit lengths 6-20):
- Higgs-c and sin^2(th_12)-h are stable at all 15 lengths tested
- Nuclear magneton-alpha resolves only at length 10 (dim 8)

## Usage

```bash
python3 upc_test.py                       # full test suite
python3 upc_test.py --test 1836.15267     # test any number
python3 upc_test.py --test random         # test a random number
python3 upc_test.py --scale chromatic     # use all 13 reference constants
python3 upc_test.py --sweep               # digit-length stability test
python3 upc_test.py --explore             # experimental: normal numbers, primes
python3 upc_test.py --calibrate           # noise floor only
python3 upc_test.py --calibrate --trials 5000
python3 upc_test.py --test 0.2357 --length 8  # custom digit length
```

## Reference constants (parents)

Default subset ("pentatonic", 5 parents):
- `c` — speed of light (299792458 m/s)
- `h` — Planck constant (6.62607015 x 10^-34 J*s)
- `alpha` — fine structure constant (7.2973525693 x 10^-3)
- `pi` — 3.14159265358979...
- `zeta2` — zeta(2) = pi^2/6 = 1.64493406684...

Full set ("chromatic", 13 parents) includes Boltzmann, Avogadro,
elementary charge, Euler's number, golden ratio, and the first
three Riemann zeta zeros.

## Experimental: --explore

Tests mathematical constants across all digit lengths and all 13
parents.  Key findings:

- **Copeland-Erdos constant** (concatenated primes, proven normal):
  silent at default length 10, but resonates with zeta(2) at length 8
  and with Euler's number at length 12
- **sqrt(2)**: resonates with Planck at length 10; with the first
  zeta zero at length 17
- **ln(2)**: resonates with the third zeta zero at lengths 14-15
- **Prime gaps**: silent everywhere except length 16 (second zeta zero)

## False positive analysis

The per-pair D2=0 rate is ~3.7% (90 out of 900 possible 3-digit
arithmetic progressions, divided by digit-distribution effects).
With 5 parents, ~16% of random numbers produce a false unique match.
With 13 parents, ~31%.

All 5 claimed resonances match the correct parent at 100%.
Random chance of matching a *specific* parent: 3.2%.
Discrimination ratio: 31x.

## Relation to the Resonant Field Engine

The tension operators (encode, delta2, dot) originate from the
[Resonant Field Engine](https://github.com/Legion-Systems-SE/critical-fold),
a research project exploring zeta-zero-seeded manifold dynamics.
The UPC extracts the digit-curvature framework as a standalone test.

## Files

- `upc_test.py` — test suite and CLI (all logic here)
- `tension.py` — minimal digit-curvature operators (5 functions)

## Authors

Mattias Hammarsten / Claude (Anthropic)

Uppsala, 2026
