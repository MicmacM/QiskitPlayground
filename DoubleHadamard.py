from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.primitives import SamplerV2

# Initialize the simulator
sim = AerSimulator()

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply Hadamard gates to both qubits
qc.h(0)
qc.h(1)
qc.measure_all()  # Add measurement to all qubits

fig = qc.draw(output="mpl")
fig.savefig("figs/DoubleHadamard.png")  # Save as PNG

# Transpile the circuit for the simulator
qc = transpile(qc, sim, optimization_level=0)

# Initialize the sampler
sampler = SamplerV2()

# Run the sampler on the Hadamard circuit
job = sampler.run([qc], shots=1024)
result = job.result()

# Display results
print(f"Counts for the Hadamard circuit: {result[0].data.meas.get_counts()}")
