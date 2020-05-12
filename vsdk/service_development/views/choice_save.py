from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect
from django.utils import timezone

from ..models import ChoiceSaved

class ChoiceSave(TemplateView):

    def post(self, request, session_id):
        """
        Saves selected choice to DB
        """
        
        print("++++ Save choice ++++")

        if 'selected_choice_url' in request.POST:
            choice_url = request.POST['selected_choice_url']
        else:
            raise ValueError('Incorrect request, selected_choice_url not set')

        if 'selected_choice_name' in request.POST:
            choice_name = request.POST['selected_choice_name']
        else:
            raise ValueError('Incorrect request, selected_choice_name not set')

        choice = ChoiceSaved(
            call_date = timezone.now(),
            choice = choice_name
        )
        choice.save()

        print(choice_url)
        print(choice_name)

        print("------ Saved. ------")

        

        return HttpResponseRedirect(choice_url)