import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BOARD)  # Sett GPIO-nummerering til fysisk nummer
GPIO.setup(3, GPIO.OUT)  # Konfigurer pinne 3 som utgang
GPIO.setup(5, GPIO.OUT)  # Konfigurer pinne 5 som utgang

# Funksjon for å slå på pinne 3 og 5 i ett sekund asynkront
def blink_pins():
    GPIO.output(3, GPIO.HIGH)  # Slå på pinne 3
    GPIO.output(5, GPIO.HIGH)  # Slå på pinne 5
    time.sleep(1)  # Vent i ett sekund
    GPIO.output(3, GPIO.LOW)  # Slå av pinne 3
    GPIO.output(5, GPIO.LOW)  # Slå av pinne 5

# Kjør blink-funksjonen i en løkke for å fortsette å blinke pinsene
while True:
    blink_pins()