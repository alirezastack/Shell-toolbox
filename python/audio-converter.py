# sox should have been compiled with mp3 encoding support
# sudo apt-get install sox libsox-fmt-mp3
p = Popen(['sox', '-t', 'wav', wav_filepath, '-t', 'mp3', mp3_filepath])

# wait command cause script to wait until conversion is done
# timeout is set 30 sec
p.wait(30)
