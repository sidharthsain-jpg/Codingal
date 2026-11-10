names=["Pranav","Avinab","Rudraa","Emilea","Aditya"]
scores=[40,99,100,97,0]
for c in range(0,5):
    print(names[c],scores[c])
    break
for p in range(0,5):
    for e in range(p+1,5):
        if scores[p]+scores[e]== 197:
            print(names[p],names[e])