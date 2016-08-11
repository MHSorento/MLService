import json
import numpy as np

INPUT_FILE = '/Users/rangoli/Dropbox/MLService/data/sku-data.json'
IMAGE_DIRECTORY = '/Users/rangoli/Dropbox/MLService/data/dev.json'

def get_all_skus():

	with open(INPUT_FILE) as data_file:    
		data = json.load(data_file)
	
	print len(data.keys())
	return data.keys()

def get_all_style_tags():
	style_tags = set()
	with open(INPUT_FILE) as data_file:
		data = json.load(data_file)
		for sku, blob in data.items():
			for style in blob["styles"]:
				style_tags.add(style)

	print len(list(style_tags))
	return	list(style_tags)

def get_sku_colors(skus):
	colors = []
	with open(INPUT_FILE) as data_file:
		data = json.load(data_file)
		for sku in skus:
			color = (data[sku]["color"]["rgb"].
				replace("r","").
				replace("g","").
				replace("b","").
				replace("(","").
				replace(")",""))

			color = [float(channel)/255. for channel in color.split(",")]
			colors.append(np.asarray(color))

	colors = np.asarray(colors)
	print colors.shape
	return colors

def get_style_tags(skus, style_tags):
	tags = []
	with open(INPUT_FILE) as data_file:
		data = json.load(data_file)
		for sku in skus:
			sku_tags = (data[sku]["styles"])
			tag_vector = np.zeros([1, len(style_tags)])

			for tag in sku_tags:
				idx = style_tags.index(tag)
				tag_vector[0, idx] = 1
			
			tags.append(tag_vector)

	tags = np.squeeze(np.asarray(tags))
	print tags.shape
	return tags

def get_image_data(skus):
	pass

def main():
	skus = get_all_skus()
	styles = get_all_style_tags()
	sku_colors = get_sku_colors(skus)
	sku_tags = get_style_tags(skus, styles)
	np.save('/Users/rangoli/Dropbox/MLService/mlengine/skus', skus)
	np.save('/Users/rangoli/Dropbox/MLService/mlengine/styles', styles)
	np.save('/Users/rangoli/Dropbox/MLService/mlengine/sku_colors', sku_colors)
	np.save('/Users/rangoli/Dropbox/MLService/mlengine/sku_tags', sku_tags)

if __name__ == "__main__":
	main()
