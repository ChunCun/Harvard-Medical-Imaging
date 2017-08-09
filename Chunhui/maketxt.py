import numpy as np

DD_logits = [1, 2, 3, 4]
filename = "newstuff"
OutputFile = open('%s.txt' %("new"), 'wb')
np.savetxt(OutputFile, DD_logits, fmt='%.5f')



