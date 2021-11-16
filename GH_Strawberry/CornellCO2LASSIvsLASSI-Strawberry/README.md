# CO2 LASSI VS LASSI
**Treatments**: Strawberries were grown in two greenhouses in Ithaca, NY; one greenhouse recieved CO2 LASSI treatment (light and CO2 were integrated to target a “virtual” DLI of 20 mol/m2/d) while the other recieved instead a LASSI treatment (DLI of 20 mol/m2/d was targeted) which did not supplement CO2.

**Location**: Ithaca, NY

**Citation**: Experiment will be Chapter 2 (_Greenhouse Application – Supplemental Light and Carbon Dioxide Interactions Affect Strawberry Yield, Fruit Quality and Energy Consumption_) of the Ph.D. Thesis by Jonathan Asher Karall at Cornell University, 2021. Advisor: Dr. Neil Mattson.

**Funding**: This project was funded as part of the Greenhouse Lighting and Systems Engineering (GLASE) consortium by the New York State Energy Research & Development Authority.

**Related data**: [A similar data set is available for tomatoes.](../CornellCO2LASSIvsLASSI-Tomato/)


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

**Cultivar** 
cv. albion and cv. cabrillo (AL and CA respectively)

**Treatment** 
Control (LASSI) or CO2 LASSI algorithm used targeting 20 mol·m-2·d-1 daily light integral (DLI) or virtual DLI, respectively. Plants in troughs were grown for 4 weeks under 20 mol·m-2·d-1 acclimation/establishment before LASSI and CO2 LASSI treatments began on December 29, 2020. Treatments were delivered for 13 weeks. Plants were harvested twice weekly at the trough level.  


### “Harvest” Sheet:
Harvest data at the trough (i.e. bucket) level. Each trough had 4 plants of the same cultivar.

**TB#**
Total berry number.  A count of the number of berries harvested

**TBFW (g)**
Total Berry Fresh Weight

**TWF/Berry (g)**
Total fresh weight per berry calculated as the TBFW / TB#

**MB#** 
The number of marketable berries harvested. Marketability was defined as any berry greater than or equal to 10 g with a minimum 90% pigmentation and the absence of any fruit disfigurement (i.e. defects in pollination).

**MBFW (g)**
Total Marketable Berry Fresh Weight 

**MFW/Berry  (g)**
Total Marketable Berry Fresh Weight divided by the number of marketable berries


### “Harvest Sum” Sheet:

Data summed and averaged from Harvest sheet.


### “Brix & TA” Sheet:

**Berry #**
Identifying number for one berry of the three randomly selected berries sampled per condition

**Brix**
A measure of dissolved sugar (number of grams of sucrose in 100 grams of solution). Data were taken from a 0.5 mL sample of juice (after straining a pulp sample through a 10-mesh filter). °Brix was measured with a refractometer (HI96801, Hanna Instruments, Woonsocket, RI) 

**TA** 
Titratable Acidity. Samples were titrated with 0.1 M NaOH to a pH 8.1 end point using an automated endpoint titrator (DL12 Endpoint Titrator; Mettler Toledo LLC., Columbus, OH USA). units are grams per liter (g/L)


### “Plant Data” Sheet:
Collected at the conclusion of the treatments.

**Plant FW (g)**
Whole plant fresh weight

**Plant DW (g)**
Whole plant dry weight
