# 🎛️ RTL-SDR Scanner 📡

A powerful and user-friendly software tool for scanning radio frequencies using RTL-SDR devices. This scanner covers a wide frequency range with customizable settings, real-time signal analysis, and an intuitive interface.

## 🚀 Features
- 📶 **Wide Frequency Coverage**: Scan from 24 MHz to 1766 MHz.
- ⚙️ **Customizable Settings**: Set start/stop frequencies and step sizes with optional default values.
- 📊 **Real-Time Visualization**: Analyze and display signal strengths using a dynamic power spectrum plot.
- ⏱️ **Efficient Scanning**: Utilizes a progress bar for better tracking.
- 🖥️ **Interactive Menu**: Welcomes users with a stylish interface including author credit and GitHub link.

## 🛠️ Installation

### Prerequisites
Ensure you have Python 3 installed along with the following libraries:
- `numpy`
- `matplotlib`
- `rtlsdr`
- `tqdm`

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/timdigga/rtlsdrscanner
   cd rtlsdrscanner
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scanner:**
   ```bash
   python 
   ```

4. **Follow the on-screen prompts** to start scanning.

## 🔍 Usage

The program will prompt you to enter the start and stop frequencies, as well as the step size. Press **Enter** to use the default values.

## 📡 Example

```
################################################
#                                              #
#              RTL SDR SCANNER                #
#                                              #
#                by Tim Digga                 #
#    GitHub: https://github.com/timdigga       #
#                                              #
################################################

Enter start frequency in MHz (default 24):
Enter stop frequency in MHz (default 1766):
Enter step size in kHz (default 200):

Scanning from 24.0 MHz to 1766.0 MHz...
Scanning frequencies: 100%|████████████████████| 1000/1000 [00:30<00:00, 33.33 freq/s]
High-power frequencies detected at (MHz): [88.5, 101.7, 145.0]
```

## 🤝 Contributing

Feel free to submit issues or fork the repository to contribute improvements.

## 🤓 About the Author
Developed with passion by **Tim Digga**.  
GitHub: [timdigga](https://github.com/timdigga)

## 📜 License
MIT License.
