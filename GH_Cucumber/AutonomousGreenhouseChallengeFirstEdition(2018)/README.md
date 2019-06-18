# Autonomous Greenhouse Challenge 2018
**Organizer website**: https://www.autonomousgreenhouses.com/
**Dataset source**: [https://data.4tu.nl/repository/uuid:e4987a7b-04dd-4c89-9b18-883aad30ba9a](https://data.4tu.nl/repository/uuid:e4987a7b-04dd-4c89-9b18-883aad30ba9a)
  

# Dataset Description
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