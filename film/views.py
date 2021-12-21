from django.http import HttpResponseRedirect
from django.views.generic import ListView, FormView
from . import models, forms


# Create your views here.
# class AnimeView(ListView):
#     model = models.Anime
#     template_name = 'anime/anime_list.html'
#
#     def get_queryset(self):
#         return models.Anime.objects.all()

class MovieView(ListView):
    model = models.Movie
    template_name = 'movie/movie_list.html'

    def get_queryset(self):
        return models.Movie.objects.all()

# class ParserAnimeView(FormView):
#     template_name = 'anime/anime_parser.html'
#     form_class = forms.ParserForm
#     success_url = '/anime/'
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.parser_data()
#             return HttpResponseRedirect(self.success_url)
#         else:
#             return super(ParserAnimeView, self).post(request, *args, **kwargs)

class ParserMovieView(FormView):
    template_name = 'movie/movie_parser.html'
    form_class = forms.ParserForm
    success_url = '/movie/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserCartoonView, self).post(requests, *args, **kwargs)