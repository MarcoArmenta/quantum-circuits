# Quantum circuits with Qiskit

## Description
Some quantum circuits with Qiskit.

## How to run
First, install dependencies   
```bash
# set-up project's environment
conda env create -f requirements/quantum.yml

# activate the environment so that we install the project's package in it
conda activate quantum
pip install -e .

# run scripts and follow instructions
python QuantumTeleportation.py

python Bernstein-Vazirani.py
