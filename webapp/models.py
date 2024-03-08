import _uuid
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


# ---------- Hero section ---------- #
class Hero(models.Model):
    res_name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='hero/%Y/%m/%d', blank=False)
    
    def __str__(self):
        return self.res_name
    

# ---------- Discounted section ---------- #
class Discounted(models.Model):
    name_of_resturant = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='discounted/%Y/%m/%d', blank=False)
    discounted = models.DecimalField(max_digits=10, decimal_places=2)
    # i want a field that can count down till when item is expired
    # maybe like a positive int field or something that check if this item is still discounted
    url_to_dish = models.URLField()

    def __str__(self):
        return self.name_of_resturant
    

# ---------- PopularRestaurant section ---------- #
class PopularRestaurantsView1(models.Model):
    image = models.ImageField(upload_to='popuralar_1/%Y/%m/%d', blank=False)
    dish = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=1000, blank=True)
    url_to_dish = models.URLField()
    
    def __str__(self):
        return self.dish
     
class PopularRestaurantsView2(models.Model):
    image = models.ImageField(upload_to='popuralar_2/%Y/%m/%d', blank=False)
    dish = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=1000, blank=True)
    url_to_dish = models.URLField()
    
    def __str__(self):
        return self.dish

class PopularRestaurantsView3(models.Model):
    image = models.ImageField(upload_to='popuralar_3/%Y/%m/%d', blank=False)
    dish = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=1000, blank=True)
    url_to_dish = models.URLField()
    
    def __str__(self):
        return self.dish

class PopularRestaurantsView4(models.Model):
    image = models.ImageField(upload_to='popuralar_4/%Y/%m/%d', blank=False)
    dish = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=1000, blank=True)
    url_to_dish = models.URLField()
    
    def __str__(self):
        return self.dish


# ---------- Featured ---------- #
class FeaturedDish(models.Model):
    image = models.ImageField(upload_to='featured_dish/%Y/%m/%d', blank=False)
    # available
    logo = models.ImageField(upload_to='logo/%Y/%m/%d', blank=False)
    name = models.CharField(max_length=1000, blank=True)
    # open now or closed
    url_to_dish = models.URLField()
    
    def __str__(self):
        return self.name


# ---------- Most_ordered ---------- #
class SearchbyFood1(models.Model):
    image = models.ImageField(upload_to='most_ordered1/%Y/%m/%d', blank=False)
    dish = models.CharField(max_length=1000, blank=True)
    url_to_dish = models.URLField(default='https://www.linkedin.com/in/sundayefeterry/')
    
    def __str__(self):
        return self.dish

class SearchbyFood2(models.Model):
    image = models.ImageField(upload_to='most_ordered2/%Y/%m/%d', blank=False)
    dish = models.CharField(max_length=1000, blank=True)
    url_to_dish = models.URLField(default='https://www.linkedin.com/in/sundayefeterry/')
    
    def __str__(self):
        return self.dish
    
class SearchbyFood3(models.Model):
    image = models.ImageField(upload_to='most_ordered3/%Y/%m/%d', blank=False)
    dish = models.CharField(max_length=1000, blank=True)
    url_to_dish = models.URLField(default='https://www.linkedin.com/in/sundayefeterry/')
    
    def __str__(self):
        return self.dish
    
class SearchbyFood4(models.Model):
    image = models.ImageField(upload_to='most_ordered4/%Y/%m/%d', blank=False)
    dish = models.CharField(max_length=1000, blank=True)
    url_to_dish = models.URLField(default='https://www.linkedin.com/in/sundayefeterry/')
    
    def __str__(self):
        return self.dish
    
class SearchbyFood5(models.Model):
    image = models.ImageField(upload_to='most_ordered/5%Y/%m/%d', blank=False)
    dish = models.CharField(max_length=1000, blank=True)
    url_to_dish = models.URLField(default='https://www.linkedin.com/in/sundayefeterry/')
    
    def __str__(self):
        return self.dish
    

# ----------  writer ---------- #
class Writer(models.Model):
    heading = models.CharField(max_length=50, blank=False)
    writeUp = models.CharField(max_length=1000, blank=False)
    writer = models.CharField(max_length=50, blank=True)
    url_to_dish = models.URLField(default='https://www.linkedin.com/in/sundayefeterry/')
    
    def __str__(self):
        return self.writer

class chefspot(models.Model):
    image = models.ImageField(upload_to='chef/5%Y/%m/%d', blank=False)
    heading = models.CharField(max_length=50, blank=False)
    writeUp = models.CharField(max_length=1000, blank=False)
    writer = models.CharField(max_length=50, blank=True)
    url_to_dish = models.URLField(default='https://www.linkedin.com/in/sundayefeterry/')
    
    def __str__(self):
        return self.writer
    
    
class paid_spotlight1(models.Model):
    display_image = models.ImageField(upload_to='hero_for_all/%Y/%m/%d', blank=False)
    resturant = models.CharField(max_length=1000, blank=True)
    dish = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=1000, blank=True)
    url_to_dish = models.URLField()
    
    def __str__(self):
        return self.resturant


class paid_hero1(models.Model):
    display_image = models.ImageField(upload_to='hero_for_all/%Y/%m/%d', blank=False)
    # open or closed
    resturant = models.CharField(max_length=1000, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=1000, blank=True)
    website = models.URLField()
    
    def __str__(self):
        return self.resturant


class paid_hero2(models.Model):
    display_image = models.ImageField(upload_to='hero_for_all/%Y/%m/%d', blank=False)
    # open or closed
    resturant = models.CharField(max_length=1000, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=1000, blank=True)
    website = models.URLField()
    
    def __str__(self):
        return self.resturant
    
class paid_hero3(models.Model):
    display_image = models.ImageField(upload_to='hero_for_all/%Y/%m/%d', blank=False)
    # open or closed
    resturant = models.CharField(max_length=1000, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=1000, blank=True)
    website = models.URLField()
    
    def __str__(self):
        return self.resturant
    
    
class all_resturant(models.Model):
    display_image = models.ImageField(upload_to='all_resturant/%Y/%m/%d', blank=False)
    # open or closed
    resturant = models.CharField(max_length=1000, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=1000, blank=True)
    logo = models.ImageField(upload_to='logo/%Y/%m/%d', blank=True)
    website = models.URLField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.resturant
    
# ---------- subscribe form ---------- #
class Feedback(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    

# ---------- Join form for resturant owners ---------- #
class Join(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name
    






