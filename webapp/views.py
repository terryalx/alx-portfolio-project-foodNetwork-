from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.decorators.cache import never_cache
from .models import (
    Hero,
    Discounted,
    PopularRestaurantsView1,
    PopularRestaurantsView2,
    PopularRestaurantsView3,
    PopularRestaurantsView4,
    FeaturedDish,
    SearchbyFood1,
    SearchbyFood2,
    SearchbyFood3,
    SearchbyFood4,
    SearchbyFood5,
    paid_spotlight1,
    paid_hero1,
    paid_hero2,
    paid_hero3,
    all_resturant,
    Writer,
    chefspot,
)
from .form import FeedbackForm, JoinForm
from django.db.models import Q
from django.views.generic import ListView, DetailView
import re
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@never_cache
def home(request):
    user_agent = request.META.get('HTTP_USER_AGENT')
    is_mobile = bool(re.search(r'iPhone|iPad|iPod|Android', user_agent))

    if is_mobile:
        return redirect('mobile_view')
    else:
        return redirect('desktop_view')

@never_cache
def mobile_view(request):
    hero = Hero.objects.all()
    pop1 = PopularRestaurantsView1.objects.all()
    pop2 = PopularRestaurantsView2.objects.all()
    pop3 = PopularRestaurantsView3.objects.all()
    pop4 = PopularRestaurantsView4.objects.all()
    f_dish = FeaturedDish.objects.all()
    search1 = SearchbyFood1.objects.all()
    search2 = SearchbyFood2.objects.all()
    search3 = SearchbyFood3.objects.all()
    search4 = SearchbyFood4.objects.all()
    search5 = SearchbyFood5.objects.all()
    discounted = Discounted.objects.all()
    writer = Writer.objects.all()
    chef = chefspot.objects.all()

    context = {
        'hero': hero, 
        'discounted': discounted, 
        'pop1': pop1, 
        'pop2': pop2,
        'f_dish': f_dish,
        'search1': search1,
        'search2': search2,
        'search3': search3,
        'search4': search4,
        'search5': search5,
        'pop3' : pop3,
        'pop4' : pop4,
        'writer' : writer,
        'chefspot' : chef,
        'sitename': 'Youtube'
    }

    return render(request, 'index_mobile.html', context)

@never_cache
def desktop_view(request):
    hero = Hero.objects.all()
    pop1 = PopularRestaurantsView1.objects.all()
    pop2 = PopularRestaurantsView2.objects.all()
    pop3 = PopularRestaurantsView3.objects.all()
    pop4 = PopularRestaurantsView4.objects.all()
    f_dish = FeaturedDish.objects.all()
    search1 = SearchbyFood1.objects.all()
    search2 = SearchbyFood2.objects.all()
    search3 = SearchbyFood3.objects.all()
    search4 = SearchbyFood4.objects.all()
    search5 = SearchbyFood5.objects.all()
    discounted = Discounted.objects.all()
    writer = Writer.objects.all()
    chef = chefspot.objects.all()

    context = {
        'hero': hero, 
        'discounted': discounted, 
        'pop1': pop1, 
        'pop2': pop2,
        'f_dish': f_dish,
        'search1': search1,
        'search2': search2,
        'search3': search3,
        'search4': search4,
        'search5': search5,
        'pop3' : pop3,
        'pop4' : pop4,
        'writer' : writer,
        'chefspot' : chef,
        'sitename': 'Youtube'
    }

    return render(request, 'index_desktop.html', context)

# def home(request):
#     user_agent = request.META.get('HTTP_USER_AGENT')
#     is_mobile = bool(re.search(r'iPhone|iPad|iPod|Android', user_agent))

#     if is_mobile:
#         return redirect('mobile_view')
#     else:
#         return redirect('desktop_view')

# @never_cache
# def home(request):
#     if user_agent_select(request):
#         template = 'index_desktop.html'
#     else:
#         template = 'index_mobile.html'

#     hero = Hero.objects.all()
#     pop1 = PopularRestaurantsView1.objects.all()
#     pop2 = PopularRestaurantsView2.objects.all()
#     pop3 = PopularRestaurantsView3.objects.all()
#     pop4 = PopularRestaurantsView4.objects.all()
#     f_dish = FeaturedDish.objects.all()
#     search1 = SearchbyFood1.objects.all()
#     search2 = SearchbyFood2.objects.all()
#     search3 = SearchbyFood3.objects.all()
#     search4 = SearchbyFood4.objects.all()
#     search5 = SearchbyFood5.objects.all()
#     discounted = Discounted.objects.all()
#     writer = Writer.objects.all()
#     chef = chefspot.objects.all()

#     context = {
#         'hero': hero, 
#         'discounted': discounted, 
#         'pop1': pop1, 
#         'pop2': pop2,
#         'f_dish': f_dish,
#         'search1': search1,
#         'search2': search2,
#         'search3': search3,
#         'search4': search4,
#         'search5': search5,
#         'pop3' : pop3,
#         'pop4' : pop4,
#         'writer' : writer,
#         'chefspot' : chef,
#         'sitename': 'Youtube'
#     }

