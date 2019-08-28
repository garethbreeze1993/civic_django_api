from django.test import TestCase
from django.utils import timezone

from votes.models import Vote
from votes.serializers import VoteSerializer

class VoteSerializerTests(TestCase):
    def test_serialization(self):
        '''
        Test to make sure that the serialized data that is created is the same as the model data that is passed in to it
        '''
        time = timezone.now()
        # creating a new vote object
        vote = Vote.objects.create(
            subject='testing the seraializer',
            ayes=54,
            nays=1,
            vote_date=time,
            )
        serialized_data = VoteSerializer(vote).data # passing the vote model object in to my seraializer
        # 
        assert vote.id == serialized_data['id']
        assert vote.subject == serialized_data['subject']
        assert vote.ayes == serialized_data['ayes']
        assert vote.nays == serialized_data['nays']


        

        

