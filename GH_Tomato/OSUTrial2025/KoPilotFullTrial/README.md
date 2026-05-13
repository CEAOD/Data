# Trial Description
---
**Contributors**: Jason Hollick, Ivy Dao, Kenneth Tran, Chieri Kubota

**Contact person**: Kenneth Tran (ken@koidra.ai)

**Experiment**: Full-season greenhouse operation under **AI-assisted (KoPilot) control** at OSU’s CEA Research Complex.

**Crop**: Cherry tomato ‘Maxxiany’

**Location**: OSU CEA Research Complex.

**Greenhouse system**:
- Venlo with ETFE roof, heating, venting, screens, fertilizer injection
- Supplemental lighting and climate automation
- Pad & fan or equivalent cooling as configured for the season

**Season / data coverage**:
- **Environment**: 2025-05-10 through 2025-11-14
- **Irrigation**: 2025-05-10 through 2025-11-14
- **Production**: weekly harvest summaries from 2025-06-09 through 2025-11-10

# Dataset Description
---

## Environment (`Environment.csv`)
**Daily** greenhouse and weather aggregates (one row per **Time**). Values are daily means or integrals as exported from the climate system.

| Column | Description | Unit |
| ------ | ----------- | ---- |
| Time | Calendar date | YYYY-MM-DD |
| T Air | Inside air temperature | °C |
| T Out | Outside air temperature | °C |
| Daily Light Integral | Daily integrated photosynthetic light (DLI as exported) | mol·m⁻²·d⁻¹ |
| Rad Out Sum | Daily sum of outside global radiation | J·cm⁻² |
| Blackout Screen | Blackout screen position | % |
| Energy Screen | Energy / thermal screen position | % |
| Shading Screen | Shading screen position | % |
| Vent Lee | Leeward vent opening | % |
| Vent Wind | Windward vent opening | % |
| T Canopy | Canopy temperature | °C |
| VPD Canopy | Canopy vapor pressure deficit | kPa |
| AH | Inside absolute humidity | g·m⁻³ |
| AH Out | Outside absolute humidity | g·m⁻³ |
| RH | Inside relative humidity | % |
| RH Out | Outside relative humidity | % |
| T Dew | Dew point temperature | °C |
| CO2 | Inside CO₂ concentration | ppm |

## Production (`Production.csv`)
**Weekly** harvest and quality metrics for the KoPilot zone.

| Column | Description | Unit |
| ------ | ----------- | ---- |
| Date | Week reference | YYYY-MM-DD |
| Production | Total harvested production increment for the week | kg·m⁻² |
| Cumulative Production | Running total production | kg·m⁻² |
| Blossom End Rot Yield | BER increment for the week | kg·m⁻² |
| Split Yield | Split / cracked-class fruit increment for the week | kg·m⁻² |
| Marketable | Marketable-class increment for the week | kg·m⁻² |

## Irrigation (`Irrigation.csv`)
**Daily** irrigation and drain metrics for the KoPilot zone.

| Column | Description | Unit |
| ------ | ----------- | ---- |
| Date | Calendar date | YYYY-MM-DD |
| Dose 24h | 24 h irrigation dose | L·m⁻² |
| Drain 24h | 24 h drain volume | L·m⁻² |
| Drain% | Drain as % of applied water | % |
| EC Drain | Drain EC | mS·cm⁻¹ |
