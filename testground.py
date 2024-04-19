"""
FILE    : ADS_read.py
AUTHOR  : Chandra.Wijaya
VERSION : 1.2.0
PURPOSE : read analog input
https://github.com/chandrawi/ADS1x15-ADC/blob/main/examples/ADS_read.py

test
connect 1 potmeter 

GND ---[   x   ]------ 3.3V
           |

measure at x (connect to AIN0).
"""

import os
import time
import ADS1x15

# choose your sensor
# ADS = ADS1x15.ADS1013(1, 0x48)
# ADS = ADS1x15.ADS1014(1, 0x48)
# ADS = ADS1x15.ADS1015(1, 0x48)
# ADS = ADS1x15.ADS1113(1, 0x48)
# ADS = ADS1x15.ADS1114(1, 0x48)

ADS = ADS1x15.ADS1115(1, 0x48)

print(os.path.basename(__file__))
print("ADS1X15_LIB_VERSION: {}".format(ADS1x15.__version__))

# set gain to 4.096V max
ADS.setGain(ADS.PGA_4_096V)
f = ADS.toVoltage()
ads_to_voltage = 0.00061

while True :
    val_0 = ADS.readADC(0)
    val_1 = ADS.readADC(1)
    val_2 = ADS.readADC(2)
    val_3 = ADS.readADC(3)
    time.sleep(4)
    print("Analog0:", round(val_0*ads_to_voltage, 2),"V")
    print("Analog1:", round(val_1*ads_to_voltage, 2),"V")
    print("Analog2:", round(val_2*ads_to_voltage, 2),"V")
    print("Analog3:", round(val_3*ads_to_voltage, 2),"V")
    print("...................................")
    print("...................................")