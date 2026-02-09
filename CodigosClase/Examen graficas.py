import matplotlib as plot

meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "octubre", "noviembre", "diciembre"]
colores=["#FF0000", "#00FF00",  "#0000FF", "#FFFF00",  "#00FFFF", "#FF00FF", "#C0C0C0","#808080", "#808000","#008000","#800080","#000080"  ]
incidencias=[2,10,1,52,25,36,12,5,1,3,49]

#crear grafico de barras

plot.figure(figsize=(30,15), dpi=120)

title=("Incidencias")
subtitle=("Incidencias del año 2025")

plot.title("incidencias", fontsize=15)
plot.xlabel("mes", fontsize=10)
plot.ylabel("incidencias", fontsize=10)



