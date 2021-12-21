from django import forms
from film import parser, models



class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('Anime', 'Anime'),
        ('Movie', 'Movie')
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        # if self.data['media_type'] == 'Anime':
        #     anime_data = parser.anime_parser()
        #     for i in anime_data:
        #         models.Anime.objects.create(**i)
        if self.data['media_type'] == 'Movie':
            movie_data = parser.movie_parser()
            for i in movie_data:
                models.Movie.objects.create(**i)