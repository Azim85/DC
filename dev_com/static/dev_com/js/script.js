$('.panel-collapse').on('show.bs.collapse', function () {
    $(this).siblings('.panel-heading').addClass('active');
  });

  $('.panel-collapse').on('hide.bs.collapse', function () {
    $(this).siblings('.panel-heading').removeClass('active');
  });



  $(document).ready(function(){
    $("a.nav-link").click(function(){
      $("html, body").animate({
        scrollTop: $($(this).attr("href")).offset().top + "px"
      }, { duration:1000,
        easing: "swing" 
      });
      return false;
    });
  });