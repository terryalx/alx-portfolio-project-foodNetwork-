{% load static %}

<!DOCTYPE html>
<html lang="en-US" dir="ltr">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>foodNetwork</title>

    <link href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@200;300;400;600;700;900&amp;display=swap"
        rel="stylesheet">

    <!-- ===============================================-->
    <!-- Stylesheets -->
    <!-- ===============================================-->
    <link href="{% static 'mobile/assets/css/theme.css' %}" rel="stylesheet" />
    <!--  -->
    <link rel="stylesheet" href="{% static 'mobile/css/style.css' %}">
    <!-- Responsive CSS -->
    <link rel="stylesheet" href="{% static 'mobile/css/responsive.css' %}">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{% static 'mobile/css/custom.css' %}">
    <!--  -->

</head>

<body>

    <!-- ===============================================-->
    <!--    Main Content-->
    <!-- ===============================================-->
    <main class="main" id="top">

        <!-- Header -->

        <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top"
            data-navbar-on-scroll="data-navbar-on-scroll">
            <div class="container">
                <a class="navbar-brand d-inline-flex" href="{% url 'index' %}">
                    <!--logo image-->
                    <!-- <img class="d-inline-block" src="{% static 'assets/img/gallery/logo.svg' %}" alt="logo" /> -->
                    <span class="text-1000 fs-3 fw-bold ms-2 text-gradient">kuwiya</span>
                </a>
                <marquee>
                    Get up to 50% discount everytime you eat at your favourite restaurant..
                    <span class="fs-1 text-danger">Subscribe for discounts and more</span>
                </marquee>
            </div>
            </div>
        </nav>

        <!-- Start slides : HERO -->
        <!-- dynamically change images -->

        <div id="slides" class="cover-slides">
            <ul class="slides-container">
                <li class="text-center">
                    <img src="{% static 'mobile/images/slider-01.jpg' %}" alt="">
                    <div class="container">
                        <div class="row">
                            <div class="col-md-12">
                                <h1 class="m-b-40"><strong>Welcome To <br> kuwiya</strong></h1>
                                <p class="m-b-40">Subscribe to get 30% discount on all featured resturants this
                                    weekend!!</p>
                                <!-- link to subscribe -->
                                <p><a class="btn btn-lg btn-circle btn-outline-new-white"
                                        href="{% url 'subscribe' %}">Subscribe</a></p>
                            </div>
                        </div>
                    </div>
                </li>
                <li class="text-center">
                    <img src="{% static 'mobile/images/slider-02.jpg' %}" alt="">
                    <div class="container">
                        <div class="row">
                            <div class="col-md-12">
                                <h1 class="m-b-40"><strong>SAVE UP TO 50% OFF <br> EVERY TIME YOU EAT OUT</strong></h1>
                                <p class="m-b-40">Discount at all featured resturants</p>
                                <!-- link to featured restarants -->
                                <!-- create page and ask to subscribe to get the deals everytime they eat at featured restaurant -->
                                <p><a class="btn btn-lg btn-circle btn-outline-new-white"
                                        href="{% url 'subscribe' %}">Get Deals</a></p>
                            </div>
                        </div>
                    </div>
                </li>
                <li class="text-center">
                    <img src="{% static 'mobile/images/slider-03.jpg' %}" alt="">
                    <div class="container">
                        <div class="row">
                            <div class="col-md-12">
                                <h1 class="m-b-40"><strong>Best fine <br> dining restarants</strong></h1>
                                <!-- <p class="m-b-40"></p> -->
                                <!-- link list of all fine dining resturants -->
                                <!-- create page --> <!-- scarpy -->
                                <p><a class="btn btn-lg btn-circle btn-outline-new-white" href="{% url 'alldeal' %}">See
                                        all</a></p>
                            </div>
                        </div>
                    </div>
                </li>
            </ul>
            <div class="slides-navigation">
                <a href="#" class="next"><i class="fa fa-angle-right" aria-hidden="true"></i></a>
                <a href="#" class="prev"><i class="fa fa-angle-left" aria-hidden="true"></i></a>
            </div>
        </div>

        <!-- End slides : HERO -->

        <!-- ===============================================-->
        <!-- Discounted items-->
        <!-- ===============================================-->
        <!--py padding top and bottom-->
        <section class="py-0">

            <!-- Discounted items-->

            <div class="container">
                <div class="row h-100 gx-3 mt-5">
                    {% for items in discounted %}
                    <div
                        class="col-sm-8 d-flex align-items-center justify-content-center col-lg-3 mb-3 mb-md-0 h-100 pb-4">
                        <!--main container sizing-->
                        <div class="card card-span w-75 h-75">
                            <a href="{{ items.url_to_dish }}" role="button" target="_blank">
                                <div class="position-relative">
                                    <img class="rounded-3 fixed-image-height" src="{{ items.image }}" alt="..." />
                                    <div class="card-actions">
                                        <!--%0ff size-->
                                        <div class="badge badge-foodwagon bg-primary p-20">
                                            <div class="d-flex flex-between-center">
                                                <div class="text-white fs-5">
                                                    <span>-</span>
                                                    {{ items.discounted }}
                                                </div>
                                                <div class="d-block text-white fs-1">
                                                    <span>%</span>
                                                    <br />
                                                    <div class="fw-normal fs-1 mt-2">Off</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </div>

            <!-- Discounted items-->

        </section>
        <!-- <section> close ============================-->
        <!-- ============================================-->


        <!-- ============================================-->
        <!-- <section> begin ============================-->
        <!-- ============================================-->
        <section class="py-0 overflow-hidden pop-top">

            <div class="container pop-top">
                <div class="row h-100">
                    <div class="col-lg-7 mx-auto text-center mt-7 mb-5">
                        <h5 class="fw-bold fs-3 fs-lg-5 lh-sm">Popular Restaurants</h5>
                    </div>
                    <div class="col-12">
                        <div class="carousel slide" id="carouselPopularItems" data-bs-touch="false"
                            data-bs-interval="false">

                            <div class="carousel-inner">
                                <!-- 1 -->

                                <div class="carousel-item active" data-bs-interval="10000">
                                    <div class="row gx-3 h-100 align-items-center">
                                        {% for item in pop1|slice:"0:1" %}
                                        <div class="col-sm-6 col-md-4 col-xl mb-5 h-100">
                                            <div class="card card-span h-100 rounded-3">
                                                <img class="rounded-3 w-100 h-100 slide-image" src="{{ item.image }}"
                                                    alt="..." />
                                                <div class="card-body ps-0">
                                                    <span class="fs-1 text-danger">
                                                        {{ item.dish }}
                                                    </span>
                                                    <div>
                                                        <span class="text-warning me-1">
                                                            <i class="fas fa-map-marker-alt"></i>
                                                        </span><span class="text-danger" PAN
                                                            STYLE="font-weight:bold ">{{ item.location }}</span>
                                                    </div><span class="text-1000 fw-bold"></span>
                                                </div>
                                            </div>
                                            <div class="d-grid gap-2">
                                                <a class="btn btn-lg btn-danger" href="{{ item.url_to_dish }}"
                                                    role="button" target="_blank">Visit</a>
                                            </div>
                                        </div>
                                        {% endfor %}
                                    </div>
                                </div>

                                <!-- 2 -->

                                <div class="carousel-item" data-bs-interval="5000">
                                    <div class="row gx-3 h-100 align-items-center">
                                        {% for item in pop2|slice:"0:1" %}
                                        <div class="col-sm-6 col-md-4 col-xl mb-5 h-100">
                                            <div class="card card-span h-100 rounded-3 ">
                                                <img class="rounded-3 w-100 h-100 slide-image" src="{{ item.image }}"
                                                    alt="...">
                                                <!-- <div class="card-body ps-0"> -->
                                                <span class="fs-1 text-danger">
                                                    {{ item.dish }}
                                                </span>
                                                <div><span class="text-warning me-2">
                                                        <i class="fas fa-map-marker-alt"></i>
                                                    </span><span class="text-danger" PAN STYLE="font-weight:bold ">{{
                                                        item.location }}</span>
                                                </div><span class="text-1000 fw-bold"></span>
                                                <!-- </div> -->
                                            </div>
                                            <div class="d-grid gap-2">
                                                <a class="btn btn-lg btn-danger" href="{{ item.url_to_dish }}"
                                                    role="button" target="_blank">Visit</a>
                                            </div>
                                        </div>
                                        {% endfor %}
                                    </div>
                                </div>

                                <!-- 3 -->

                                <div class="carousel-item" data-bs-interval="5000">
                                    <div class="row gx-3 h-100 align-items-center">
                                        {% for item in pop3|slice:"0:1" %}
                                        <div class="col-sm-6 col-md-4 col-xl mb-5 h-100">
                                            <div class="card card-span h-100 rounded-3 ">
                                                <img class="rounded-3 w-100 h-100 slide-image" src="{{ item.image }}"
                                                    alt="..." />
                                                <!-- <div class="card-body ps-0"> -->
                                                <span class="fs-1 text-danger">
                                                    {{ item.dish }}
                                                </span>
                                                <div><span class="text-warning me-2">
                                                        <i class="fas fa-map-marker-alt"></i>
                                                    </span><span class="text-danger" PAN STYLE="font-weight:bold ">{{
                                                        item.location }}</span>
                                                </div><span class="text-1000 fw-bold"></span>
                                                <!-- </div> -->
                                            </div>
                                            <div class="d-grid gap-2">
                                                <a class="btn btn-lg btn-danger" href="{{ item.url_to_dish }}"
                                                    role="button" target="_blank">Visit</a>
                                            </div>
                                        </div>
                                        {% endfor %}
                                    </div>
                                </div>

                                <!-- 4 -->

                                <div class="carousel-item">
                                    <div class="row gx-3 h-100 align-items-center">
                                        {% for item in pop4|slice:"0:1" %}
                                        <div class="col-sm-6 col-md-4 col-xl mb-5 h-100">
                                            <div class="card card-span h-100 rounded-3 ">
                                                <img class="rounded-3 w-100 h-100 slide-image" src="{{ item.image }}"
                                                    alt="..." />
                                                <!-- <div class="card-body ps-0"> -->
                                                <span class="fs-1 text-danger">
                                                    {{ item.dish }}
                                                </span>
                                                <div style="padding-bottom: 0 !important;">
                                                    <span class="text-warning me-2">
                                                        <i class="fas fa-map-marker-alt"></i>
                                                    </span>
                                                    <span class="text-danger" PAN STYLE="font-weight:bold ">{{
                                                        item.location }}</span>
                                                </div>
                                                <span class="text-1000 fw-bold"></span>
                                                <!-- </div> -->
                                            </div>
                                            <div class="d-grid gap-2">
                                                <a class="btn btn-lg btn-danger" href="{{ item.url_to_dish }}"
                                                    role="button" target="_blank">Visit</a>
                                            </div>
                                        </div>
                                        {% endfor %}
                                    </div>
                                </div>
                            </div>

                            <!-- END -->

                            <div>
                                <button class="carousel-control-prev carousel-icon" type="button"
                                    data-bs-target="#carouselPopularItems" data-bs-slide="prev">
                                    <span class="carousel-control-prev-icon hover-top-shadow" aria-hidden="true">
                                    </span><span class="visually-hidden">Previous</span>
                                </button>
                                <button class="carousel-control-next carousel-icon" type="button"
                                    data-bs-target="#carouselPopularItems" data-bs-slide="next">
                                    <span class="carousel-control-next-icon hover-top-shadow"
                                        aria-hidden="true"></span><span class="visually-hidden">Next </span>
                                </button>
                            </div>

                        </div>

                    </div>
                </div>
            </div><!-- end of .container-->

        </section>
        <!-- <section> close ============================-->
        <!-- ============================================-->

        <!-- ============================================-->
        <!-- <section> begin ============================-->
        <section id="testimonial pop-top">
            <div class="container">
                <div class="row h-100">
                    <div class="col-lg-7 mx-auto text-center mb-6">
                        <h5 class="fw-bold fs-3 fs-lg-5 lh-sm mb-3">Featured Dish</h5>
                    </div>
                </div>

                <div class="row gx-2">

                    {% for item in f_dish %}

                    <div class="col-sm-6 col-md-4 col-lg-3 h-100 mb-5">
                        <div class="card card-span h-100 text-white rounded-3">
                            <a href="{{ item.url_to_dish }}" target="_blank">
                                <img class="img-fluid rounded-3 h-100" src="{{ item.image }}" alt="..." />
                                <div class="card-img-overlay ps-0">
                                    <span class="badge bg-primary ms-2 me-1 p-2"><i class="fas fa-clock me-1 fs-0"></i>
                                        <span class="fs-0">Availble</span>
                                    </span>
                                </div>
                                <div class="card-body ps-0">
                                    <div class="d-flex align-items-center mb-3">
                                        <img class="img-fluid" src="{{ item.logo }}" alt="" />
                                        <div class="flex-1 ms-3">
                                            <h5 class="mb-0 fw-bold text-1000">{{ item.name }}</h5>
                                        </div>
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>

                    {% endfor %}

                </div>

            </div>
        </section>
        <!-- <section> close ============================-->
        <!-- ============================================-->


        <!-- ============================================-->
        <!-- <section> begin ============================-->
        <section class="py-8 overflow-hidden pop-top-wf">

            <div class="container">
                <div class="row flex-center mb-0">
                    <div class="col-lg-4 text-lg-end text-center mt-0 mb-0">
                        <a class="btn btn-lg text-800 me-2" href="{% url 'search_view' %}" role="button">
                            <span class="fs-1 text-primary">SEE ALL MOST ORDERED</span>
                            <i class="fas fa-chevron-right ms-2"></i></a>
                    </div>
                </div>

                <!-- <div class="row flex-center"> -->
                <!-- <div class="col-12"> -->

                <div class="carousel slide" id="carouselSearchByFood" data-bs-touch="false" data-bs-interval="false">
                    <div class="carousel-inner mt-0">

                        <!-- Part 1 -->

                        <div class="carousel-item active" data-bs-interval="10000">
                            <div class="row h-100 align-items-center">
                                <div class="row h-100 align-items-center">
                                    {% for item in search1|slice:"0:1" %}
                                    <div class="col-sm-6 col-md-4 col-xl mb-5 h-100">
                                        <div class="card card-span h-100 rounded-circle">
                                            <a href="{{ item.url_to_dish }}" target="_blank">
                                                <img class="img-fluid rounded-circle w-100 h-100" src="{{ item.image }}"
                                                    alt="..." />
                                                <div class="card-body ps-0">
                                                    <h5 class="text-center fw-bold text-1000 text-truncate mb-2">
                                                        {{ item.dish }}</h5>
                                                </div>
                                            </a>
                                        </div>
                                    </div>
                                    {% endfor %}
                                </div>
                            </div>
                        </div>

                        <!-- Part 2 -->

                        <div class="carousel-item">
                            <div class="row h-100 align-items-center">
                                {% for item in search2|slice:"0:1" %}
                                <div class="col-sm-6 col-md-4 col-xl mb-5 h-100">
                                    <div class="card card-span h-100 rounded-circle">
                                        <a href="{{ item.url_to_dish }}" target="_blank">
                                            <img class="img-fluid rounded-circle w-100 h-100" src="{{ item.image }}"
                                                alt="..." />
                                            <div class="card-body ps-0">
                                                <h5 class="text-center fw-bold text-1000 text-truncate mb-2">
                                                    {{ item.dish }}</h5>
                                            </div>
                                        </a>
                                    </div>
                                </div>
                                {% endfor %}
                            </div>
                        </div>

                        <!-- Part 3 -->

                        <div class="carousel-item">
                            <div class="row h-100 align-items-center">
                                {% for item in search3|slice:"0:1" %}
                                <div class="col-sm-6 col-md-4 col-xl mb-5 h-100">
                                    <div class="card card-span h-100 rounded-circle">
                                        <a href="{{ item.url_to_dish }}" target="_blank">
                                            <img class="img-fluid rounded-circle w-100 h-100" src="{{ item.image }}"
                                                alt="..." />
                                            <div class="card-body ps-0">
                                                <h5 class="text-center fw-bold text-1000 text-truncate mb-2">
                                                    {{ item.dish }}</h5>
                                            </div>
                                        </a>
                                    </div>
                                </div>
                                {% endfor %}
                            </div>
                        </div>

                        <!-- Part 4 -->

                        <div class="carousel-item">
                            <div class="row h-100 align-items-center">
                                {% for item in search4|slice:"0:1" %}
                                <div class="col-sm-6 col-md-4 col-xl mb-5 h-100">
                                    <div class="card card-span h-100 rounded-circle">
                                        <a href="{{ item.url_to_dish }}" target="_blank">
                                            <img class="img-fluid rounded-circle w-100 h-100" src="{{ item.image }}"
                                                alt="..." />
                                            <div class="card-body ps-0">
                                                <h5 class="text-center fw-bold text-1000 text-truncate mb-2">
                                                    {{ item.dish }}</h5>
                                            </div>
                                        </a>
                                    </div>
                                </div>
                                {% endfor %}
                            </div>
                        </div>

                        <!-- Part 5 -->

                        <div class="carousel-item">
                            <div class="row h-100 align-items-center">
                                {% for item in search5|slice:"0:1" %}
                                <div class="col-sm-6 col-md-4 col-xl mb-5 h-100">
                                    <div class="card card-span h-100 rounded-circle">
                                        <a href="{{ item.url_to_dish }}" target="_blank">
                                            <img class="img-fluid rounded-circle w-100 h-100" src="{{ item.image }}"
                                                alt="..." />
                                            <div class="card-body ps-0">
                                                <h5 class="text-center fw-bold text-1000 text-truncate mb-2">
                                                    {{ item.dish }}</h5>
                                            </div>
                                        </a>
                                    </div>
                                </div>
                                {% endfor %}
                            </div>
                        </div>

                        <div class="col-lg-auto">
                            <button class="carousel-control-prev s-icon-prev carousel-icon" type="button"
                                data-bs-target="#carouselSearchByFood" data-bs-slide="prev"><span
                                    class="carousel-control-prev-icon hover-top-shadow" aria-hidden="true"></span><span
                                    class="visually-hidden">Previous</span></button>
                            <button class="carousel-control-next s-icon-next carousel-icon" type="button"
                                data-bs-target="#carouselSearchByFood" data-bs-slide="next"><span
                                    class="carousel-control-next-icon hover-top-shadow" aria-hidden="true"></span><span
                                    class="visually-hidden">Next</span></button>
                        </div>

                        <!-- END -->

                    </div>
                </div>
                <!-- </div> -->
                <!-- </div> -->
            </div><!-- end of .container-->

        </section>
        <!-- <section> close ============================-->
        <!-- ============================================-->

        <!-- ============================================-->
        <!-- <section> begin ============================-->
        <section class="pb-5 pt-8 pop-top-wf">

            <div class="row h-100">
                <div class="col-lg-7 mx-auto text-center mb-6">
                    <h5 class="fw-bold fs-3 fs-lg-5 lh-sm mb-3">Writer's favourite</h5>
                </div>
            </div>

            <!-- Main 00 -->

            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <div class="card card-span mb-3">
                            <div class="card-body-writer py-0">
                                <div class="row justify-content-center hover-top-shadow">
                                    {% for item in writer %}
                                    <div class="col-md-7 col-xl-5 col-xxl-4 p-4 p-lg-5">
                                        <h1 class="card-title mt-xl-5 mb-4">
                                            <span class="text-primary">{{ item.heading }}</span>
                                        </h1>
                                        <p class="fs-1">
                                            {{ item.writeUp }}
                                        </p>
                                        <h4><span>By {{ item.writer }}</span></h4>
                                        <div class="d-grid bottom-0">
                                            <a class="btn btn-lg btn-primary mt-xl-6"
                                                href="{{ item.url_to_dish }}">Visit spot<i
                                                    class="fas fa-chevron-right ms-2"></i>
                                            </a>
                                        </div>
                                    </div>
                                    {% endfor %}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- end of .container-->

        </section>
        <!-- <section> close ============================-->
        <!-- ============================================-->


        <!-- ============================================-->
        <!-- <section> begin ============================-->



        <!-- section 1 -->

        <section class="py-0">

            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <div class="card card-span mb-3">
                            <div class="card-body py-0">
                                <div class="row justify-content-center hover-top-shadow">
                                    {% for item in chefspot %}
                                    <div class="col-md-5 col-xl-7 col-xxl-8 g-0 order-md-0">
                                        <img class="img-fluid w-100 h-100 rounded" style="object-fit: cover;"
                                            src="{{ item.image }}" alt="..." />
                                    </div>
                                    <div class="col-md-7 col-xl-5 col-xxl-4 p-4 p-lg-5">
                                        <h1 class="card-title mt-xl-5 mb-4">
                                            <span class="text-primary">
                                                {{ item.heading }}
                                            </span>
                                        </h1>
                                        <p class="fs-1">{{ item.writeUp }}</p>
                                        <h4><span>By {{ item.writer }}</span></h4>
                                        <div class="d-grid bottom-0">
                                            <a class="btn btn-lg btn-primary mt-xl-6"
                                                href="{{ item.url_to_dish }}">PROCEED TO ORDER<i
                                                    class="fas fa-chevron-right ms-2"></i>
                                            </a>
                                        </div>
                                    </div>
                                    {% endfor %}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div><!-- end of .container-->

        </section>

        <!-- end of .container-->
        <!-- <section> close ============================-->
        <!-- ============================================-->

        <section class="py-0">

            <div class="bg-holder"
                style="background-image: url('{% static 'desktop/assets/img/gallery/cta-two-bg.png' %}');background-position: center; background-size: cover;">
            </div>

            <!--/.bg-holder-->

            <div class="container">
                <div class="row flex-center">
                    <div class="col-xxl-9 py-7 text-center">
                        <h1 class="fw-bold mb-4 text-white fs-6">
                            SAVE UP TO 50% OFF EVERY TIME YOU EAT OUT
                        </h1>
                        <h1 class="fw-bold mb-4 text-white fs-6">Subscribe for coupuns </h1><a class="btn btn-danger"
                            href="{% url 'subscribe' %}">
                            Subscribe<i class="fas fa-chevron-right ms-2"></i></a>
                    </div>
                </div>
            </div>
        </section>

        <!-- footer -->
        <section class="py-0 pt-7 bg-1000">

            <div class="container">
                <div class="row justify-content-lg-between">

                    <div class="col-6 col-md-4 col-lg-3 col-xxl-2 mb-3">
                        <h5 class="lh-lg fw-bold text-white">About</h5>
                        <ul class="list-unstyled mb-md-4 mb-lg-0">
                            <li class="lh-lg"><a class="text-200 text-decoration-none" href="#!">About Us</a></li>
                        </ul>
                    </div>

                    <div class="col-6 col-md-4 col-lg-3 col-xxl-2 col-lg-3 mb-3">
                        <h5 class="lh-lg fw-bold text-white">CONTACT</h5>
                        <ul class="list-unstyled mb-md-4 mb-lg-0">
                            <li class="lh-lg"><a class="text-200 text-decoration-none" href="#!">Help &amp; Support</a>
                            </li>
                        </ul>
                    </div>

                    <div class="col-6 col-md-4 col-lg-3 col-xxl-2 mb-3">
                        <h5 class="lh-lg fw-bold text-white">LEGAL</h5>
                        <ul class="list-unstyled mb-md-4 mb-lg-0">
                            <li class="lh-lg"><a class="text-200 text-decoration-none" href="#!">Terms &amp;
                                    Conditions</a></li>
                        </ul>
                    </div>

                    <div class="col-6 col-md-4 col-lg-3 col-xxl-2 mb-3">
                        <h5 class="lh-lg fw-bold text-white">Others</h5>
                        <ul class="list-unstyled mb-md-4 mb-lg-0">
                            <li class="lh-lg"><a class="text-200 text-decoration-none" href="#!">Affilate &amp;
                                    referal</a></li>
                        </ul>
                    </div>

                    <div class="col-6 col-md-4 col-lg-3 col-xxl-2 mb-3">
                        <h5 class="lh-lg fw-bold text-500">FOLLOW US</h5>
                        <div class="text-start my-3">

                            <a href="#!">
                                <svg class="svg-inline--fa fa-instagram fa-w-14 fs-2 me-2" aria-hidden="true"
                                    focusable="false" data-prefix="fab" data-icon="instagram" role="img"
                                    viewBox="0 0 448 512">
                                    <path fill="#BDBDBD"
                                        d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z">
                                    </path>
                                </svg>
                            </a>

                            <a href="#!">
                                <svg class="svg-inline--fa fa-facebook fa-w-16 fs-2 mx-2" aria-hidden="true"
                                    focusable="false" data-prefix="fab" data-icon="facebook" role="img"
                                    viewBox="0 0 512 512">
                                    <path fill="#BDBDBD"
                                        d="M504 256C504 119 393 8 256 8S8 119 8 256c0 123.78 90.69 226.38 209.25 245V327.69h-63V256h63v-54.64c0-62.15 37-96.48 93.67-96.48 27.14 0 55.52 4.84 55.52 4.84v61h-31.28c-30.8 0-40.41 19.12-40.41 38.73V256h68.78l-11 71.69h-57.78V501C413.31 482.38 504 379.78 504 256z">
                                    </path>
                                </svg>
                            </a>

                            <a href="#!">
                                <svg class="svg-inline--fa fa-twitter fa-w-16 fs-2 mx-2" aria-hidden="true"
                                    focusable="false" data-prefix="fab" data-icon="twitter" role="img"
                                    viewBox="0 0 512 512">
                                    <path fill="#BDBDBD"
                                        d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z">
                                    </path>
                                </svg>
                            </a>

                        </div>
                    </div>
                </div>
            </div>

        </section>

    </main>
    <!-- ===============================================-->
    <!--    End of Main Content-->
    <!-- ===============================================-->



    <!-- ===============================================-->
    <!--    JavaScripts-->
    <!-- ===============================================-->

    <script src="{% static 'mobile/vendors/@popperjs/popper.min.js' %}"></script>
    <script src="{% static 'mobile/vendors/bootstrap/bootstrap.min.js' %}"></script>
    <script src="{% static 'mobile/vendors/is/is.min.js' %}"></script>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=window.scroll"></script>
    <script src="{% static 'mobile/vendors/fontawesome/all.min.js' %}"></script>
    <script src="{% static 'mobile/assets/js/theme.js' %}"></script>

    <a href="#" id="back-to-top" title="Back to top" style="display: none;">&uarr;</a>

    <script src="{% static 'mobile/js/jquery-3.2.1.min.js' %}"></script>
    <script src="{% static 'mobile/js/popper.min.js' %}"></script>
    <script src="{% static 'mobile/js/bootstrap.min.js' %}"></script>

    <!-- ALL PLUGINS -->
    <script src="{% static 'mobile/js/jquery.superslides.min.js' %}"></script>
    <script src="{% static 'mobile/js/images-loded.min.js' %}"></script>
    <script src="{% static 'mobile/js/isotope.min.js' %}"></script>
    <script src="{% static 'mobile/js/baguetteBox.min.js' %}"></script>
    <script src="{% static 'mobile/js/form-validator.min.js' %}"></script>
    <script src="{% static 'mobile/js/contact-form-script.js' %}"></script>
    <script src="{% static 'mobile/js/custom.js' %}"></script>

    <input type="hidden" id="screen-size-input" name="screen_size" value="">
    <script>
        // Get screen width
        const screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

        // Determine screen size and set the value of the hidden input
        const screenSizeInput = document.getElementById('screen-size-input');
        if (screenWidth < 768) {  // Example breakpoint for small screens (adjust as needed)
            screenSizeInput.value = 'small';
        } else {
            screenSizeInput.value = 'normal';
        }
    </script>


</body>

</html>