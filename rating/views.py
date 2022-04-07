from django.views import generic

from .models import Rating
from .forms import RatingForm


class RatingList(generic.ListView):
    queryset = Rating.objects.order_by('-date')
    template_name = 'rating/rating_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(RatingList, self).get_context_data(**kwargs)
        context['range'] = range(1, 6)
        return context


class RatingAdd(generic.FormView):
    form_class = RatingForm
    template_name = 'rating/rating_add.html'
    success_url = '/rating/'

    def form_valid(self, form):
        rating = Rating(username=form.cleaned_data['username'], rating=form.cleaned_data['rating'],
                        body=form.cleaned_data['body'])
        rating.save()
        return super().form_valid(form)
