wav_filepath = 'audio-file.wav'
# open newly created temp file in binary mode to write audio file to it
r = binary_data
with open(wav_filepath, 'wb+') as f:
	f.write(r)


