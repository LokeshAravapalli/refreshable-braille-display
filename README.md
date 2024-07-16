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
### Prerequisites
Make sure you have python installed in Raspberry Pi before proceeding.

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/electronics-hackathon-project.git
    cd electronics-hackathon-project
    ```

2. Install necessary dependencies:
    ```sh
    pip install -r requirements.txt
    ```
or you can install these one by one

rpicam2
```-sh
code
```
pytesseract
gpiozero
pillow



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
