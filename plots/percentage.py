import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tests_df = pd.read_csv('../data/all_tests.csv')
all_tests = 2074  # 1248 sick


print(tests_df['test_suite'].nunique())

grouped = tests_df.groupby(['smell'], as_index=False).count().sort_values(by='test_suite', ascending=False)
grouped['percentage'] = round(grouped['test_suite'] / all_tests, 4) * 100

# g = sns.barplot(x="percentage", y="smell", data=grouped,
#                 color='steelblue')
#
# g.set(xlim=(0, 100))
# g.bar_label(g.containers[0])
#
# plt.ylabel('')
# plt.xlabel('smell proc', size=11)
# plt.yticks(size=11)
# plt.savefig('images/percentage/all_perc.png', dpi=300)
