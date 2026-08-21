# JURY — ROMEO-HYDRA QUANTIK

**Role of this repo:** Public door. Not the full product surface.

---

## Where to evaluate (pass criteria)

| Target | URL | Pass if |
|--------|-----|--------|
| Product surface | [romeo-hydra-master-repository-hub](https://github.com/robinmacv2-ui/romeo-hydra-master-repository-hub) | `pip install -e .` installs zero third-party deps; `python -m romeo_agent -c "status ::"` → allow |
| Pure kernel | [hydra-genesis-zero](https://github.com/robinmacv2-ui/hydra-genesis-zero) | `python3 main.py` runs offline without pip |
| This door | `python3 main.py` | Prints routing instructions only |

Full checklist: [JURY_CHECKLIST.md on hub](https://github.com/robinmacv2-ui/romeo-hydra-master-repository-hub/blob/main/JURY_CHECKLIST.md)

---

## Hard non-claims

- No CNBV certification  
- No production banking warranty  
- No LLM  
- Numpy / lab extras are never required for the product surface claim  

---

**Author:** Luis Angel Vazquez Martinez · ORCID 0009-0006-8163-3759
