import ephem

mars = ephem.Mars('2000/01/01')
#n = ephem.Planet.name
#print(n)
constellation = ephem.constellation(mars)
print(constellation)

# define planets


#here = ephem.Observer()
#neptune.compute(here)
#print(neptune[0])
#neptune_const = ephem.constellation(neptune)
constellation = ephem.constellation(neptune)
print ("neptune const:", constellation)