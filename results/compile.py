import os
import json

directory = "./"

instancias = ["020","040","060","080","100","200","400"]
alphas = ["alpha-5", "alpha-17"]
local = ["best-improving", "first-improving"]
heuristic = ["standart-heuristic", "pop-heuristic", "random-plus"]

resultados = {a :
              {l :
               {h :
                 {i : ("custo", "tempo")
                  for i in instancias}
                for h in heuristic}
               for l in local}
              for a in alphas}

for filename in os.listdir(directory):
    if not filename.startswith("alpha"):
        continue

    a, l, h = filename.split("_")
    with open(filename, "r") as fd:
        for inst in instancias:
            res = fd.readline().split("]")
            time = fd.readline().split()
            resultados[a][l][h][inst] = (res[0][26:-2], time[2])

with open("compiled_results.json", "w") as fd:
    fd.write(json.dumps(resultados, indent=4, sort_keys=True))
