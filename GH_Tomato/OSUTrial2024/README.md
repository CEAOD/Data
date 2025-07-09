# Trial Description
---
**Contributors**: Changhyeon Kim, Ivy Dao, Kenneth Tran, Chieri Kubota
**Contact person**: Kenneth Tran (ken@koidra.ai)

**Crop**: cherry tomato ‘Maxxiany’, planted at 3 plants/m² density.
**Location**: 2 identical 487 m2 compartments at OSU’s CEA Research Complex
**Greenhouse system**:
- Venlo with ETFE roof, heating, venting, screens, fertilizer injection system
- LED light: 300 µmol/m2/s
- Mechanical cooling with pad & fan
- Priva climate control system
**Duration**: Jun 24, 2024 (transplant) – Nov 15, 2024 (final harvest)

# Dataset Description
---
The dataset contains 2 datasets for KoPilot-control zone and Reference zone.
Each dataset has 4 sub-datasets:
## Crop
Time series data at daily granularity.

| Column                                             | Description                                                 | Unit       |
| -------------------------------------------------- | ----------------------------------------------------------- | ---------- |
| Date                                               | Date of crop registration                                   | YYYY-MM-DD |
| Label                                              | Sample identifier                                           | -          |
| Stem length                                        | Length increase of the main stem from the last registration | cm         |
| Leaf number increase                               | Increase in number of leaves since the last measurement     | count      |
| Leaf length                                        | Length of the largest leaf                                  | cm         |
| Stem diameter                                      | Diameter of the main stem                                   | mm         |
| Number of flowering trusses                        | Total number of flowering trusses                           | count      |
| Distance between shoot tip and 1st flowering truss | Distance from shoot tip to the first flowering truss        | cm         |
| Remaining leaves                                   | Number of remaining (non-pruned) leaves                     | count      |
| Leaf pruning                                       | Number of leaves pruned                                     | count      |
| Crop height                                        | Total plant height                                          | cm         |
| Number of remaining trusses                        | Number of trusses remaining on the plant                    | count      |
| Number of harvested trusses                        | Number of trusses harvested                                 | count      |

## Environment
Time series data at 5-minute granularity.

| Column            | Description                                     | Unit |
| ----------------- | ----------------------------------------------- | ---- |
| T Air             | Air temperature inside the greenhouse           | °C   |
| RH                | Relative humidity inside the greenhouse         | %    |
| T Out             | Outside air temperature                         | °C   |
| RH Out            | Outside relative humidity                       | %    |
| CO2               | CO₂ concentration inside the greenhouse         | ppm  |
| Vent Lee          | Opening percentage of leeward (lee) ventilation | %    |
| Vent Wind         | Opening percentage of windward ventilation      | %    |
| Exhaust Fan Speed | Speed of the exhaust fans                       | %    |
| Blackout Screen   | Closing percentage of blackout screen           | %    |
| Energy Screen     | Closing percentage of energy screen             | %    |
| VPD Air           | Vapor Pressure Deficit inside the greenhouse    | kPa  |

## Production
Time series data at daily granularity.

| Column                        | Description                                               | Unit       |
| ----------------------------- | --------------------------------------------------------- | ---------- |
| Date                          | Date of harvest                                           | YYYY-MM-DD |
| Label                         | Sample identifier                                         | -          |
| Marketable yield              | Total weight of marketable fruits                         | g          |
| Unmarketable yield            | Total weight of unmarketable fruits                       | g          |
| Number of trusses             | Number of fruit-bearing trusses per plant                 | count      |
| Number of marketable yield    | Number of marketable fruits harvested                     | count      |
| Number of unmarketable fruits | Number of unmarketable fruits harvested                   | count      |
| Number of fruits with crack   | Number of fruits showing cracking symptoms                | count      |
| Number of unmature fruits     | Number of fruits not yet mature                           | count      |
| Average marketable fruit size | Average weight per marketable fruit                       | g          |
| Total yield                   | Total fruit weight (marketable + unmarketable)            | kg         |
| Marketable fruit (%)          | Percentage of marketable fruits relative to total yield   | %          |
| Cracking (%)                  | Percentage of fruits with cracks relative to total fruits | %          |
## Resource Consumption
Time series data at daily granularity.

| Column                    | Description                                  | Unit |
| ------------------------- | -------------------------------------------- | ---- |
| Air Circulation Fan Power | Energy consumption of air circulation fans   | kWh  |
| Exhaust Fan Power         | Energy consumption of exhaust fans           | kWh  |
| Lighting Power            | Energy consumption for supplemental lighting | kWh  |
| Water                     | Water use per unit of cultivated area        | L/m² |
| Crop Heating Energy       | Thermal energy supplied to the crop          | kJ   |
| Perimeter Heating Energy  | Thermal energy used for perimeter heating    | kJ   |
| Rail Heating Energy       | Thermal energy used for rail (pipe) heating  | kJ   |