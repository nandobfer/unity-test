import UnityEngine as ue

all_objects = ue.Object.FindObjectsOfType(ue.GameObject)
for go in all_objects:
    ue.Debug.log(go.name)