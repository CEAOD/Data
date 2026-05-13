# Trial Description
---
**Contributors**: Jason Hollick, Ivy Dao, Kenneth Tran, Chieri Kubota

**Contact person**: Kenneth Tran (ken@koidra.ai)

**Experiment**: Side-by-side comparison of greenhouse operation under **AI-assisted (KoPilot) control** versus **expert grower control** in OSU’s CEA Research Complex.

**Crop**: Cherry tomato ‘Maxxiany’

**Location**: OSU CEA Research Complex (paired compartments or management zones for AI vs Expert).

**Greenhouse system**:
- Venlo with ETFE roof, heating, venting, screens, fertilizer injection
- Supplemental lighting and climate automation 
- Pad & fan or equivalent cooling as configured for the season

**Season / data coverage (from files in this folder)**:
- **Crop — Expert**: 2025-04-22 through 2025-07-22 (per-plant / per-row samples)
- **Crop — AI**: 2025-04-22 through 2025-11-25 (per-plant / per-row samples)
- **Environment & irrigation**: 2025-05-10 through 2025-07-28 (daily aggregates)
- **Production**: weekly harvest summaries from 2025-06-09 through 2025-07-28

# Dataset Description
---
This folder holds **paired AI vs Expert** tables. Use the `_AI` / `_Expert` suffix (or the ` - AI` / ` - Expert` column pairs) to align treatments.

## Crop (`Crop_AI.csv`, `Crop_Expert.csv`)
Time series at weekly registration. Rows are keyed by **Date** and **Sample**.

### `Crop_Expert.csv`

| Column | Description | Unit |
| ------ | ----------- | ---- |
| Date | Registration date | YYYY-MM-DD |
| Sample | Sample / row identifier | - |
| Leaf Pruning | Leaves removed since last week | count |
| Truss Length | Truss length | cm |
| Leaf Length | Representative leaf length | cm |
| Leaf Number Increase | New leaves since last week | count |
| Head Thickness | Stem or “head” thickness | mm |
| Distance Btw Shoot Tip And 1St Flower Truss | Shoot tip to first flowering truss | cm |
| Stem density | Stem density metric | stems·m⁻² |
| Stem Length | Stem length | cm |
| Stem Length Increase | Stem elongation since last week | cm |
| Total Leaves | Total leaf count on plant | count |

### `Crop_AI.csv`

| Column | Description | Unit |
| ------ | ----------- | ---- |
| Date | Registration date | YYYY-MM-DD |
| Sample | Sample / row identifier | - |
| Fruit Set | Fruit set count per week | fruits·m⁻² |
| Head Thickness | Stem or “head” thickness | mm |
| Leaf Length | Representative leaf length | cm |
| New Leaves | New leaves since last week | count |
| Truss Length | Truss length | cm |
| Stem Length Increase | Stem elongation since last week | cm |
| Distance Btw Shoot Tip And 1St Flower Truss | Shoot tip to first flowering truss | cm |


## Environment (`Environment_AI.csv`, `Environment_Expert.csv`)
**Daily** greenhouse and weather aggregates (one row per **Date**). Values are daily means or integrals as exported from the climate system.

| Column | Description | Unit |
| ------ | ----------- | ---- |
| Date | Calendar date | YYYY-MM-DD |
| T Air | Inside air temperature | °C |
| T Out | Outside air temperature | °C |
| Daily Light Integral | Daily integrated photosynthetic light (inside or canopy-relevant DLI as exported) | mol·m⁻²·d⁻¹ (typical; confirm in Priva) |
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
**Weekly** harvest and quality metrics with **parallel columns for AI and Expert**.

| Column | Description | Unit |
| ------ | ----------- | ---- |
| Date | Week reference | datetime |
| Harvest - AI / Harvest - Expert | Marketable harvest increment for the week | kg·m⁻² |
| Cumulative Marketable Yield - AI / Cumulative Marketable Yield - Expert | Running total marketable yield | kg·m⁻² |
| Blossom End Rot - AI / Blossom End Rot - Expert | BER incidence or mass for the week | kg·m⁻² |
| Cracked - AI / Cracked - Expert | Cracked fruit metric for the week | kg·m⁻² |
| Fruit weight - AI / Fruit Weight - Expert | Average marketable fruit mass | g |

## Irrigation (`Irrigation.csv`)
**Daily** irrigation and drain metrics with **parallel columns for AI and Expert**.

| Column | Description | Unit |
| ------ | ----------- | ---- |
| Date | Calendar date | datetime |
| Dose 24h - AI / Dose 24h - Expert | 24 h irrigation dose | L·m⁻² |
| Drain 24h - AI / Drain 24h - Expert | 24 h drain volume | L·m⁻² |
| Drain% - AI / Drain% - Expert | Drain as % of applied water | % |
| EC Drain - AI / EC Drain - Expert | Drain EC | mS·cm⁻¹ |
