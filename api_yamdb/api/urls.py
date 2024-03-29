from api.reviews_views import CommentViewSet, ReviewViewSet
from api.titles_views import CategoryViewSet, GenreViewSet, TitleViewSet
from api.users_views import SignupView, TokenView, UserViewSet
from api.utils import OptionalSlashRouter
from django.urls import include, path, re_path

router = OptionalSlashRouter()
router.register("users", UserViewSet, basename="user")
router.register("categories", CategoryViewSet, basename="category")
router.register("genres", GenreViewSet, basename="genre")
router.register("titles", TitleViewSet, basename="title")
router.register(
    r"titles/(?P<title_id>\d+)/reviews",
    ReviewViewSet, basename="review")
router.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet, basename="comment")

urlpatterns = [
    re_path(r"^v1/auth/signup/?",
            SignupView.as_view(),
            name="request_confirmation"),
    re_path(r"^v1/auth/token/?", TokenView.as_view(), name="obtain_token"),
    path("v1/", include(router.urls)),
]
