# ROMEO-HYDRA QUANTIK

**Public evaluation door** for the offline fail-closed governance agent.

Gate ex-ante · Fail-closed allow/deny · Receipts + lineage · Core = Python 3.11 stdlib · No cloud · No external APIs.

[![Offline](https://img.shields.io/badge/offline-100%25-green.svg)](#)
[![Fail-closed](https://img.shields.io/badge/gate-FAIL--CLOSED-black.svg)](#)
[![Stdlib](https://img.shields.io/badge/core-stdlib%20only-success.svg)](#)

---

## 📜 Autoria y Propiedad Intelectual

**Autor y Titular:** Luis Angel Vazquez Martinez  
[![ORCID iD](https://img.shields.io/badge/ORCID-0009--0006--8163--3759-green?style=flat&logo=orcid)](https://orcid.org/0009-0006-8163-3759)
[![INDAUTOR](https://img.shields.io/badge/INDAUTOR-03--2026--081813295300--01-blue?style=flat&logo=shield)](https://orcid.org/0009-0006-8163-3759)

### 🛡️ Registro Oficial de Derechos de Autor
* **Obra / Proyecto:** ROMEO-HYDRA (Marco Ontológico, Sistema y Código Fuente de Gobernanza y Auditoría de IA)
* **Número de Registro:** `03-2026-081813295300-01`
* **Fecha:** 24 de Agosto de 2026
* **Rama:** Programas de Computación
* **Titularidad:** 100% Propiedad Intelectual de Luis Angel Vazquez Martinez

---

## Jury path (2 minutes)

### Option A — Full product surface (recommended)

```bash
git clone --depth 1 https://github.com/robinmacv2-ui/romeo-hydra-master-repository-hub.git
cd romeo-hydra-master-repository-hub
python3 -m venv .venv && source .venv/bin/activate
pip install -e .          # ZERO third-party packages for product surface
python main.py
python -m romeo_agent -c "status ::"
python -m romeo_agent -c "help ::"
```

Checklist: [JURY_CHECKLIST.md](https://github.com/robinmacv2-ui/romeo-hydra-master-repository-hub/blob/main/JURY_CHECKLIST.md)

### Option B — Pure kernel only

```bash
git clone --depth 1 https://github.com/robinmacv2-ui/hydra-genesis-zero.git
cd hydra-genesis-zero
python3 main.py
```

### Option C — This repo (door only)

```bash
git clone --depth 1 https://github.com/robinmacv2-ui/romeo-hydra-quantik.git
cd romeo-hydra-quantik
python3 main.py
```

Prints the evaluation map. Does not run the full agent (by design).

---

## What QUANTIK is

| Piece | Role |
|-------|------|
| This repo | Clean public door + jury routing |
| [master-repository-hub](https://github.com/robinmacv2-ui/romeo-hydra-master-repository-hub) | Pilot, ledger, DOI, product surface |
| [hydra-genesis-zero](https://github.com/robinmacv2-ui/hydra-genesis-zero) | Immutable stdlib kernel |

**Claim:** a decision is (or is not) *technically admissible* under declared rules, with cryptographic evidence.  
**Non-claim:** automatic legal nullity, CNBV certification, production banking.

---

## License

Dual: AGPL-3.0 (evaluation / non-commercial) · Commercial EMMOROR (regulated production).

**Author:** Luis Angel Vazquez Martinez (`robinmacv2-ui`)  
**ORCID:** [0009-0006-8163-3759](https://orcid.org/0009-0006-8163-3759)  
**Contact:** robinmac.v2@gmail.com
