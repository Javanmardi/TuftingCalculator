# Tufting Carpet Weight Calculator 🧵

A simple Python application to calculate tufting carpet weight based on textile parameters.  
This project includes both **command-line** and **GUI (Tkinter)** interfaces, making it easy to use interactively or in batch mode.

---

## 📐 Formula

The tufting carpet weight is calculated using the formula:

\[
tuft = \frac{1}{ga} \cdot (1000/25.4) \cdot st \cdot 10 \cdot \big((pl \cdot 2) + (10/st)\big) \cdot 0.001 \cdot \frac{den}{9000}
\]

Where:
- `ga` → Gauge  
- `st` → Stitch rate  
- `pl` → Pile height  
- `den` → Yarn denier  

---

## 🚀 Features
- **Command-line interactive mode**: enter values step by step.
- **Command-line arguments mode**: pass values directly with flags.
- **GUI interface (Tkinter)**:
  - Input fields for all parameters
  - Support for fractions (e.g., `1/8`, `5/32`) as well as decimals
  - Reset button to clear inputs
  - Instant calculation display

---

## 🛠️ Installation

Clone the repository:
```bash
git clone https://github.com/Javanmardi/TuftingCalculator.git
cd TuftingCalculator

1. Interactive Command Line
```bash
python tuft_weight.py
```


2. Command Line Arguments
```bash
python tuft_cli.py --gauge 1/8 --stitch 32 --pile 10.0 --den 3400 --
```

3. GUI Mode
```bash
python tuft_gui.py
```

## License
This project is licensed under the MIT License — feel free to use, modify, and share.



