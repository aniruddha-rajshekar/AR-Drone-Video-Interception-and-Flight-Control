all: attack

attack: video_capture.pcap
	tcptrace -e video_capture.pcap
	ffmpeg -f h264 -i am2an_contents.dat video_capture.avi
	ffplay video_capture.avi

clean:
	rm *.dat
	rm video_capture.avi
