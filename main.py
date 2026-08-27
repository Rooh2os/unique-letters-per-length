import csv
import matplotlib.pyplot as plot
import numpy
with open("/usr/share/dict/words","rt") as f:
    words = f.read().split()

start = len(words)
print(f"Words started out at {start}")

data = []
for word in words:
    if "'" not in word:
        data.append({
            "Word": word,
            "Length": len(word),
            "Unique Letters": len(set(word)),
            "Ratio": len(set(word))/len(word)
        })


afterRemove = len(data)
print(f"Words narrowed down to {afterRemove} after removing '\nThats a difference of {start-afterRemove}")

sortedData = sorted(data, key=lambda dict: dict["Ratio"])

with open("saves/data.csv","wt") as f:
    writer = csv.DictWriter(f,["Word","Length","Unique Letters","Ratio"])
    writer.writeheader()
    writer.writerows(sortedData)

lengths = [d["Length"] for d in data]
ratios = [d["Ratio"] for d in data]
jitteredLengths = [d + numpy.random.uniform(-0.35,0.35) for d in lengths]
jitteredRatios = [d + numpy.random.uniform(-0.01,0.01) for d in ratios]

plot.figure(1,figsize=(10,6))
plot.scatter(jitteredLengths,jitteredRatios,alpha=.2,c="blue",edgecolors="none")

plot.title("Word Length vs. Unique Letter Ratio with jitter", fontsize=14, fontweight="bold")
plot.xlabel("Word Length (Number of Characters)", fontsize=11)
plot.ylabel("Unique Letter Ratio (Unique / Total)", fontsize=11)

plot.grid(True)

plot.savefig("saves/Figure_1.svg", format="svg", bbox_inches="tight")

plot.figure(2,figsize=(10,5))
plot.hist(lengths,color="blue",edgecolor="black")

plot.title("Distribution of lengths", fontsize=14, fontweight="bold")
plot.xlabel("Word Length (Number of Characters)", fontsize=11)
plot.ylabel("Count", fontsize=11)

plot.savefig("saves/Figure_2.svg", format="svg", bbox_inches="tight")

plot.figure(3,figsize=(10,5))
plot.hist(ratios,color="blue",edgecolor="black")

plot.title("Distribution of ratios", fontsize=14, fontweight="bold")
plot.xlabel("Unique Letter Ratio (Unique / Total)", fontsize=11)
plot.ylabel("Count", fontsize=11)

plot.grid(True)

plot.savefig("saves/Figure_3.svg", format="svg", bbox_inches="tight")

plot.figure(4,figsize=(10,6))
plot.scatter(lengths,ratios,alpha=.2,c="blue",edgecolors="none")

plot.title("Word Length vs. Unique Letter Ratio without jitter", fontsize=14, fontweight="bold")
plot.xlabel("Word Length (Number of Characters)", fontsize=11)
plot.ylabel("Unique Letter Ratio (Unique / Total)", fontsize=11)

plot.grid(True)

plot.savefig("saves/Figure_4.svg", format="svg", bbox_inches="tight")

plot.show()