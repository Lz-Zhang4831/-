第一部分：RC 低通滤波电路（任务 1）

1.电路图
   <img width="915" height="531" alt="RC低通滤波电路图" src="https://github.com/user-attachments/assets/78e91969-1223-4194-97bd-3494a0bf56ed" />

2.理论计算

电路参数：
R = 1kΩ, C = 1μF。
截止频率： 
fc = 1/2πRC ≈ 159.15Hz
时间常数： 
τ = RC = 1×10 ^ −3 s = 1 ms

3.仿真结果
    <img width="1500" height="800" alt="RC低通滤波电路波形图" src="https://github.com/user-attachments/assets/11a51e21-2673-448b-8f51-39799ca7c1e2" />

4.对比表格
    <img width="1236" height="483" alt="RC低通滤波电路对比表格" src="https://github.com/user-attachments/assets/259dcf64-bc7e-4f9c-be93-8994817ef07d" />

第二部分：戴维南定理验证（任务 2）

1.电路图
    <img width="942" height="516" alt="戴维南定理验证电路图" src="https://github.com/user-attachments/assets/c1c1aff4-d6ba-4056-ba1e-da8b9de6c7fd" />

2.理论计算

电路设计：使用 10V 电压源，串联 1kΩ 电阻 (R1)，再并联 2kΩ 负载电阻 (R2)。
戴维南等效电压Voc（开路电压）：Voc = 10V × 2k/(1k+2k) = 6.67V
戴维南等效电阻Rth：Rth = R1||R2 = 666.67Ω
短路电流Isc：Isc = Voc/Rth = 10mA

3.仿真结果
    <img width="576" height="147" alt="戴维南定理验证输出结果" src="https://github.com/user-attachments/assets/ee889f36-361e-4541-80be-6ed52a762c51" />

4.对比表格

    <img width="1236" height="315" alt="戴维南定理验证电路对比表格" src="https://github.com/user-attachments/assets/f21e9c95-3d76-4133-9ea5-d80f2f012bd3" />

第三部分：NMOS共源放大电路（任务 3）

1.电路图
    <img width="1014" height="723" alt="NMOS共源放大电路图" src="https://github.com/user-attachments/assets/3598dcd5-4874-4276-8166-9603ed797ec0" />

2.理论计算

参数：VDD = 5v，Rg1 = 60kΩ，Rg2 = 40kΩ，Rd = 2kΩ，K = 0.8mA/V^2，Vth = 1v，λ = 0.02V^-1。
栅极电压：VG = VDD × Rg2/(Rg1+Rg2) = 2.0V
静态漏极电流（假设饱和）：ID = K(VGS - Vth)^2 = 0.8mA
静态漏极电压：VD = VDD - ID × Rd = 3.4V
饱和区判定：需要VDS > VGS - Vth 即3.4V > 2.0V - 1.0V = 1.0V，假设成立，工作在饱和区
小信号参数：gm = 2√(K × ID) = 1.6mA/V = 1.6mS
输出电阻ro = 1/(λ × ID) = 62.5kΩ
增益Av = -gm(Rd||ro) ≈ -3.10

3.仿真结果
    <img width="1500" height="800" alt="NMOS共源放大电路波形图" src="https://github.com/user-attachments/assets/de23b4b7-63c2-4642-800e-737d253d9e58" />

4.对比表格

    <img width="1128" height="429" alt="NMOS共源放大电路结果对比表格" src="https://github.com/user-attachments/assets/c6dde96d-9075-44c5-8c0d-34c962b8e946" />
