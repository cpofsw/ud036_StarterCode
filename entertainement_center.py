#Chama o arquivo que transforma a lista de filmes em um website.
import fresh_tomatoes

#Chama o arquivo que contem a class Movie e seus metodos.
import media

#Lista dos objetos Movie:
arrival = media.Movie ("Arrival",
                       "Aliens come to earth. Why they are here?",
                       "https://m.media-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=tFMo3UJ4B4g")


lucky_number_slevin = media.Movie ("Lucky Number Slevin",
                         "A case of mistaken identity lands Slevin into the middle of a war",
                         "https://m.media-amazon.com/images/M/MV5BMTk0OTAzMDM1N15BMl5BanBnXkFtZTcwNjczMTkwOA@@._V1_.jpg",
                         "https://www.youtube.com/watch?v=fVIUEcizkPc")

the_jacket = media.Movie ("The Jacket",
                          "A Gulf war veteran is wrongly sent to a mental institution for insane criminals",
                          "https://m.media-amazon.com/images/M/MV5BZjNjNDcxOTYtYTYxYS00ZWU3LTlhYzQtNGY5ZjJmYzE0OTFmXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX700_CR0,0,700,999_AL_.jpg",
                          "https://www.youtube.com/watch?v=eAbvFMRTBe0")

eternal_sunshine_of_the_spotless_mind = media.Movie ("Eternal Sunshine of the Spotless Mind",
                                                     "When their relationship turns sour, a couple undergoes a medical procedure to have each other erased from their memories.",
                                                     "https://m.media-amazon.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                                                     "https://www.youtube.com/watch?v=07-QBnEkgXU")


crossroads = media.Movie ("Crossroads",
                          "A kid who can make a slide guitar sing. An old pro who knows it. Together, they're headed to a place where deals are made.",
                          "https://m.media-amazon.com/images/M/MV5BMDg3MmVmNmUtMzI4NC00NDY1LTg5YTAtMDJiODJlNmM0MTAwXkEyXkFqcGdeQXVyNjc3MjQzNTI@._V1_SY1000_CR0,0,667,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=OJNl7If64Xg")


fear_and_loathing_in_las_vegas = media.Movie ("Fear and Loathing in Las Vegas",
                                              "An oddball journalist and his psychopathic lawyer travel to Las Vegas for a series of psychedelic escapades.",
                                              "https://m.media-amazon.com/images/M/MV5BNjA2ZDY3ZjYtZmNiMC00MDU5LTgxMWEtNzk1YmI3NzdkMTU0XkEyXkFqcGdeQXVyNjQyMjcwNDM@._V1_.jpg",
                                              "https://www.youtube.com/watch?v=8m662obIvhY")


#Chama o metodo fresh_tomatoes.open_movies_page que usa a lista de filmes para
#gerar o website de trailers.
movies = [arrival, lucky_number_slevin, the_jacket, eternal_sunshine_of_the_spotless_mind, crossroads, fear_and_loathing_in_las_vegas]
fresh_tomatoes.open_movies_page(movies)
                        
