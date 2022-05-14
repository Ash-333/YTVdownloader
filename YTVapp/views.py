
from django.shortcuts import render
from pytube import YouTube

def index(request):

	try:
		
		# check request.method is post or not
		if request.method == 'POST':
			try:
				# get link from the html form
				link = request.POST['link']
				video = YouTube(link)

				# set video resolution
				stream = video.streams.get_highest_resolution()
				
				# download the video 
				stream.download()

				# render HTML page
				return render(request, 'index.html', {'msg':'Video downloaded'})
			except Exception as e:
				return render(request, 'index.html', {'msg':'Video not downloaded'+str(e)})
		return render(request, 'index.html', {'msg':''})
	except:
		return render(request, "index.html", {"msg":"Sorry something went wrong!"})