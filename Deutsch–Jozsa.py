from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_aer.primitives import SamplerV2
from qiskit_aer import AerSimulator
import matplotlib as plt

nqbits = 1

def Uf(nqbits, f_type = "balanced"):
    oracle = QuantumCircuit(nqbits + 1)

    if f_type == "constant":
        # Constant oracle: Apply X to the ancilla for f(x) = 1
        oracle.x(nqbits)  # Ancilla qubit index is n_qubits

    elif f_type == "balanced":
        # Balanced oracle: Flip the ancilla for half the inputs
        for i in range(nqbits):
            oracle.cx(i, nqbits)  # Controlled-X (CNOT) from input qubits to ancilla

    oracle_gate = oracle.to_gate(label=f"Oracle ({f_type})")
    return oracle_gate

dj_circuit = QuantumCircuit(nqbits + 1)

dj_circuit.h(range(nqbits))  # Apply Hadamard to input qubits
dj_circuit.x(nqbits)  # Flip the ancilla qubit to |1>
dj_circuit.h(nqbits)  # Apply Hadamard to ancilla

oracle = Uf(nqbits, f_type="balanced")  # Choose "balanced" or "constant"
dj_circuit.append(oracle, range(nqbits + 1))

dj_circuit.h(range(nqbits))  # Apply Hadamard again to input qubits

dj_circuit.measure_all()

fig = dj_circuit.draw(output="mpl")
fig.savefig("figs/Deutsch-Jozsa.png")  # Save as PNG

sim_statevector = AerSimulator(method="statevector")
# Transpile the circuit for the simulator
#dj_circuit = transpile(dj_circuit, sim, optimization_level=0)

job_statevector = sim_statevector.run(dj_circuit, shots=128)
counts_statevector = job_statevector.result().get_counts(0)

#print(counts_statevector)