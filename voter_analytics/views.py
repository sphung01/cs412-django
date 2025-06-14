from django.shortcuts import render
from django.views.generic import ListView, DetailView ## NEW
from .models import Voter
import plotly
import plotly.graph_objs as go

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
        context['calender_year'] = range(1913, 2026)
        return context

class VoterDetailView(DetailView):
    template_name = 'voter_analytics/voter_detail.html'
    model = Voter
    context_object_name = 'voter'

class VotersGraphListView(ListView):
    template_name = 'voter_analytics/graphs.html'
    model = Voter
    context_object_name = 'voters'

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
        context = super().get_context_data(**kwargs)

        # Count voters by year of birth
        birth_year_counts = {}
        for voter in self.get_queryset():
            year = voter.date_of_birth.year
            if year in birth_year_counts:
                birth_year_counts[year] += 1
            else:
                birth_year_counts[year] = 1

        # Sort by year
        sorted_items = sorted(birth_year_counts.items())
        x = [year for year, count in sorted_items]
        y = [count for year, count in sorted_items]

        # Create Plotly Histogram (Bar Chart)
        fig = go.Bar(x=x, y=y)
        title=f'Voter Distribution by Year of Birth (n={self.get_queryset().count()})'
        graph_div_histogram = plotly.offline.plot({"data": [fig], 
                                         "layout_title_text": title,
                                         }, auto_open=False, output_type="div",
                                         
                                         )

        # We will create a Pie Chart based on whichever Party Affiliation
        # each Voter is in.

        # First, we need to find the labels for X.
        x = ['U', 'D', 'R', 'CC', 'L', 'T', 'O', 'G', 'J', 'Q', 'FF']

        # Y will have the values of each party affiliation based on the filtering.
        # We need to call the get_queryset method to get the voters from the search filter.
        # Using .count() method will return the number of voters
        unenrolled = self.get_queryset().filter(party_affiliation='U ').count()
        democrat = self.get_queryset().filter(party_affiliation='D ').count()
        republican = self.get_queryset().filter(party_affiliation='R ').count()
        city_committee = self.get_queryset().filter(party_affiliation='CC').count()
        libertarian = self.get_queryset().filter(party_affiliation='L ').count()
        tea_party = self.get_queryset().filter(party_affiliation='T ').count()
        other = self.get_queryset().filter(party_affiliation='O ').count()
        green = self.get_queryset().filter(party_affiliation='G ').count()
        justice = self.get_queryset().filter(party_affiliation='J ').count()
        constitutional = self.get_queryset().filter(party_affiliation='Q ').count()
        freedom_front = self.get_queryset().filter(party_affiliation='FF').count()
        y = [
            unenrolled,
            democrat,
            republican,
            city_committee,
            libertarian,
            tea_party,
            other,
            green,
            justice,
            constitutional,
            freedom_front,
        ]

        # Finally, we can start creating a Pie Chart.
        fig = go.Pie(labels=x, values=y)
        title = f"Voter Distribution by Party Affiliation (n={self.get_queryset().count()})"
        graph_div_pie = plotly.offline.plot({"data": [fig], 
                                         "layout_title_text": title,
                                         }, 
                                         auto_open=False, 
                                         output_type="div")
        
        # We will create a Histogram that based on the participations
        # of all 5 elections.

        # First, we need to find a label for X.
        x = ['v20state', 'v21town', 'v21primary', 'v22general', 'v23town']

        # Find the values and store to Y
        v20state_voters = self.get_queryset().filter(v20state=True).count()
        v21town_voters = self.get_queryset().filter(v21town=True).count()
        v21primary_voters = self.get_queryset().filter(v21primary=True).count()
        v22general_voters = self.get_queryset().filter(v22general=True).count()
        v23town_voters = self.get_queryset().filter(v23town=True).count()
        y = [v20state_voters, v21town_voters, v21primary_voters, v22general_voters, v23town_voters]

        # Finally, we can create the Histogram (Bar Chart)
        fig = go.Bar(x=x, y=y)
        title = f"Voter Distribution by Party Affiliation (n={self.get_queryset().count()})"
        graph_div_bar = plotly.offline.plot({"data": [fig], 
                                         "layout_title_text": title,
                                         }, auto_open=False, output_type="div",) 
        context['graph_div_passed'] = graph_div_bar

        # All of the contexts that will be passed to HTML
        context['birth_year_histogram'] = graph_div_histogram
        context['party_affiliation_pie_chart'] = graph_div_pie
        context['election_bar_chart'] = graph_div_bar
        context['voter_scores'] = range(6)  # 0 to 5 inclusive
        context['calender_year'] = range(1913, 2026)
        return context