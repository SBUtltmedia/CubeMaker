import pyvista as pv

bunny = pv.read("SetTest.obj")

points = pv.wrap(bunny.points)
surf = points.reconstruct_surface(nbr_sz=1)

pl = pv.Plotter(shape=(1, 2))
pl.add_mesh(points)
pl.add_title("Point Cloud of 3D Surface")
pl.subplot(0, 1)
pl.add_mesh(surf, color=True, show_edges=True)
pl.add_title("Reconstructed Surface")
pl.show()
