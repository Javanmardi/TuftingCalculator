# Tufting Carpet Weight Calculator 🧵

A simple Python application to calculate tufting carpet weight based on textile parameters.  
This project includes both **command-line** and **GUI (Tkinter)** interfaces, making it easy to use interactively or in batch mode.

---

## 📐 Formula

The tufting carpet weight is calculated using the formula:

tuft = (1/gauge) × (1000/25.4) × stitch × 10 × ((pile × 2) + (10/stitch)) × 0.001 × (den/9000)

Where:
- `gauge` → Gauge (inch) 
- `stitch` → Stitch rate (per dm) 
- `pile` → Pile height (mm) 
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

1. Clone the repository:
```bash
git clone https://github.com/Javanmardi/TuftingCalculator.git
cd TuftingCalculator

1. Interactive Command Line
```bash
python tuft_weight.py
```


2. Command Line Arguments
```bash
python tuft_cli.py --gauge 1/8 --stitch 32 --pile 10 --den 3400 --piletype Cut
```

3. GUI Mode
```bash
python tuft_gui.py
```

## Acknowledgement

I express my sincere gratitude to **Dr. Mohsen Bahador** and **Mr. Mohammad Taghi Zyia** for their valuable guidance and support during the development of the tufting calculator project. Their expertise and contributions played an important role in shaping the direction and quality of this work.

## License
This project is licensed under the MIT License — feel free to use, modify, and share.



