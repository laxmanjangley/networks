HTTP/1.1 200 OK
Date: Mon, 05 Oct 2015 19:29:17 GMT
Server: Apache/2.2.22 (Ubuntu) mod_fcgid/2.3.6 mod_ssl/2.2.22 OpenSSL/1.0.1
Last-Modified: Mon, 05 Oct 2009 22:40:36 GMT
ETag: "1a2046-31d-47537cd5e4100"
Accept-Ranges: bytes
Content-Length: 797
Content-Type: application/javascript

// $Id: panels.js,v 1.2.4.1 2009/10/05 22:40:35 merlinofchaos Exp $

(function ($) {
  Drupal.Panels = {};

  Drupal.Panels.autoAttach = function() {
    if ($.browser.msie) {
      // If IE, attach a hover event so we can see our admin links.
      $("div.panel-pane").hover(
        function() {
          $('div.panel-hide', this).addClass("panel-hide-hover"); return true;
        },
        function() {
          $('div.panel-hide', this).removeClass("panel-hide-hover"); return true;
        }
      );
      $("div.admin-links").hover(
        function() {
          $(this).addClass("admin-links-hover"); return true;
        },
        function(){
          $(this).removeClass("admin-links-hover"); return true;
        }
      );
    }
  };

  $(Drupal.Panels.autoAttach);
})(jQuery);
HTTP/1.1 400 Bad Request
Date: Mon, 05 Oct 2015 19:29:17 GMT
Server: Apache/2.2.22 (Ubuntu) mod_fcgid/2.3.6 mod_ssl/2.2.22 OpenSSL/1.0.1
Vary: Accept-Encoding
Content-Length: 354
Connection: close
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>400 Bad Request</title>
</head><body>
<h1>Bad Request</h1>
<p>Your browser sent a request that this server could not understand.<br />
</p>
<hr>
<address>Apache/2.2.22 (Ubuntu) mod_fcgid/2.3.6 mod_ssl/2.2.22 OpenSSL/1.0.1 Server at www.iitd.ernet.in Port 80</address>
</body></html>
