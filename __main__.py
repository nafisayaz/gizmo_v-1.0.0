

# -*- coding: utf-8 -*-
"""
Created on Sat May 26 14:21:20 2018

@author: nafis
"""


from audio_record import audio_record as ar
from speech_synthesizer import speech_synthesizer as ss
from audio_recognizer import audio_recognizer as AU
from profiler import profiler as pr

from os import path
import threading


AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "new_file.wav")


def listen():
	m = ar.Audio_record()
	m.record()
	m.writeFile()
	m.readFile()



def reply():
	text = AU.Audio_recognizer(AUDIO_FILE).text() # client text
	g.reply(text)
#	g.reply("hi")
	return text


if __name__ == "__main__":

	g = ss.speech_syn("Gizmo", "Hi");

	review_list = []

	while 1:
		listen()

		data = reply()
		print("FROM __MAIN__   =>  ", data)
	#	data = "yes"
		if data == "yes":
			tag_value = pr.Profiler().pro_fetch_questions()
			index = 0;
			while 1:
				labelled_str = pr.Profiler().pro_labelling(tag_value[index])
				g.say(labelled_str); 
				listen();
				text = AU.Audio_recognizer(AUDIO_FILE).text()
			#	print(text)
				s = pr.Profiler().pro_process(tag_value[index][0], text);
				if s[0] == 1:
					review_list.append(s)
					index +=1
				if index == len(tag_value):
					print("-->", review_list)
					break;


		if data == "bye":
			break;

#    help(AU)

	


#
