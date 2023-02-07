# **International Autonomous Greenhouse Challenge - 3rd edition - 2nd experiment**

**Contributor**: Koala Team, [Koidra Tech Inc.](https://koidra.ai) - Winner of the 3rd International Autonomous Greenhouse Challenge.

**Crop**: Lettuce

**Cultivar**: Lugano

**Location**: Bleiswijk, The Netherlands

**Duration**: May 02, 2022 to June 17, 2022

**Note**: There is no plant data until date. Approximated plant weight for each team can be found on [this video](https://youtu.be/s2Ap7HcGPiI?t=13868) from the organizers.

**License**: MIT

## **Time-series datasets**

The dataset contains data on outdoor and indoor greenhouse climate, status of actuators, realized climate setpoints, and plant density data.

Economic calculations are not included in the dataset. However, the prices for the computation of costs and income, thus net profit, can be found in the competition document (`Greenhouse climate control`), section `Economics`.

The five greenhouse compartments have a total area of 96 m² and a growing area of 16 m². The participating teams in the challenge, who contributed to the creation of the dataset, are:

-   Team DigitalCucumbers

-   Team CVA

-   Team Koala

-   Team MondayLettuce

-   Team VeggieMight

-   The Reference, represented by a group of WUR researchers

### **Weather data**

| **Column heading** | **Parameter description**   | **Unit**                     |
| ------------------ | --------------------------- | ---------------------------- |
| T_Out              | Outside temperature         | °C                           |
| airflow_Out        | Wind speed                  | m/s                          |
| heat_emission      | Heat emission: pyrgeometer  | W/m²                         |
| is_rain            | Rain (status 1=rain, 0=dry) | [1=rain, 0=dry]              |
| par_Out            | PAR weather measurement     | µmol/m²s                     |
| rad_Out            | Solar radiation             | W/m²                         |
| rad_Out_sum        | Radiation sum               | J/cm²                        |
| rh_Out             | Outside relative humidity   | %                            |
| wind_direction     | Wind direction              | Compass direction [0 to 128] |
| timestamp          | Time                        | yyyy-mm-dd HH:MM:SS          |

### **Indoor climate data**

| **Column heading**             | **Parameter description**                                                | **Unit**            | **Comments**                                                                                                                                                                                        |
| ------------------------------ | ------------------------------------------------------------------------ | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| T_Air                          | Greenhouse air temperature                                               | °C                  | -                                                                                                                                                                                                   |
| rh_Air                         | Greenhouse relative humidity                                             | %                   | -                                                                                                                                                                                                   |
| co2_Air                        | CO2 greenhouse                                                           | ppm                 | -                                                                                                                                                                                                   |
| humidity_deficit               | Greenhouse humidity deficit                                              | g/m³                | -                                                                                                                                                                                                   |
| lee_vent                       | Leeward vents opening                                                    | % [0 to 100]        | -                                                                                                                                                                                                   |
| wind_vent                      | Windward vents opening                                                   | % [0 to 100]        | -                                                                                                                                                                                                   |
| thermal_opening                | Energy curtain opening                                                   | % [0 to 100]        | -                                                                                                                                                                                                   |
| blackout_opening               | Blackout curtain opening                                                 | % [0 to 100]        | -                                                                                                                                                                                                   |
| net_radiation\_\_ridder        | Estimated net radiation in the greenhouse                                | W/m2                | -                                                                                                                                                                                                   |
| T_Canopy\_\_ridder             | Estimated leaf temperature                                               | °C                  | -                                                                                                                                                                                                   |
| transpiration\_\_ridder        | Estimated crop transpiration                                             | g/m2                | -                                                                                                                                                                                                   |
| rh_Air\_\_sigrow               | Greenhouse relative humidity measured by the Sigrow sensor               | %                   | -                                                                                                                                                                                                   |
| T_Air\_\_sigrow                | Greenhouse Air temperature measured by the Sigrow sensor                 | °C                  | -                                                                                                                                                                                                   |
| par\_\_sigrow                  | PAR sum from LED lamps and solar radiation measured by the Sigrow sensor | µmol/m²s            | Measured slightly above the crop level. Accounts for the proportional control of dimmable LEDS with a maximum contribution of LEDS 270µmol/m²s for all teams except the Reference with 150 µmol/m²s |
| stomata_conductivity\_\_sigrow | Stomatal conductance measured by the Sigrow sensor                       | mmol/m²s            | -                                                                                                                                                                                                   |
| par                            | PAR sum from LED lamps and solar radiation                               | µmol/m²s            | Measured above the crop level. Accounts for the proportional control of dimmable LEDS with a maximum contribution of LEDS 270µmol/m²s for all teams except the Reference with 150 µmol/m²s          |
| timestamp                      | Time                                                                     | yyyy-mm-dd HH:MM:SS | -                                                                                                                                                                                                   |

### **Operational data**

| **Column heading**      | **Parameter description**                                                     | **Unit**   |
| ----------------------- | ----------------------------------------------------------------------------- | ---------- |
| effective_plant_density | Effective plant density (a.k.a average head per meter square until that date) | plant/m2   |
| fixed_total_wur         | Total fixed cost                                                              | Euro/m2    |
| fixed_plants            | Fixed cost for plants                                                         | Euro/m2    |
| fixed_gh                | Fixed cost for renting greenhouse                                             | Euro/m2    |
| fixed_light             | Fixed cost for buying supplemental lamps                                      | Euro/m2    |
| fixed_co2               | Fixed cost for buying CO2 dosing system                                       | Euro/m2    |
| var_electricity         | Variable cost for using electricity                                           | Euro/m2    |
| var_gas                 | Variable cost for using gas                                                   | Euro/m2    |
| var_co2                 | Variable cost for using CO2                                                   | Euro/m2    |
| var_penalty             | Variable cost for being penaltied                                             | Euro/m2    |
| plant_density           | Plant density at that time                                                    | plant/m2   |
| timestamp               | Time                                                                          | yyyy-mm-dd |

## **References**

\[1] Hemming, S. (2022, September 15). [**Familiar face leads 'team koala' to win the Autonomous Greenhouse Challenge for a second time**](https://www.wur.nl/en/newsarticle/familiar-face-leads-team-koala-to-win-the-autonomous-greenhouse-challenge-for-a-second-time.htm). WUR. 

\[2] Stiffler, L. (2022, August 30). [**How a former Microsoft researcher used AI to grow award-winning lettuce from 5,000 miles away**](https://www.geekwire.com/2022/how-a-former-microsoft-researcher-used-ai-to-grow-award-winning-lettuce-from-5000-miles-away/). GeekWire. 