from rest_framework import serializers
from contacts.models import Contact

class ContactsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = ('id', 'first_name', 'last_name', 
				'email', 'phone', 'created', 'modified')
