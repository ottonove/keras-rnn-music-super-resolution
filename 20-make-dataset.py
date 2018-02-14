import numpy as np
from scipy.io import wavfile 

import pickle
import time
import random
deg = np.array(wavfile.read('waves/degradation.wav')[1], dtype=np.int16)
org = np.array(wavfile.read('waves/origin.wav')[1], dtype=np.int16)

deg = deg.tolist()
org = org.tolist()

Xs, Ys = [], []
for index, d in enumerate(range(len(deg)-1)):
  d = deg[d]
  #print(d)
  xs = [d]*5
  ys = []
  for i in range(5): 
    key_org = index*5 + i
    o = org[key_org]
    ys.append(o)
  Xs.append(xs)
  Ys.append(ys)

sources, targets = [], []
for i in range(0,len(Xs),20):
  source = sum(Xs[i:i+50],[])
  target = sum(Ys[i:i+50],[]) 
  if random.random() > 0.8:
    continue
  if len(source) == 250 and len(target) == 250:
    sources.append( source )
    targets.append( target )

length = len(sources)
sources = np.array(sources, dtype=float).reshape((length, 250,1))/32767
targets = np.array(targets, dtype=float).reshape((length, 250,1))/32767
print(sources.shape)
open('dataset.pkl', 'wb').write( pickle.dumps( (sources, targets) ) )


sources, targets = [], []
for i in range(0,len(Xs),50):
  source = sum(Xs[i:i+50],[])
  target = sum(Ys[i:i+50],[]) 
  if len(source) == 250 and len(target) == 250:
    sources.append( source )
    targets.append( target )

length = len(sources)
sources = np.array(sources, dtype=float).reshape((length, 250,1))/32767
targets = np.array(targets, dtype=float).reshape((length, 250,1))/32767
print(sources.shape)
open('predict.pkl', 'wb').write( pickle.dumps( (sources, targets) ) )
