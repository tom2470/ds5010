import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def label_get(list):
    for i in range(len(list)):
        list[i]=str(list[i])[0]
    return list

def main():
    df=pd.read_csv("data/penguins.csv")
    df.dropna(how="any",inplace=True)
    myplot=sns.barplot(data=df, x="island", y="body_mass_g", hue="sex")
    label=myplot.get_xticklabels()
    label=[str(x)[12] for x in label ]
    myplot.set_xticklabels(label)
    handles, labels = myplot.get_legend_handles_labels()
    myplot.legend(handles, label_get(labels))
    myplot.set_title("penguins")
    plt.savefig("figs/penguins.png")
    plt.show()
    
main()