#     return render(request, template, context)
    
@never_cache
def success(request):
    return render(request, 'success.html')

# def search(request):
#     all_items = all_resturant.objects.all()

#     query = request.GET.get('query')
#     if query:
#         # Perform filtering based on multiple parameters
#         all_items = all_items.filter(
#             Q(resturant__icontains=query) |
#             Q(location__icontains=query)
#             # Add more fields for filtering if needed
#         ).distinct()

#         # If search query is present, don't render default content
#         default_content = None
        
#     else:
        
#         # Fetch default content for the homepage
#         default_content = all_resturant.objects.all()

#     paginator = Paginator(all_items, 6)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'searchitems.html', {
#         'all': page_obj,
#         'default_content': default_content  # Pass default content to the template
#     })
    

class SearchListView(ListView):
    template_name = 'searchitems.html'
    context_object_name = 'all'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_queryset(self):
        all_items = all_resturant.objects.all()
        query = self.request.GET.get('query')

        if query:
            # Perform filtering based on multiple parameters
            all_items = all_items.filter(
                Q(resturant__icontains=query) |
                Q(location__icontains=query)
                # Add more fields for filtering if needed
            ).distinct()

        return all_items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_items = self.get_queryset()
        paginator = Paginator(all_items, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        default_content = all_resturant.objects.none() if not all_items else all_resturant.objects.all()
        context['all'] = page_obj
        context['default_content'] = default_content
        return context


@never_cache
def alldeal(request):
    p1 = paid_spotlight1.objects.all()
    paid1 = paid_hero1.objects.all()
    paid2 = paid_hero2.objects.all()
    paid3 = paid_hero3.objects.all()
    all_items = all_resturant.objects.all()

    query = request.GET.get('query')
    if query:
        # Filtering based on multiple parameters
        all_items = all_items.filter(
            Q(resturant__icontains=query) |
            Q(location__icontains=query)
            # Add more fields for filtering if needed
        ).distinct()

        # If search query is present, don't render default content
        default_content = None
    else:
        # Fetch default content for the homepage
        default_content = all_resturant.objects.all()

    paginator = Paginator(all_items, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the valid form data to the database
            return redirect('alldeal')  # Replace 'success_url' with your success URL
        else:
            # If form is invalid, re-render the page with the form and other data
            return render(request, 'list_resturants.html', {
                'p1': p1,
                'paid1': paid1,
                'paid2': paid2,
                'paid3': paid3,
                'all': page_obj,
                'default_content': default_content,
                'form': form  # Pass the form with errors to display in the template
            })
    else:
        form = FeedbackForm()  # Create a new form instance

    return render(request, 'list_resturants.html', {
        'p1': p1,
        'paid1': paid1,
        'paid2': paid2,
        'paid3': paid3,
        'all': page_obj,
        'default_content': default_content,
        'form': form  # Pass the form to the template for rendering
    })


class PostDetailView(DetailView):
    model = all_resturant
    template_name = 'postdetail.html'
    

@never_cache
def subscribe(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FeedbackForm()
    return render(request, 'subscribe.html', {'form': form})


@never_cache
def subscribe_mobile(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FeedbackForm()
    return render(request, 'subscribe_mobile.html', {'form': form})

# new view for resturant owners

@never_cache
def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = JoinForm()
    return render(request, 'join.html', {'form': form})

@never_cache
def join_mobile(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = JoinForm()
    return render(request, 'join_mobile.html', {'form': form})


# *********************************************************************************************

@never_cache
def live(request):
    hero = Hero.objects.all()
    pop1 = PopularRestaurantsView1.objects.all()
    pop2 = PopularRestaurantsView2.objects.all()
    pop3 = PopularRestaurantsView3.objects.all()
    pop4 = PopularRestaurantsView4.objects.all()
    f_dish = FeaturedDish.objects.all()
    search1 = SearchbyFood1.objects.all()
    search2 = SearchbyFood2.objects.all()
    search3 = SearchbyFood3.objects.all()
    search4 = SearchbyFood4.objects.all()
    search5 = SearchbyFood5.objects.all()
    discounted = Discounted.objects.all()
    writer = Writer.objects.all()
    chef = chefspot.objects.all()

    context = {
        'hero': hero, 
        'discounted': discounted, 
        'pop1': pop1, 
        'pop2': pop2,
        'f_dish': f_dish,
        'search1': search1,
        'search2': search2,
        'search3': search3,
        'search4': search4,
        'search5': search5,
        'pop3' : pop3,
        'pop4' : pop4,
        'writer' : writer,
        'chefspot' : chef,
        'sitename': 'Youtube'
    }

    return render(request, 'live.html', context)



