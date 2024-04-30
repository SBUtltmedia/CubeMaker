import pymeshlab
import sys
import trimesh
import pyvista as pv
import pymeshfix
import numpy as np
import pycork

tee = "4/tee.obj"
inModel = sys.argv[1]
ModelOut =inModel.split("/")[1].split(".")[0]
print (ModelOut)
def pymeshlab_intersection() -> None:
  
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(inModel)
    ms.load_new_mesh(tee)
    ms.apply_filter(
    'generate_boolean_intersection',
    first_mesh=0,
    second_mesh=1,
    transfer_face_color=True,
    transfer_face_quality=True,
    transfer_vert_color=True,
    transfer_vert_quality=True)
  
    # intersection_volume = ms.get_geometric_measures()["mesh_volume"]
    # print(f"pymeshlab - intersection volume = {intersection_volume}")



def pycork_intersection() -> None:
    meshA = trimesh.load_mesh(tee)
    meshB = trimesh.load_mesh(inModel)

    # Extra list of vertices and triangular faces from the meshes
    vertsA = meshA.vertices
    trisA = meshA.faces

    vertsB = meshB.vertices
    trisB = meshB.faces

    pycork.isSolid(vertsA, trisA)
    pycork.isSolid(vertsB, trisB)

    #Perform the boolean opertions directly with Cork library
    vertsC, trisC = pycork.union(vertsA, trisA,
                                vertsB, trisB)

    vertsD, trisD = pycork.intersection(vertsA, trisA,
                                        vertsB, trisB)


    meshC = trimesh.Trimesh(vertices=vertsC, faces=trisC, process=True)
    meshC.export(f"{ModelOut}bool.obj")





def pymesh_intersection() -> None:

    mesh_A = pymesh.load_mesh(tee)
    mesh_B = pymesh.load_mesh(inModel)
    output_mesh = pymesh.boolean(mesh_A, mesh_B,operation="intersection",engine="igl")
    pymesh.save_mesh(f"{ModelOut}bool.obj", mesh)

def pyvista_intersection() -> None:

    teevis = trimesh.load_mesh(tee, process=False, maintain_order=True)
    tee_pv = pv.wrap(teevis)
    inModelvis = trimesh.load_mesh(inModel, process=False, maintain_order=True)
    inModel_pv = pv.wrap(inModelvis)
    intersection = tee_pv.boolean_difference(inModel_pv)
    #intersection.compute_normals(inplace=True)
    tin = pymeshfix.PyTMesh()
    tin.load_array(intersection.points,intersection.faces.reshape((-1, 4))[:, 1:])
    tin.clean(max_iters=10, inner_loops=3)
    intersection.save(f"{ModelOut}bool.stl")
    print(f"pyvista - intersection volume = {intersection.volume}")



if __name__ == "__main__":
    pycork_intersection()
    #pyvista_intersection()
    #pymeshlab_intersection()
