import matplotlib.pyplot as plt

languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'

popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

colors = ["#8c564b", "#9467bd", "#d62728", "#2ca02c", "#ff7f0e", "#1f77b4"]

explode = (0.1, 0, 0, 0,0,0)

plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()