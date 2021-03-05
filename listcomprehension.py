temp = [221,223,259,456,-999]
mod_temp = [temps / 10 for temps in temp if temps> 0]
print(type(mod_temp))
print(mod_temp)

temp1 = [221,223,259,456,-999]
mod_temp1 = [temps / 10 if temps> 0 else 0 for temps in temp1 ]
print(type(mod_temp1))
print(mod_temp1) 