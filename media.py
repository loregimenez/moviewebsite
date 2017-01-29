import webbrowser

class Movie(): #The class Movie is created
	def __init__(self, title, image, trailer_youtub):
		#Variables for Movie
		self.title = title
		self.image = image
		self.trailer = trailer

	def show_trailer(self):
		webbrowser.open(self.trailer) #Opens the movie trailer for the movie selected