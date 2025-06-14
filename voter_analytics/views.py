from django.shortcuts import render
from django.views.generic import ListView, DetailView ## NEW
from .models import Voter

# Create your views here.
class VotersListView(ListView):
    """
        A view that will display all of the 
        Voters existing in the database.
    """

    template_name = 'voter_analytics/voters.html'
    model = Voter
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        
        # Start with entire queryset
        voters = super().get_queryset().order_by('date_of_birth')

        # Filter results by these field(s):
        if 'party' in self.request.GET:
            party = self.request.GET['party']
            if party:
                voters = voters.filter(party_affiliation=party)

        if 'year_start' in self.request.GET and 'year_end' in self.request.GET:
            year_start = self.request.GET['year_start']
            year_end = self.request.GET['year_end']
            if year_start:
                voters = voters.filter(date_of_birth__year__gte=year_start)
            elif year_end:
                voters = voters.filter(date_of_birth__year__lte=year_end)
            elif year_start and year_end:
                voters = voters.filter(date_of_birth__year__gte=year_start)
                voters = voters.filter(date_of_birth__year__lte=year_end)

        if 'voter_score' in self.request.GET:
            voter_score = self.request.GET['voter_score']
            if voter_score:
                voters = voters.filter(voter_score=voter_score)

        election_fields = ['v20state', 'v21town', 'v21primary', 'v22general', 'v23town']
        for voted_field in election_fields:
            if voted_field in self.request.GET:
                voters = voters.filter(**{voted_field: True})

                
        return voters

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['voter_scores'] = range(6)  # 0 to 5 inclusive
        context['calender_year'] = range(1900, 2026)
        return context

class VoterDetailView(DetailView):
    template_name = 'voter_analytics/voter_detail.html'
    model = Voter
    context_object_name = 'voter'