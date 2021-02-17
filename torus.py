import gmsh

gmsh.initialize()
gmsh.model.add("torus")
lc = 1e-1

# view
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)
gmsh.write("cube.msh")
gmsh.fltk.run()
gmsh.finalize()
