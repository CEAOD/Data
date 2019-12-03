# Autonomous Greenhouse Challenge 2018

This contains data from the 1st edition of the [Autonomous Greenhouse Challenge](http://autonomousgreenhouses.com). The challenge and dataset are detailed in [Hemming et al.](https://www.mdpi.com/1424-8220/19/8/1807). There are 6 subdatasets, correponding to the 6 teams participating in the challenge. The dataset is kept in the original WUR's data collection format. (Note that Team Sonoma, [the winning team](https://venturebeat.com/2018/12/14/microsoft-researchers-beat-tencent-and-intel-in-autonomous-greenhouse-competition/), also [contributed their data](https://github.com/CEAOD/Data/tree/master/GH_Cucumber/MicrosoftResearch) in the format recommended in [CEAOD's data guidelines](https://ceaod.github.io/data-guide/).)  

See more details at [Hemming, S., de Zwart, F., Elings, A., Righini, I., & Petropoulou, A. Remote Control of Greenhouse Vegetable Production with Artificial Intelligence—Greenhouse Climate, Irrigation, and Crop Production. Sensors, 19(8). 2019](https://www.mdpi.com/1424-8220/19/8/1807).
> The global population is increasing rapidly, together with the demand for healthy fresh food. The greenhouse industry can play an important role, but encounters difficulties finding skilled staff to manage crop production. Artificial intelligence (AI) has reached breakthroughs in several areas, however, not yet in horticulture. An international competition on “autonomous greenhouses” aimed to combine horticultural expertise with AI to make breakthroughs in fresh food production with fewer resources. Five international teams, consisting of scientists, professionals, and students with different backgrounds in horticulture and AI, participated in a greenhouse growing experiment. Each team had a 96 m2 modern greenhouse compartment to grow a cucumber crop remotely during a 4-month-period. Each compartment was equipped with standard actuators (heating, ventilation, screening, lighting, fogging, CO2 supply, water and nutrient supply). Control setpoints were remotely determined by teams using their own AI algorithms. Actuators were operated by a process computer. Different sensors continuously collected measurements. Setpoints and measurements were exchanged via a digital interface. Achievements in AI-controlled compartments were compared with a manually operated reference. Detailed results on cucumber yield, resource use, and net profit obtained by teams are explained in this paper. We can conclude that in general AI performed well in controlling a greenhouse. One team outperformed the manually-grown reference. [1]


## Dataset Description
### The `meteo` dataset
| Column    | Parameter description                 | Unit          | Interval | Dataset name | Type     | Data collection |
|-----------|---------------------------------------|---------------|----------|--------------|----------|-----------------|
| Tout      | outside temperature                   | °C            | 5 min    | meteo        | raw data | Weather station |
| Rhout     | outside Relative Humidity             | %             | 5 min    | meteo        | raw data | Weather station |
| Iglob     | radiation                             | W/m2          | 5 min    | meteo        | raw data | Weather station |
| Windsp    | wind speed                            | m/s           | 5 min    | meteo        | raw data | Weather station |
| RadSum    | radiation sum                         | J/cm2         | 5 min    | meteo        | raw data | Weather station |
| Winddir   | wind direction                        | 0-360?        | 5 min    | meteo        | raw data | Weather station |
| Rain      | rain (status 1=rain, 0=dry)           | 1=rain, 0=dry | 5 min    | meteo        | raw data | Weather station |
| PARout    | PAR weather measurement               | µmol/m²/s     | 5 min    | meteo        | raw data | Weather station |
| Pyrgeo    | heat emission: pyrgeometer            | W/m2          | 5 min    | meteo        | raw data | Weather station |
| AbsHumOut | absolute humidity content outside air | g/m3          | 5 min    | meteo        | raw data | Weather station |
| Time      | Timestamp 5 minute (Excel format)     |               |          |              |          | Weather station |

### The other dataset
Describes in each team's directory
