{% load static %}

<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title>welcome to foodNetwork</title>
  <!-- <link rel="stylesheet" href="css/form.css"> -->
  <link href="{% static 'desktop/assets/css/form.css' %}" rel="stylesheet" />
  <link href='https://fonts.googleapis.com/css?family=Lato:400,700' rel='stylesheet' type='text/css'>
</head>

<body>
  <form action="#" method="post" name="sign up for beta form">
    <img src="{% static 'mobile/images/slider-03.jpg' %}" alt="" style="width: 85%; height: 85%;">
    {% csrf_token %}
    <div>
      {% if form.errors %}
      <div class="error-message">
        <ul style="list-style: none;">
          {% for field in form %}
          {% for error in field.errors %}
          <li style="list-style: none; color: red;">{{ error }}</li>
          {% endfor %}
          {% endfor %}
        </ul>
      </div>
      {% endif %}
    </div>
    <div class="header">
      <p>Hurry! Welcome to foodNetwork</p>
    </div>
    <div class="description">
      <p>
        foodNetwork is an online community space where you get discounted fine dining restaurants,
        the best local restaurants around you, inns, and anything food-related. We partner with top restaurants around
        you and deliver unbelievable
        discounts of up to 75% for our community when you eat out.
      </p>
      <br>
      <p>
        Join foodNetwork's waiting list now to get the hottest and latest discount deals on your favorite fine-dining
        restaurant coming soon....
      </p>
    </div>
    <div class="input column">
      <input type="text" class="button" id="email" name="email" placeholder="Emain">
      <input type="submit" class="button" id="submit" value="JOIN">
    </div>
    <div class="more-info">
      <p>
        For more information and to register as a restaurateur kindly send us an email admin@foodNetwork.com
      </p>
    </div>
  </form>

  <!-- <a href="{% url 'index' %}">HOME<i class="fa-duotone fa-house"></i></a> -->

</body>

</html>