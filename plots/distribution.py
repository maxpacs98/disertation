import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tests_df = pd.read_csv('../data/all_tests.csv')

with sns.axes_style('white'):
    g = sns.catplot(y="smell", data=tests_df, aspect=2,
                    kind="count", color='steelblue')

# plt.show()

plt.ylabel('')
plt.xlabel('smell count', size=11)
plt.yticks(size=11)
plt.savefig('images/all_count.png', dpi=300)
