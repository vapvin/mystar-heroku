from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from pictures.models import PictureModel
from pictures.serializers import PictureSerializer
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.authentication import TokenAuthentication


class PictureListView(viewsets.ModelViewSet):
    queryset = PictureModel.objects.order_by("-date_created")
    serializer_class = PictureSerializer
    lookup_field = "slug"
    permission_classes = [HasAPIKey | permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [HasAPIKey | permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PicureDetailView(viewsets.ModelViewSet):
    queryset = PictureModel.objects.order_by("-date_created")
    serializer_class = PictureSerializer
    lookup_field = "slug"
    permission_classes = [HasAPIKey | permissions.IsAuthenticated]


class PictureFeaturedView(ListAPIView):
    queryset = PictureModel.objects.all().filter(featured=True)
    serializer_class = PictureSerializer
    lookup_field = "slug"
    permission_classes = [HasAPIKey | permissions.IsAuthenticated]


class PictureCategoryView(APIView):
    serializer_class = PictureSerializer
    permission_classes = [HasAPIKey | permissions.IsAuthenticated]

    def post(self, request, format=None):
        data = self.request.data
        category = data["category"]
        queryset = PictureModel.objects.order_by("-date_created").filter(
            category__iexact=category
        )

        serializer = PictureSerializer(queryset, many=True)
        return Response(serializer.data)
