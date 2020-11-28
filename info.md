{% if installed %}
{% if version_installed.replace("v", "").replace(".","") | int < 100  %}
**_Please see the [release notes](https://github.com/ntilley905/faastatus/releases/tag/v1.0.0) before updating to v1.0.0! Major breaking changes!_**
To update, an uninstall and fresh install is required. Updating via HACS will fail.
{% endif %}
---
{% endif %}

**Configuration**

As of v1.0.0 this component is configurable via the user interface. To configure, go to the integrations page, click the orange button, then search for FAA Delays. On the setup page, enter in any supported aiprort's IATA code (see below). 

**Supported airports:**

The FAA officially supports the airports below. However, most airports in the United States will return data. The component will check to see if the airport returns any data and if it does, it will setup the sensors normally. This should not cause any problems, but this is not officially supported per the API.

BOS, LGA, TEB, EWR, JFK, PHL, PIT, IAD, BWI, DCA, RDU, CLT, ATL, MCO, TPA, MCO, FLL, MIA, DTW, CLE, MDW, ORD, IND, CVG, BNA, MEM, STL, MCI, MSP, DFW, IAH, DEN, SLC, PHX, LAS, SAN, LAX, SJC, SFO, PDX, SEA

## Sensors

After configuring, there will be five new binary sensors, one for each type of airport delay. The sensor will be `on` if a delay of that type is present and `off` otherwise. Each sensor has additional attributes for details on the delay, including the reason, any applicable delay times (average delay, start and end time) and any trends. All information about delays provided by the API is provided. 
