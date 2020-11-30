import matplotlib.pyplot as plt
import csv
plt.style.use('seaborn-whitegrid')

#give the Plot a name

plotname = "Plot_Difference.eps"
plotname_zoom = "zoomed_difference.eps"
molecule1 = "Aldehyde"
molecule2 = "Carbene"

x_diff = []
y_diff = []

with open('diff.csv', 'r') as csvfile_diff:
    plots = csv.reader(csvfile_diff, delimiter=',')
    for row in plots:
        x_diff.append(float(row[0]))
        y_diff.append(float(row[1])/5)

x_p1 = []
y_p1 = []

with open('aldehyde.csv', 'r') as csvfile_p1:
    plots = csv.reader(csvfile_p1, delimiter=',')
    for row in plots:
        x_p1.append(float(row[0]))
        y_p1.append(float(row[1])/4 + 0.15)

x_p2 = []
y_p2 = []

with open('carbene.csv', 'r') as csvfile_p2:
    plots = csv.reader(csvfile_p2, delimiter=',')
    for row in plots:
        x_p2.append(float(row[0]))
        y_p2.append(float(row[1])/4 - 0.15)

#full spectra
plt.plot(x_diff, y_diff, marker='o', markersize=0.0000001, linewidth=0.5, color="#008F00", label="Difference")
plt.plot(x_p1, y_p1, marker='o', markersize=0.0000001, linewidth=0.5, color="#8B2E2E", label=molecule1)
plt.plot(x_p2, y_p2, marker='o', markersize=0.000001, linewidth=0.5, color="#6388AC", label=molecule2)
plt.xlabel('Wavenumber / cm$^{-1}$')
plt.ylabel('Intensity / a.u.')
plt.axis([4000, 500, -0.16, 0.16])
plt.savefig(plotname, format='eps')

#zoomed spectra
plt.axis([1510, 500, -0.16, 0.16])
plt.savefig(plotname_zoom, format='eps')