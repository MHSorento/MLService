import numpy as np

class SKUFeatureValues(object):
	def __init__(self):
		self.skus = None
		self.features = None

	def get_closest_sku(self, sku, n_skus):
		if self.skus is None:
			self.load_skus()

		if self.features is None:
			self.load_features()

		n_skus = min(n_skus, len(self.skus))

		sku_idx = self.skus.index(sku)
		print sku_idx

		if sku_idx is None:
			return None
		else:
			sku_feature = self.features[sku_idx, :]
			dist_2 = np.sum((self.features - sku_feature)**2, axis=1)
			indices = np.argsort(dist_2)[:(n_skus+1)].tolist()

		return [self.skus[idx] for idx in indices[1:]]

	def load_skus(self):
		self.skus = ['a','b', 'c', 'd', 'e']

	def load_features(self):
		self.features = np.zeros([5, 2])
		self.features[0, :] = np.asarray([[.15, .15]])
		self.features[1, :] = np.asarray([[.21, .21]])
		self.features[2, :] = np.asarray([[.3, .3]])
		self.features[3, :] = np.asarray([[.4, .4]])
		self.features[4, :] = np.asarray([[.44, .44]])
		print self.features

def main():
	obj = SKUFeatureValues()
	print obj.get_closest_sku('b', 1)
	print obj.get_closest_sku('d', 3)

if __name__ == "__main__":
	main()
