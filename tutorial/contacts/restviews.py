from rest_framework import viewsets

from .models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # super(TodoListViewSet, self).perform_create(serializer)


