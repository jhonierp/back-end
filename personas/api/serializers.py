from rest_framework import serializers
from personas.models import Persona

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields=['id','nombre','apellido','telefono','correo','tipo_persona']