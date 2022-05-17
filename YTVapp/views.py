
from django.shortcuts import render
from pytube import YouTube
from threading import Thread
from pytube import Playlist
from django.contrib import messages
def download_videos(link):
	playlist=Playlist(link)
	for video in playlist.videos:
		stream = video.streams.get_highest_resolution()
		stream.download()

def index(request):

	try:
		
		# check request.method is post or not
		if request.method == 'POST':
			try:
				# get link from the html form
				link = request.POST['link']
				#check weather link is of video or playlist

				if "playlist" in link:
					#download video using different thread
					t1 = Thread(target=download_videos(link))
					t1.start()

				else:
					video = YouTube(link)

				# set video resolution
					stream = video.streams.get_highest_resolution()
				
				# download the video 
					stream.download()

				# render HTML page
				messages.success(request, 'Video downloaded successfully!')
				return render(request, 'index.html', {'msg':'Video downloaded'})
				
			except Exception as e:
				messages.error(request, 'Video not downloaded!')
				return render(request, 'index.html', {'msg':'Video not downloaded'})
				#+str(e)
		return render(request, 'index.html', {'msg':''})
	except Exception as e:
		messages.error(request, 'Video downloaded successfully!')
		return render(request, "index.html", {"msg":"Sorry something went wrong!"+str(e)})
		