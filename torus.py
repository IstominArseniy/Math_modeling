import gmsh
import math

gmsh.initialize()
gmsh.model.add("torus")
lc = 0.5
center = gmsh.model.geo.addPoint(10, 0, 0)
p1 = gmsh.model.geo.addPoint(10, 0, 1, lc)
p2 = gmsh.model.geo.addPoint(10 - 3**0.5 / 2, 0, -0.5, lc)
p3 = gmsh.model.geo.addPoint(10 + 3**0.5 / 2, 0, -0.5, lc)
# basic circle
arc1 = gmsh.model.geo.addCircleArc(p1, center, p2)
arc2 = gmsh.model.geo.addCircleArc(p2, center, p3)
arc3 = gmsh.model.geo.addCircleArc(p3, center, p1)
# circle = gmsh.model.geo.addCurveLoop([arc1, arc2, arc3])
# print(circle)
# circle_plane = gmsh.model.geo.addPlaneSurface([circle])
# external torus
torus1_1 = gmsh.model.geo.revolve([(1, arc1), (1, arc2), (1, arc3)], 0, 0, 0, 0, 0, 1, 2 / 3 * math.pi)
torus1_2 = gmsh.model.geo.copy(torus1_1)
gmsh.model.geo.rotate(torus1_2, 0, 0, 0, 0, 0, 1, math.pi * 2 / 3)
s = gmsh.model.getEntities(2)
print(s)
# l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
# gmsh.model.geo.addVolume([l])
# torus1_3 = gmsh.model.geo.copy(torus1_2)
# print(torus1_3)
# gmsh.model.geo.rotate(torus1_3, 0, 0, 0, 0, 0, 1, math.pi * 2 / 3)

# torus1_2 = gmsh.model.geo.revolve(torus1_1, 0, 0, 0, 0, 0, 1, 2/3 * math.pi)
# torus1_3 = gmsh.model.geo.revolve([(1, arc1), (1, arc2), (1, arc3)], 0, 0, 0, 0, 0, 1, 2/3 * math.pi)

# view
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)
gmsh.write("cube.msh")
gmsh.fltk.run()
gmsh.finalize()
