# Refreshable Braille Display

## Table of Contents
- [Introduction](#introduction)
- [Project Description](#project-description)
- [Hardware Components](#hardware-components)
- [Software Setup](#software-setup)
- [Circuit Diagram](#circuit-diagram)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project aims to develop a refreshable braille display to assist visually impaired individuals. The display will convert digital/printed text into braille in real-time, enabling users to read digital/printed content through the braille display.

## Overview



## Hardware Components Used
| **Component**       | **Description**                     |
|---------------------|-------------------------------------|
| **IC Chips**        | 74HC595 (Shift Register) x4 <br> L293D (H-Bridge) x6           |
| **Microcontroller** | Raspberry Pi Zero 2W                 |
| **Camera Module**| Raspberry Pi camera module|
| **SD card**|Storage for Raspberry Pi 32GB|
| **Power Supply**    | Rechargebale Batteries (3.2V, 6000mah 3C ) x2                   |
| **Other Components**| Insulated Copper Wire (50m) <br> Iron Nails x12 <br> Magnets x24 <br> Hookup Wires <br> Perf Board <br> Push Buttons x3|


## Software Setup
1. **Install Raspbian OS**: Follow the official Raspberry Pi documentation to install Raspbian OS on the Raspberry Pi Zero 2W.
2. **Enable Camera**: Use `raspi-config` to enable the camera module. 
3. **Install Required Libraries**:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-rpi.gpio python3-picamera
   sudo pip3 install rpicam2 pytesseract gpiozero pillow
   ```
4. Clone the Project Repository
   ```bash
   git clone https://github.com/LokeshAravapalli/refreshable-braille-display.git
   cd refreshable-braille-display
   ```

# Table for Pin Connections
| **Component**          | **Pin Name**         | **Raspberry Pi Pin** | **Description**        |
|------------------------|----------------------|----------------------|------------------------|
| Camera Module          | CSI Interface        | CSI Interface        | Camera connection      |
| 74HC595 Shift Register | SER (Serial Data)    | GPIO 17              | Serial Data            |
|                        | SRCLK (Shift Clock)  | GPIO 27              | Shift Clock            |
|                        | RCLK (Latch Clock)   | GPIO 22              | Latch Clock            |
|                        | OE (Output Enable)   | GPIO 5               | Output Enable          |
| L293D H-Bridge         | IN1                  | GPIO 6               | Motor control input 1  |
|                        | IN2                  | GPIO 13              | Motor control input 2  |
|                        | IN3                  | GPIO 19              | Motor control input 3  |
|                        | IN4                  | GPIO 26              | Motor control input 4  |
| Push Buttons           | Button 1             | GPIO 18              | User input button 1    |
|                        | Button 2             | GPIO 23              | User input button 2    |



## Circuit Diagram
![Circuit Diagram](hardware/schematic.png)

Describe the circuit design briefly. Include any specific connections or configurations.

## Usage
Provide instructions on how to use the project:
1. How to upload the code to the microcontroller (if applicable).
2. How to assemble the hardware components.
3. How to run the software.

## Contributing
We welcome contributions! Please read our [contributing guidelines](docs/contributing.md) for more information.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



## Contributors
Thanks to the following people who have contributed to this project:
- **[Lokesh]** - [[GitHub Profile Link](https://github.com/LokeshAravapalli)]
- **[Sujit]** - [[GitHub Profile Link](https://github.com/GSujit)]
- **[Lohitaksh]** - [[GitHub Profile Link](https://github.com/LohitakshMaruvada)]
  
## Contact
Any queries, please contact us at [Lokeshkumar.Aravapalli@iiitb.ac.in] / [Sujit.Ghantasala@iiitb.ac.in] /[Lohitaksh.Maruvada@iiitb.ac.in].
