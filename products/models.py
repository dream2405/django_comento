import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # UUID를 사용하여 파일 이름 생성
        filename = f'{uuid4().hex}.{ext}'
        # 기존 경로 구조 유지
        return os.path.join(self.path, filename)


# 회사 상품
class Product(models.Model):
    name = models.CharField(max_length=30)  # 이름
    pub_date = models.DateField('date published')  # 출시일
    price = models.IntegerField(validators=[MinValueValidator(0)])  # 상품 가격(원)
    desc = models.TextField()  # 상품 상세 설명
    summary = models.CharField(max_length=50)  # 상품 요약 설명
    img = models.ImageField(
        upload_to=PathAndRename('products/images/%Y/%M/%d/'),
        null=True,
        blank=True
    )  # 상품 이미지 경로

    def __str__(self):
        return f'[{self.pk}]{self.name}'


# 상품 리뷰
class Review(models.Model):
    title = models.CharField(max_length=50)  # 리뷰 제목
    review = models.TextField()  # 리뷰글
    score = models.SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)])  # 평점(0~10, 정수)
    pub_date = models.DateTimeField(auto_now_add=True)  # 게시일
    author = None  # 작성자(id)

    def __str__(self):
        return f'[{self.pk}]{self.title}'
