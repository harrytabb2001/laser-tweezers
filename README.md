# Neutrino Oscillations
## Summary
First lab experiment from my third year undergraduate in Physics at The University of Manchester.

This experiment aimed to investigate the motion of micron-sized silica beads in an optical trap. Two different methods for calculating the optical trap stiffness as a function of laser power were then compared. The first method used the Boltzmann distribution to predict the probability of a particle's position. The second method used the mean squared displacement of the particle's position. It was concluded that the Boltzmann distribution method was more accurate as it produced a better linear fit.
As an extension, I also simulated the experiment in Python to overcome the limitations of the practical setup. Using this, I investigated the effects of a 3-dimensional optical trap, temperature and viscosity gradients, multiple optical traps and intensity gradients.

## Technical Highlights
* Monte Carlo simulation techniques in Python
* Stochastic Calculus
* Fitting non-linear functions to data (Gaussians)
* Chi-Square contour analysis for errors on fit parameters
* Data Visualisation in Matplotlib

## Files 

* Brownian Motion.ipynb contains my simulation for brownian motion. This was done to overcome limitations of the experiment such as only being able to record motion in 2 dimensions. It is worth noting that this went significantly beyond what was expected by the lab script.
* Laser Tweezers Lab Notebook.pdf contains my handwritten notes from during the experiment including schematic diagrams, key figures, snippets of the recorded data, calculations, data analysis and conclusions.
* Lazer Tweezers Lab Script.pdf contains a breif outline of the experiment given to me before I started.
* Lazer Tweezers Lab Report.pdf contains my official lab report for the experiment, this explains the experiment and theory in academic format
* currentpower.py and kappa vs power.py contain basic python code to plot 2 dimensional plots for the lab notebook and script


