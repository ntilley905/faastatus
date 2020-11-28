# custom_component to get info from FAA Airspace API
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

A platform which allows you to get information from the FAA National Airspace System API.


To get started put all the files from `/custom_components/faadelays/` here:
`<config directory>/custom_components/faadelays/`

**Configuration**

As of v1.0.0 this component is configurable via the user interface. To configure, go to the integrations page, click the orange button, then search for FAA Delays. On the setup page, enter in any supported aiprort's IATA code (see below). 

**Supported airports:**

The FAA officially supports the airports below. However, most airports in the United States will return data. The component will check to see if the airport returns any data and if it does, it will setup the sensors normally. This should not cause any problems, but this is not officially supported per the API.

BOS, LGA, TEB, EWR, JFK, PHL, PIT, IAD, BWI, DCA, RDU, CLT, ATL, MCO, TPA, MCO, FLL, MIA, DTW, CLE, MDW, ORD, IND, CVG, BNA, MEM, STL, MCI, MSP, DFW, IAH, DEN, SLC, PHX, LAS, SAN, LAX, SJC, SFO, PDX, SEA

## Sensors

After configuring, there will be five new binary sensors, one for each type of airport delay. The sensor will be `on` if a delay of that type is present and `off` otherwise. Each sensor has additional attributes for details on the delay, including the reason, any applicable delay times (average delay, start and end time) and any trends. All information about delays provided by the API is provided. 
