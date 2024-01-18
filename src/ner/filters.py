from django_filters import FilterSet, CharFilter, ChoiceFilter

from .models import Item

PUBLISH_CHOICES = (
    (0, "False"),
    (1, "True"),
)

STATUS_CHOICES = (
    (0, "Not Started"),
    (1, "In Progress"),
    (2, "Complete"),
)


class ItemFilter(FilterSet):
    author = CharFilter(
        field_name="author", label="Author Name Contains", lookup_expr="icontains"
    )
    publish = ChoiceFilter(
        field_name="publish", label="Publish", choices=PUBLISH_CHOICES
    )
    review_status = ChoiceFilter(
        field_name="review_status", label="Editorial Review", choices=STATUS_CHOICES
    )

    class Meta:
        model = Item
        fields = (
            "author",
            "publish",
            "review_status",
        )
