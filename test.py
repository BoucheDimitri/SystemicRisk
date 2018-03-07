import numpy as np
import importlib
import BankNetwork

importlib.reload(BankNetwork)

# Initialization of toy parameters
r = 0.03
xi = 0.7
zeta = 0.7
n = 5
m = 2
R0 = 1000
mL = 1000
stdL = 100
mQ = 500
stdQ = 250
alpha0 = 0.4
L = np.random.normal(mL, stdL, (n, n))
R = R0 * np.ones(shape=(n, ))
Q = np.absolute(np.random.normal(mQ, stdQ, (n, m)))
alphas = alpha0 * np.ones(shape=(n, ))

# Initialization of the BankNetwork
network = BankNetwork.BankNetwork(L, R, Q, alphas, r, xi, zeta)

# Test for the class methods
network.add_liquidator()
network.net_loans_matrix()
print(network.get_loans())
print(network.get_debts())

# Test for protfolio update
prices = np.random.normal(10, 1, m)
network.update_portfolios(prices)
print(network.Q)
print(network.P)

# Test for equity update
network.update_equities()
print(network.get_equities())

# Test for defaulting and defaulted
network.update_defaulted()
network.E[2] = 0
print(network.get_defaulting())
print(network.get_defaulted())
network.update_defaulted()
print(network.get_defaulted())



# Test for compute psi et pi
network.compute_pi()
network.compute_psi()
#print(network.get_pi())
#print(network.get_psi())
#print(network.L)