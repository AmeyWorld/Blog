from django.apps import AppConfig


class MyblogConfig(AppConfig):
    name = 'MyBlog'

    def ready(self):
        import MyBlog.signals