from picamera2 import Picamera2
from PIL import Image
import pytesseract
from gpiozero import LED, Button
import time

text = ""
letter1 = 0
letter2 = 1
num_of_characters = 2
camera = Picamera2()

def capture():
    global text
    config = camera.create_still_configuration()
    camera.configure(config)

    camera.start()
    camera.capture_file('image.jpg')
    camera.stop()
    print("Image Saved")
    text = pytesseract.image_to_string(Image.open('image.jpg'))
    print(text)


# Define GPIO pins
latchPin = 17
clockPin = 27
dataPin = 22

# Define input pins for buttons
button1Pin = 26
button2Pin = 19
button3Pin = 23

# Braille dictionary
brailleDictionary = {
    'A': 0b000001,
    'B': 0b000011,
    'C': 0b001001,
    'D': 0b011001,
    'E': 0b010001,
    'F': 0b001011,
    'G': 0b011011,
    'H': 0b010011,
    'I': 0b001010,
    'J': 0b011010,
    'K': 0b000101,
    'L': 0b000111,
    'M': 0b001101,
    'N': 0b011101,
    'O': 0b010101,
    'P': 0b001111,
    'Q': 0b011111,
    'R': 0b010111,
    'S': 0b001110,
    'T': 0b011110,
    'U': 0b100101,
    'V': 0b100111,
    'W': 0b111010,
    'X': 0b101101,
    'Y': 0b111101,
    'Z': 0b110101
}

# Initialize shift register data
d1 = 0
d2 = 0
d3 = 0
d4 = 0

# Initialize LEDs and buttons
latch = LED(latchPin)
clock = LED(clockPin)
data = LED(dataPin)
button1 = Button(button1Pin, pull_up=True)
button2 = Button(button2Pin, pull_up=True)
button3 = Button(button3Pin, pull_up=True)

def updateShiftRegisters():
    latch.off()
    shiftOut(data, clock, d4)
    shiftOut(data, clock, d3)
    shiftOut(data, clock, d2)
    shiftOut(data, clock, d1)
    latch.on()

def shiftOut(data, clock, val):
    for i in range(8):
        clock.off()
        data.value = (val & (1 << (7 - i))) != 0
        clock.on()

def getBraillePattern(letter):
    return brailleDictionary.get(letter.upper(), 0)

def createByte(b7, b6, b5, b4, b3, b2, b1, b0):
    return ((1 if b7 else 0) << 7) | ((1 if b6 else 0) << 6) | ((1 if b5 else 0) << 5) | ((1 if b4 else 0) << 4) | ((1 if b3 else 0) << 3) | ((1 if b2 else 0) << 2) | ((1 if b1 else 0) << 1) | (1 if b0 else 0)


def displayBraille(text):
    global d1, d2, d3, d4
    braillePattern1 = getBraillePattern(text[0])
    braillePattern2 = getBraillePattern(text[1])

    d1 = createByte(
        0,
        braillePattern1 & 0b010000,
        braillePattern1 & 0b000010,
        not (braillePattern1 & 0b000001),
        not (braillePattern1 & 0b001000),
        braillePattern1 & 0b001000,
        braillePattern1 & 0b000001,
        0
    )

    d2 = createByte(
        0,
        not (braillePattern1 & 0b000100),
        not (braillePattern1 & 0b100000),
        braillePattern1 & 0b100000,
        braillePattern1 & 0b000100,
        not (braillePattern1 & 0b000010),
        not (braillePattern1 & 0b010000),
        0
    )

    d3 = createByte(
        0,
        braillePattern2 & 0b010000,
        braillePattern2 & 0b000010,
        not (braillePattern2 & 0b000001),
        not (braillePattern2 & 0b001000),
        braillePattern2 & 0b001000,
        braillePattern2 & 0b000001,
        0
    )

    d4 = createByte(
        0,
        not (braillePattern2 & 0b000100),
        not (braillePattern2 & 0b100000),
        braillePattern2 & 0b100000,
        braillePattern2 & 0b000100,
        not (braillePattern2 & 0b000010),
        not (braillePattern2 & 0b010000),
        0
    )
    print(braillePattern2&0b100000)
    print(f'd1: {d1:08b}, d2: {d2:08b}, d3: {d3:08b}, d4: {d4:08b}')
    updateShiftRegisters()

def main():
    ## displayBraille("AA")
    global letter1, letter2, text, num_of_characters
    try:
        while True:
            #text = input()
            if button1.is_pressed:
                print("Button 1 pressed. Capturing Image")
                capture()
                letter1 = 0
                letter2 = 1
                displayBraille(text[letter1]+text[letter2])
            elif button2.is_pressed:
                print("Button 2 pressed. Displaying next letters")
                letter1 = letter1+num_of_characters
                letter2=letter2+num_of_characters
                displayBraille(text[letter1]+text[letter2])
            elif button3.is_pressed:
                print("Button 3 pressed. Displaying the previous letters")
                letter1 = letter1-num_of_characters
                letter2=letter2-num_of_characters
                displayBraille(text[letter1]+text[letter2])
            time.sleep(0.1)  # Check button state every 0.1 second
    except KeyboardInterrupt:
        pass

main()
