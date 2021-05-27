
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=15)
    phone = models.IntegerField()
    manager_id = models.IntegerField(db_column='managerID')

    class Meta:
        db_table = 'hotels'

    def __str__(self):
        return self.name


class RoomType(models.Model):
    room_type = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    description = models.TextField()
    NUM_PEOPLE = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('family', 'Family'),
    )
    num_person = models.CharField(choices=NUM_PEOPLE, max_length=10)
    area = models.SmallIntegerField()

    class Meta:
        db_table = 'room_type'

    def __str__(self):
        return self.room_type + self.num_person


class Room(models.Model):
    room_number = models.SmallIntegerField(primary_key=True)
    room_type = models.ForeignKey('RoomType', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(
        max_length=32,
        choices=(
            ('available', 'Available'),
            ('using', 'Using'),
            ('not clean', 'Need Clean'),
            ('broken', 'Broken'),
        ),
        default='available',
    )

    class Meta:
        db_table = 'room'

    def __str__(self):
        return self.room_type.room_type


class Image(models.Model):
    room_type = models.ForeignKey('RoomType', models.DO_NOTHING, blank=True, null=True)
    image = models.ImageField(upload_to='room_images')

    class Meta:
        db_table = 'image'

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="{}" width="auto" height="100px" />'.format(self.image.url))

    image_tag.short_description = 'View'

    def __str__(self):
        return self.room_type.__str__()
