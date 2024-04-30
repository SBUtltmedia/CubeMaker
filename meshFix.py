import pymeshfix
import trimesh
import sys
model = trimesh.load(sys.argv[1])

# Create object from vertex and face arrays
meshfix = pymeshfix.MeshFix(model.vertices, model.faces)

# Repair the mesh
meshfix.repair(True)

# rewrite the model
model_repair = trimesh.Trimesh(vertices=meshfix.v, faces=meshfix.f)
#meshfix.mesh.plot()
model_repair.export('stuff.obj')