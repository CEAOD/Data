# **International Autonomous Greenhouse Challenge - 3rd edition**

The dataset was generated for the needs of the 3rd International Autonomous Greenhouse Challenge in the experimental facilities of the Greenhouse Horticulture Business Unit in Bleiswijk, The Netherlands during the first lettuce experiment of 2022. Information regarding the competition can be found here [http://www.autonomousgreenhouses.com/](http://www.autonomousgreenhouses.com/).

**Contributor**: Autonomous Greenhouse Challenge Organizers

**Crop**: Lettuce

**Cultivar**: Lugano

**Location**: Bleiswijk, The Netherlands

**Duration**: Feb 01, 2022 - Mar 21, 2022

## Parameters' Description

The dataset contains data on outdoor and indoor greenhouse climate, status of actuators, realized climate setpoints ("Weather", "GreenhouseControls" and "GreenhouseClimate"), as well as, crop measurements during the experiment ("Destructive Measurements") the final harvest ("Final Harvest"), and plant density data.

Economic calculations are not included in the dataset. However, the prices for the computation of costs and income, thus net profit, can be found in the document "Economics" attached to the dataset.

The 5 greenhouse compartments have a total area of 96 m² and a growing area of 16 m².

The teams taking part in the challenge, thus contributing to the creation of the dataset, are:

- Team DigitalCucumbers: ....

- Team CVA: ...

- Team Koala: ...

- Team MondayLettuce: ...

- Team VeggieMight: ...

The Reference, represented by a group of WUR researchers, included the following members: ...

## Weather data

| **Column heading** | **Parameter description**                | **Unit**                        | **Interval** | **Dataset name** | **Data Type** | **Comments** | **Datacollection** |
|--------------------|------------------------------------------|---------------------------------|--------------|------------------|---------------|--------------|--------------------|
| Tout               | Outside temperature                      | °C                              | 5 min        | Weather          | Raw data      | -            | Weather station    |
| Rhout              | Outside relative humidity                | %                               | 5 min        | Weather          | Raw data      | -            | Weather station    |
| Iglob              | Solar Radiation                          | W/m²                            | 5 min        | Weather          | Raw data      | -            | Weather station    |
| Windsp             | Wind speed                               | m/s                             | 5 min        | Weather          | Raw data      | -            | Weather station    |
| RadSum             | Radiation sum                            | J/cm²                           | 5 min        | Weather          | Raw data      | -            | Weather station    |
| Winddir            | Wind direction                           | Compass direction [0 to 128]    | 5 min        | Weather          | Raw data      | -            | Weather station    |
| Rain               | Rain (status 1=rain, 0=dry)              | [1=rain, 0=dry]                 | 5 min        | Weather          | Raw data      | -            | Weather station    |
| PARout             | PAR weather measurement                  | µmol/m²s                        | 5 min        | Weather          | Raw data      | -            | Weather station    |
| Pyrgeo             | Heat emission: pyrgeometer               | W/m²                            | 5 min        | Weather          | Raw data      | -            | Weather station    |
| AbsHumOut          | Absolute humidity content of outside air | g/m³                            | 5 min        | Weather          | Raw data      | -            | Weather station    |
| Date               | Time                                     | dd-mm-yyyy HH:MM (Excel format) | 5 min        | Weather          | Raw data      | -            | Weather station    |

Greenhouse indoor climate

| **Column heading** | **Parameter description**                                                | **Unit**                        | **Interval** | **Dataset name**  | **Data Type** | **Comments**                                                                                                                                                                                        | **Data collection** |
|--------------------|--------------------------------------------------------------------------|---------------------------------|--------------|-------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Tair               | Greenhouse Air temperature                                               | °C                              | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Process Computer    |
| Rhair              | Greenhouse relative humidity                                             | %                               | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Process Computer    |
| CO2air             | CO2 greenhouse                                                           | ppm                             | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Process Computer    |
| HumDef             | Greenhouse humidity deficit                                              | g/m³                            | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Process Computer    |
| VentLee            | Leeward vents opening                                                    | % [0 to 100]                    | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Process Computer    |
| Ventwind           | Windward vents opening                                                   | % [0 to 100]                    | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Process Computer    |
| AssimLight         | LED lamps status(on-off)                                                 | % [0 or 100]                    | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Process Computer    |
| EnScr              | Energy curtain opening                                                   | % [0 to 100]                    | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Process Computer    |
| BlackScr           | Blackout curtain opening                                                 | % [0 to 100]                    | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Process Computer    |
| Tpipe              | Rail pipe Temperature (Lower circuit)                                    | °C                              | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Process Computer    |
| CO2reg             | CO2 regulation                                                           | [0 to 1]                        | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Process Computer    |
| PARin              | PAR sum from LED lamps and solar radiation                               | µmol/m²s                        | 5 min        | GreenhouseClimate | Raw data      | Measured above the crop level. Accounts for the proportional control of dimmable LEDS with a maximum contribution of LEDS 270µmol/m²s for all teams except the Reference with 150 µmol/m²s          | Process Computer    |
| Tair_sigrow        | Greenhouse Air temperature measured by the Sigrow sensor                 | °C                              | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Sigrow sensor       |
| Rhair_sigrow       | Greenhouse relative humidity measured by the Sigrow sensor               | %                               | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Sigrow sensor       |
| PARin_sigrow       | PAR sum from LED lamps and solar radiation measured by the Sigrow sensor | µmol/m²s                        | 5 min        | GreenhouseClimate | Raw data      | Measured slightly above the crop level. Accounts for the proportional control of dimmable LEDS with a maximum contribution of LEDS 270µmol/m²s for all teams except the Reference with 150 µmol/m²s | Sigrow sensor       |
| Netrad_ridder      | Estimated net radiation in teh greenhouse                                | W/m2                            | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Ridder soft sensor  |
| Transp_ridder      | Estimated crop transpiration                                             | g/m2                            | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Ridder soft sensor  |
| Tleaf_ridder       | Estimated leaf temperature                                               | °C                              | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Ridder soft sensor  |
| Date               | Time                                                                     | dd-mm-yyyy HH:MM (Excel format) | 5 min        | GreenhouseClimate | Raw data      | -                                                                                                                                                                                                   | Process Computer    |

## VIP (realized setpoints)

| **Column heading** | **Parameter description**                           | **Unit**                        | **Interval** | **Dataset name**   | **Data Type** | **Comments** | **Data collection** |
|--------------------|-----------------------------------------------------|---------------------------------|--------------|--------------------|---------------|--------------|---------------------|
| CO2_vip            | CO2 VIP                                             | ppm                             | 5 min        | GreenhouseControls | Raw data      | -            | Process Computer    |
| dx_vip             | Humidity deficit VIP                                | g/m³                            | 5 min        | GreenhouseControls | Raw data      | -            | Process Computer    |
| heating_temp_vip   | Heating temperature VIP                             | °C                              | 5 min        | GreenhouseControls | Raw data      | -            | Process Computer    |
| net_pipe_vip       | Rail pipe minimum temperature VIP                   | °C                              | 5 min        | GreenhouseControls | Raw data      | -            | Process Computer    |
| assim_vip          | Assimilation lighting VIP (HPS lamp)                | % [0 or 100]                    | 5 min        | GreenhouseControls | Raw data      | -            | Process Computer    |
| scr_enrg_vip       | Energy curtain VIP                                  | % [0 or 100]                    | 5 min        | GreenhouseControls | Raw data      | -            | Process Computer    |
| scr_blck_vip       | Blackout curtain VIP                                | % [0 or 100]                    | 5 min        | GreenhouseControls | Raw data      | -            | Process Computer    |
| t_ventlee_vip      | Ventilation temperature VIP (leeward vents)         | °C                              | 5min         | GreenhouseControls | Raw data      | -            | Process Computer    |
| lee_wind_min_vip   | Leeside window position minimum VIP (leeward vents) | %                               | 5 min        | GreenhouseControls | Raw data      | -            | Process Computer    |
| Date               | Time                                                | dd-mm-yyyy HH:MM (Excel format) | 5 min        | GreenhouseControls | Raw data      | -            | Process Computer    |

## Greenhouse Crop – "Final Harvest" Sheet

| **Column heading** | **Parameter description**                       | **Unit**                                               | **Interval**       | **Dataset name**               | **Data Type** | **Comments**                                                                                 | **Data collection** |
|--------------------|-------------------------------------------------|--------------------------------------------------------|--------------------|--------------------------------|---------------|----------------------------------------------------------------------------------------------|---------------------|
| Plant number       | Sampled plant                                   | #                                                      | At date of harvest | GreenhouseCrop "Final Harvest" | Raw data      |                                                                                              | Manual registration |                                                                                           |                     |
| Greenhouse side    | Side of growing area that the plant was sampled | [L -left R-right]                                      | At date of harvest | GreenhouseCrop "Final Harvest" | Raw data      | There are growing gutters in two sides in the greenhouse under the growing area of the 16m2. | Manual registration |
| Tip-burn           | Tip burn occurrence in sampled lettuces         | [scale=1,scale=5]                                      | At date of harvest | GreenhouseCrop "Final Harvest" | Raw data      | Sampled lettuce is classified for tip burn occurrence within a scale of 1-5                  | Manual registration |
| Fresh Weight       | Fresh weight of sampled lettuce                 | gr                                                     | At date of harvest | GreenhouseCrop "Final Harvest" | Raw data      | Sampled lettuce is weighed manually on scales                                                | Manual registration |
| Height             | Height of lettuce head                          | cm                                                     | At date of harvest | GreenhouseCrop "Final Harvest" | Raw data      | Height of sampled lettuce                                                                    | Manual registration |
| Width              | Width of lettuce head                           | cm                                                     | At date of harvest | GreenhouseCrop "Final Harvest" | Raw data      | Diameter of sampled lettuce                                                                  | Manual registration |
| Dry Weight         | Dry weight of sampled lettuce                   | gr                                                     | At date of harvest | GreenhouseCrop "Final Harvest" | Raw data      | Sampled lettuce is evaluated for botrytis appearance                                         | Manual registration |
| Botrytis           | Botrytis appearance in sampled plants           | [appearance=x, absence=-]                              | At date of harvest | GreenhouseCrop "Final Harvest" | Raw data      | This refers to 10 sample stems (total value)                                                 | Manual registration |
| Class A            | Classification of sampled lettuce as class A    | [assignment as class A=x, assignment as other class=-] | At date of harvest | GreenhouseCrop "Final Harvest" | Raw data      |                                                                                              | Manual registration |
| Class B            | Classification of sampled lettuce as class B    | [assignment as class B=x, assignment as other class=-] | At date of harvest | GreenhouseCrop "Final Harvest" | Raw data      | -                                                                                            | Manual registration |
| Class C            | Classification of sampled lettuce as class C    | [assignment as class C=x, assignment as other class=-] | At date of harvest | GreenhouseCrop "Final Harvest" | Raw data      | -                                                                                            | Manual registration |
| Date               | Time                                            | dd-mm-yyyy HH:MM (Excel format)                        | Daily              | GreenhouseCrop "Final Harvest" | Raw data      | -                                                                                            | Manual registration |

## Greenhouse Crop – "Plant Density" Sheet

| **Column heading** | **Parameter description**                   | **Unit**                        | **Interval** | **Dataset name**               | **Data Type** | **Comments** | **Data collection** |
|--------------------|---------------------------------------------|---------------------------------|--------------|--------------------------------|---------------|--------------|---------------------|
| Plant density      | Number of lettuce heads per m2 growing area | heads/m2                        | Daily        | GreenhouseCrop "Plant Density" | Raw data      | -            | Data Interface      |
| Date               | Time                                        | dd-mm-yyyy HH:MM (Excel format) | Daily        | GreenhouseCrop "Plant Density" | Raw data      | -            | Data Interface      |
