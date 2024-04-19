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
ads_to_voltage0 = 0.0006195
ads_to_voltage1 = 0.000625
ads_to_voltage2 = 0.000625
ads_to_voltage3 = 0.000623
while True :
    val_0 = ADS.readADC(0)
    val_1 = ADS.readADC(1)
    val_2 = ADS.readADC(2)
    val_3 = ADS.readADC(3)
    time.sleep(4)
    print("Analog0:", round(val_0*ads_to_voltage0, 3),"V")
    print("Analog1:", round(val_1*ads_to_voltage1, 3),"V")
    print("Analog2:", round(val_2*ads_to_voltage2, 3),"V")
    print("Analog3:", round(val_3*ads_to_voltage3, 3),"V")
    print("...................................")
    print("...................................")