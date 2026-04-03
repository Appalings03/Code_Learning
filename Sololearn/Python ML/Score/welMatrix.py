#233 65 109 480 
#0.8038
#0.7819
#0.6813
#0.7281
tp, fp, fn, tn = [int(x) for x in input().split()]

ac = (tp + tn) / (tp+fp+fn+tn)
pr = tp / (tp + fp)
re = tp / (tp + fn)
f1 = (2 * pr * re) / (pr + re)

output = [ac, pr, re, f1]

for i in output:
	print(round(i, 4))