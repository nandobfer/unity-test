import UnityEngine

all_objects = UnityEngine.Object.FindObjectsOfType(UnityEngine.TextMeshProUGUI)
for object in all_objects:
    print(object)
