district = ["ST", "BD", "BTL", "CG", "DD", "HBT"]
popu = [150300, 247100, 333300, 266800, 420900, 318000]
area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
density = []
for a, b in zip(popu, area):
    c = a/b
    density.append(c)
maxi = max(popu)
mini = min(popu)
print("Maximum population:", maxi)
print("Minimum population:", mini)
max_distr = district[popu.index(maxi)]
min_distr = district[popu.index(mini)]
print("The district that have the maximum population:", max_distr)
print("The district that have the minimum population:", min_distr)
averge_density = sum(density)/len(density)
print("The average density is:", averge_density)