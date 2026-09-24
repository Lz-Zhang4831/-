# pyright: reportUndefinedVariable=false
import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

def build_circuit(load_resistance=None):
    circuit = Circuit('Thevenin Verification')
    circuit.V('source', 'n1', circuit.gnd, 10@u_V)
    circuit.R('1', 'n1', 'n2', 1@u_kOhm)
    circuit.R('2', 'n2', circuit.gnd, 2@u_kOhm)
    if load_resistance:
        circuit.R('load', 'n2', circuit.gnd, load_resistance)
    return circuit

# 1. 计算开路电压 Voc
circuit_oc = build_circuit()
sim_oc = circuit_oc.simulator()
op_oc = sim_oc.operating_point()
voc_sim = float(op_oc['n2'][0])  # 修改了这里：添加 [0]
print(f"Simulated Voc: {voc_sim:.2f} V")

# 2. 计算短路电流 Isc (使用 1uOhm 近似短路)
circuit_sc = build_circuit(load_resistance=1@u_mOhm)
sim_sc = circuit_sc.simulator()
op_sc = sim_sc.operating_point()
isc_sim = float(op_sc['n2'][0]) / 0.001 # 修改了这里：添加 [0]
print(f"Simulated Isc: {isc_sim*1000:.2f} mA")

# 3. 验证带载能力 (负载设为 Rth = 666.67 Ohm)
rth_theoretical = 666.67
circuit_load = build_circuit(load_resistance=rth_theoretical@u_Ohm)
sim_load = circuit_load.simulator()
op_load = sim_load.operating_point()
v_load_sim = float(op_load['n2'][0]) # 修改了这里：添加 [0]
i_load_sim = v_load_sim / rth_theoretical
print(f"Loaded Voltage: {v_load_sim:.2f} V, Loaded Current: {i_load_sim*1000:.2f} mA")