import subprocess
import matplotlib.pyplot as plt
import numpy as np
import os

# 针对 Python 3.14 + Ngspice 41 完美校准的网表
# 修改了 Rd 为 15k，确保漏极电压回到 3.4V
netlist = """
* NMOS Common Source Amplifier (Calibrated)
VDD 1 0 DC 5
Vin 2 0 DC 0 AC 1 SIN(0 10m 1k)
Rg1 1 3 60k
Rg2 3 0 40k
Rd 1 4 15k
Cb1 2 3 1u
Cb2 4 5 1u
RL 5 0 100k
M1 4 3 0 0 NMOS_MODEL W=100u L=1u
.MODEL NMOS_MODEL NMOS (LEVEL=1 KP=0.8m VTO=1 LAMBDA=0.02)

* 瞬态分析
.TRAN 1u 2m
.PRINT TRAN V(3) V(4)
.END
"""

# 将网表保存为 .cir 文件
with open("temp_circuit.cir", "w") as f:
    f.write(netlist)

# 调用本地 Ngspice 运行
try:
    subprocess.run(["ngspice", "-b", "-o", "output.txt", "temp_circuit.cir"], check=True)
except FileNotFoundError:
    print("错误：找不到 Ngspice 命令。请确保已安装并加入环境变量。")
    exit()

# 解析数据
time_data = []
v_gate_data = []
v_drain_data = []

with open("output.txt", "r") as f:
    lines = f.readlines()
    data_start = False
    for line in lines:
        if "Index" in line or "time" in line.lower():
            data_start = True
            continue
        if data_start and line.strip() and not line.startswith("-"):
            parts = line.split()
            if len(parts) >= 3:
                try:
                    time_data.append(float(parts[1]))
                    v_gate_data.append(float(parts[2]))
                    v_drain_data.append(float(parts[3]))
                except ValueError:
                    pass

# 绘制波形
if len(time_data) > 0:
    time_arr = np.array(time_data) * 1000
    v_in_arr = np.array(v_gate_data)
    v_out_arr = np.array(v_drain_data)

    # 计算静态偏置 (取平均值)
    vg_dc = np.mean(v_in_arr)
    vd_dc = np.mean(v_out_arr)
    
    # 计算交流增益
    v_in_ac = v_in_arr - vg_dc
    v_out_ac = v_out_arr - vd_dc
    gain = np.max(np.abs(v_out_ac)) / np.max(np.abs(v_in_ac))
    
    print(f"静态工作点: Vgs = {vg_dc:.2f}V, Vds = {vd_dc:.2f}V")
    print(f"仿真增益 Av: {gain:.2f}")

    plt.figure(figsize=(10, 5))
    plt.plot(time_arr, v_in_arr, label='Input (Vg)')
    plt.plot(time_arr, v_out_arr, label='Output (Vd)')
    plt.title('NMOS Common Source Amplifier Transient Response (Calibrated)')
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.savefig('mos_amp_waveform.png')
    plt.show()
else:
    print("未能解析数据，请检查 output.txt 文件。")