from django_tables2 import Column, tables, TemplateColumn
from .models import Item


class ItemList(tables.Table):
    review_status = Column(
        attrs={
            "td": {
                "class": lambda value: "text-success"
                if value == "Complete"
                else ("text-warning" if value == "In Progress" else "text-danger")
            }
        },
        orderable=False,
    )

    class Meta:
        model = Item
        template_name = "django_tables2/bootstrap5.html"
        attrs = {"class": "table table-sm"}
        row_attrs = {"review_status": lambda value: value.name}
        fields = [
            "id",
            "date",
            "author",
            "title",
            "publish",
            "review_status",
        ]

    id = Column(verbose_name="ID", orderable=False)
    date = Column(orderable=False)
    author = Column(orderable=False)
    title = Column(orderable=False)
    publish = Column(orderable=False)
    review = TemplateColumn(template_name="tables/view_item.html", orderable=False)
