from rea.models.resources import Resource

from .core import REASerializer


class ResourceSerializer(REASerializer):
    """
    Serializer for the `Resource` model
    """
    class Meta:
        model = Resource
        fields = ( "id", "title", "slug" )

