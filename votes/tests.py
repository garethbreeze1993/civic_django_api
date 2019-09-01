from django.test import TestCase
from django.utils import timezone

from rest_framework.test import APITestCase # similar to django test case use when testing REST API
from rest_framework.test import APIRequestFactory 
# APIRequestFactory: This is similar to Django’s RequestFactory. It allows you to create requests with any http method, 
#which you can then pass on to any view method and compare responses.

from votes.models import Vote
from votes.serializers import VoteSerializer
from votes.views import VoteList, VoteDetail


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
		
class VoteViewTests(APITestCase):
	
	def setUp(self):
		self.factory = APIRequestFactory()
		self.view = VoteList.as_view() # getting n instance of view
		self.uri = '/votes/' # path to API endpoint

	def test_vote_list_get_request_assert_200_response_code(self):
		'''
		This test makes a get request to the /votes/ api endpoint we then write this test to ensure we get a http status code back of
		200 in the response object
		'''
		request = self.factory.get(self.uri) # call a get request on api endpoint /votes/
		response = self.view(request) # pass this request object in to our viewList CBV  to get a response object
		self.assertEqual(response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)) 
# assert we get a response code of 200 i.e. a successful http response
        

        

