import numpy as np

def calculate(list):
    if len(list)<9:
      raise ValueError("List must contain nine numbers.")
   
    else:
      TwoDnumpyArray=np.array(list).reshape(3,3)
      mean1=np.mean(TwoDnumpyArray,axis=0).tolist()
      mean2=np.mean(TwoDnumpyArray,axis=1).tolist()
      mean3=np.mean(TwoDnumpyArray).tolist()

      var1=np.var(TwoDnumpyArray,axis=0).tolist()
      var2=np.var(TwoDnumpyArray,axis=1).tolist()
      var3=np.var(TwoDnumpyArray).tolist()

      standardDeviation1=np.std(TwoDnumpyArray,axis=0).tolist()
      standardDeviation2=np.std(TwoDnumpyArray,axis=1).tolist()
      standardDeviation3=np.std(TwoDnumpyArray).tolist()

      max1=np.max(TwoDnumpyArray,axis=0).tolist()
      max2=np.max(TwoDnumpyArray,axis=1).tolist()
      max3=np.max(TwoDnumpyArray).tolist()

      min1=np.min(TwoDnumpyArray,axis=0).tolist()
      min2=np.min(TwoDnumpyArray,axis=1).tolist()
      min3=np.min(TwoDnumpyArray).tolist()

      sum1=np.sum(TwoDnumpyArray,axis=0).tolist()
      sum2=np.sum(TwoDnumpyArray,axis=1).tolist()
      sum3=np.sum(TwoDnumpyArray).tolist()

      dictionary={
        "mean":[mean1,mean2,mean3],
        "variance":[var1,var2,var3],
        "standard deviation":[standardDeviation1,standardDeviation2,standardDeviation3],
        "max":[max1,max2,max3],
        "min":[min1,min2,min3],
        "sum":[sum1,sum2,sum3]

      }

    return dictionary

