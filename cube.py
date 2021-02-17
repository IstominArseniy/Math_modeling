import gmsh

gmsh.initialize()
gmsh.model.add("cube")
lc = 1e-1
# lower square
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(1, 1, 0, lc, 3)
gmsh.model.geo.addPoint(0, 1, 0, lc, 4)
# upper square
gmsh.model.geo.addPoint(0, 0, 1, lc, 5)
gmsh.model.geo.addPoint(1, 0, 1, lc, 6)
gmsh.model.geo.addPoint(1, 1, 1, lc, 7)
gmsh.model.geo.addPoint(0, 1, 1, lc, 8)
# lower square lines
gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)
# upper square line
gmsh.model.geo.addLine(5, 6, 5)
gmsh.model.geo.addLine(6, 7, 6)
gmsh.model.geo.addLine(7, 8, 7)
gmsh.model.geo.addLine(8, 5, 8)
# vertical lines
gmsh.model.geo.addLine(1, 5, 9)
gmsh.model.geo.addLine(2, 6, 10)
gmsh.model.geo.addLine(3, 7, 11)
gmsh.model.geo.addLine(4, 8, 12)
# curve loops
gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)
gmsh.model.geo.addCurveLoop([5, 6, 7, 8], 2)
gmsh.model.geo.addCurveLoop([1, 10, -5, -9], 3)
gmsh.model.geo.addCurveLoop([2, 11, -6, -10], 4)
gmsh.model.geo.addCurveLoop([3, 12, -7, -11], 5)
gmsh.model.geo.addCurveLoop([4, 9, -8, -12], 6)
# plane surfaces
for i in range(1, 7):
    gmsh.model.geo.addPlaneSurface([i], i)
# volume
l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(6)])
gmsh.model.geo.addVolume([l])
# view
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)
gmsh.write("cube.msh")
gmsh.fltk.run()
gmsh.finalize()
