# This is some code to graph accuracy of binary classifiers 
import numpy as np
import matplotlib.pyplot as plt

# TP, TN, FP, FN

A8 = [21, 16, 4, 4]
AW = [19, 24, 1, 6]
CB = [21, 22, 3, 4]
D6 = [20, 22, 3, 5]
FC = [19, 19, 6, 6]
JH = [6, 6, 1, 1]
FF = [9, 20, 1, 5]

def normalize_scores(values):
    total = sum(values)
    for x in range(0, 4):
        values[x] = float(values[x]) / total


normalize_scores(A8)
normalize_scores(AW)
normalize_scores(CB)
normalize_scores(D6)
normalize_scores(FC)
normalize_scores(JH)
normalize_scores(FF)

print(A8)
print(AW)
print(CB)
print(D6)
print(FC)
print(JH)
print(FF)

N = 7
true_positives = np.array([A8[0], AW[0], CB[0], D6[0], FC[0], JH[0], FF[0]])
true_negatives = np.array([A8[1], AW[1], CB[1], D6[1], FC[1], JH[1], FF[1]])
false_positives = np.array([A8[2], AW[2], CB[2], D6[2], FC[2], JH[2], FF[2]])
false_negatives = np.array([A8[3], AW[3], CB[3], D6[3], FC[3], JH[3], FF[3]])
width = 0.35
ind = np.arange(7)


plt.rcParams.update({'font.size': 30})

# two shades of green then two shades of red, change segmentation of red to orange

p2 = plt.bar(ind, true_positives, width, color='DarkGreen')
p1 = plt.bar(ind, true_negatives, width, color='Green', bottom=true_positives)
p3 = plt.bar(ind, false_positives, width, color='Orange', bottom=true_negatives + true_positives)
p4 = plt.bar(ind, false_negatives, width, color='DarkOrange', bottom=true_negatives+true_positives+false_positives)
plt.ylabel('Scaled Accuracy')
plt.title('Scaled Accuracy for Each Classifier')
plt.xticks(ind + width/2., ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7'))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.show()

plt.legend((p4[0], p3[0], p1[0], p2[0]), ('False Negatives', 'False Positives', 'True Negatives', 'True Positives'))
#Fals = red
# add false thignies to the graph
# change colors so not the segmentation
print(str(sum(false_positives) / 7))
plt.show()


# Thinner boxes for the method, try having them be verticle
