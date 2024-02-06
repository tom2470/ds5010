from readit import readit_all
import matplotlib.pyplot as plt
from process import process_da_data 

def plotit(x, y, z, xlabel, ylabel, zlabel, title):
  # Get a list of unique categories
  species = list(set(z))

  # Get the tableau colormap
  colormap = {s: ['tab:blue', 'tab:orange', 'tab:green'][i] for i,s in enumerate(species)}

  # To include a legend, we'll use the OO API
  fig, ax = plt.subplots()

  for s in species:
    xs = [d for i, d in enumerate(x) if s == z[i]]
    ys = [d for i, d in enumerate(y) if s == z[i]]
    ax.scatter(xs, ys, c=colormap[s], label=s)

  ax.legend()
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  ax.set_title(title)
  plt.savefig("figs/penguins.png")
  plt.show()



def main():
  xlabel = "bill_length_mm"
  ylabel = "flipper_length_mm"
  zlabel = "species"
  x, y, z = process_da_data(readit_all('data/penguins.csv'), xlabel, ylabel, zlabel)
  plotit(x, y, z, xlabel, ylabel, zlabel, "Penguins")

main()