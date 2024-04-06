
import logging
from websocket_server import WebsocketServer
import smbus
import time
import threading


def new_client(client, server):
    server.send_message_to_all("Hey all, a new client has joined us")

def message_received(client, server, message):
    print("Received message from client {}: {}".format(client['id'], message))
    # Gjør ønsket behandling av den mottatte meldingen her
    if message == "CHARGING_PLATE_ON":
        print ("plate is on")
        
    elif message == "CHARGING_PLATE_OFF":
        server.send_message_to_all("ras_say_the_plate_is_off")
        print ("plate is off")


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

def server():
    server = WebsocketServer(host='192.168.1.169', port=8765, loglevel=logging.INFO)
    server.set_fn_new_client(new_client)
    server.set_fn_message_received(message_received)
    print("in try")
    server.run_forever()


server_thread = threading.Thread(target=server)
server_thread.start()

while True:
        adc0 = read_adc_single_ended(0)
        adc1 = read_adc_single_ended(1)

        print("ADC 0:", adc0)
        print("ADC 1:", adc1)
