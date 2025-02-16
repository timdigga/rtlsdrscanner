import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
from tqdm import tqdm

def display_menu():
    print("""
    ################################################
    #                                              #
    #              RTL SDR SCANNER                #
    #                                              #
    #                by Tim Digga                 #
    #    GitHub: https://github.com/timdigga       #
    #                                              #
    ################################################
    """)

def scan_spectrum():
    display_menu()
    start_freq_mhz = input("Enter start frequency in MHz (default 24): ") or 24
    stop_freq_mhz = input("Enter stop frequency in MHz (default 1766): ") or 1766
    step_size_khz = input("Enter step size in kHz (default 200): ") or 200
    start_freq_mhz = float(start_freq_mhz)
    stop_freq_mhz = float(stop_freq_mhz)
    step_size_khz = float(step_size_khz)
    sdr = RtlSdr()
    sdr.sample_rate = 2.4e6  # Hz
    sdr.gain = 'auto'
    start_freq = int(start_freq_mhz * 1e6)
    stop_freq = int(stop_freq_mhz * 1e6)
    step_size = int(step_size_khz * 1e3)
    frequencies = np.arange(start_freq, stop_freq, step_size)
    power_levels = []
    print(f"Scanning from {start_freq_mhz} MHz to {stop_freq_mhz} MHz...")
    for freq in tqdm(frequencies, desc="Scanning frequencies"):
        sdr.center_freq = freq
        samples = sdr.read_samples(1024 * 128)
        spectrum = np.fft.fftshift(np.abs(np.fft.fft(samples))**2)
        power = 10 * np.log10(np.mean(spectrum))
        power_levels.append(power)
    sdr.close()
    threshold = np.mean(power_levels) + np.std(power_levels)
    high_power_indices = np.where(np.array(power_levels) > threshold)[0]
    high_power_freqs = frequencies[high_power_indices] / 1e6
    print("High-power frequencies detected at (MHz):", high_power_freqs)
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies / 1e6, power_levels, color='blue')
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('Power (dB)')
    plt.title('RTL-SDR Frequency Scan')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    scan_spectrum()
