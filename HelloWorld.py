from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_aer.primitives import Estimator
import matplotlib as plt
 
# Create a new circuit with two qubits
qc = QuantumCircuit(2)
 
# Add a Hadamard gate to qubit 0
qc.h(0)
 
# Perform a controlled-X gate on qubit 1, controlled by qubit 0
qc.cx(0, 1)
 
# Return a drawing of the circuit using MatPlotLib ("mpl"). This is the
# last line of the cell, so the drawing appears in the cell output.
# Remove the "mpl" argument to get a text drawing.
fig = qc.draw(output="mpl")
fig.savefig("circuit.png")  # Save as PNG

observables = SparsePauliOp("ZZ")
estimator = Estimator()
job = estimator.run(qc, observables)
exact_value = job.result().values[0]
print(exact_value)