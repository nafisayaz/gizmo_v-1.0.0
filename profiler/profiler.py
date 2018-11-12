
from processor import textProcessor as tp
import xml.etree.ElementTree as ET
import os
from NLU_unit import NLU_Unit as nlu

class Profiler:
	"""docstring for ClassName"""
	def __init__(self):
		self.data = None


	def pro_fetch_questions(self):
		file_path = "/home/nafis/projects/JobsMarkt/hunting_gizmo/XMLs/registration"
		xml_file = os.path.join(file_path, 'registration.xml')
		tree = ET.parse(xml_file)
		root = tree.getroot()

		tags = [(child.tag,child.text) for child in root ]
		return tags
		

	def pro_labelling(self, tag_ques_pair):
		print(tag_ques_pair)
		labelled_str = tp.textProcessor().put_frequency(tag_ques_pair[1])
		print(labelled_str)
		return labelled_str


	def pro_process(self, tag, text):
		if text == None and tag == None:
			return None

		return nlu.NLU_Unit().nlu_process(tag, text);

		














