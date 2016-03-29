from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from tags.models import Tag


class Post(models.Model):

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        unique=True,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )
    image = models.ImageField()
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    tag_set = models.ManyToManyField(
        Tag,
    )
# related_name ="post_set" 으로 자동으로 만들어줌
# 그래서 shell에서 tag.post_set.all()하면 찾을수있다.
# 연결하기위해선 add 를 쓴다.
# tag.post_set.all() =[<Post: Post object>]
# post.tag_set.all() =[<Tag: #커피>]
# 자동으로 tag와 post 를 연결해주는 태블릿 만들어줌
# post.tags > Manager << tags 란이름이 매니져이다.

    def init_hash_id(self):
        from yoostargram.utils.hash_id import get_encoded_hash_id
        self.hash_id = get_encoded_hash_id(self)
        self.save()

    def get_absolute_url(self):
        return reverse(
            "posts",
            kwargs={
                "pk": post.id,
            }
        )
