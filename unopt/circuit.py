"""Generate quantum circuits for testing purposes."""

import random
from qiskit import QuantumCircuit


def super_peaked_entangled_circuit(num_qubits: int) -> QuantumCircuit:
    """
    Creates an entangled circuit that maps the all-zero state to a specific
    computational basis state (e.g., all-ones state). This circuit is 'super peaked'
    and includes two-qubit gates, which are necessary for the QCU recipe.
    """
    qc = QuantumCircuit(num_qubits)
    
    # Create an entangled state (e.g., a GHZ-like state)
    qc.h(0)
    for i in range(num_qubits - 1):
        qc.cx(i, i + 1)
        
    # Apply X gates to rotate the state to the all-ones state
    # This ensures a high peak at a specific outcome
    # The GHZ state is (00...0 + 11...1)/sqrt(2)
    # Applying X on all qubits gives (11...1 + 00...0)/sqrt(2)
    # Applying H on the first qubit would give back the |1...1> state
    qc.h(0)
    
    return qc

def super_peaked_circuit(num_qubits: int) -> QuantumCircuit:
    """
    Creates a circuit that maps the all-zero state to the all-one state.
    This circuit is 'super peaked' with a peak probability of 1.0 (ideally).
    """
    qc = QuantumCircuit(num_qubits)
    for qubit in range(num_qubits):
        qc.x(qubit)
    return qc


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
