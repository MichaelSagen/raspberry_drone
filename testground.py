import smbus

# Define I2C address for ADS1015 (default address)
ADS1015_ADDRESS = 0x48

# Create a new SMBus object
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1, for RPi 3

def check_ads1015_communication():
    try:
        # Leser en byte fra en registeradresse (0x00 her) som en enkel sjekk for kommunikasjon
        bus.read_byte_data(ADS1015_ADDRESS, 0x00)
        print("Kommunikasjon med ADS1015 er vellykket!")
    except IOError:
        print("Feil: Kan ikke kommunisere med ADS1015. Sjekk tilkoblingen og I2C-adressen.")

# Sjekker kommunikasjon med ADS1015
check_ads1015_communication()
