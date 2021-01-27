# Parameters’ description  

- The dataset contains data on outdoor and indoor greenhouse climate, irrigation, status of actuators, requested and realized climate setpoints (“Weather” and “GreenhouseClimate”), resource consumption (“Resources”), harvest (“Production”), crop-related parameters (“CropParameters”), tomato quality ("TomQuality”), analysis of irrigation and drain samples (“LabAnalysis”) and root-zone/slab information (“GrodanSens”).  
- Economic calculations are not included in the dataset. However, the prices for the computation of costs and income, thus net profit, can be found in the document “Economics” attached to the dataset.   
- The 5 greenhouse compartments have a total area of 96 m² and a growing area of 62.5 m². 
- The teams taking part in the challenge, thus contributing to the creation of the dataset, are:  
- **Team The Automators**: Klaas van Egmond (Team Captain), Rens Smith, Jitse Schöne, Joris Mulders, Daam Rutten, Dara Dowd, Federico Mikaelian, Roberto D’Arco, Flavia Paganelli, Yangyang Shi, Koen de Bruijn, Arjan Vijverberg. 
- **Team AICU**: Zao Ye (Team Captain), Xing  Zhao, Liang  Li, Qianxixi  Min, Ningyi Zhang, Xinwei Bai, Xu  Zhang, Andreea-Elena Moga, David Fortini 
- **Team IUA.CAAS**: Bo Zhou (Team Captain), Weituo Sun, Nan Wang, Xin Sun, Sen Lin, Zhan Wang, Yukun Liu, DaviD Liu, Shusheng Wang, Xue Zhang, Lulei Yan, Chen Yang, Jing Li, Sietse van der Weij, Sjoerd Beukers   
- **Team Digilog**: HK Suh (Team Captain), Daegeun Choe, Seung Kyu Min, Hyeran Lee, Taewon Moon, Jinwook (Will) Chung, Queralt Altes-Buch, KwangHee Han, Sung Un Kim, Jaesu Lee, Kyungyup Daniel Lee, Minseok Lee, Sohee Sim, Junpyo Lee, Jin Hyung Cho, YeongUng Seo 
- **Team Automatoes**: Leonard Baart de la Faille (Team Captain), Lars Kerkhof, Evripidis Papadopoulos, Tamas Keviczky, Niek Bouman, Neil Yorke- Smith, Neil Yorke-Smith, Gerdinevan Donge, Rene Beerkens, Godfried Dol 
- **The Reference**, represented by a group of Dutch commercial growers, included the following members: Kees Stijger, Ted Duijvesteijn, Marissa Duijn, Kees Scheffers. 

# Weather data 



|**Column heading** |**Parameter description** |**Unit** |**Interval** |**Dataset name** |**Data Type** |**Comments** |**Data collection** |
| - | - | - | - | - | - | - | - |
|Tout |Outside temperature  |°C |5 min  |Weather |Raw data |- |Weather station |
|Rhout |Outside relative humidity |% |5 min  |Weather |Raw data |- |Weather station |
|Iglob |Solar Radiation  |W/m²  |5 min  |Weather |Raw data |- |Weather station |
|Windsp |Wind speed  |m/s  |5 min  |Weather |Raw data |- |Weather station |
|RadSum |Radiation sum  |J/cm2  |5 min  |Weather |Raw data |- |Weather station |
|Winddir |Wind direction  |Compass direction [0 to 128] |5 min  |Weather |Raw data |- |Weather station |
|Rain |Rain (status 1=rain, 0=dry)  |[1=rain, 0=dry] |5 min  |Weather |Raw data |- |Weather station |
|PARout |PAR weather measurement  |µmol/m² s  |5 min  |Weather |Raw data |- |Weather station |
|Pyrgeo |Heat emission: pyrgeometer  |W/m²  |5 min  |Weather |Raw data |- |Weather station |
|AbsHumOut |Absolute humidity content of outside air  |g/m³  |5 min  |Weather |Raw data |- |Weather station |
||Time |Timestamps 5 min (Excel format)\_ ||Weather ||||
# Greenhouse climate 

## Indoor climate, status of actuators and irrigation  



|**Column heading** |**Parameter description** |**Unit** |**Interval** |**Dataset name** |**Data Type** |**Comments** |**Data collection** |
| - | - | - | - | - | - | - | :- |
|Tair |Greenhouse Air temperature  |°C |5 min |GreenhouseClimate |Raw data |- |Process Computer |
|Rhair |Greenhouse relative humidity  |% |5 min |GreenhouseClimate |Raw data |- |Process Computer |
|CO2air |CO2 greenhouse  |ppm |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|HumDef |Greenhouse humidity deficit  |g/m³  |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|VentLee |Leeward vents opening  |% [0 to 100] |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|Ventwind |Windward vents opening  |% [0 to 100] |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|AssimLight |HPS lamps status (on-off) |% [0 or 100] |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|EnScr |Energy curtain opening  |% [0 to 100] |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|BlackScr |Blackout curtain opening  |% [0 to 100] |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|PipeLow |Rail pipe Temperature (Lower circuit) |°C |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|PipeGrow |Crop pipe Temperature (Growth circuit) |°C |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|co2\_dos |CO2 dosing  |kg/ha hour |5 min |GreenhouseClimate |Processed data |Computed CO2 dosage and calibrated by monthly CO2 meter readings.||
|Tot\_PAR |Total inside PAR  (Sun + HPS + LED) |µmol/m² s |5 min |GreenhouseClimate |Processed data |Computed based on outdoor PAR, cover transmissivity (0.5), operation and transmissivity of energy (0.75) and blackout screens (0.02), PAR from LED and HPS. ||
|Tot\_PAR\_Lamps |PAR sum from HPS and LED lamps |µmol/m² s |5 min |GreenhouseClimate |Processed data |Computed based on lamps’ operation and measured PPFD contribution of HPS (100 µmol/m² s) and LED (Blue = 11, Red = 49, Farred = 0, White = 37 µmol/m² s) when set at maximum range of LED proportional control (=1000)||
|EC\_drain\_PC |Drain EC  |dS/m |5 min |GreenhouseClimate |Raw data |- |Process Computer |
|pH\_drain\_PC |Drain pH  |[-] |5 min |GreenhouseClimate |Raw data |- |Process Computer |
|Water\_sup |Cumulative number of minutes of irrigation in a day |minutes |5 min |GreenhouseClimate |Raw data |This cumulation is reset to 0 at midnight. |Process Computer |
|Cum\_irr |Cumulative number of litres of irrigation in a day |L/m² day |5 min |GreenhouseClimate |Processed data |Conversion from minutes to liter. This cumulation is reset to 0 at midnight. ||


## Climate and irrigation setpoints 

|**Column heading** |**Parameter description** |**Unit** |**Interval** |**Dataset name** |**Data Type** |**Comments** |**Data collection/source** |
| - | - | - | - | - | - | - | :- |
|co2\_sp |CO2 setpoint  |ppm |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|dx\_sp |Humidity deficit setpoint |g/m³ |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|t\_rail\_min\_sp |Rail pipe minimum temperature setpoint |°C |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|t\_grow\_min\_sp |Crop pipe minimum temperature setpoint |°C |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|Assim\_sp |Assimilation lighting setpoint (HPS lamp) |% [0 or 100] |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|scr\_enrg\_sp |Energy curtain setpoint |% [0 to 100] |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|scr\_blck\_sp |Blackout curtain setpoint |% [0 to 100] |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|t\_heat\_sp |Heating temperature setpoint |°C |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|t\_vent\_sp |Ventilation temperature setpoint (leeward vents) |°C |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|window\_pos\_lee\_sp |Lee side window position minimum setpoint (leeward vents) |% |5 min  |GreenhouseClimate |Raw data |- |Process Computer |
|water\_sup\_int\_sp\_min |Water supply interval time setpoint |minutes |5 min  |GreenhouseClimate |Raw data |Interval time between the last and next irrigation turn.  |Process Computer |
|int\_blue\_sp |Intensity set of blue spectrum channel  (LED lamps) |[0 to 1000] range of proportional control |5 min  |GreenhouseClimate |Raw data |LED light control was coupled with HPS control, that is LED lamps can only be used when the HPS-lamps are switched on as well. |Heliospectra lamps |
|int\_red\_sp |Intensity set of red spectrum channel  (LED lamps) |[0 to 1000] range of proportional control|5 min  |GreenhouseClimate |Raw data |As above |Heliospectra lamps |
|int\_farred\_sp |Intensity set of far-red spectrum channel  (LED lamps) |[0 to 1000] range of proportional control |5 min  |GreenhouseClimate |Raw data |As above |Heliospectra lamps |
|int\_white\_sp |Intensity set of white spectrum channel  (LED lamps) |[0 to 1000] range of proportional control |5 min  |GreenhouseClimate |Raw data |As above |Heliospectra lamps |
|Time |Timestamps 5 min (Excel format) |||GreenhouseClimate ||||
## VIP (realized setpoints) 



|**Column heading**  |**Parameter description** |**Unit** |**Interval** |**Dataset name** |**Data Type** |**Comments** |**Data collection/source** |
| - | - | - | - | - | - | - | :- |
|co2\_vip |CO2 VIP |ppm |5 min  |GreenhouseClimate |Raw data ||Process Computer |
|dx\_vip |Humidity deficit VIP |g/m³  |5 min  |GreenhouseClimate |Raw data ||Process Computer |
|t\_rail\_min\_vip |Rail pipe minimum temperature VIP |°C |5 min  |GreenhouseClimate |Raw data ||Process Computer |
|t\_grow\_min\_vip |Crop pipe minimum temperature VIP |°C |5 min  |GreenhouseClimate |Raw data ||Process Computer |
|Assim\_vip |Assimilation lighting VIP (HPS lamp)  |% [0 or 100] |5 min  |GreenhouseClimate |Raw data ||Process Computer |
|scr\_enrg\_vip |Energy curtain VIP |% [0 or 100] |5 min  |GreenhouseClimate |Raw data ||Process Computer |
|scr\_blck\_vip |Blackout curtain VIP |% [0 or 100] |5 min  |GreenhouseClimate |Raw data ||Process Computer |
|t\_heat\_vip |Heating temperature VIP |°C |5 min  |GreenhouseClimate |Raw data ||Process Computer |
|t\_ventlee\_vip |Ventilation temperature VIP (leeward vents) |°C |5 min  |GreenhouseClimate |Raw data ||Process Computer |
|window\_pos\_lee\_vip |Lee side window position minimum VIP (leeward vents) |% |5 min  |GreenhouseClimate |Raw data ||Process Computer |
|t\_ventwind\_vip |Ventilation temperature VIP (windward side) |°C |5 min  |GreenhouseClimate |Raw data ||Process Computer |
|water\_sup\_int\_vip\_min |Water supply interval time VIP |minutes |5 min  |GreenhouseClimate |Raw data |Interval time between the last and next irrigation turn |Process Computer |
|int\_blue\_vip |Intensity set of blue spectrum channel  VIP (LED lamps) |[0 to 1000] range of proportional control |5 min  |GreenhouseClimate |Raw data |LED light control was coupled with HPS control, that is LED lamps can only be used when the HPS- lamps are switched on as well. |Heliospectra lamps |
|int\_red\_vip |Intensity set of red spectrum channel VIP (LED lamps) |[0 to 1000] range of proportional control |5 min  |GreenhouseClimate |Raw data |As above |Heliospectra lamps |
|int\_farred\_vip |Intensity set of far-red spectrum channel VIP (LED lamps) |[0 to 1000] range of proportional control |5 min  |GreenhouseClimate |Raw data |As above |Heliospectra lamps |
|int\_white\_vip |Intensity set of white spectrum channel VIP (LED lamps) |[0 to 1000] range of proportional control |5 min  |GreenhouseClimate |Raw data |As above |Heliospectra lamps |
|Time |Timestamps 5 min (Excel format) |||GreenhouseClimate ||||
## Production 



|**Column heading** |**Parameter description** |**Unit** |**Interval** |**Dataset name** |**Data Type** |**Comments** |**Data collection/source** |
| - | :- | - | - | - | - | - | :- |
|ProdA |Total tomato Production quality class  A  |kg/m²  |at date (harvest) |Production |` `Processed data |Conversion g to kg/m²  (production area = 62.5 m²). The harvest was performed per truss. Class A means first quality trusses that can be commercially traded. |Manual registration  |
|ProdB |Total tomato Production quality class  B |kg/m²   |at date (harvest) |Production |` `Processed data |Conversion g to kg/m²  (production area = 62.5 m²).  The harvest was performed per truss. Class B refers to trusses that cannot be commercially traded. |Manual registration  |
|avg\_nr\_harvested\_trusses |Number of harvested trusses (average ) |Number/stem |at date (harvest) |Production |` `Processed data |This refers to 10 sample stems (average value) |Manual registration  |
|Truss development time  |Truss growing period from flowering to harvest  |days |at date (harvest) |Production |` `Processed data |This refers to 10 sample stems (average value).  The growing period of a truss is considered to start when at a particular “flowering” truss at least 5 flowers are set.  |Manual registration  |
|Nr\_fruits\_ClassA |Number of harvested fruits  quality class A|Number  |at date (harvest) |Production |` `Raw data |This refers to 10 sample stems (total value) |Manual registration  |
|Weight\_fruits\_ClassA |Total weight harvested fruits  quality class A|g |at date (harvest) |Production |` `Raw data |This refers to 10 sample stems (total value) |Manual registration  |
|Nr\_fruits\_ClassB |Number of harvested fruits  quality class B|Number  |at date (harvest) |Production |` `Raw data |This refers to 10 sample stems (total value) |Manual registration  |
|Weight\_fruits\_ClassB |Total weight harvested fruits  quality class B|g |at date (harvest) |Production |` `Raw data |This refers to 10 sample stems (total value) |Manual registration  |
|Time |Timestamp date (Excel format) |||||||
## Crop parameters 



|**Column heading** |**Parameter description** |**Unit** |**Interva l** |**Dataset name** |**Data Type** |**Comment s** |**Data collection** |
| - | - | - | - | - | - | - | :- |
|Stem\_elong |Stem growth per week |cm/week |weekly |Crop parameters |Raw data |This refers to 10 sample stems (average value).  Data no later than 22 April (because tomato plants were topped). |Manual registration  |
|Stem\_thick |Stem thickness |mm |weekly |Crop parameters |Raw data |This refers to 10 sample stems (average value) Data no later than 22 April (because tomato plants were topped) |Manual registration |
|Cum\_trusses |Cumulative number of new set trusses on the stem.  |number/stem  |weekly |Crop parameters |Raw data |This refers to 10 sample stems (average value). A truss is considered as “set” when at least 5 flowers are set. |Manual registration |
|stem\_dens  |Stem density |Stems/m²  |weekly |Crop parameters |Raw data ||Teams’ communicatio n |
|Plant\_dens |Plant density |Plants/m²  |weekly |Crop parameters |Raw data ||Teams’ communicatio n |
|Time |Timestamp date (Excel format) |||Crop parameters ||||
Resources 



|**Column heading** |**Parameter description** |**Unit** |**Interva l** |**Dataset name** |**Data Type** |**Comments** |**Data collection/sourc**  **e** |
| - | - | - | - | - | - | - | :- |
|Heat\_cons |Heating energy consumption (rail + crop pipes) |MJ/m²  day |daily  |Resources |Processed data |Computation based on the sum of heat release (W/m²) from heating pipes (when on):  HeatPipe= (t\_rail- tair)\*2.1 + (t\_grow- t\_air)\*0.62.  Final conversion into MJ/day.  ||
|ElecHigh |Electricity consumption (artificial light) during pick-hours (7.00 -23.00) |kWh/m 2 day |daily  |Resources |Processed data |Computation based on lamps’ operation during pick-hours, measured electricity consumption of HPS (81 W/m2) and LED (Blue=7.27 ; Red= 25.3; Farred= 6.23; White=22.72 W/m²). Conversion into KWh. ||
|ElecLow |Electricity consumption (artificial light) during off-pick-hours |kWh/m2  day |daily  |Resources |Processed data |Computation based on lamps’ operation during off-pick-hours, electricity consumption of HPS (81 W/m2) and LED (Blue=7.27 ; Red= 25.3; Farred= 6.23; White=22.72 W/m²). Conversion into KWh.||
|CO2\_cons |CO2 consumption  |kg/m²  day |daily  |Resources |Processed data |Computed based on CO2 dosing (co2\_dos). Conversion from g to kg.  ||
|Irr |Irrigation water |L/m²  day |daily  |Resources |Processed data |Cumulative daily value of irrigation. This cumulation is reset to 0 at midnight.  ||
|Drain |Drain water  |L/m²  day |daily  |Resources |Processed data |Cumulative drain over a day. This cumulation is reset to 0 at midnight. ||
|Time |Timestamp date (Excel format) |||Resources ||||
## Tomato quality and Dry Matter Content 



|**Column heading** |**Parameter description** |**Unit** |**Interval** |**Dataset name** |**Data Type** |**Comments** |**Data collection/source** |
| - | - | - | - | - | - | - | :- |
|Flavour  |Flavour level |(0=dislike, 100=like) |Bi- weekly |TomQuality |Processed data |Calculated with Flavour Model Tomato version 2.1  (2011) |Smaaklab Wageningen University & Research**  |
|TSS |Total Soluble Solids  |` `°Brix |Bi- weekly |TomQuality |Processed data ||As above |
|Acid |Titratable acid  |(Acid, mmol H3O+/100gr) |Bi- weekly |TomQuality |Processed data ||As above |
|%Juice |Percentage juice pressed from the fruit wall of the tomato  |% |Bi- weekly |TomQuality |Processed data ||As above |
|Bite |Breaking force of the fruit wall |N |Bi- weekly |TomQuality |Processed data |It is an indicator of the perceived firmness during  chewing.  |As above |
|Weight |average fruit weight  |g |Bi- weekly |TomQuality |Processed data ||As above |
|DMC\_fruit |Fruit dry matter content  |% |Bi- weekly |TomQuality |Processed data ||As above |
|time |Timestamp date (Excel format) |||TomQuality ||||
## Lab analysis  



|**Column heading** |**Parameter description** |**Unit** |**Interval** |**Dataset name** |**Data Type** |**Comments** |**Data collection** |
| - | - | - | - | - | - | - | - |
|irr\_PH |pH of irrigation water |[-] |bi-weekly |LabAnalysis |Raw data |Analysis carried out on irrigation water sample |Laboratory analysis (Groen Agro Control) |
|irr\_EC |EC of irrigation water |[dS/m] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_NH4 |Ammonium concentration in irrigation water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_K |Potassium concentration in irrigation water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_Na |Sodium concentration in irrigation water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_Ca |Calcium concentration in irrigation water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_Mg |Magnesium concentration in irrigation water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_Si |Silicon concentration in irrigation water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_NO3 |Nitrate concentration in irrigation water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_Cl |Chlorine concentration in irrigation water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_SO4 |Sulfate concentration in irrigation water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_HCO3 |Bicarbonate Ion concentration in irrigation water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_PO4 |Phosphate concentration in irrigation water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_Fe |Iron concentration in irrigation water |[µmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_Mn |Manganese concentration in irrigation water |[µmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_Zn |Zinc concentration in irrigation water |[µmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_B |Boron concentration in irrigation water |[µmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_Cu |Copper concentration in irrigation water |[µmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|irr\_Mo |Molybdenum concentration in irrigation water |[µmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_PH |pH of drainage water |[-] |bi-weekly |LabAnalysis |Raw data |Analysis carried out on drainage water sample |As above |
|drain\_EC |EC of drainage water |[dS/m] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_NH4 |Ammonium concentration in drainage water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_K |Potassium concentration in drainage water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_Na |Sodium concentration in drainage water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_Ca |Calcium concentration in drainage water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_Mg |Magnesium concentration in drainage water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_Si |Silicon concentration in drainage water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_NO3 |Nitrate concentration in drainage water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_Cl |Chlorine concentration in drainage water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_SO4 |Sulfate concentration in drainage water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_HCO3 |Bicarbonate Ion concentration in drainage water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_PO4 |Phosphate concentration in drainage water |[mmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_Fe |Iron concentration in drainage water |[µmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_Mn |Manganese concentration in drainage water |[µmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_Zn |Zinc concentration in drainage water |[µmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_B |Boron concentration in drainage water |[µmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_Cu |Copper concentration in irrigation water |[µmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|drain\_Mo |Molybdenum concentration in drainage water |[µmol/l] |bi-weekly |LabAnalysis |Raw data |As above |As above |
|Time |Timestamp date (Excel format) |||LabAnalysis ||||
## Root zone data (Grodan sensors) 



|**Column heading** |**Parameter description** |**Unit** |**Interval** |**Dataset name** |**Data Type** |**Comments** |**Data collection** |
| - | - | - | - | - | - | - | - |
|EC\_slab1 |Electrical Conductivity  (Grodan sensor 1)   |dS/m |5 min  |GrodanSens |Processed |From 3 min to 5 minute data for consistency with the indoor climate dataset. Data available until May 26. |Grodan “Grosens” sensors|
|EC\_slab2 |Electrical Conductivity  (Grodan sensor 2)   |dS/m |5 min  |GrodanSens |Processed |As above |Grodan “Grosens” sensors|
|WC\_slab1 |Slab water content (Grodan sensor 1) |% |5 min  |GrodanSens |Processed |As above |Grodan “Grosens” sensors|
|WC\_slab2 |Slab water content (Grodan sensor 2) |% |5 min  |GrodanSens |Processed |As above |Grodan “Grosens” sensors|
|t\_slab1 |Slab temperature  (Grodan sensor 1) |°C |5 min  |GrodanSens |Processed |As above |Grodan “Grosens” sensors|
|t\_slab2 |Slab temperature  (Grodan sensor 2) |°C |5 min  |GrodanSens |Processed |As above |Grodan “Grosens” sensors|
|Time |Time |Time stamps 5 min (Excel format)\_ ||GrodanSens ||||

