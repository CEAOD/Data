# **International Autonomous Greenhouse Challenge - 3rd edition - 1st experiment**

The dataset was generated for the needs of the 3rd International Autonomous Greenhouse Challenge in the experimental facilities of the Greenhouse Horticulture Business Unit in Bleiswijk, The Netherlands during the first lettuce experiment of 2022. Information regarding the competition can be found here [http://www.autonomousgreenhouses.com/](http://www.autonomousgreenhouses.com/).

**Contributor**: Autonomous Greenhouse Challenge Organizers, processed by Koala Team, [Koidra Tech Inc.](https://koidra.ai) - Winner of the 3rd International Autonomous Greenhouse Challenge.

**Crop**: Lettuce

**Cultivar**: Lugano

**Location**: Bleiswijk, The Netherlands

**Duration**: February 1, 2022 to March 21, 2022

**License**: MIT


## **Time-series datasets**
The dataset contains data on outdoor and indoor greenhouse climate, status of actuators, realized climate setpoints, as well as crop measurements during the experiment, the final harvest, and plant density data.

Economic calculations are not included in the dataset. However, the prices for the computation of costs and income, thus net profit, can be found in the competition document, section `Economics`.

The five greenhouse compartments have a total area of 96 m² and a growing area of 16 m². The participating teams in the challenge, who contributed to the creation of the dataset, are:

- Team DigitalCucumbers

- Team CVA

- Team Koala

- Team MondayLettuce

- Team VeggieMight

- The Reference, represented by a group of WUR researchers

### **Climate - Weather data**

| **Column heading** | **Parameter description**                | **Unit**                        |
|--------------------|------------------------------------------|---------------------------------|
| Tout               | Outside temperature                      | °C                              |
| Rhout              | Outside relative humidity                | %                               |
| Iglob              | Solar radiation                          | W/m²                            |
| Windsp             | Wind speed                               | m/s                             |
| RadSum             | Radiation sum                            | J/cm²                           |
| Winddir            | Wind direction                           | Compass direction [0 to 128]    |
| Rain               | Rain (status 1=rain, 0=dry)              | [1=rain, 0=dry]                 |
| PARout             | PAR weather measurement                  | µmol/m²s                        |
| Pyrgeo             | Heat emission: pyrgeometer               | W/m²                            |
| AbsHumOut          | Absolute humidity content of outside air | g/m³                            |
| Date               | Time                                     | mm/dd/yyyy HH:MM  |

### **Climate - Greenhouse Indoor**

| **Column heading** | **Parameter description**                                                | **Unit**                        |**Comments**                                                                                                                                                                                        |
|--------------------|--------------------------------------------------------------------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tair               | Greenhouse Air temperature                                               | °C                              | -                                                                                                                                                                                                   |
| Rhair              | Greenhouse relative humidity                                             | %                               | -                                                                                                                                                                                                   |
| CO2air             | CO2 greenhouse                                                           | ppm                             | -                                                                                                                                                                                                   |
| HumDef             | Greenhouse humidity deficit                                              | g/m³                            | -                                                                                                                                                                                                   |
| VentLee            | Leeward vents opening                                                    | % [0 to 100]                    | -                                                                                                                                                                                                   |
| Ventwind           | Windward vents opening                                                   | % [0 to 100]                    | -                                                                                                                                                                                                   |
| AssimLight         | LED lamps status(on-off)                                                 | % [0 to 100]                    | -                                                                                                                                                                                                   |
| EnScr              | Energy curtain opening                                                   | % [0 to 100]                    | -                                                                                                                                                                                                   |
| BlackScr           | Blackout curtain opening                                                 | % [0 to 100]                    | -                                                                                                                                                                                                   |
| Tpipe              | Rail pipe temperature (Lower circuit)                                    | °C                              | -                                                                                                                                                                                                   |
| CO2reg             | CO2 regulation                                                           | [0 to 1]                        | -                                                                                                                                                                                                   |
| PARin              | PAR sum from LED lamps and solar radiation                               | µmol/m²s                        | Measured above the crop level. Accounts for the proportional control of dimmable LEDS with a maximum contribution of LEDS 270µmol/m²s for all teams except the Reference with 150 µmol/m²s          |
| Tair_sigrow        | Greenhouse Air temperature measured by the Sigrow sensor                 | °C                              | -                                                                                                                                                                                                   |
| Rhair_sigrow       | Greenhouse relative humidity measured by the Sigrow sensor               | %                               | -                                                                                                                                                                                                   |
| PARin_sigrow       | PAR sum from LED lamps and solar radiation measured by the Sigrow sensor | µmol/m²s                        | Measured slightly above the crop level. Accounts for the proportional control of dimmable LEDS with a maximum contribution of LEDS 270µmol/m²s for all teams except the Reference with 150 µmol/m²s |
| Netrad_ridder      | Estimated net radiation in the greenhouse                                | W/m2                            | -                                                                                                                                                                                                   |
| Transp_ridder      | Estimated crop transpiration                                             | g/m2                            | -                                                                                                                                                                                                   |
| Tleaf_ridder       | Estimated leaf temperature                                               | °C                              | -                                                                                                                                                                                                   |
| Date               | Time                                                                     | mm/dd/yyyy HH:MM                | -                                                                                                                                                                                                   |

### **Climate - Realized setpoints**

| **Column heading** | **Parameter description**                           | **Unit**                        |
|--------------------|-----------------------------------------------------|---------------------------------|
| CO2_vip            | CO2 setpoints                                             | ppm                             |
| dx_vip             | Humidity deficit setpoints                                | g/m³                            |
| heating_temp_vip   | Heating temperature setpoints                             | °C                              |
| net_pipe_vip       | Rail pipe minimum temperature setpoints                   | °C                              |
| assim_vip          | Assimilation lighting setpoints (HPS lamp)                | % [0 to 100]                    |
| scr_enrg_vip       | Energy curtain setpoints                                  | % [0 to 100]                    |
| scr_blck_vip       | Blackout curtain setpoints                                | % [0 to 100]                    |
| t_ventlee_vip      | Ventilation temperature setpoints (leeward vents)         | °C                              |
| lee_wind_min_vip   | Leeside window position minimum setpoints (leeward vents) | %                               |
| Date               | Time                                                | mm/dd/yyyy HH:MM                |

### **Crop – Final Harvest**

| **Column heading** | **Parameter description**                       | **Unit**                                               | **Comments**                                                                                 | 
|--------------------|-------------------------------------------------|--------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Plant number       | Sampled plant                                   |                                                        |                                                                                              |
| Greenhouse side    | Side of growing area that the plant was sampled | [L - left, R - right]                                  | There are growing gutters in two sides in the greenhouse under the growing area of the 16m2. |
| Tip-burn           | Tip burn occurrence in sampled lettuces         | [scale=1, scale=5]                                     | Sampled lettuce is classified for tip burn occurrence within a scale of 1-5                  |
| Fresh Weight       | Fresh weight of sampled lettuce                 | gr                                                     | Sampled lettuce is weighed manually on scales                                                |
| Height             | Height of lettuce head                          | cm                                                     | Height of sampled lettuce                                                                    |
| Width              | Width of lettuce head                           | cm                                                     | Diameter of sampled lettuce                                                                  |
| Dry Weight         | Dry weight of sampled lettuce                   | gr                                                     | Sampled lettuce is evaluated for botrytis appearance                                         |
| Botrytis           | Botrytis appearance in sampled plants           | [appearance=x, absence=-]                              | This refers to 10 sample stems (total value)                                                 |
| Class A            | Classification of sampled lettuce as class A    | [assignment as class A=x, assignment as other class=-] | -                                                                                            |
| Class B            | Classification of sampled lettuce as class B    | [assignment as class B=x, assignment as other class=-] | -                                                                                            |
| Class C            | Classification of sampled lettuce as class C    | [assignment as class C=x, assignment as other class=-] | -                                                                                            |
| Date               | Time                                            | mm/dd/yyyy                                             | -                                                                                            |

### **Crop – Plant Density**

| **Column heading** | **Parameter description**                   | **Unit**                        | 
|--------------------|---------------------------------------------|---------------------------------|
| Plant density      | Number of lettuce heads per m2 growing area | heads/m2                        |
| Date               | Time                                        | mm/dd/yyyy                      |

### **Crop – Plant Weight**
| **Column heading** | **Parameter description**                   | **Unit**                        | 
|--------------------|---------------------------------------------|---------------------------------|
| Dry weight         | Dry weights of sampled plants               | gr                              |
| Fresh weight       | Fresh weights of sampled plants             | gr                              |
| Date               | Time                                        | mm/dd/yyyy                      |

## **Images datasets**
### **Overview**
This dataset contains images and measured data of lettuce crops grown under controlled greenhouse conditions. The lettuce samples of the crops were destructively measured every 7 days. The images were taken using two types of cameras: RealSense D415 and Sigrow Stomata Camera.

- **RealSense D415 Camera**: The RGB and depth images were taken with RealSense D415 camera. The images have similar camera intrinsics and resolution (1080x1920). The RGB images are stored in the `RGB Images` folder and the depth images are stored in the `Depth Images` folder. The depth images can be converted to 3D point clouds using the intrinsics below or the intrinsics in GT JSON. The `GroundTruth_All_239_Images.json` file contains all ground truth information. Daily images were also taken with RealSense D415 cameras installed in each greenhouse compartment. The images are named after the specific camera, date, and time (e.g. `d415_12_2022_02_02_12_00_01_depth.png`).

- **Sigrow Stomata Camera**: The color and thermal images were taken with [Sigrow Stomata Camera](https://sigrow.com/stomata-camera/). The dataset also includes time series stomatal conductance estimations. Each image is named after the specific camera, date, and time (e.g. `1037_2022_02_02_12_00_20.stomata.png`).

### **Structure**
- **Ground Truth**: contains a `json` file with all ground truth information.
- **Depth Images**: contains 239 depth images in `png` format (16 bit).
- **RGB Images**: contains 239 RGB images in `png` format (3x8 bit).
- **Daily Images**: contains images taken daily with RealSense and Sigrow cameras in `png` format.

### **File Naming Convention**
Each file is named after the date of destructive measurement, the compartment, the area of cultivation within the compartment, and the type of image (`YYYY-MM-DD_xxx_x1_imagetype`). For example, the file named `2022-02-08_303_L1_depth.png` corresponds to the depth image of the first lettuce head from the left side of compartment 303, destructively measured on February 8th, 2022.

### **Destructive Measurements**
The lettuce plants were destructively measured for the following crop traits:
- Fresh Weight (unit: `gr/head`): refers to the edible and sellable part of the shoot, starting at the attachment point of the first leaves.
- Height (unit: `cm`): height of the highest part of the plant, measured from the attachment point of the first leaves.
- Width (unit: `cm`): principal diameter of the projection of the lettuce plant on a horizontal surface.
The destructive measurements correspond to the plants above the written tag at planting, whereas for the rest of the growing period the measurements correspond to the plants below the tag.

### **Links** 
- RGB: https://drive.google.com/drive/folders/1-GsTG_UhDQ8gg_bTEMylnSecDVeJySNz?usp=share_link
- Depth: https://drive.google.com/drive/folders/1-IJ7Lur4QAp9YzqmtGQkQWC60gtGTOHi?usp=share_link
- Ground truth: https://drive.google.com/drive/folders/1-ICDqpAsy7MjVdrEmVKI5kIcK598XdwY?usp=share_link
- Daily images: https://drive.google.com/drive/folders/11lz97i-8G3Y5xzrFn2rxvbvrGjMvtyUU?usp=share_link

### **Additional images**
These links contain images crawled through public API of the competition. There are 3 folders: `realsense` contains RGB images, `stomata` contains stomatal images, and `thermal` contains thermal images. Images' name have the structure of crawled date and timestamp.

- CVA: https://drive.google.com/drive/folders/108P7HyRS21XSt3yvLlmHGREKX_Bl3tRm?usp=share_link
- Digital Cucumbers: https://drive.google.com/drive/folders/10SUiifJUAqUEIcmXO9iOS1hSuYR3ok6x?usp=share_link
- Koala: https://drive.google.com/drive/folders/10074IrhbALyrMPljK9IssriF9QntZ9nQ?usp=share_link
- Monday Lettuce: https://drive.google.com/drive/folders/10JDUixHY4lfJNPH2IvEmzaJRbZ9QHuip?usp=share_link
- Reference: https://drive.google.com/drive/folders/104zYQXSNFer73uNdLIXIrE--nRoiRoSc?usp=share_link
- Veggie Might: https://drive.google.com/drive/folders/10AXAZeRgSAEYHIzX6092GHMj4XJFvWed?usp=share_link


## **References**

\[1\] Hemming, S. (2022, September 15). [**Familiar face leads 'team koala' to win the Autonomous Greenhouse Challenge for a second time**](https://www.wur.nl/en/newsarticle/familiar-face-leads-team-koala-to-win-the-autonomous-greenhouse-challenge-for-a-second-time.htm ). WUR. 

\[2\] Stiffler, L. (2022, August 30). [**How a former Microsoft researcher used AI to grow award-winning lettuce from 5,000 miles away**](https://www.geekwire.com/2022/how-a-former-microsoft-researcher-used-ai-to-grow-award-winning-lettuce-from-5000-miles-away/ ). GeekWire. 