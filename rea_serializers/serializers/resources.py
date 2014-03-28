from rea.models.resources import Resource

from cqrs.serializers import CQRSPolymorphicSerializer


class ResourceSerializer(CQRSPolymorphicSerializer):
    '''
    Polymorphic serializer for the `Resource` model
    '''
    class Meta:
        model = Resource
