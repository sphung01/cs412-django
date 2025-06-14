# File: voter_analytics/models.py
# Author: Steven Phung (sphung01@bu.edu), 6/12/2025
# Description: This is where we define a structured
# stored data of the model. Then we will migrate once
# a model has been created or edited.

from django.db import models

# Create your models here.
class Voter(models.Model):
    """
        A data that represents a Voter from Newton. The data includes:
        Last Name, First Name, Street Number, Street Name, Apartment Number,
        Zip Code, DoB, DoR, Party Affiliation, Precinct Number, v20state, 
        v21town, v21primary, v22general, v23town, and voter score.
    """

    # Here are the attributes for the voter

    # Name of the Voter
    last_name = models.TextField()
    first_name = models.TextField()

    # Where the Voter lives
    street_number = models.TextField()
    street_name = models.TextField()
    apartment_number = models.TextField()
    zip_code = models.CharField(max_length=5)

    # Date of birth and registration from Voter
    date_of_birth = models.DateField()
    date_of_registration = models.DateField()

    # Affiliation and precinct number
    party_affiliation = models.CharField(max_length=2)
    precinct_number = models.CharField(max_length=3)

    # True or False on voting
    v20state = models.BooleanField()
    v21town = models.BooleanField()
    v21primary = models.BooleanField()
    v22general = models.BooleanField()
    v23town = models.BooleanField()


    # How many times the Voter registered
    voter_score = models.IntegerField()

    def __str__(self):
        """
            Returns a string representation of the object
        """
        return f'{self.last_name}, {self.first_name}'
    
def load_data():
    """
        A function that loads a data from a CSV file into model instances.
    """

    # This will help delete all the existing records
    # from the database to prevent duplications
    Voter.objects.all().delete()

    # Find the path to the CSV file
    filepath = '/Users/itzsinnoh/Desktop/django/newton_voters.csv'

    # We will then open that file
    file = open(filepath)

    # Then use readline() to get rid of headers
    file.readline()

    # Now we loop through each row and create the Voter instances
    for row in file:
        fields = row.strip().split(',')

        try:
            # We will try to make an instance of the Voter object
            voter = Voter(
                last_name = fields[1],
                first_name = fields[2],
                street_number = fields[3],
                street_name = fields[4],
                apartment_number = fields[5],
                zip_code = fields[6],
                date_of_birth = fields[7],
                date_of_registration = fields[8],
                party_affiliation = fields[9],
                precinct_number = fields[10],
                v20state = fields[11].strip().upper() == 'TRUE',
                v21town = fields[12].strip().upper() == 'TRUE',
                v21primary = fields[13].strip().upper() == 'TRUE',
                v22general = fields[14].strip().upper() == 'TRUE',
                v23town = fields[15].strip().upper() == 'TRUE',
                voter_score =fields[16],
            )

            voter.save() # Save to the database
            print(f'Created Voter: {voter}')

        except Exception as e:
            print(f"Skipped: {fields} due to error: {e}")
    
    print(f'Done. Created {Voter.objects.count()} Results.')
