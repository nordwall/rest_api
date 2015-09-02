from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from contacts.models import Contact
from contacts.serializers import ContactsSerializer

class Contacts(APIView):
	
	def get(self, request, contact_id=None, format=None):
		
		if contact_id is None:
			contacts = Contact.objects.all()
		else:
			contacts = Contact.objects.filter(id=contact_id)

		if contacts.count() == 0:
			return Response('Not found.', status=status.HTTP_404_NOT_FOUND)

		contacts_data = ContactsSerializer(measurements, many=True).data

		return Response(contacts_data, status=status.HTTP_200_OK)
	
	def post(self, request, format=None):
		serializer = ContactsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
