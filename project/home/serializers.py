from models import Photo, Area, Source, Album, CatPhoto, CatTag
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'date_text', 'title', 'description', 'source_key', 'source_url', 'source', 'area', 'lat', 'lon',
                  'azimuth', 'confidence', 'azimuth_confidence')


class CatResultsPhotoSerializer(serializers.ModelSerializer):
    thumb_height = serializers.IntegerField()
    thumb_width = serializers.IntegerField()

    class Meta:
        model = CatPhoto
        fields = ('id', 'title', 'thumb_height', 'thumb_width', 'source_url')


class CatTaggerTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatTag
        fields = ('name',)


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'name', 'lat', 'lon')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name')


class CuratorAlbumSelectionAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name', 'open')


class CuratorMyAlbumListAlbumSerializer(serializers.ModelSerializer):
    photo_count = serializers.IntegerField(source='photos.count')

    class Meta:
        model = Album
        fields = ('id', 'name', 'photo_count')


class CuratorAlbumInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name', 'description', 'open', 'is_public', 'subalbum_of')


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'name', 'description')