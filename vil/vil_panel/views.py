from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import StoreDetail
from users.models import Profile
from .forms import StoreDetailForm,SearchForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import ListView,UpdateView,CreateView,DeleteView,DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

#FBV part
@login_required
def home(request):
	if request.user.profile.user_type == 'ST':
		return redirect('vilpanel-storedetailcreate')
	elif request.user.profile.user_type == 'SM':
		return redirect('vilpanel-storemanager')
	elif request.user.profile.user_type == 'ZN':
		return redirect('vilpanel-zonal')
	elif request.user.profile.user_type == 'CL':
		return redirect('vilpanel-storedetaillist')
		
    
def store(request):
	submitted = False
	if request.method == 'POST':
		form = StoreDetailForm(request.POST)
		if form.is_valid():
			new_storedetail = form.save(commit=False)
			new_storedetail.profile = request.user.profile
			new_storedetail.save()
			return redirect('vilpanel-store')
	else:
		form = StoreDetailForm()
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'vil_panel/StoreDetail.html', {'form': form, 'submitted': submitted})
	

def storemanager(request):
	context = {
			'profiles': Profile.objects.filter(zone_name = request.user.profile.zone_name),
			'form': SearchForm()
		}
	return render(request, 'vil_panel/StoreManager.html',context)

	
def zonalmanager(request):
	return render(request, 'vil_panel/ZonalManager.html')

def circlemanager(request):
	return render(request, 'vil_panel/CircleManager.html')

#GCBV part

class StoreDetailListView(ListView):
	model = StoreDetail
	template_name = 'vil_panel/StoreDetailList.html'
	paginate_by = 5

	
class StoreDetailView(DetailView):
	model = StoreDetail

	
class StoreDetailCreateView(LoginRequiredMixin, CreateView):
	model = StoreDetail
	form_class = StoreDetailForm
	success_url = reverse_lazy('vilpanel-storedetailcreate')
	
	def form_valid(self,form):
		form.instance.profile = self.request.user.profile
		return super().form_valid(form)
			
	
class StoreDetailUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = StoreDetail
	form_class = StoreDetailForm
	success_url = reverse_lazy('vilpanel-storedetailcreate')
	
	def form_valid(self,form):
		form.instance.profile = self.request.user.profile
		return super().form_valid(form)
	
	def test_func(self):
		storedetail = self.get_object()
		if self.request.user.profile == storedetail.profile:
			return True
		return False
	

class StoreDetailDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = StoreDetail
	form_class = StoreDetailForm
	success_url = reverse_lazy('vilpanel-storedetailcreate')
	
	def form_valid(self,form):
		form.instance.profile = self.request.user.profile
		return super().form_valid(form)
	
	def test_func(self):
		storedetail = self.get_object()
		if self.request.user.profile == storedetail.profile:
			return True
		return False


class SearchResultsView(ListView):
    model = StoreDetail
    template_name = 'vil_panel/StoreDetailList.html'
	
    def get_queryset(self):
        cust_mobile_no = self.request.GET.get('customer_mobile_no')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        object_list = StoreDetail.objects.filter(Q(customer_mobile_no = cust_mobile_no)).filter( 
		insertion_date_time__gte = start_date , insertion_date_time__lte = end_date)
        return object_list	
		
		 
		
	
		
	
    
    