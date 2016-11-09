import media
import fresh_tomatoes
toy_story = media.Movie("Finding Dory",
                        "Dory (Ellen DeGeneres) is a wide-eyed, blue tang fish who suffers from memory loss every 10 seconds or so. The one thing she can remember is that she somehow became separated from her parents as a child. With help from her friends Nemo and Marlin, Dory embarks on an epic adventure to find them. Her journey brings her to the Marine Life Institute, a conservatory that houses diverse ocean species. Dory now knows that her family reunion will only happen if she can save mom and dad from captivity.",

                        "http://img.lum.dolimg.com/v1/images/uk_dory_flexherobg_n_6032b443.jpeg?region=0,0,1500,844&width=1200",
                        "https://www.youtube.com/watch?v=cxskm6dDfIY")
# print(toy_story.storyline)
avatar = media.Movie("Aftershock",
                     "An earthquake in China Tangshan",
                     "http://t3.gstatic.com/images?q=tbn:ANd9GcSpaXryAPruhEjYOQ7FmEA_vqlLY8apJ5Z2zetYgNF9-vmbVhoq",
                     "https://www.youtube.com/watch?v=pJMlKjYlTXg")
# avatar.storyline
# avatar.show_trailer()
m2012 = media.Movie("2012",
                    "A disaster for earth",
                    "http://www.gstatic.com/tv/thumb/movieposters/193479/p193479_p_v8_an.jpg",
                    "https://www.youtube.com/watch?v=rvI66Xaj9-o")
# m2012.show_trailer()
school_of_rock = media.Movie("Train To Busan",
                             "A man (Gong Yoo), his estranged daughter and other passengers become trapped on a speeding train during a zombie outbreak in South Korea.",
                             "http://t1.gstatic.com/images?q=tbn:ANd9GcSL7v79L_4drBAwzvXKCaTms0G9gx86N-pbxTCduLStbkr_vZ6M",
                             "https://www.youtube.com/watch?v=RuxONKl0z3k")

movies = [toy_story, avatar, m2012, school_of_rock]
# fresh_tomatoes.open_movies_page(movies)
# print media.Movie.VALID_RATINGS
print media.Movie.__doc__, media.Movie.__name__, media.Movie.__module__
