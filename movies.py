import fresh_tomatoes
import media

#List of movies with titles, box art imagery links and trailer links.

interstellar = media.Movie("Interstellar",
	"https://goo.gl/4LsHWP", 
	"https://www.youtube.com/watch?v=zSWdZVtXT7E")

star_wars = media.Movie("Star Wars", 
	"https://goo.gl/we3qkg" , 
	"https://www.youtube.com/watch?v=sGbxmsDFVnE")

enders_game = media.Movie("Ender's Game",
	"https://goo.gl/eXdsKr", 
	"https://www.youtube.com/watch?v=2UNWLgY-wuo")

iron_man = media.Movie("Iron Man",
	"https://goo.gl/UnkQts", 
	"https://www.youtube.com/watch?v=8hYlB38asDY")

hunger_games = media.Movie("The Hunger Games",
	"https://goo.gl/K5euzV", 
	"https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [interstellar, star_wars, enders_game, iron_man, hunger_games]
fresh_tomatoes.open_movies_page(movies)