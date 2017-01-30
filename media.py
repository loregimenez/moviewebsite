import webbrowser

class Movie(): #The class Movie is created
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		#Variables for Movie
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer) #Opens the movie trailer for the movie selected