from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status


from .serializers import (
	UserSerializer, PostSerializer, 
	NewPostSerializer, PhotoSerializer
)

from .models import User, Post, Photo
from .permissions import PostAuthorCanEditPermission


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    lookup_field = 'username'


class PostMixin(object):
    model = Post
    #serializer_class = PostSerializer
    permission_classes = [
        PostAuthorCanEditPermission
    ]	
    def post(self, request, *args, **kwargs):
        """Force author to the current user on save"""
        request.data['author'] = self.request.user.pk
	serializer = self.get_serializer(data=request.data)	
	if serializer.is_valid():
           serializer.save()
        return Response(
        	serializer.data,
                status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostList(PostMixin, generics.ListCreateAPIView):
    def get_serializer_class(self):
	if self.request.method == 'POST':
	    return NewPostSerializer
	return PostSerializer

    queryset = Post.objects.all()


class PostDetail(PostMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class UserPostList(generics.ListAPIView):
    model = Post
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super(UserPostList, self).get_queryset()
        return queryset.filter(author__username=self.kwargs.get('username'))


class PhotoList(generics.ListCreateAPIView):
    model = Photo
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Photo
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PostPhotoList(generics.ListAPIView):
    model = Photo
    serializer_class = PhotoSerializer

    def get_queryset(self):
	post = Post.objects.get(pk=self.kwargs.get('pk'))	
	return post.photos.all()

