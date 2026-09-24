第一部分：RC 低通滤波电路（任务 1）

1. 电路图
   <img width="915" height="531" alt="RC低通滤波电路图" src="https://github.com/user-attachments/assets/78e91969-1223-4194-97bd-3494a0bf56ed" />

2. 理论计算

电路参数：
R = 1kΩ, C = 1μF。
截止频率： 
fc = 1/2πRC ≈ 159.15Hz
时间常数： 
τ = RC = 1×10 ^ −3 s = 1 ms

3.仿真结果
    <img width="1500" height="800" alt="RC低通滤波电路波形图" src="https://github.com/user-attachments/assets/11a51e21-2673-448b-8f51-39799ca7c1e2" />

4.对比表格

参数	理论值	仿真值	误差
截止频率 fc	159.15Hz	159.15Hz	0%
时间常数 τ	1.00ms	1.00ms	0%
输入信号峰值Vin	1.00V	1.00V	0%
输出信号峰值Vout	0.71V	0.75V	约5.6% (仿真读数的微小偏差)
电压增益Av	0.707 (-3dB)	0.75 (0.75V / 1.00V)	约 6.1% (符合 -3dB 衰减趋势)
相位差 ϕ	-45° (输出超前输入)	约 -45° (输出滞后输入)	观察波形一致，滞后约 1/4 周期

