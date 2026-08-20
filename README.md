# ROMEO-HYDRA QUANTIK

**Punto de entrada público del agente de gobernanza offline fail-closed.**

> Gate ex-ante · Fail-closed allow/deny · Receipts + lineage · Core = Python 3.11 stdlib · Sin cloud · Sin APIs externas.

---

## Qué es

QUANTIK es el **portal oficial** de evaluación del ecosistema ROMEO-HYDRA.

No afirma compliance automática ni certificación CNBV.  
Afirma: *“esta decisión es (o no es) técnicamente admisible según las reglas definidas y deja evidencia criptográfica”*.

## Componentes

| Pieza | Dónde vive | Rol |
|-------|------------|-----|
| **Core (stdlib)** | `romeo-hydra-core` (privado) + extracto Genesis | Motor determinista fail-closed |
| **Hub + Pilot + Ledger** | [`romeo-hydra-master-repository-hub`](https://github.com/robinmacv2-ui/romeo-hydra-master-repository-hub) | Orquestación, auditorías, DOI |
| **Este repo (Quantik)** | Aquí | Entrada limpia + documentación de evaluación |

## Cómo evaluar (2 minutos)

```bash
# Opción recomendada para jurado — hub público limpio
git clone https://github.com/robinmacv2-ui/romeo-hydra-master-repository-hub.git
cd romeo-hydra-master-repository-hub
python3 -m venv .venv && source .venv/bin/activate
pip install -e .          # ZERO dependencias de terceros
python main.py
```

Ver también: [`JURY_CHECKLIST.md`](https://github.com/robinmacv2-ui/romeo-hydra-master-repository-hub/blob/main/JURY_CHECKLIST.md)

## Modelo

- **Este repositorio** → entrada y demo de evaluación.
- **Core + escenarios + frontend** → Demo profesional / Piloto (comercial).
- **Licencia comercial** → obligatoria para producción en entidades reguladas.

## Licencia

Dual: AGPL-3.0 (evaluación / no comercial) · Comercial EMMOROR (producción regulada).

## Autor

**Luis Angel Vazquez Martinez** (`robinmacv2-ui`)  
Founder of HYDRA GOVERNANCE SYSTEMS · México  
ORCID: 0009-0006-8163-3759  
Contacto: robinmac.v2@gmail.com
