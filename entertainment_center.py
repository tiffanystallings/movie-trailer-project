import media
import fresh_tomatoes

# The idea to split long strings into individual concatenated lines came from StackOverflow
# when I was researching a project months ago. This is meant to avoid any whitespace errors
# while keeping the code neat and easy to read.

little_shop = media.Movie("Little Shop of Horrors",
                          # This is IMDBs description. The rest are my own
                          "A nerdy florist finds his chance " +
                          "for success and romance with the " +
                          "help of a giant man-eating plant " +
                          "who demands to be fed.",
                          "https://upload.wikimedia.org/wikipedia" +
                          "/en/5/5b/Little_shop_of_horrors.jpg",
                          "https://www.youtube.com/watch?v=jFENSU8CmZk")

phantom_opera = media.Movie("Phantom of the Opera",
                            "A mysterious 'Angel of Music " +
                            "controls the goings-on of an " +
                            "1870's opera house.",
                            "https://upload.wikimedia.org/wikipedia" +
                            "/en/d/d6/Poto2.jpg",
                            "https://www.youtube.com/watch?v=N91AL8sAh9o")

moulin_rouge = media.Movie("Moulin Rouge",
                           "A story of love in Bohemian " +
                           "Revolution era France.",
                           "https://upload.wikimedia.org/wikipedia" +
                           "/en/9/9f/Moulin_rouge_poster.jpg",
                           "https://www.youtube.com/watch?v=2PpgPxjzbkA")

sweeney_todd = media.Movie("Sweeney Todd",
                           "A transported barber returns " +
                           "to London to avenge his broken " +
                           "family.",
                           "https://upload.wikimedia.org/wikipedia" +
                           "/en/4/4b/Sweeneylarge.jpg",
                           "https://www.youtube.com/watch?v=iGm8s3XKWcI")

repo = media.Movie("Repo! The Genetic Opera",
                   "In a world of commercialized organ transplants, " +
                   "failure to make on-time payments could mean a " +
                   "grim visit from GeneCo's Repo Man.",
                   "https://upload.wikimedia.org/wikipedia" +
                   "/en/7/7a/RepoGeneticOperaOfficialPoster.jpg",
                   "https://www.youtube.com/watch?v=MzgpU25C6fg")

les_miserables = media.Movie("Les Miserables",
                             "A prisoner on parole finds himself caught " +
                             "in the midst of a violent revolution as he " +
                             "flees the police.",
                             "https://upload.wikimedia.org/wikipedia" +
                             "/en/b/b0/Les-miserables-movie-poster1.jpg",
                             "https://www.youtube.com/watch?v=YmvHzCLP6ug")
    
movies = [little_shop,
          phantom_opera,
          moulin_rouge,
          sweeney_todd,
          repo,
          les_miserables]

fresh_tomatoes.open_movies_page(movies)
