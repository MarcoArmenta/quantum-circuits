import numpy as np
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit import *

if __name__ == "__main__":
	teleport = QuantumCircuit(3,3)
	teleport.x(0) #initialize q0=|1> for teleportation
	teleport.h(1) #entangle qubits q1 and q2
	teleport.cx(1,2)
	teleport.cx(0,1)
	teleport.h(0)
	teleport.measure([0,1],[0,1])
	teleport.cx(1,2)
	teleport.cz(0,2)
	teleport.measure(2,2)
	teleport.draw(output='mpl')

	print('Qubit q0 after the X gate is in state |1>'\
		' which will be teleported to qubit q2.')

	hist = execute(teleport, backend = Aer.get_backend('qasm_simulator'), 
			shots = 256).result().get_counts()
	print('We can see in the histogram that we only have results for states'\
		' where qubit q2 is in state |1>. This confirms teleportation.')
	plot_histogram(hist)
	plt.show()
