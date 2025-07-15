# Data Description

The CSV files contain plant growth and glass greenhouse environmental condition data from two trials of a reciprocal grafting study in basil described in detail by Hollick and Kubota (2022) published in Frontiers in Plant Science (<https://doi.org/10.3389/fpls.2022.921440>). `BZL_EXP2_Nutrient.csv` contains tissue nutrient analysis data collected in the second trial of the same study.

Objective of this data collection: to identify the effect of reciprocal grafting two basil cultivars of differing vigor on plant growth and leaf mineral nutrient concentration  

**Funding source**: USDA NIFA Specialty Crop Research Initiative Grants program (Project number: 2016-51181-25404) 

**Data collected by**: Jason R. Hollick

**Contact person**: Chieri Kubota (kubota.10@osu.edu)

**Data collection site**: glass greenhouse located at the Ohio State University, Columbus, Ohio (40°00′07.2′ N, 83°01′42.7′ W)  

Experiment: Reciprocal grafts of two basil cultivars ('Nufar' and 'Dolce Fresca') as well as un-grafted controls were grown in a glass greenhouse in two trials with the first trial running from 30 September to 9 December 2020 and the second from 15 January to March 11, 2021. Detailed description of the experiment can be found at (<https://doi.org/10.3389/fpls.2022.921440>).

**BZL_EXP1_EXP2_Growth.csv**  
- EXP: trial number (1 (30 September to 9 December 2020) or 2 (15 January to March 11 2021))
- DAS: days after seeding (plants harvested 70 DAS (Trial 1; 9 December 2020) or 55 DAS (Trial 2; March 11 2021)
- Block: (A,B,C,D,E,F)
- Treatment: grafting treatments (N=un-grafted Nufar, NN= self-grafted Nufar, NDF= Nufar scion grafted to Dolce Fresca Rootstock, DF= un-grafted Dolce Fresca, DFDF= self-grafted Dolce Fresca, DFN= Dolce Fresca Scion grafted to Nufar rootstock)  
- SC: Scion (N=Nufar, DF=Dolce Fresca)  
- RS: Rootstock (N=Nufar, DF=Dolce Fresca, X=No rootstock (not grafted))  
- Leaf\_Number: Number of true leaves with a lamina length exceeding 1 cm. Values are the average of 2 plants of the same treatment in the same block. 
- M\_Stem (cm): Length of the main stem in centimeters. Values are the average of 2 plants of the same treatment in the same block.
- Shoot\_Dry (g): Dry mass of shoot tissue in grams. Values are the average of 2 plants of the same treatment in the same block.
- Root\_Dry (g): Dry mass of root tissue in grams. Values are the average of 2 plants of the same treatment in the same block.
- S\_R\_Dry: Ratio of the dry shoot mass to dry root mass. Values are the average of 2 plants of the same treatment in the same block.

**BZL_EXP2_Nutrient.csv** 

- EXP: trial number (2 (15 January to March 11 2021); plants harvested on March 11 2021)
- DAS: days after seeding
- Block:(A,B,C,D,E,F)
- Treatment: grafting treatments (N=un-grafted Nufar, NN= self grafted Nufar, NDF= Nufar scion grafted to Dolce Fresca Rootstock, DF= un-grafted Dolce Fresca, DFDF= self-grafted Dolce Fresca, DFN= Dolce Fresca Scion grafted to Nufar rootstock)  
- SC: Scion (N=Nufar, DF=Dolce Fresca)    
- RS: Rootstock (N=Nufar, DF=Dolce Fresca, X=No rootstock (not grafted))  
- N (%): Percent nitrogen in dry leaf tissue  
- P (%): Percent phosphorus in dry leaf tissue  
- K (%): Percent potassium in dry leaf tissue  
- Ca (%): Percent calcium in dry leaf tissue  
- Mg (%): Percent magnesium in dry leaf tissue  
- S (ppm): concentration (ppm) of sulfur in dry leaf tissue  
- Fe (ppm): concentration (ppm) of iron in dry leaf tissue  
- Mn (ppm): concentration (ppm) of manganese in dry leaf tissue 
- B (ppm): concentration (ppm) of boron in dry leaf tissue  
- Cu (ppm): concentration (ppm) of copper in dry leaf tissue  
- Zn (ppm): concentration (ppm) of zinc in dry leaf tissue  
- Na (ppm): concentration (ppm) of sodium in dry leaf tissue

All values for nutrients are derived from a combined dry tissue sample from two plants of the same block and treatment.

**‘BZL\_EXP1EXP2\_Temperature\_Data\_for\_Upload.csv’**

- Year: 2020 (trial 1) or 2021 (trial 2)
- Day.of.year: Day of year
- Time: Time in 15 minute intervals (for example: 15 = 00:15, 630 = 06:30, 1945 = 19:45)
- DAS: days after seeding
- PAR: Photosynthetic photon flux density summed over 15 minutes  
- Panel.Temp: Temperature of dataloguer panel in degrees Celsius
- T1: Air temperature (°C) at plant canopy level measured by type t thermocouple (gauge 36, connected to the extension of gauge 24). Values are 15 minute averages. 
- T2: Air temperature (°C) at plant canopy level measured by type t thermocouple (gauge 36, connected to the extension of gauge 24). Values are 15 minute averages.   
- T3: Air temperature (°C) at plant canopy level measured by type t thermocouple (gauge 36, connected to the extension of gauge 24). Values are 15 minute averages.
- EXP: trial number (2 (15 January to March 11 2021))  
- DorN: Day (light period) or night (dark period)
- avgtemp: Average air temperature at plant canopy for the experimental area (average of T1, T2, T3).
- Growing\_Period: Stage of experiment relative to grafting/healing process (pregraft, graft (only un-granfted control plants present in the greenhouse at this time), and postgraft).  
- Pre\_Post\_Trans: Stage of experiment relative to transplanting into pots (pre-tranplant or post-transplant).

## References

Hollick, J.R., and Kubota, C. 2022. Effect of self- and inter-cultivar grafting on growth and nutrient content in sweet basil (*Ocimum basilicum* L.). Front. Plant Sci. 13: 92144. Doi: 10.3389/fpls.2022.921440
