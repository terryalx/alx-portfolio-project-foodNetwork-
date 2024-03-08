from django.contrib import admin

from .models import Hero, Discounted, PopularRestaurantsView1, PopularRestaurantsView2, PopularRestaurantsView3, PopularRestaurantsView4, FeaturedDish
from .models import Feedback, Join
from .models import paid_spotlight1
from .models import paid_hero1
from .models import paid_hero2
from .models import paid_hero3
from .models import all_resturant
from .models import SearchbyFood1, SearchbyFood2, SearchbyFood3, SearchbyFood4, SearchbyFood5
from .models import Writer
from .models import chefspot

# Register your models here.
admin.site.register(Hero)
admin.site.register(Discounted)
admin.site.register(PopularRestaurantsView1)
admin.site.register(PopularRestaurantsView2)
admin.site.register(PopularRestaurantsView3)
admin.site.register(PopularRestaurantsView4)
admin.site.register(FeaturedDish)
admin.site.register(SearchbyFood1)
admin.site.register(SearchbyFood2)
admin.site.register(SearchbyFood3)
admin.site.register(SearchbyFood4)
admin.site.register(SearchbyFood5)
admin.site.register(paid_spotlight1)
admin.site.register(paid_hero1)
admin.site.register(paid_hero2)
admin.site.register(paid_hero3)
admin.site.register(all_resturant)
admin.site.register(Writer)
admin.site.register(chefspot)

admin.site.register(Feedback)
admin.site.register(Join)


