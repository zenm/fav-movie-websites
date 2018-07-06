import webbrowser


class Video():
    '''Used to create instance of videos with a title'''
    def __init__(self, media_title):
        self.title = media_title


class Movie(Video):
    '''Used to create instances of Movies, shows trailers and stores info on storyline, poster and a youtube url'''
    def __init__(self, title, storyline, poster_image, youtube_trailer):
        Video.__init__(self, title)
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
