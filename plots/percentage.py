import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def show_values(axs, orient="v", space=.01):
    def _single(ax):
        if orient == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height() * 0.01)
                value = '{:.1f}'.format(p.get_height())
                ax.text(_x, _y, value, ha="center")
        elif orient == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height() * 0.5) + float(space)
                value = '{:.2f}%'.format(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        _single(axs)


proj = 'pytorch'


tests_df = pd.read_csv(f'../data/{proj}_tests.csv')
flask_count, pillow_count, sanic_count, pytorch_count, pandas_count = 338, 1064, 672, 167, 5398

all_tests = flask_count + pillow_count + sanic_count + pytorch_count + pandas_count

print(tests_df['test_name'].nunique())

# Maximum
# maxed = tests_df.groupby(['test_name'], as_index=False).count().sort_values(by='test_suite', ascending=False)
# grouped['percentage'] = round(grouped['test_suite'] / all_tests, 4) * 100

grouped = tests_df.groupby(['smell'], as_index=False).count().sort_values(by='test_suite', ascending=False)
grouped['percentage'] = round(grouped['test_suite'] / pytorch_count, 4) * 100

g = sns.barplot(x="percentage", y="smell", data=grouped,
                color='steelblue')

g.set(xlim=(0, 100))
show_values(g, "h", 0.1)
plt.ylabel('')
plt.xlabel(f'Percentage (%) of total {proj.capitalize()} tests ', size=12)
plt.yticks(size=12)

plt.savefig(f'images/percentage/{proj}.png', dpi=300, bbox_inches='tight')
