from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from finca.serializers import PropertyTypeSerializer, UserSerializer, GroupSerializer, PropertySerializer, StateSerializer, CitySerializer, TransationSerializer, CategorySerializer, ReviewSerializer
from .models import PropertyType, State, City, Category, Transation, Property, Review


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PropertyTypeSerializerViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, pk=None):
        try:
            PropertyType.objects.filter(id=pk).delete()
            return Response({'status': 'success', 'message': 'property type removed'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            propertyType = PropertyType.objects.filter(id=pk)

            content = self.inputValidator(request)
            if content['status'] == 'error':
                return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            propertyType.update(slug=request.POST['slug'].lower())

            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def inputValidator(self, request):
        if 'slug' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: slug'}

        return {'status': 'success', 'message': 'property type updated'}


class StateSerializerViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Method DELETE
    def destroy(self, request, pk=None):
        try:
            State.objects.filter(id=pk).delete()
            return Response({'status': 'success', 'message': 'state removed'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def inputValidator(self, request):
        if 'slug' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: slug'}

        return {'status': 'success', 'message': 'state updated'}

    # Method PUT
    def update(self, request, pk=None):
        try:
            state = State.objects.filter(id=pk)

            content = self.inputValidator(request)
            if content['status'] == 'error':
                return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            state.update(slug=request.POST['slug'].lower())

            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CitySerializerViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # Method PUT
    def update(self, request, pk=None):
        try:
            city = City.objects.filter(id=pk)

            content = self.inputValidator(request)
            if content['status'] == 'error':
                return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            city.update(slug=request.POST['slug'].lower(),
                        state=request.POST['state'].lower(),
                        zip=request.POST['zip'].lower())

            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Method PATCH
    def partial_update(self, request, pk=None):
        try:
            city = City.objects.filter(id=pk)

            if 'slug' in request.POST:
                city.update(slug=request.POST['slug'].lower())

            if 'state' in request.POST:
                city.update(state=request.POST['state'].lower())

            if 'zip' in request.POST:
                city.update(zip=request.POST['zip'].lower())

            return Response({'status': 'success', 'message': 'city updated'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # Method DELETE
    def destroy(self, request, pk=None):
        try:
            City.objects.filter(id=pk).delete()
            return Response({'status': 'success', 'message': 'city removed'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def inputValidator(self, request):
        if 'slug' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: slug'}

        if 'state' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: state'}

        if 'zip' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: zip'}

        return {'status': 'success', 'message': 'city updated'}


class CategorySerializerViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    # Method DELETE
    def destroy(self, request, pk=None):
        try:
            Category.objects.filter(id=pk).delete()
            return Response({'status': 'success', 'message': 'city removed'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Method PUT
    def update(self, request, pk=None):
        try:
            category = Category.objects.filter(id=pk)

            content = self.inputValidator(request)
            if content['status'] == 'error':
                return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            category.update(slug=request.POST['slug'].lower())

            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Method PATH
    def partial_update(self, request, pk=None):
        try:
            category = Category.objects.filter(id=pk)

            if 'slug' in request.POST:
                category.update(slug=request.POST['slug'].lower())

            return Response({'status': 'success', 'message': 'category updated'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def inputValidator(self, request):
        if 'slug' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: slug'}

        return {'status': 'success', 'message': 'category updated'}


class TransationSerializerViewSet(viewsets.ModelViewSet):
    queryset = Transation.objects.all()
    serializer_class = TransationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, pk=None):
        try:
            Transation.objects.filter(id=pk).delete()
            return Response({'status': 'success', 'message': 'transation removed'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            transation = Transation.objects.filter(id=pk)

            content = self.inputValidator(request)
            if content['status'] == 'error':
                return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            transation.update(slug=request.POST['slug'].lower(
            ), propertyTypes=request.POST['property_types'].lower())

            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Method PATH
    def partial_update(self, request, pk=None):
        try:
            transation = Transation.objects.filter(id=pk)

            if 'slug' in request.POST:
                transation.update(slug=request.POST['slug'].lower())

            return Response({'status': 'success', 'message': 'transation updated'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def inputValidator(self, request):
        if 'slug' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: slug'}

        if 'property_types' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: property_types'}

        return {'status': 'success', 'message': 'transation updated'}


class PropertySerializerViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # Method DELETE
    def destroy(self, request, pk=None):
        try:
            Property.objects.filter(id=pk).delete()
            return Response({'status': 'success', 'message': 'property removed'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Method PUT
    def update(self, request, pk=None):
        try:
            property = Property.objects.filter(id=pk)

            content = self.inputValidator(request)
            if content['status'] == 'error':
                return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            property.update(title=request.POST['title'].lower(),
                            image=request.POST['image'].lower(),
                            city=request.POST['city'].lower(),
                            category=request.POST['category'].lower(),
                            sqft=request.POST['sqft'].lower(),
                            baths=request.POST['baths'].lower(),
                            beds=request.POST['beds'].lower(),
                            price=request.POST['price'].lower())

            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Method PATH
    def partial_update(self, request, pk=None):
        try:
            property = Property.objects.filter(id=pk)

            if 'title' in request.POST:
                property.update(title=request.POST['title'].lower())

            if 'image' in request.POST:
                property.update(image=request.POST['image'].lower())

            if 'category' in request.POST:
                property.update(category=request.POST['category'].lower())

            if 'sqft' in request.POST:
                property.update(sqft=request.POST['sqft'].lower())

            if 'baths' in request.POST:
                property.update(baths=request.POST['baths'].lower())

            if 'beds' in request.POST:
                property.update(beds=request.POST['beds'].lower())

            if 'price' in request.POST:
                property.update(price=request.POST['price'].lower())

            return Response({'status': 'success', 'message': 'property updated'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def inputValidator(self, request):
        if 'title' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: title'}

        if 'image' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: image'}

        if 'city' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: city'}

        if 'category' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: category'}

        if 'sqft' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: sqft'}

        if 'baths' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: baths'}

        if 'beds' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: beds'}

        return {'status': 'success', 'message': 'property updated'}


class ReviewSerializerViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Method DELETE
    def destroy(self, request, pk=None):
        try:
            Review.objects.filter(id=pk).delete()
            return Response({'status': 'success', 'message': 'review removed'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Method PUT
    def update(self, request, pk=None):
        try:
            review = Review.objects.filter(id=pk)

            content = self.inputValidator(request)
            if content['status'] == 'error':
                return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            review.update(feedback=request.POST['feedback'].lower(),
                          avatar=request.POST['avatar'].lower(),
                          rating=request.POST['rating'].lower(),)

            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Method PATH
    def partial_update(self, request, pk=None):
        try:
            review = Review.objects.filter(id=pk)

            if 'feedback' in request.POST:
                review.update(feedback=request.POST['feedback'].lower())

            if 'avatar' in request.POST:
                review.update(avatar=request.POST['avatar'].lower())

            if 'rating' in request.POST:
                review.update(rating=request.POST['rating'].lower())

            return Response({'status': 'success', 'message': 'review updated'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def inputValidator(self, request):
        if 'feedback' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: feedback'}

        if 'avatar' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: avatar'}

        if 'rating' not in request.POST:
            return {'status': 'error', 'message': 'parameter not found: rating'}

        return {'status': 'success', 'message': 'review updated'}
