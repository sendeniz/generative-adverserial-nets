import numpy as np
import pandas as pd

from packaging import version
from collections import defaultdict

from scipy import stats
import tensorflow as tf
import tensorboard as tb

major_ver, minor_ver, _ = version.parse(tb.__version__).release
assert major_ver >= 2 and minor_ver >= 3, \
    "This notebook requires TensorBoard 2.3 or later."
print("TensorBoard version: ", tb.__version__)

from tensorflow.python.summary.summary_iterator import summary_iterator
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator

event_data = input("Event Data File: ")

for event in summary_iterator(event_data):
    for value in event.summary.value:
        print(value.tag)
        if value.HasField('simple_value'):
            print(value.simple_value)
			
def parse_events_file(path: str) -> pd.DataFrame:
    metrics = defaultdict(list)
    for e in summary_iterator(path):
        for v in e.summary.value:

            if isinstance(v.simple_value, float):
                metrics[v.tag].append(v.simple_value)
            if v.tag == 'loss' or v.tag == 'accuracy':
                print(v.simple_value)
    metrics_df = pd.DataFrame({k: v for k,v in metrics.items() if len(v) > 1})
    return metrics_df

def get_hist(path):

  STEP_COUNT = 50

  event_acc = EventAccumulator(path, size_guidance={
      'histograms': STEP_COUNT,
  })
  event_acc.Reload()
  tags = event_acc.Tags()
  result = []
  for hist in tags['histograms']:
      histograms = event_acc.Histograms(hist)
      result = np.array([np.repeat(np.array(h.histogram_value.bucket_limit), np.array(h.histogram_value.bucket).astype(np.int)) for h in histograms])
  return result

 event_out = parse_events_file(event_data)
event_hist = get_hist("./event")