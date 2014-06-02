from rea.models.resources import Resource

from cqrs.serializers import CQRSPolymorphicSerializer


class ResourceSerializer(CQRSPolymorphicSerializer):

    class Meta:
        model = Resource
