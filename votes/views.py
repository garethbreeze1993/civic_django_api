from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from votes.models import Vote
from votes.serializers import VoteSerializer

class VoteList(generics.ListCreateAPIView):
    '''
    Used for read-write endpoints to represent a collection of model instances.
    Provides get and post method handlers.
    '''
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'votes/vote_list.html'
    context_object_name = 'votes_list'
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # django rest framework built in permissiomn class if user is logged in they can do post request anyone can do get request
    
    def get_renderers(self):
        '''
        Overwrite the method so only staff members can only view the browsable API.
        '''
        renderer_classes = self.renderer_classes
        if self.request.user.is_staff:
            renderer_classes += [BrowsableAPIRenderer]
        return [renderer() for renderer in renderer_classes]    
    
    def create(self, request, *args, **kwargs):
        '''
        Overwrite the create method for this CBV  to allow me to add a form to the template to create a new vote
        '''
        response = super(VoteList, self).create(request, *args, **kwargs) # overwrite the create method for this CBV
        # below condition checks that the browser has rendered out html template and we have created a vote using that form
        # 201 status code is a create request
        if request.accepted_renderer.format == 'html' and response.status_code == 201:
            return redirect('/votes/') # redirects to basename/votes which is our list of votes with information
        return response        
                
class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Used for read-write-delete endpoints to represent a single model instance. Provides get, put, patch and delete method handlers.
    '''
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'votes/vote.html'
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_renderers(self):
        '''
        Overwrite the method so only staff members can only view the browsable API.
        '''
        renderer_classes = self.renderer_classes
        if self.request.user.is_staff:
            renderer_classes += [BrowsableAPIRenderer]
        return [renderer() for renderer in renderer_classes] 
