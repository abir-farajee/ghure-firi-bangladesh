(function($) {
    "use strict";
    $('.select').niceSelect();

    function bgParallax() {
        if ($(".parallax").length) {
            $(".parallax").each(function() {
                var height = $(this).position().top;
                var resize = height - $(window).scrollTop();
                var doParallax = -(resize / 5);
                var positionValue = doParallax + "px";
                var img = $(this).data("bg-image");
                $(this).css({ backgroundImage: "url(" + img + ")", backgroundPosition: "50%" + positionValue, backgroundSize: "cover" });
            });
        }
    }

    function sliderBgSetting() {
        if ($(".hero-slider .slide").length) {
            $(".hero-slider .slide").each(function() {
                var $this = $(this);
                var img = $this.find(".slider-bg").attr("src");
                $this.css({ backgroundImage: "url(" + img + ")", backgroundSize: "cover", backgroundPosition: "center center" })
            });
        }
    }

    function heroSlider() { if ($(".hero-slider").length) { $(".hero-slider").slick({ autoplay: true, autoplaySpeed: 6000, pauseOnHover: true, arrows: true, prevArrow: '<button type="button" class="slick-prev">Previous</button>', nextArrow: '<button type="button" class="slick-next">Next</button>', dots: false, fade: true, cssEase: 'linear' }); } }
    $(window).on('scroll', function() {
        var scroll = $(window).scrollTop(),
            mainHeader = $('#sticky-header'),
            mainHeaderHeight = mainHeader.innerHeight();
        if (scroll > 1) { $("#sticky-header").addClass("sticky"); } else { $("#sticky-header").removeClass("sticky"); }
    });

    function pageLoader() { if ($('.page-loader').length) { $('.page-loader').delay(100).fadeOut(500, function() { heroSlider(); }); } }
    $('.main-menu .nav_mobile_menu').slicknav({ label: '', duration: 1000, easingOpen: "easeOutBounce", prependTo: '.mobile_menu' });
    var wow = new WOW({ boxClass: 'wow', animateClass: 'animated', offset: 0, mobile: true, live: true });
    if ($("#contact-form").length) {
        $("#contact-form").validate({
            rules: { name: { required: true, minlength: 2 }, fname: "required", lname: "required", subject: "required", email: "required", address: "required", },
            messages: { fname: "Please enter your First name", lname: "Please enter your Last name", subject: "Please enter your Subject", email: "Please enter your email address", address: "Please enter your address", },
            submitHandler: function(form) {
                $.ajax({
                    type: "POST",
                    url: "mail.php",
                    data: $(form).serialize(),
                    success: function() {
                        $("#loader").hide();
                        $("#success").slideDown("slow");
                        setTimeout(function() { $("#success").slideUp("slow"); }, 3000);
                        form.reset();
                    },
                    error: function() {
                        $("#loader").hide();
                        $("#error").slideDown("slow");
                        setTimeout(function() { $("#error").slideUp("slow"); }, 3000);
                    }
                });
                return false;
            }
        });
    }

    function cloneNavForSticyMenu($ele, $newElmClass) { $ele.addClass('original').clone().insertAfter($ele).addClass($newElmClass).removeClass('original'); }
    if ($('.site-header .navigation').length) { cloneNavForSticyMenu($('.site-header .navigation'), "sticky-header"); }
    var lastScrollTop = '';

    function stickyMenu($targetMenu, $toggleClass) {
        var st = $(window).scrollTop();
        var mainMenuTop = $('.site-header .navigation');
        if ($(window).scrollTop() > 1000) { if (st > lastScrollTop) { $targetMenu.removeClass($toggleClass); } else { $targetMenu.addClass($toggleClass); } } else { $targetMenu.removeClass($toggleClass); }
        lastScrollTop = st;
    }
    $(window).on("scroll", function() { toggleBackToTopBtn(); });
    $(window).on('load', function() {
        pageLoader();
        sliderBgSetting();
        sortingGallery();
    });

    function testimonial_carousel() {
        var owl = $(".testimonial-slider2");
        owl.owlCarousel({ loop: true, margin: 30, nav: false, items: 5, smartSpeed: 2000, dots: true, autoplay: false, autoplayTimeout: 5000, responsive: { 0: { items: 1 }, 480: { items: 1 }, 760: { items: 2 }, 1080: { items: 2 } } });
    }
    testimonial_carousel();
    $(document).ready(function() { $('.team-active ').owlCarousel({ loop: true, margin: 30, autoplay: false, smartSpeed: 1500, mouseDrag: true, navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'], nav: true, responsive: { 0: { items: 1 }, 600: { items: 1 }, 1000: { items: 1 } } }); });

    function gift_carousel() {
        var owl = $(".Gift-carousel");
        owl.owlCarousel({ loop: true, margin: 0, navText: false, nav: false, items: 5, smartSpeed: 1000, dots: false, autoplay: false, autoplayTimeout: 3000, responsive: { 0: { items: 3 }, 480: { items: 2 }, 760: { items: 4 }, 1080: { items: 6 } } });
    }
    gift_carousel();
    if ($(".odometer").length) {
        $('.odometer').appear();
        $(document.body).on('appear', '.odometer', function(e) {
            var odo = $(".odometer");
            odo.each(function() {
                var countNumber = $(this).attr("data-count");
                $(this).html(countNumber);
            });
        });
    }
    $("body").append("<a href='#' class='back-to-top'><i class='fa fa-angle-up'></i></a>");

    function toggleBackToTopBtn() { var amountScrolled = 1000; if ($(window).scrollTop() > amountScrolled) { $("a.back-to-top").fadeIn("slow"); } else { $("a.back-to-top").fadeOut("slow"); } }
    $(".back-to-top").on("click", function() { $("html,body").animate({ scrollTop: 0 }, 700); return false; })
    if ($(".fancybox").length) { $(".fancybox").fancybox({ openEffect: "elastic", closeEffect: "elastic", wrapCSS: "project-fancybox-title-style" }); }
    if ($(".video-play-btn").length) { $(".video-play-btn").on("click", function() { $.fancybox({ href: this.href, type: $(this).data("type"), 'title': this.title, helpers: { title: { type: 'inside' }, media: {} }, beforeShow: function() { $(".fancybox-wrap").addClass("gallery-fancybox"); } }); return false }); }
    $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({ type: 'iframe', mainClass: 'mfp-fade', removalDelay: 160, preloader: false, fixedContentPos: false });
    if ($(".popup-image").length) { $('.popup-image').magnificPopup({ type: 'image', zoom: { enabled: true, duration: 300, easing: 'ease-in-out', opener: function(openerElement) { return openerElement.is('img') ? openerElement : openerElement.find('img'); } } }); }
    if ($(".popup-gallery").length) { $('.popup-gallery').magnificPopup({ delegate: 'a', type: 'image', gallery: { enabled: true }, zoom: { enabled: true, duration: 300, easing: 'ease-in-out', opener: function(openerElement) { return openerElement.is('img') ? openerElement : openerElement.find('img'); } } }); }

    function sortingGallery() {
        if ($(".sortable-gallery .gallery-filters").length) {
            var $container = $('.gallery-container');
            $container.isotope({ filter: '*', animationOptions: { duration: 750, easing: 'linear', queue: false, } });
            $(".gallery-filters li a").on("click", function() {
                $('.gallery-filters li .current').removeClass('current');
                $(this).addClass('current');
                var selector = $(this).attr('data-filter');
                $container.isotope({ filter: selector, animationOptions: { duration: 750, easing: 'linear', queue: false, } });
                return false;
            });
        }
    }
    sortingGallery();
    if ($(".country-carousel".length)) { $(".country-carousel").owlCarousel({ loop: !0, autoplaySpeed: 3e3, navSpeed: 3e3, paginationSpeed: 3e3, slideSpeed: 3e3, smartSpeed: 3e3, autoplay: false, margin: 30, nav: true, navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'], dots: !1, responsive: { 0: { items: 1 }, 480: { items: 1 }, 600: { items: 1 }, 1024: { items: 2 }, 1200: { items: 2 } }, }); }
    if ($(".populer-carousel".length)) { $(".populer-carousel").owlCarousel({ loop: !0, autoplaySpeed: 3e3, navSpeed: 3e3, paginationSpeed: 3e3, slideSpeed: 3e3, smartSpeed: 3e3, autoplay: false, margin: 30, nav: true, navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'], dots: !1, responsive: { 0: { items: 1 }, 480: { items: 1 }, 600: { items: 2 }, 1024: { items: 2 }, 1200: { items: 3 } }, }); }
    if ($(".deals-carousel".length)) { $(".deals-carousel").owlCarousel({ loop: !0, autoplaySpeed: 3e3, navSpeed: 3e3, paginationSpeed: 3e3, slideSpeed: 3e3, smartSpeed: 3e3, autoplay: false, margin: 30, nav: true, navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'], dots: !1, responsive: { 0: { items: 1 }, 480: { items: 1 }, 600: { items: 1 }, 1024: { items: 1 }, 1200: { items: 1 } }, }); }
    if ($(".testimonial-slider".length)) { $(".testimonial-slider").owlCarousel({ loop: !0, autoplaySpeed: 3e3, navSpeed: 3e3, paginationSpeed: 3e3, slideSpeed: 3e3, smartSpeed: 3e3, autoplay: false, margin: 30, nav: true, navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'], dots: !1, responsive: { 0: { items: 1 }, 480: { items: 1 }, 600: { items: 2 }, 1024: { items: 2 }, 1200: { items: 2 }, 1500: { items: 3 } }, }); }

    function masonryGridSetting() {
        if ($('.masonry-gallery').length) {
            var $grid = $('.masonry-gallery').masonry({ itemSelector: '.grid-item', columnWidth: '.grid-item', percentPosition: true });
            $grid.imagesLoaded().progress(function() { $grid.masonry('layout'); });
        }
    }
    $(document).on('click', function(event) { if (!$(event.target).closest('.map-wrapper').length) { $('.map-wrapper').removeClass('open'); } });
    $("#slider-range").slider({ range: true, min: 1000, max: 50000, values: [0, 100], slide: function(event, ui) { $("#amount").val(ui.values[1]); } });
    $("#amount").val("TK" + $("#slider-range").slider("values", 0) +
        " - $" + $("#slider-range").slider("values", 1));
    $("#slider-range2").slider({ range: true, min: 1000, max: 50000, values: [1000, 50000], slide: function(event, ui) { $("#amount2").val("KM" + ui.values[0] + " - KM" + ui.values[1]); } });
    $("#amount2").val("KM" + $("#slider-range2").slider("values", 0) +
        " - KM" + $("#slider-range2").slider("values", 1));
    $(document).ready(function() { $("#date").datepicker(); });
    $(".cart-plus-minus").append('<div class="dec qtybutton">-</div><div class="inc qtybutton">+</div>');
    $(".qtybutton").on("click", function() {
        var $button = $(this);
        var oldValue = $button.parent().find("input").val();
        if ($button.text() == "+") { var newVal = parseFloat(oldValue) + 1; } else { if (oldValue > 0) { var newVal = parseFloat(oldValue) - 1; } else { newVal = 0; } }
        $button.parent().find("input").val(newVal);
    });
})(window.jQuery);