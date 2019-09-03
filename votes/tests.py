from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from rest_framework.test import APIClient # similar to DjangoTest Client but used for REST API
from rest_framework.test import APITestCase # similar to django test case use when testing REST API
from rest_framework.test import APIRequestFactory 
# APIRequestFactory: This is similar to Django’s RequestFactory. It allows you to create requests with any http method, 
#which you can then pass on to any view method and compare responses.

from votes.models import Vote
from votes.serializers import VoteSerializer
from votes.views import VoteList, VoteDetail

time = timezone.now()


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
        self.view_detail = VoteDetail.as_view()
        self.uri = '/votes/' # path to API endpoint
        self.uri_detail = '/votes/1'
        self.user = self.setup_user() # create a user at the start of every test so can call if needed
        self.client = APIClient()
        self.params = {
            'subject':'testing the creation',
            'ayes':54,
            'nays':1,
            'vote_date':time,
            }
        
    def create_vote(self):
        self.client.login(username='test', password='test_pass') # login to app via my user I created in setup method
        time = timezone.now()
        # creating a new vote object
        response = self.client.post(self.uri, self.params)
	
    @staticmethod	
    def setup_user():
        User = get_user_model() # call the django user model via the get_user_model method
        return User.objects.create_user('test', email='test_user@gmail.com', password='test_pass') # create a user so I can login so I can get around permissions

    def test_vote_list_get_request_assert_200_response_code(self):
        '''
        This test makes a get request to the /votes/ api endpoint we then write this test to ensure we get a http status code back of
        200 in the response object
        '''
        request = self.factory.get(self.uri) # call a get request on api endpoint /votes/
        response = self.view(request) # pass this request object in to our viewList CBV  to get a response object
        self.assertEqual(response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)) 
# assert we get a response code of 200 i.e. a successful http response

    def test_vote_detail_get_request_assert_200_response_code(self):
        '''
        This test makes a get request to the /votes/1 api endpoint we then write this test to ensure we get a http status code back of
        200 in the response object
        '''
        self.create_vote()
        request = self.factory.get(self.uri_detail) # call a get request on api endpoint /votes/
        response = self.view_detail(request, pk=1) # pass this request object in to our viewList CBV  to get a response object
        self.assertEqual(response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)) 
        # assert we get a response code of 200 i.e. a successful http response
        
    def test_vote_detail_test_correct_data_received(self):
        '''
        This test makes a get request to the /votes/1 api endpoint we then write this test to ensure we get a http status code back of
        200 in the response object
        '''
        self.create_vote()
        request = self.factory.get(self.uri_detail) # call a get request on api endpoint /votes/
        response = self.view_detail(request, pk=1) # pass this request object in to our viewList CBV  to get a response object
        self.assertEqual(response.data['ayes'], self.params['ayes'])
        self.assertEqual(response.data['nays'], self.params['nays'])
        self.assertEqual(response.data['subject'], self.params['subject'])
                                                       

        # assert we get a response code of 200 i.e. a successful http response    

    def test_vote_list_create_new_vote(self):
        self.client.login(username='test', password='test_pass') # login to app via my user I created in setup method
        time = timezone.now()
        # creating a new vote object
        params = {
            'subject':'testing the creation',
            'ayes':54,
            'nays':1,
            'vote_date':time,
            }
        response = self.client.post(self.uri, params) # do a post request via APIClient using the endpoint /votes/ and using the data specified in the params dictionary
        self.assertEqual(response.status_code, 201, 'Expected Response Code 201, received {0} instead.'.format(response.status_code)) 
        # assert that the vote was created via a 201 http status code
        

        

