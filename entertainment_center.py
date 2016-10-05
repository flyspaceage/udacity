# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

city_of_god = media.Movie("City of God",
                          "In the poverty-stricken favelas of Rio de Janeiro in the 1970s, two young men choose different paths.",
                          "http://www.gstatic.com/tv/thumb/movieposters/30586/p30586_p_v8_aa.jpg",
                          "https://www.youtube.com/watch?v=ioUE_5wpg_E")

training_day = media.Movie("Training Day",
                                        "An LAPD detective's first day on the job",
                                        "https://upload.wikimedia.org/wikipedia/en/b/b3/Training_Day_Poster.jpg",
                                        "https://www.youtube.com/watch?v=gKTVQPOH8ZA")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

hackers = media.Movie("Hackers",
                      "A cult classic about the exploits of a group of young hackers",
                      "https://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg",
                      "https://www.youtube.com/watch?v=Ql1uLyuWra8")

gladiator = media.Movie("Gladiator",
                        "Maximus rises through the ranks of the gladiatorial arena to avenge the murders of his family and his emperor",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=AxQajgTyLcM")

boyz_n_the_hood = media.Movie("Boyz n' the Hood",
                          "Tre is sent to live with his father in South Central LA",
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcQ1FrEli1XqqkLkuNfXB7Ziwend4Ylcy80hUi7hLUEIwFtu9XUO",
                          "https://www.youtube.com/watch?v=AE4BdijGtu4")

hustle_and_flow = media.Movie("Hustle and Flow",
                              "DJay is a pimp living day to day on the tough streets of Memphis, Tennessee",
                              "https://upload.wikimedia.org/wikipedia/en/e/e9/Hustle_and_flow.jpg",
                              "https://www.youtube.com/watch?v=otn1YORTxDo")

crouching_tiger_hidden_dragon = media.Movie("Crouching Tiger, Hidden Dragon",
                                            "The disappearance of a magical jade sword spurs a breathtaking quest for the missing treasure.",
                                            "http://www.gstatic.com/tv/thumb/movieposters/25570/p25570_p_v8_aa.jpg",
                                            "https://www.youtube.com/watch?v=oEaGsdiA0y0")

road_trip = media.Movie("Road Trip",
                        "When you're in a committed relationship and have sex with another person it's not cheating if.... You're in different area codes",
                        "http://www.gstatic.com/tv/thumb/dvdboxart/24671/p24671_d_v8_aa.jpg",
                        "https://www.youtube.com/watch?v=RXmANh0-2Bg")

movies = [city_of_god, training_day, avatar, hackers, gladiator, boyz_n_the_hood, hustle_and_flow, crouching_tiger_hidden_dragon, road_trip]
fresh_tomatoes.open_movies_page(movies)
