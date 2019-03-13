# __Int UVB Plant Data Kubota Eguchi__ and __Int UVB Environ Data Kubota Eguchi__

> Folders `IntUVBPlantDataKubotaEguchi` and `IntUVBEnvironDataKubotaEguchi` contains plant data and growth chamber environmental data collected during the experiment of testing varied doses of UV-B radiation on tomato plants (growth and incidence of physiological disorder called intumescence). The description of this experiment is described by Kubota et al. (2017) published in Scientia Horticulturae (http://dx.doi.org/10.1016/j.scienta.2017.09.006).  

__Objective of this data collection:__ To identify the minimum dose of UV-B radiation to maintain tomato plants without causing intumescence injury when tomato plants are grown under LEDs.  
__Funding source:__ USDA NIFA SCRI (Award #2011-51181-30963)  
__Data collected by:__ Tomomi Eguchi  
__Contact person:__ Chieri Kubota (kubota.10@osu.edu)  
__Data collection site:__ University of Arizona campus agriculture center growth chamber (Tucson, AZ)  

__Experiment:__ Tomato rootstock seedlings (cv. Beaufort) were grown under red/blue LEDs supplemented by different durations of UV-B radiation (0, 1.5, 3, and 6 hours) and when grown under T5 white fluorescent lamps. More specific conditions and experimental design can be found in our publication, Kubota et al. (2017).

## Data collected: 
### __IntUVB Plant Data Kubota Eguchi__
  - `IM_data.csv`
    - Name of treatment (Control = LEDs without UV-B radiation, UV1.5h = LEDs with 1.5-h per day UV-B radiation, UV3h = LEDs with 3-h per day UV-B radiation, UV6h = LEDs with 6-h per day UV-B radiation, WFL = T5 white fluorescent lamps)
    - Block # (1, 2, or 3)
    - Plant ID (each block has four plants with #1, #2, #3, and #4)
    - Number of leaves were counted for those true leaves greater than 10 mm leaf length.
    - Number of leaves showing intumescence injury
    - Percent number of leaves showing intumescence injury
    - Days after seeding when intumescence injuries were first noticed on a true leaf
    - Intumescence injury’s severity rating of individual leaves and cotyledons of tomato. The rating scale of 0–5 was used: 0 = no intumescence injury, 1 = intumescences covering less than 10% area, 2 = intumescences covering 10% to 50% area, 3 = intumescences covering 50% to 75% area, showing minor epinasty, 4 =intumescences covering 75% to 100% area, showing severe epinasty, 5 = leaf abscission (most severe).
    - Incidence of cotyledon drop (senescence) (0 = no, 1 = yes)
    - Intumescence injury seen on cotyledons (0 = no, 1 = yes)
    - Incidence of leaf drop (0 = no, 1 = yes)
    - Incidence of stem intumescence injury (0 = no, 1 = yes)

  - `Growth_data.csv`
    - Name of treatment (Control = LEDs without UV-B radiation, UV1.5h = LEDs with 1.5-h per day UV-B radiation, UV3h = LEDs with 3-h per day UV-B radiation, UV6h = LEDs with 6-h per day UV-B radiation, WFL = T5 white fluorescent lamps)
    - Block # (1, 2, or 3)
    - Plant ID (each block has four plants with #1, #2, #3, and #4)
    - Hypocotyl length (mm)
    - Epicotyl length (mm)
    - Shoot length (mm) 
    - Number of true leaves 
    - Stem diameter (mm)
    - Leaf area including cotyledons (cm2)
    - Leaf area without including cotyledons (cm2)
    - Shoot fresh weight (g)
    - Shoot dry weight (g) 

- Data collection methods and quality:
  - Plants were visually inspected every day to obtain the data in ‘IM data’ sheet. 
  - Length of hypocotyl and epicotyl was measured using an ordinary ruler (resolution 0.1 mm)
  - Length of shoot was derived as the sum of hypocotyl and epicotyl lengths. 
  - Number of leaves were counted for those true leaves greater than 10 mm leaf length.
  - Stem diameter was measured using a caliper (resolution 0.01 mm)
  - Leaf area (total cm2 per plant) including cotyledons, measured by scanning leaf and cotyledon images and analyzing the area using a software called LIA 32 (Nagoya University, Japan)
  - Leaf area (total cm2 per plant) without including cotyledons, measured by scanning leaf images and analyzing the area using a software called LIA 32 (Nagoya University, Japan)
  - Shoot fresh weight was measured using an electronic balance with a resolution of 0.0001 gram.
  - Shoot dry weight was measured using an electronic balance with a resolution of 0.0001 gram after drying shoot tissue sample at 60°C.


### __InvUVB Environ Data Kubota Eguchi__  
- `Data.csv`
  - ID – data row id number 
  - Year
  - Julian day
  - Date
  - Time in military format
  - LED1 and LED2 – air temperature inside two plant growth shelves equipped with LEDs (LED1 and LED2); unit oC [one location inside each shelf]
  - WFL - air temperature inside the plant growth shelf equipped with white fluorescent lamps; unit oC [one location inside shelf]
  - UV – air temperature inside a shelf equipped with a UV lamp; unit oC [one location inside the shelf] 
  - Air – air temperature inside the growth chamber; unit oC [one location at the center of the growth chamber]
  - RH – relative humidity inside the growth chamber; unit % [one location at the center of the growth chamber]
  - CO2 concentration inside the growth chamber; unit ppm ormol mol-1.

- Data collection methods and quality:
  - Air temperatures inside the plant growth shelves were measured using T-type thermocouples, calibrated for two measurement points in a water bath with certified reference thermometer. 
  - Air temperature and relative humidity inside the growth chamber were measured using a Vaisala temperature and humidity prove (model HMP10, Vaisala, Helsinki, Finland). As sensor was not under direct radiation, no radiation shield nor aspiration was applied in this sensor.  The sensors were new and manufacturer-calibrated prior to the start of data collection.  
  - All sensors were connected to a Campbell CR1000 data logger and the sensor readings were scanned every second to average over 5 min.  
  - CO2 concentration was measured with an infrared gas analyzer (Licor, Lincoln, NE) calibrated against zero and span gas (3?? ppm). 


__Data collection:__ 6/23/2016 - 7/8/2016  
__Data notation used:__  
- __M1:__ Missing value because no value is available.  

__Date the data set was last modified:__ 1/12/2019  

## References
Kubota, C., T. Eguchi, and M. Kroggel. 2017. UV-B radiation dose requirement for suppressing intumescence injury on tomato plants. Scientia Horticulturae 226:366-371.    [http://dx.doi.org/10.1016/j.scienta.2017.09.006](http://dx.doi.org/10.1016/j.scienta.2017.09.006) 
