# pyright: reportUndefinedVariable=false
import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import matplotlib.pyplot as plt

# 1. 创建电路
circuit = Circuit('RC Low Pass Filter')
circuit.SinusoidalVoltageSource('in', 'input', circuit.gnd, amplitude=1@u_V, frequency=159.15@u_Hz) # 输入 159.15Hz 正弦波
circuit.R(1, 'input', 'output', 1@u_kOhm)
circuit.C(1, 'output', circuit.gnd, 1@u_uF)

# 2. 瞬态仿真
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.transient(step_time=1@u_ms, end_time=10@u_ms)

# 3. 绘制波形
plt.figure(figsize=(10, 5))
plt.plot(analysis.time, analysis.input, label='Input (Vin)')
plt.plot(analysis.time, analysis.output, label='Output (Vout)')
plt.title('RC Low Pass Filter Transient Response')
plt.xlabel('Time [s]')
plt.ylabel('Voltage [V]')
plt.legend()
plt.grid()
plt.savefig('rc_filter_waveform.png')
plt.show()

# 4. 提取截止频率（进行 AC 扫描）
ac_analysis = simulator.ac(start_frequency=1@u_Hz, stop_frequency=10@u_kHz, number_of_points=100, variation='dec')
gain = 20 * PySpice.Logging.Logging.np.log10(PySpice.Logging.Logging.np.abs(ac_analysis.output))
freq = ac_analysis.frequency

# 找到增益下降 3dB 的点
cutoff_idx = PySpice.Logging.Logging.np.argmin(PySpice.Logging.Logging.np.abs(gain + 3))
print(f"仿真截止频率: {freq[cutoff_idx]:.2f} Hz")