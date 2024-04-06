import smbus
import time

# Define I2C address for ADS1015 (default address)
ADS1015_ADDRESS = 0x48

# Create a new SMBus object
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1, for RPi 3

def read_adc_single_ended(channel):
    # Configuring register settings for single-ended measurement
    config = 0
    config |= 0b01000000  # Start single-ended conversion
    config |= (channel & 0x03) << 12  # Select channel
    config |= 0b11100000  # +/- 6.144V range
    config |= 0b00000000  # Continuous conversion mode

    # Write configuration to the ADC
    bus.write_i2c_block_data(ADS1015_ADDRESS, 0x01, [(config >> 8) & 0xFF, config & 0xFF])

    # Wait for conversion to complete (about 0.2 seconds for a single conversion)
    time.sleep(0.2)

    # Read the conversion result (16 bits, big-endian)
    data = bus.read_i2c_block_data(ADS1015_ADDRESS, 0x00, 2)
    result = (data[0] << 8) | data[1]

    # Convert result to signed 16-bit integer
    if result > 0x7FFF:
        result -= 0xFFFF

    return result

# Main loop for reading ADC values
while True:
    # Read ADC values from channel 0 and channel 1
    adc0 = read_adc_single_ended(0)
    adc1 = read_adc_single_ended(1)
    adc2 = read_adc_single_ended(2)
    adc3 = read_adc_single_ended(3)
    # Print ADC values
    print("ADC 0:", adc0)
    print("ADC 1:", adc1)
    print("ADC 2:", adc2)
    print("ADC 3:", adc3)

    # Wait before next reading
    time.sleep(1)
