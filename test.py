import UnityEngine as ue

test = None

all_objects = ue.Object.FindObjectsOfType(ue.GameObject)
for go in all_objects:
    if go.name == 'Teste':
        test = go
        break
    
print("{}".format(dir(test)))