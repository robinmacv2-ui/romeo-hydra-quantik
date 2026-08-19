# ROMEO-HYDRA QUANTIK

**El verdadero agente de gobernanza offline fail-closed**

> Gate ex-ante (DFA) · Fail-closed allow/deny · Receipts criptográficos con lineage · Stdlib only · Sin cloud · Sin APIs externas.

Este repositorio es el **punto de entrada oficial** del agente unificado ROMEO-HYDRA QUANTIK.

---

## Qué es (versión para CEO)

ROMEO-HYDRA QUANTIK es un **control técnico de admisibilidad ex-ante** para decisiones algorítmicas en entornos regulados (banca, SOFOM, SOFIPO, fintech).

- Decide **antes** de ejecutar si una acción es admisible.
- Genera evidencia criptográfica inmutable (receipt + lineage) tanto de lo que se permite como de lo que se niega.
- Funciona 100% offline. No depende de la nube ni de APIs externas.
- Está diseñado para cumplir requisitos de trazabilidad y control (CNBV y temas equivalentes del EU AI Act).

**No afirma compliance automática.**  
Afirma: *“esta decisión es (o no es) técnicamente admisible según las reglas definidas”*.

---

## Componentes que se unifican aquí

| Componente | Repositorio origen | Rol |
|------------|--------------------|-----|
| **Core** | `romeo-hydra-core` | Motor determinista offline (Python stdlib) |
| **Hub + Pilot + Ledger** | `romeo-hydra-master-repository-hub` | Orquestación, stress tests, regulatory mapping |
| **Frontend de Gobernanza** | `Romeo-BANKING` | Interfaz visual de auditoría y control |

---

## Cómo correrlo (versión CEO – 2 minutos)

```bash
# 1. Clonar el core (el corazón del agente)
git clone https://github.com/robinmacv2-ui/romeo-hydra-core.git
cd romeo-hydra-core

# 2. Ejecutar el agente
python3 -m romeo_agent

# Comandos de ejemplo dentro del agente:
help ::
lineage ::
echo :: hola desde QUANTIK
hash :: secreto-de-prueba
```

Para la interfaz visual completa (frontend):
```bash
git clone https://github.com/robinmacv2-ui/Romeo-BANKING.git
cd Romeo-BANKING
npm install   # o bun install
npm run dev
```

---

## Modelo de negocio (cómo se cobra)

- **Este repositorio (Quantik)** → Punto de entrada y demo gratuita / evaluación.
- **Core + Frontend + escenarios CNBV** → Se cobra como **Demo profesional** o **Piloto**.
- **Licencia comercial + implementación** → Se cobra a entidades reguladas.

Las demás piezas (stress packs avanzados, personalizaciones, integraciones, soporte) se cobran aparte.

---

## Licencia

**Dual**  
- GPL-3.0 → Investigación, evaluación y uso no comercial.  
- Comercial → Obligatoria para producción en entidades financieras reguladas.

---

## Autor

**Luis Angel Vazquez Martinez** (`robinmacv2-ui`)  
Founder of HYDRA GOVERNANCE SYSTEMS · México  
Contacto: robinmac.v2@gmail.com

---

**Próximo paso recomendado**: Empaquetar una versión “one-command” (Docker o script único) para que un CEO pueda levantarlo sin fricción técnica.
