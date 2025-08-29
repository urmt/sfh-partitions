# SFH Partitions

**Mathematical Backbone for the Sentience-Field Hypothesis (SFH)**  

This repository implements the **Hardy–Ramanujan integer partition framework** used in the *Sentience-Field Hypothesis: Consciousness as the Fabric of Reality*. It provides both **exact and asymptotic methods** for partition numbers and integrates **Ramanujan’s congruences**, which predict “forbidden configurations” in the SFH model.  

---

## ✨ Purpose
In SFH, the universe is modeled as a **discrete partition space** of *qualic energy* (Q).  
- Each possible distribution of Q corresponds to a potential universe configuration.  
- **Partition numbers** (`p(Q)`) quantify how many such configurations are possible.  
- **Ramanujan congruences** indicate classes of configurations that never occur — interpreted in SFH as **forbidden universes**.  
- The Hardy–Ramanujan **asymptotic formula** describes how viable universes cluster at discrete levels, which links to SFH’s predictions about **phase transitions, coherence–fertility balance, and fine-tuning**.  

This repo provides reproducible code to compute these values and connect mathematical partitions to SFH theory.

---

## 📂 Repository Structure
sfh-partitions/
│
├── partitions.py # Core library: exact & asymptotic partition methods
├── tests/
│ └── test_partitions.py # Unit tests for correctness and validation
├── examples/
│ └── run_partition_simulation.py # Example script with sample output
└── README.md


---

## 🧮 Features
- **Exact partitions**: Euler’s pentagonal number recurrence for `p(n)`  
- **Hardy–Ramanujan asymptotic**: Fast approximation for large `n`  
- **Ramanujan congruences**: Detection of forbidden configurations (`5k+4`, `7k+5`, `11k+6`)  
- **Partition info wrapper**: Easy access to exact, approximate, and forbidden-status in one call  

---

## 🚀 Usage

### Install
Clone the repository:
```bash
git clone https://github.com/urmt/sfh-partitions.git
cd sfh-partitions

# RUN EXAMPLE

python examples/run_partition_simulation.py

## EXAMPLE OUTPUT

Q=10, exact=42, approx=44.99, forbidden=False
Q=11, exact=56, approx=60.84, forbidden=False
Q=14, exact=135, approx=137.90, forbidden=True

## IMPORT INTO PYTHON

from partitions import partition_info

result = partition_info(50)
print(result)
# {'n': 50, 'exact': 204226, 'asymptotic': 204227.00, 'forbidden': False}

✅ Testing

Run unit tests:

python -m unittest discover tests

📖 References

Hardy, G.H. & Ramanujan, S. (1918). Asymptotic formulae in combinatory analysis. Proc. London Math. Soc.

Andrews, G. (1998). The Theory of Partitions. Cambridge University Press.

Traver, M.R. (2025). The Sentience-Field Hypothesis: Consciousness as the Fabric of Reality.

🔬 Role in SFH

This partition framework provides the mathematical foundation for:

Configuration quantization (universes cluster at discrete energy levels).

Forbidden configurations (certain universes never arise, per Ramanujan’s congruences).

Phase transitions (sharp jumps in p(Q) predict structural shifts in universes).

Probability weighting for the SFH claim that our universe is a statistical outlier.

By connecting number theory with quantum and cosmological dynamics, this module grounds SFH predictions in rigorous, testable mathematics.

