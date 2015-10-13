HTTP/1.1 200 OK
Date: Tue, 06 Oct 2015 18:26:48 GMT
Server: Apache/2.2.22 (Ubuntu) mod_fcgid/2.3.6 mod_ssl/2.2.22 OpenSSL/1.0.1
Last-Modified: Fri, 18 Jun 2010 15:04:18 GMT
ETag: "1a298c-2b6-4894f44e32080"
Accept-Ranges: bytes
Content-Length: 694
Content-Type: application/javascript

// $Id: views_nivo_slider.js,v 1.1.2.5.2.2 2010/06/18 15:04:17 pedrofaria Exp $ 
Drupal.behaviors.views_nivo_sliderBehavior = function (context) {
  $('.views-nivo-slider').each(function() {
    var id = $(this).attr('id');
    var vns = $(this);
    var cfg = Drupal.settings.views_nivo_slider[id];

    // Fix sizes
    vns.data('hmax', 0).data('wmax', 0);
    $('img', vns).each(function () {
      hmax =  (vns.data('hmax') > $(this).height()) ? vns.data('hmax') : $(this).height();
      wmax =  (vns.data('wmax') > $(this).width()) ? vns.data('hmax') : $(this).width();

      vns.width(wmax).height(hmax).data('hmax', hmax).data('wmax', wmax);
    });

    vns.nivoSlider(cfg);
  });
};
// $Id: views_nivo_slider.js,v 1.1.2.5.2.2 2010/06/18 15:04:17 pedrofaria Exp $ 
Drupal.behaviors.views_nivo_sliderBehavior = function (context) {
  $('.views-nivo-slider').each(function() {
    var id = $(this).attr('id');
    var vns = $(this);
    var cfg = Drupal.settings.views_nivo_slider[id];

    // Fix sizes
    vns.data('hmax', 0).data('wmax', 0);
    $('img', vns).each(function () {
      hmax =  (vns.data('hmax') > $(this).height()) ? vns.data('hmax') : $(this).height();
      wmax =  (vns.data('wmax') > $(this).width()) ? vns.data('hmax') : $(this).width();

      vns.width(wmax).height(hmax).data('hmax', hmax).data('wmax', wmax);
    });

    vns.nivoSlider(cfg);
  });
};
