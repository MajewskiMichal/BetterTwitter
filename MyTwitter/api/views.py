from rest_framework import generics, mixins
from MyTwitter.models import Tweet
from .serializers import TweetSerializer


class TweetCreateView(mixins.CreateModelMixin, generics.ListAPIView): #CreatelView
    lookup_field = 'pk'
    serializer_class = TweetSerializer
    # queryset = Tweet.objects.all()

    def get_queryset(self):
        qs = Tweet.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class TweetRudView(generics.RetrieveUpdateDestroyAPIView): #DetailView
    lookup_field = 'pk'
    serializer_class = TweetSerializer
    # queryset = Tweet.objects.all()

    def get_queryset(self):
        return Tweet.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return Tweet.objects.get(pk=pk)
