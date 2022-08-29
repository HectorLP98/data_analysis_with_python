import numpy as np

def calculate(list):
    n = len(list)
    if n ==9:
        arrayf = np.array(list)
           
        array = arrayf.reshape((3,3))
        meanl = []
        varl = []
        stdl = []
        maxl = []
        minl = []
        suml = []
        for k in range(2):
            meanl.append(np.mean(array, axis=k).tolist())
            stdl.append(np.std(array, axis=k).tolist())
            varl.append(np.var(array, axis=k).tolist())
            maxl.append(np.max(array, axis=k).tolist())
            minl.append(np.min(array, axis=k).tolist())
            suml.append(np.sum(array, axis = k).tolist())
        
        calculations = {
            'mean': [meanl[0], meanl[1], np.mean(arrayf)],
            'variance': [varl[0], varl[1], np.var(arrayf)],
            'standard deviation': [stdl[0], stdl[1], np.std(arrayf)],
            'max': [maxl[0], maxl[1], np.max(arrayf)],
            'min': [minl[0], minl[1], np.min(arrayf)],
            'sum': [suml[0], suml[1], np.sum(arrayf)]
            }
        #print(meanl)
        
    else:
        raise ValueError("List must contain nine numbers.")

    

    return calculations