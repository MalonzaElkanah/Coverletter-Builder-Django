from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from settings.models import Letter, UserProfile, JobProfile, Qualification, Attribute


class IndexView(generic.ListView):
	model = Letter


class LetterView(generic.ListView):
	model = Letter


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
