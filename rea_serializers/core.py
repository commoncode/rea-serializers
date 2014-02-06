from rest_framework import serializers


class CQRSSerializer(serializers.ModelSerializer):

    mongoID = serializers.CharField(required=False)
