from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.http import HttpResponseRedirect

from model_utils.managers import InheritanceManager

import voicelabels

# Create your models here.
class VoiceServiceElement(models.Model):

    #use django_model_utils to be able to find out what is the subclass of this element
    #see: https://django-model-utils.readthedocs.io/en/latest/managers.html#inheritancemanager
    objects = InheritanceManager()

    creation_date = models.DateTimeField('date created', auto_now_add = True)
    modification_date = models.DateTimeField('date last modified', auto_now = True)
    name = models.CharField(max_length=100)
#    service = models.ForeignKey('VoiceService', on_delete = models.CASCADE)
    description = models.CharField(
            max_length = 500,
            blank = True)
    voice_label = models.ForeignKey(
            voicelabels.models.VoiceLabel,
            on_delete = models.SET_NULL,
            null = True,
            blank = True,
            )

    def __str__(self):
        return "Element: %s" % self.name

    def is_valid(self):
        return len(self.validator()) == 0
    is_valid.boolean = True

    def validator(self):
        if self.voice_label:
            return self.voice_label.validator()
        else:
            return ['No VoiceLabel in element: "%s"'%self.name]

    def get_voice_fragment_url(self, session):
        return self.voice_label.get_voice_fragment_url(session)

    def get_absolute_url(self, session):
        #this is a dirty hack to refer to the subclass object of this reference, and then call the same method there.
        #return reverse('service_development:choice', args=[str(self.id),str(session.id)])
        #TODO what happens here? error message?
        #subclass_objects = self.select_subclasses()
        #if 
     #   return 
        #return VoiceServiceElement.objects.get_subclass(pk=self.id)
        return reverse(self._urls_name, kwargs= {'element_id':str(self.id), 'session_id':session.id})

class MessagePresentation(VoiceServiceElement):
    final_element = models.BooleanField('This element will terminate the call',default = False)
    next_element = models.ForeignKey(
            VoiceServiceElement,
            on_delete = models.SET_NULL,
            null = True,
            blank = True,
            related_name='%(app_label)s_%(class)s_related')

    def __str__(self):
        return 'Message Element: %s' % self.name


class Choice(VoiceServiceElement):
    _urls_name = 'service_development:choice'

    def __str__(self):
        return self.name

    def is_valid(self):
        return len(self.validator()) == 0
    is_valid.boolean = True

    def validator(self):
        #TODO: check all children (choice options)
        
        if self.voice_label:
            return self.voice_label.validator()
        else:
            return ['No VoiceLabel in element: "%s"'%self.name]  


    #def get_absolute_url(self, **kwargs):
    #    """
    #    Give the URL to reach this Choice, arguments must match those in urls.py
    #    """
    #    return reverse('service_development:choice')
    #    return reverse('service_development:choice', kwargs= {'element_id':'str(self.id)'})

class ChoiceOption(VoiceServiceElement):
    parent = models.ForeignKey(
            Choice,
            #TODO: controlerne of dit wel echt cascade moet zijn???
            on_delete = models.CASCADE,
            related_name='choice_options')
    _redirect = models.ForeignKey(
            VoiceServiceElement, 
            #TODO: controlerne of dit wel echt cascade moet zijn???
            on_delete = models.CASCADE,
            related_name='%(app_label)s_%(class)s_redirect_related',
            blank = True,
            null = True)

    @property
    def redirect(self):
        """
        Returns the actual subclassed object that is redirected to,
        instead of the VoiceServiceElement superclass object (which does
        not have specific fields and methods).
        """
        return VoiceServiceElement.objects.get_subclass(id = self._redirect.id)

    def __str__(self):
        return "(%s): %s" % (self.parent.name,self.name)
    
    def is_valid(self):
        return len(self.validator()) == 0
    is_valid.boolean = True

    def validator(self):
        errors = []
        #check if voice label is present
        if self.voice_label:
            errors.extend(self.voice_label.validator())
        else:
            errors.append('No VoiceLabel in choice option: "%s"'%self.name)

        #check if redirect is present
        if not self._redirect:
            errors.append('No redirect in choice option: "%s"'%self.name)
        #check whether element that will be redirected to is appointed to the same voice service
        #elif not self.redirect in self.service.get_elements():
        #    errors.append('Redirect "%s" in choice option "%s" does not belong to same voice service'% (self.redirect.name, self.name))

        return errors
 
class DataPresentation(VoiceServiceElement):
    pass

class VoiceService(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=10)
    creation_date = models.DateTimeField('date created', auto_now_add = True)
    modification_date = models.DateTimeField('date last modified', auto_now = True)
    active = models.BooleanField('Voice service active')
    _start_element = models.ForeignKey(
            VoiceServiceElement,
            related_name='%(app_label)s_%(class)s_related',
            null = True,
            blank = True)
    requires_registration = models.BooleanField('Requires user registration')

    supported_languages = models.ManyToManyField(voicelabels.models.Language, blank = True)

    @property
    def start_element(self):
        """
        Returns the actual subclassed object that is redirected to,
        instead of the VoiceServiceElement superclass object (which does
        not have specific fields and methods).
        """
        return VoiceServiceElement.objects.get_subclass(id = self._start_element.id)

    def __str__(self):
        return 'Voice Service: %s' % self.name

    def is_valid(self):
        return len(self.validator()) == 0
    is_valid.boolean = True

    def validator(self):
        errors = []
        if not self._start_element:
            errors.append('No starting element')
        else:
            errors.extend(self.start_element.validator())
        if len(self.supported_languages.all()) == 0:
            errors.append('No supported languages')
        return errors

    def get_elements(self):
        #TODO
        return []