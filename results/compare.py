import json

instancias = ["020","040","060","080","100","200","400"]
alphas = ["alpha-5", "alpha-17"]
local = ["best-improving", "first-improving"]
heuristic = ["standart-heuristic", "pop-heuristic", "random-plus"]

with open("compiled_results.json", "r") as fd:
    resultados = json.loads(fd.read())

# resultados[alpha][best/first][heuristic][inst]
# Comparação entre alphas
for i in instancias:
    print(i)
a = "alpha-5"
h = "pop-heuristic"
for l in local:
    print(l)
    for i in instancias:
        print(resultados[a][l][h][i][0])
