from rea.models.resources import Resource

from cqrs.mongo import CQRSSerializer


class ResourceSerializer(CQRSSerializer):
    """
    Serializer for the `Resource` model
    """
    class Meta:
        model = Resource
        fields = ( "id", "title", "slug" )

