from django.contrib import admin

from .models import (
    Socialmedia,
    Banner,
    About,
    Service,
    Place,
    Destination,
    Package,
    Review,
    ReplayReview,
    Gallary,
    Guides,
    Testimonial,
    Articlescategory,
    Articlestag,
    Articles,
    ArticleReview,
    ReplayArticleReview,
    Newslatter,
)

admin.site.register([
    Socialmedia,
    Banner,
    About,
    Service,
    Place,
    Destination,
    Package,
    Review,
    ReplayReview,
    Gallary,
    Guides,
    Testimonial,
    Articlescategory,
    Articlestag,
    Articles,
    ArticleReview,
    ReplayArticleReview,
    Newslatter,
])