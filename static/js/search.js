(function($){

  'use strict';

  $(document).ready(function(){
    var showResults = function(results){
      //console.log(results);
      for(var i in results){
        var result = results[i];
        var el = $($("#result-template").html());
        //console.log($("#result-template").html());
        el.find(".organization").html(result["organization"]);
        el.find(".office-description").html(result["description"]);
        el.find(".office-name").html(result["officeName"]);
        el.find(".address-line1").html(result["address1"]);
        el.find(".address-line2").html(result["address2"]);
        el.find(".city").html(result["city"]);
        el.find(".state").html(result["state"]);
        el.find(".zipcode").html(result["zipcode"]);
        el.find(".country").html(result["country"]);
        //console.log(result.contacts);
        if(result.contacts){
          for(var j in result.contacts){
            var contact = result.contacts[j];
            el.find(".office-phone").html("<span>" + contact.contact_type + "</span><br><span>" +
                                          contact.phone + "</span>");
          }
        }
        if(result.mails){
          for(var k in result.mails){
            var mail = result.mails[k];
            el.find(".office-email").html("<span>" + mail.description +"</span><br><span>" + mail.email + "</span>");
          }
        }

        $("#result-box").append(el);

      }
    };

    var resultNotFound = function(){

      var empty = $("#result-not-found").show().html("Your search does not match with any of the organizations. <br> <b>Please make sure you have typed it correctly</b>");

    };

    var showLoader = function(show){
      if(show == true){
        $("#loading").show();
      }
      else {
        $("#loading").hide();
      }
    };
    var searchOffices = function(){
      $("#result-box").html("");
      $("#result-not-found").html("");
      $.get("/office/search/",{
        org : $("#search-b").val(),
        city : $("#city-search").val()
      },function(data){

        showLoader(false);
        var results = data['results'];
        if (typeof results !== 'undefined' && results.length > 0){
          showResults(results);
        }
        else{
          resultNotFound();
        }
      })
        .fail(function(){
          alert('Network ERROR !! Check your internet connection!');
          showLoader(false);
        }
             );

    };

    $(".search-text").keypress(function(){
      $("#error-line").hide();
    });

    $("#search-btn").click(function(){
      if($("#search-b").val()==""){
        $("#error-line").show().html("*Enter the organization name.");

      }
      else{
        searchOffices();
        showLoader(true);

      }

    });

    $(".search-text").keypress(function(e){
      if(e.keyCode == 13){
        $(".search-btn").click();
      }

    });

  });

})($);
