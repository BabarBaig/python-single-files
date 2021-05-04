import aah_media
import fresh_tomatoes

''' In this sample file:
~ Read some data from a text file
~ Pass it to a website to check for profanities
~ Print website response (true/false) for any profanities
'''

toy_story = aah_media.Movie('Toy Story', 'A story of a buy and his toys that come to life',
                        'http://upload.wikiaah_media.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=vwyZH85NQC4')
print(toy_story.title)
print(toy_story.storyline)
print(toy_story.poster_image_url)
print(toy_story.trailer_youtube_url)

avatar = aah_media.Movie('Avatar', 'A marine on an alien planet',
                     'http://upload.wikiaah_media.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
                     'http://www.youtube.com/watch?v=a0CDJZu4M5I')
print(avatar.title)
print(avatar.storyline)
print(avatar.poster_image_url)
print(avatar.trailer_youtube_url)
# avatar.show_trailer()

school_of_rock = aah_media.Movie('School or Rock', 'Using rock music to learn',
                             'http://upload.wikiaah_media.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                             'https://www.youtube.com/watch?v=3PsUJFEBC74')

movies = [toy_story, avatar, school_of_rock]
# fresh_tomatoes.open_movies_page( movies)
print(aah_media.Movie.__doc__)
