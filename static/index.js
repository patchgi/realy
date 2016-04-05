;(function(window, $) {
  'use strict';
  $('#result-container').hide();
    var requestReal=function(data){
      $.post('/realy',data).done(function(res){
        $('#result-text').show();
        $('#result-text').html(res.replace(/\n/g,'<br/>'));
        $('#progressbar').hide();

        var url = "https://twitter.com/intent/tweet?text=" + res + ' #realy';
        while ( url.indexOf("#",0) != -1 ){
          url=url.replace("#","%23");
        }
        $("#share-container").empty().append( '<a class="twitter-share-button" href="' + url + '" data-size="large"> <span class="label" id="l">Tweet</span></a>' );
      });
    };

    $("#real-btn").click(function(){
        $('#result-text').hide();
        $('#result-container').show();
        $('#progressbar').show();
        var data = { text: $('#textarea').val() };
        requestReal(data)
    })

})(this, jQuery);
