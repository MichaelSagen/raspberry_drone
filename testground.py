import smbus

# Opprett en SMBus-objekt for I2C-kommunikasjon (velg riktig I2C-bussnummer)
bus = smbus.SMBus(1)  # For Raspberry Pi 3 og 4, bruk 1. For eldre modeller, kan det være 0.

def scan_i2c_devices():
    print("Skanne etter tilkoblede I2C-enheter...")
    for device in range(128):  # Går gjennom alle mulige I2C-adresser (0x00 til 0x7F)
        try:
            bus.read_byte(device)
            print("Enhet funnet på adresse: 0x{:02X}".format(device))
        except IOError:
            pass

# Skann etter I2C-enheter
scan_i2c_devices()