import pyaudio
import wave
from array import array

def record_audio():
	def is_silent(data):
		#wheh it's silent, max(data) tend to be 100~200
		return max(data) < THRESHOLD

	THRESHOLD = 500
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 44100
	CHUNK = 8192
	MINIMUM_RECORD_SECONDS = 3 #seconds (approximate)

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
				input_device_index=2)
				#^this value should be modified with mic index (use get_dev_index.py)

	print "* Recording audio..."

	frames = array('h')
	minimum = 0
	silent_counter = 0
	while True:
		data = array('h', stream.read(CHUNK))
		#record sounds while at least 3 seconds
		if minimum < int(RATE / CHUNK * MINIMUM_RECORD_SECONDS):
			frames.extend(data)
			minimum = minimum + 1
		#after 3 seconds
		else:
			silent = is_silent(data)
			#if it is noisy
			if not silent:
				frames.extend(data)
				silent_counter = 0;
			#if it is silent, wait a second more
			elif silent and silent_counter < 5: #1 second (approximate)
				frames.extend(data)
				silent_counter = silent_counter + 1
			#after a second, finish the recording
			else:
				break

	print "* done\n" 

	stream.stop_stream()
	stream.close()
	p.terminate()

	file = open("sound.raw", "w")
	frames.tofile(file)	
	file.close()

if __name__ == "__main__":
	record_audio()
