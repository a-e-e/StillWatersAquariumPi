# Stage 3: Use smart plugs to control water heater and water pump

Referencing 

# To get started
Stage 3 uses all components from stage 2 & 1

We will need the following:
- Everything from stage 2
- 1 Water Pumps
- 1 Aquarium heater
- 2 TP-Link Smart Wi-Fi Plug HS100 or similar  
https://www.amazon.com/dp/B01KBFWW0O/ref=dp_iou_view_product?ie=UTF8&psc=1

## Connect smart plug to wall and set up using KASA app
- Ask your network administrator
https://apps.apple.com/us/app/kasa-smart/id1034035493  
https://play.google.com/store/apps/details?id=com.tplink.kasa_android&hl=en_US&gl=US
- Name each plug to be memorable e.g. pump_1, heater_1, etc
- Connect pump and aquarium heater to smart plug

## Install required libraries
- `cd Code/StillWatersAquariumPi`
- `pip3 install -r requirements.txt`

# Running code
- Open Thornny Python IDE
- Load -> Code/StillWatersAquariumPi/stage_3/discover_smart_plugs.py
- Note IP address of smart plugs and insert into line 13 and 16 of print_and_monitor_water_level_and_temp.py  
`<SmartPlug model HS100(US) at 192.168.1.88 (Pump 1), is_on: False - dev specific: {'LED state': True, 'On since': datetime.datetime(2021, 1, 19, 19, 21, 39, 475457)}>`
- Load -> Code/StillWatersAquariumPi/stage_3/print_water_level_and_temperature.py
- Click 'Run'
