import smbus
import time

# Define I2C address for ADS1015
ADS1015_ADDRESS = 0x48

# Create a new SMBus object
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1, for RPi 3

def read_adc_single_ended(channel):
    # Configuring register settings for single-ended measurement
    config = 0
    config |= 0b01000000  # Start single-ended conversion
    config |= (channel & 0x07) << 12  # Select channel
    config |= 0b11100000  # +/- 6.144V range
    config |= 0b00000000  # Continuous conversion mode

    # Write configuration to the ADC
    bus.write_i2c_block_data(ADS1015_ADDRESS, 0x01, [(config >> 8) & 0xFF, config & 0xFF])

    # Wait for conversion to complete
    time.sleep(0.1)

    # Read the conversion result
    data = bus.read_i2c_block_data(ADS1015_ADDRESS, 0x00, 2)
    result = (data[0] << 8) | data[1]

    # Convert result to signed 16-bit integer
    if result > 0x7FFF:
        result -= 0xFFFF

    return result

def main():
    while True:
        adc0 = read_adc_single_ended(0)
        adc1 = read_adc_single_ended(1)

        print("ADC 0:", adc0)
        print("ADC 1:", adc1)

        time.sleep(1)

if __name__ == "__main__":
    main()
