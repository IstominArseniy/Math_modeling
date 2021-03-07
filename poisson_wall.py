from dolfin import *
from matplotlib import pyplot as plt
# Create mesh and define function space
mesh = UnitSquareMesh(64, 64)
V = FunctionSpace(mesh, "Lagrange", 1)

# Define Dirichlet boundary (x = 0 or x = 1)
def boundary(x):
    return x[0] > 1.0 - DOLFIN_EPS

# Define boundary condition
u0 = Constant(0.0)
bc = DirichletBC(V, u0, boundary)

# Define variational problem
u = TrialFunction(V)
v = TestFunction(V)
f = Expression("(x[0]-x_0) * (x[0]-x_0) + (x[1]-y_0) * (x[1]-y_0) <= r * r ? 1.0 : 0.0", degree=2, x_0=0.5, y_0=0.5, r=0.01)
a = inner(grad(u), grad(v))*dx
L = f*v*dx

# Compute solution
u = Function(V)
solve(a == L, u, bc)

# Save solution in VTK format
file = File("poisson/poisson_wall.pvd")
file << u

