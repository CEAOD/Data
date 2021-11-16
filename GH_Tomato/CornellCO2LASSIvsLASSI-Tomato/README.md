# CO2 LASSI VS LASSI
**Treatments**: Tomatoes were grown in two greenhouses in Ithaca, NY; one greenhouse recieved CO2 LASSI treatment (light and CO2 were integrated to target a “virtual” DLI of 25 mol/m2/d) while the other recieved instead a LASSI treatment (DLI of 25 mol/m2/d was targeted) which did not supplement CO2.

**Location**: Ithaca, NY

**Citation**: Experiment was Chapter 2 (_Effects of a Coordinated Supplemental Lighting and CO2 Control Strategy on Tomato Yield and Quality_) of the M.S. Thesis by Masaki Kurosaki at Cornell University, 2021. Advisor: Dr. Neil Mattson 

**Contact**: Dr. Neil Mattson, neil.mattson@cornell.edu

**Funding**: This project was funded as part of the Greenhouse Lighting and Systems Engineering (GLASE) consortium by the New York State Energy Research & Development Authority.

**Related data**: [A similar data set is available for strawberries.](../../GH_Strawberry/CornellCO2LASSIvsLASSI-Strawberry/)

## Environmental Data:

Environmental data was measured every minute and averaged over 5 minute intervals.

**Temp (F)**
Greenhouse air temperature in Fahrenheit 

**RH (%)**
Greenhouse air relative humidity in percent

**Light Bench 1,2,3 Final State (%)**
Percentage of time the Lights were on during the 5 minute interval.  100% represents ON for 5 minutes, 0% represents OFF for the entire time.

**Shade Roof Current Timed Position (%)**
100% represents a retracted shade curtain providing no shade to the greenhouse
0% represents a closed shade curtain (shading the greenhouse)

**PAD Vent Shutter Current Timed Position (%)**
Cooling pad shutter open/close
100% - fully open
0% - fully closed

**Exhaust Fans VFD Current Timed Position (%)**
100% exhaust fans fully on
0% exhaust fans off

**PPFD (umol/m2/s)**
measured light values

**DLI (mol/m2/d)**
A running integral updating every time interval

**CO2(ppm)**
Measured CO2 in greenhouse with circulation fans running continually.  Missing values filled with 400 to enable virtual growth/DLI calculations

**Virtual Growth**
PPFD modified by CO2 values for each time interval

**Virtual DLI**
A running summation of Virtual Growth

**Daily Virtual DLI**
The final value of the day’s virtual DLI at sunrise.

**Daily DLI**
The final value of the day’s DLI at sunrise.


## Harvest Data:

All weights were measured in grams

**Barcode**
Unique plant identification code.  Plants coded with a leading 1 received CO2 LASSI treatment (light and CO2 were integrated to target a “virtual” DLI of 25 mol/m2/d)  Plants coded with a leading 2 were in an greenhouse without enriched CO2 receiving a LASSI treatment (DLI of 25 mol/m2/d was targeted).

All fruits on a truss were harvested at the stage when 90% of the surface of representative fruits were red.

**Total Weight**
Complete fresh weight of a truss before further processing including fruit and truss stems

**Fruit Number**
The total number of fruits harvested in a given week

**Fruit Fresh Weight**
The weight of 3 representative fruit per cluster

**Brix**
A measure of dissolved sugar (number of grams of sucrose in 100 grams of solution). Data were taken Three fruits per truss were used to measure °Brix with a refractometer (HI96801, Hanna Instruments, Woonsocket, RI).

**Truss Weight**
The fresh weight of the truss stem supporting each fruit (i.e. the peduncles connecting to the fruit)

**Total Fruit Weight**
The fresh weight of all the fruit on a truss (determined as the Total Weight minus the Truss Weight)

**Fruit Dry Weight**
Weight of three representative fruit after moisture removed (fruit were dried in an oven at 70 C for three days)

**D/F**
Ratio of fruit dry weight to fresh weight (Fruit Dry Weight/Total Fruit Fresh Weight)

**Total DW**
The total fruit dry weight (calculate from the dry weight of three fruit multiplied by the D/F (i.e. raio of dry weight to fresh weight)

**Individual Fruit Weight**
Fresh weight of individual fruit, calculated as the Total Fruit Weight/Fruit Number

**Red Fruit Weight**
Individual fruit fresh weight based on the 3 representative fruit used for dry weights

**FW:DW**
Ratio of fresh weight to dry weight (calculated as Total Fruit Weight/Total DW)

**Drymatter%**
Percent dry matter (calculated as Total DW/Total Fruit Weight *100)

