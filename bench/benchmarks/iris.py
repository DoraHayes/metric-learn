import numpy as np
from sklearn.datasets import load_iris

import metric_learn

CLASSES = {
    'Covariance': metric_learn.Covariance(),
    'ITML_Supervised': metric_learn.ITML_Supervised(n_constraints=200),
    'LFDA': metric_learn.LFDA(k=2, dim=2),
    'LMNN': metric_learn.LMNN(n_neighbors=5, learn_rate=1e-6, verbose=False),
    'LSML_Supervised': metric_learn.LSML_Supervised(n_constraints=200),
    'MLKR': metric_learn.MLKR(),
    'NCA': metric_learn.NCA(max_iter=700, n_components=2),
    'RCA_Supervised': metric_learn.RCA_Supervised(dim=2, n_chunks=30,
                                                  chunk_size=2),
    'SDML_Supervised': metric_learn.SDML_Supervised(n_constraints=1500)
}


class IrisDataset(object):
  params = [sorted(CLASSES)]
  param_names = ['alg']

  def setup(self, alg):
    iris_data = load_iris()
    self.iris_points = iris_data['data']
    self.iris_labels = iris_data['target']

  def time_fit(self, alg):
    np.random.seed(5555)
    CLASSES[alg].fit(self.iris_points, self.iris_labels)
