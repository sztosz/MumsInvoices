from rest_framework import serializers

from authentication.serializers import AccountSerializer
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    autor = AccountSerializer(read_only=True, required=True)

    class Meta:
        model = Post

        fields = ('id', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


    # PROBABLY FROM OLD VERSION
    # def get_validation_exclusions(self, *args, **kwargs):
    #     exclusions = super.get_validation_exclusions()
    #
    #     return exclusions + ['author']
