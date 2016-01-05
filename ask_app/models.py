from django.db import models
import datetime
from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def most_resent(self):
        return self.order_by('-id')

    def hotest(self):
        return self.order_by('-like_counter')

    def answers(self, id):
        return self.get(id=id).answer_set.order_by('-id')


class TagManager(models.Manager):
    def get_questions(self, tag_id):
        return self.get(id=tag_id).question_set.order_by('-id')


class Profile(User):
    path_to_avatar = models.CharField('avatar_path', max_length=100, default=' ')

    def __str__(self):
        return self.user_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=32)
    objects = TagManager()

    def __str__(self):
        return self.tag_name


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    creator = models.ForeignKey(Profile)
    date = models.DateTimeField('date', default=datetime.datetime.now)
    tags = models.ManyToManyField(Tag)
    objects = QuestionManager()

    def likes_count(self):
        likes = self.questionlike_set.all()
        like_counter = 0
        for like in likes:
            if like.value == 1:
                like_counter += 1
            else:
                like_counter -= 1
        return like_counter

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=1000)
    creator = models.ForeignKey(Profile)
    question = models.ForeignKey(Question)
    date = models.DateTimeField('date', default=datetime.datetime.now)
    tags = models.ManyToManyField(Tag)

    def likes_count(self):
        likes = self.answerlike_set.all()
        like_counter = 0
        for like in likes:
            if like.value == 1:
                like_counter += 1
            else:
                like_counter -= 1
        return like_counter

    def __str__(self):
        return self.text


class QuestionLike(models.Model):
    voter = models.ForeignKey(Profile)
    question = models.ForeignKey(Question)
    value = models.BooleanField()

    def __str__(self):
        if self.value == 1:
            return "like"
        else:
            return "dislike"


class AnswerLike(models.Model):
    voter = models.ForeignKey(Profile)
    question = models.ForeignKey(Answer)
    value = models.BooleanField()

    def __str__(self):
        if self.value == 1:
            return "like"
        else:
            return "dislike"
