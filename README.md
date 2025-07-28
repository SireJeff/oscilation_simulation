# Waves Simulation Using Mass-Spring Systems

A comprehensive computational physics project that simulates wave dynamics through coupled oscillator systems, exploring normal modes, symmetry effects, and wave propagation phenomena.

## 📋 Project Overview

This project implements numerical simulations of wave behavior using mass-spring systems, providing insights into fundamental wave physics concepts through computational modeling. The study is divided into two main parts that progressively build complexity from simple coupled oscillators to advanced multi-oscillator systems.

## 🎯 Objectives

- **Model Coupled Oscillators**: Define physical parameters and derive equations of motion for interconnected pendulum systems
- **Numerical Simulation**: Implement differential equation solvers to simulate time evolution of oscillatory systems  
- **Visualization & Analysis**: Create dynamic visualizations and analyze normal modes, energy distribution, and parameter effects
- **Wave Propagation Study**: Extend simulations to multiple oscillators for investigating wave phenomena
- **Real-World Physics**: Incorporate damping effects and nonlinear dynamics for realistic system modeling

## 🔬 Physics Concepts Explored

- **Normal Modes**: Natural oscillation frequencies where system components move harmonically
- **Energy Transfer**: Propagation and distribution of energy through coupled systems
- **Wave Propagation**: Disturbance transmission through oscillator networks
- **Resonance & Damping**: System response to external forces and energy dissipation effects
- **Symmetry Effects**: Impact of geometric arrangements on oscillation patterns

## 📁 Project Structure

### Part 1: Two Coupled Oscillators
- **System Modeling**: Define parameters (masses, spring constants, pendulum lengths)
- **Equations of Motion**: Derive differential equations using Newton's laws
- **Numerical Implementation**: Solve coupled ODEs using scipy integration methods
- **Visualization**: Create time-series plots and phase space representations
- **Normal Mode Analysis**: Identify and characterize fundamental oscillation modes

### Part 2: Advanced Multi-Oscillator Systems
- **Extended Systems**: Simulate networks of 6+ interconnected oscillators
- **Eigenvalue Analysis**: Solve matrix eigenvalue problems for normal frequencies
- **Complex Dynamics**: Investigate wave propagation and interference patterns
- **Symmetry Studies**: Analyze effects of circular and geometric arrangements
- **Damping Effects**: Model energy dissipation in realistic systems

## 🛠️ Technical Implementation

**Languages & Libraries:**
- Python 3.x
- NumPy (numerical computations)
- SciPy (differential equation solving)
- Matplotlib (visualization and animation)

**Key Features:**
- Fourth-order Runge-Kutta integration
- Real-time animation capabilities
- Parameter sweep analysis
- Normal mode decomposition
- Phase space trajectory plotting

## 📊 Simulation Capabilities

- Time evolution of coupled pendulum systems
- Normal mode identification and visualization
- Energy transfer patterns between oscillators
- Wave propagation through oscillator chains
- Parameter sensitivity analysis
- Damping and nonlinear effect modeling

## 🎓 Educational Value

This project serves as an excellent introduction to:
- Computational physics methods
- Classical mechanics and wave theory
- Numerical integration techniques
- Scientific visualization
- Linear algebra applications in physics

## 📈 Results & Visualizations

The project generates comprehensive visual outputs including:
- Time-series plots of oscillator displacements
- Phase space trajectories
- Normal mode animations
- Energy distribution patterns
- Wave propagation snapshots

## 🔧 Usage

Each Python script is self-contained and can be run independently:

```bash
# Part 1 simulations
cd part1/
python part1.py  # Basic coupled oscillator modeling
python part2.py  # Extended analysis
python part3.py  # Visualization enhancements
python part4.py  # Normal mode analysis

# Part 2 simulations  
cd part2/
python part1.py  # Multi-oscillator systems
python part2.py  # Eigenvalue analysis
python part3.py  # Advanced dynamics
python part4.py  # Comprehensive studies
```

## 📖 Documentation

Complete theoretical background, mathematical derivations, and detailed analysis are provided in the comprehensive LaTeX report (`latex/report.pdf`).

## 🎯 Applications

Understanding gained from this project applies to:
- Mechanical vibrations in engineering structures
- Acoustic wave propagation
- Molecular dynamics simulations
- Seismic wave analysis
- Telecommunications and signal processing

## 👨‍🎓 Author

Mohammad Hasan Shiri  
Sharif University of Technology  
Fall 2024

---

*This project demonstrates the power of computational methods in understanding fundamental physics concepts and provides practical experience with numerical simulation techniques used in modern scientific research.*
