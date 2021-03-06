"""graphqlStudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Following graphene for django guide: https://docs.graphene-python.org/projects/django/en/latest/installation/

from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
    # Change graphiql=True to graphiql=False if you do not want to use the GraphiQL API browser.
    path("graphql", GraphQLView.as_view(graphiql=True)),
]