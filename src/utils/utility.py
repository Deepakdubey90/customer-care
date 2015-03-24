from django.contrib.contenttypes.models import ContentType


def get_content_type(app, label):
    return ContentType.objects.get(app_label=app, model=label)

