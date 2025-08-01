"""Generate quantum circuits for testing purposes."""

import random
from qiskit import QuantumCircuit


def fully_connected_graph_state(num_qubits: int) -> QuantumCircuit:
    """Generates an n-qubit fully-connected graph state circuit..

    Args:
        num_qubits: The number of qubits in the circuit.

    Returns:
        The generated graph state circuit.
    """
    qc = QuantumCircuit(num_qubits)
    for qubit in range(num_qubits):
        qc.h(qubit)
    for i in range(num_qubits):
        for j in range(i + 1, num_qubits):
            qc.cz(i, j)
    return qc


def generate_random_two_qubit_gate_circuit(num_qubits: int, depth: int) -> QuantumCircuit:
    """Generate a random quantum circuit consisting of two-qubit gates.

    Args:
        num_qubits: The number of qubits in the circuit.
        depth: The target depth of the circuit.

    Returns:
        The generated random circuit.
    """
    qc = QuantumCircuit(num_qubits)

    for _ in range(depth):
        used_pairs = set()
        for _ in range(num_qubits // 2):
            # Select a pair of qubits that hasn't been used in this layer.
            while True:
                qubit1, qubit2 = random.sample(range(num_qubits), 2)
                if (qubit1, qubit2) not in used_pairs and (qubit2, qubit1) not in used_pairs:
                    used_pairs.add((qubit1, qubit2))
                    break

            # Randomly choose a two-qubit gate.
            gate = random.choice(["cx", "cz", "swap"])
            if gate == "cx":
                qc.cx(qubit1, qubit2)
            elif gate == "cz":
                qc.cz(qubit1, qubit2)
            elif gate == "swap":
                qc.swap(qubit1, qubit2)

    return qc
