**Description of ‘Indoor strawberry phenotyping data’**

Excel file ‘Characterizing the Growth, Morphology, Productivity, and Fruit Quality of Twenty-Three Strawberry Cultivars in an Indoor Environment with Sole Source Electric Lighting’. The description of this experiment is described by Lin et al. (2025) published in Frontiers in Horticulture (doi.org/10.3389/fhort.2025.1621763).

Objective of this data collection: To identify strawberry cultivars with traits desirable for indoor farming.

Funding source: FFAR (Award #21-000051)

Data collected by: Yiyun Lin

Contact person: Chieri Kubota ([kubota.10@osu.edu](mailto:kubota.10@osu.edu))

Data collection site: a walk-in growth chamber at the Controlled Environment Food Production Research Complex (CEARC) at The Ohio State University (Columbus, OH).

Experiment: Twenty-three publicly available strawberry cultivars were selected from the USDA-ARS National Clonal Germplasm Repository and evaluated in a walk-in growth chamber to identify cultivars with high productivity, early production, low sensitivity to dormancy-inducing short-day environment, and desirable fruit quality. More specific conditions and experimental design can be found in our publication, Lin et al. (2025).

Data collected:

**Indoor strawberry phenotyping productivity data**

| Data label | Description |
| --- | --- |
| Cultivar name | Strawberry cultivar name |
| Cultivar ID | A specific ID was assigned to each cultivar in Kubota Lab |
| Replicate | Plant replicate |
| Average weekly yield (g) | Average weekly yield (g) was calculated per plant as the total fruit weight divided by the number of weeks from the week of the first harvest to the week when the 200-g harvest goal was reached |
| Maximum weekly yield (g) | Maximum weekly yield (g) was defined as the highest yield produced per plant in one week |
| Time to first flower from transplant (d) | Number of days from transplanting to first open flower |
| Time to first harvest from transplant (d) | Number of days from transplanting to first fruit harvest |
| Flower to fruit harvest time (d) | Number of days from first open flower to first fruit harvest |
| Average fruit size (g) | Average fruit size (g) was calculated as the total fruit fresh weight divided by the total number of fruit |

**Indoor strawberry phenotyping fruit morphology & firmness data**

| Data label | Description |
| --- | --- |
| Cultivar name | Strawberry cultivar name |
| Cultivar ID | A specific ID was assigned to each cultivar in Kubota Lab |
| Replicate | Plant replicate |
| Subsample | Three strawberry fruits were used as subsamples |
| Calyx to fruit area ratio | Calyx to fruit area ratio was calculated by dividing the calyx area with fruit interior area |
| Fruit diameter to length ratio | Fruit diameter to length ratio was calculated by dividing maximum fruit width using maximum fruit length |
| Fruit interior NDAI | The Normalized difference anthocyanin index (NDAI) of fruit interior measured using imaging-base analysis |
| Fruit exterior NDAI | The Normalized difference anthocyanin index (NDAI) of fruit exterior measured using imaging-base analysis |
| Fruit firmness (N) | Firmness of fruit measured using a texture analyzer |

**Indoor strawberry phenotyping fruit Brix & TA data**

| Data label | Description |
| --- | --- |
| Cultivar name | Strawberry cultivar name |
| Cultivar ID | A specific ID was assigned to each cultivar in Kubota Lab |
| Replicate | Plant replicate |
| Brix (%) | Fruit total soluble solids (TSS) |
| TA (g/L) | Fruit titratable acidity (citric acid equivalent) |
| Brix to TA ratio | Brix to TA ratio |

**Indoor strawberry phenotyping plant morphology data**

| Data label | Description |
| --- | --- |
| Cultivar name | Strawberry cultivar name |
| Cultivar ID | A specific ID was assigned to each cultivar in Kubota Lab |
| Replicate | Plant replicate |
| Maximum height (cm) | The largest plant height in six months after transplant |
| Maximum projected canopy area (cm2) | The largest plant canopy area in six months after transplant |
| SD-LD plant height difference (%) | The percent change in plant height (%) from SD to LD photoperiod calculated as (heightLD - heightSD)/ heightSD, indicating plant sensitivity to dormancy-inducing SD photoperiod |

Data collection methods:

*   Each cultivar included three plants as replicates, and one plant per cultivar was included in each block.
*   Time to first flower (d) and time to first harvest (d) from transplanting were recorded for each plant. The first fully open flower of each plant was considered as the first flower. Fruit was deemed harvestable when the redness reached the top row of achenes.
*   Fruit was harvested at least three times a week, and the fresh weight of each harvest and the number of fruit were recorded. Average fruit size was calculated as the total fruit fresh weight divided by the total number of fruit.
*   The harvest goal for each plant was 200 g, and the number of weeks from the first harvest to when the harvest goal was reached was recorded. Average weekly yield (g) was calculated as the total fruit weight divided by the number of weeks from first harvest to when the harvest goal was reached.
*   Maximum weekly yield (g) was defined as the highest yield produced in one week.
*   Three representative fruits were selected as subsamples to represent color and fruit shape from each plant.
*   The calyx was separated from the fruit, and the fruit was dissected into two halves lengthwise along the widest side. The calyx, and the exterior and the interior of the fruit were scanned using a desktop scanner (CanoScan LiDE 210, Canon, Tokyo, Japan) covered with a black cloth. The scanned RGB images were analyzed using the Python program described above to determine calyx area (cm2), fruit interior total area (cm2), fruit diameter (cm), and fruit length (cm). Fruit diameter and length were the maximum width and length of the cross section, respectively.
*   Fruit interior redness and fruit exterior redness were quantified using the normalized difference anthocyanin index (NDAI) reported by Kim and van Iersel (2023). Specifically, the pixel intensities of the red and green channels of the scanned images (Ired and Igreen) were used to calculate the NDAI values of the fruit objects using the equation: NDAI=(Ired−Igreen)/(Ired+Igreen).
*   Fruit firmness (N) was measured with an additional three fruits as sub-samples using a texture analyzer (TA.XTPlus, Stable Micro Systems Texture Technologies, Scarsdale, NY, USA) fitted with a 4-mm probe. The fruits were harvested into a tray with ice and transported immediately to the lab on ice for firmness measurements to eliminate change of fruit texture. Each fruit was dissected into two halves and 25% of the halved fruit was penetrated at a speed of 1.7 mm s\-1. The maximum gram force developed during the test was recorded and converted to Newton (N).
*   The concentration of fruit total soluble solids (TSS, or Brix) was analyzed with the supernatant of 50-g pureed fruit using a digital refractometer (PR-32 alpha, ATAGO, Tokyo, Japan).
*   Titratable acidity (TA, g L\-1) was analyzed using the supernatant of 50-g pureed fruit gradually titrated with NaOH. The pH was monitored using a pH meter (accumet AB150, Thermo Fisher Scientific, Waltham, MA, USA) and TA was determined using citric acid as the representative acid.
*   Plant height (cm) from the top of the substrate to the highest point of the plant shoot was measured using a ruler. The maximum values of plant height of each plant were selected to be the maximum plant height.
*   Images of the plant canopies were collected and analyzed in a custom-made image analyzer operated with a Python program (v. 3.8) using the OpenCV library (v. 4.5.4) following the approach by Kim and van Iersel (2023). Specifically, plant objects and backgrounds in the images were separated using intensity-based thresholding with the saturation channel in the HSV color model. The number of pixels in the plant objects was counted and converted into length (cm) and area (cm2) based on a reference scale. The maximum values of projected canopy area of each plant were selected to be the maximum projected canopy area.
*   Plant sensitivity to dormancy-inducing SD photoperiod was quantified by the percent change in plant height (%), which was calculated as the percent difference between the average plant height under SD and LD conditions: (heightLD - heightSD)/ heightSD, where heightSD was determined using plant height measured after plants were grown five and nine weeks in SD environment, and heightLD was determined using plant height measured after plants were grown seven weeks in LD environment.

Data collection: 3/22/2023 - 11/8/2023

References:

Lin, Y., Kim, C., Bassil, N. V., Oliphant, J. J., Hardigan, M. A., and Kubota, C. 2025. Characterizing the growth, morphology, productivity, and fruit quality of twenty-three strawberry cultivars in an indoor environment with sole source electric lighting. Front. Hortic. 4: 1621763. https://doi.org/10.3389/fhort.2025.1621763.