from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

def f(theta, m, x):
	return np.cos(m*theta - x*np.sin(theta))

def J(m, x):
	I, err = integrate.quad(f, 0, np.pi, args = (m, x))
	return I/np.pi	
