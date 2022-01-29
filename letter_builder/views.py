from django.views import generic, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.template import RequestContext, Template
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.shortcuts import render, redirect

from settings.models import Letter, UserProfile, JobProfile, Qualification, Attribute

import datetime as dt


class IndexView(generic.ListView):
	model = Letter
	template_name = 'settings/index.html'

	def get_context_data(self, ** kwargs):
		context = super().get_context_data( ** kwargs)
		user_profiles = UserProfile.objects.all()
		job_profiles = JobProfile.objects.all()
		context['user_profiles'] = user_profiles
		context['job_profiles'] = job_profiles
		return context


class LetterView(generic.ListView):
	model = Letter


class LetterDetailView(generic.DetailView):
	model = Letter

	def get_context_data(self, ** kwargs):
		context = super().get_context_data( ** kwargs)
		user_profiles = UserProfile.objects.all()
		if user_profiles.count() > 0: user_profiles = user_profiles[0]
		else: user_profiles = None

		job_profiles = JobProfile.objects.all()
		if job_profiles.count() > 0: job_profiles = job_profiles[0]
		else: job_profiles = None

		template = get_letter_template(self.request, self.get_object(), job_profiles, user_profiles)
		if template:
			context['letter_html'] = template['html_template']
			context['letter_text'] = template['text_template']
		return context


class IframeLetterView(generic.DetailView):
	model = Letter

	def get(self, request, *args, **kwargs):
		user_profiles = UserProfile.objects.all()
		if user_profiles.count() > 0: user_profiles = user_profiles[0]
		else: user_profiles = None

		job_profiles = JobProfile.objects.all()
		if job_profiles.count() > 0: job_profiles = job_profiles[0]
		else: job_profiles = None

		template = get_letter_template(self.request, self.get_object(), job_profiles, user_profiles)
		if template:
			return HttpResponse(template['html_template'])
		return HttpResponse("Data Error")


class CreateLetterView(CreateView):
	model = Letter
	fields = ['name', 'file', 'description']


class UpdateLetterView(UpdateView):
	model = Letter
	fields = ['name', 'file', 'description']

	def get_context_data(self, ** kwargs):
		context = super().get_context_data( ** kwargs)
		context['state'] = 'EDIT'
		return context


class DeleteLetterView(DeleteView):
	model = Letter
	success_url = reverse_lazy('letters')


class EditLetterTemplateFileView(generic.DetailView, View):
	template_name = 'settings/letter_template_edit.html'
	model = Letter

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		letter = self.get_object()
		if letter.file_extension() == 'txt':
			letter_text = letter.file.read().decode()
			letter_html = '<br/>'.join(letter_text.split('\n'))
			context['letter_text'] = letter_html
		return context

	def post(self, request, *args, **kwargs):
		letter = self.get_object()
		new_data = request.POST['letter']
		file = letter.file
		file.open('w')
		file.write(new_data)
		file.close()
		return redirect('view-letter', letter.id)


class UserProfileView(generic.ListView):
	model = UserProfile


class CreateUserProfileView(CreateView):
	model = UserProfile
	fields = ['title', 'first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'location']


class UpdateUserProfileView(UpdateView):
	model = UserProfile
	fields = ['title', 'first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'location']

	def get_context_data(self, ** kwargs):
		context = super().get_context_data( ** kwargs)
		context['state'] = 'EDIT'
		return context


class DeleteUserProfileView(DeleteView):
	model = UserProfile
	success_url = reverse_lazy('user-profiles')


class JobProfileView(generic.ListView):
	model = JobProfile


class CreateJobProfileView(CreateView):
	model = JobProfile
	fields = ['name', 'experience', 'description', 'organization', 'address', 'email']


class UpdateJobProfileView(UpdateView):
	model = JobProfile
	fields = ['name', 'experience', 'description', 'organization', 'address', 'email']

	def get_context_data(self, ** kwargs):
		context = super().get_context_data( ** kwargs)
		context['state'] = 'EDIT'
		return context


class DeleteJobProfileView(DeleteView):
	model = JobProfile
	success_url = reverse_lazy('job-profiles')


def get_letter_template(request, letter, job_profile, user_profile):
	if letter.file_extension() == 'txt':
		letter_text = letter.file.read().decode()
		# HTML Letter Version
		letter_br = '<br/>'.join(letter_text.split('\n'))
		letter_html = '<p>'+letter_br+'</p>'
		today = dt.datetime.today()
		context = RequestContext(
			request, 
			{"job_profile": job_profile, "user_profile":user_profile, 'today': today}
		)
		html_template = Template(letter_html)
		# Text Version
		text = '\n'.join(letter_text.split('<br>'))
		text_template = Template(strip_tags(text))
		return {"html_template": html_template.render(context), "text_template": text_template.render(context)} 

	return False