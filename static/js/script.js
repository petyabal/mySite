$(".click_me_to_hide").click(function(){
      $(".filterField").hide(); // Для скрытия
      $(".click_me_to_show").show();
    });

    $(".click_me_to_show").click(function(){
      $(".filterField").show(); // Для отображения
      $(".click_me_to_show").hide();
    });

    $(".audienceValue").click(function(){
      if ($(".audienceList").is(':hidden')) {
        $(".audienceList").show();
        $(".audienceValue").css("background-color", "rgba(255,0,0,0.3)");
        }
      else {
        $(".audienceList").hide();
        $(".audienceValue").css("background-color", "rgba(255,0,0,0)");
      }
    });

    $(".adminsNumber").click(function(){
      if ($(".adminsList").is(':hidden')) {
        $(".adminsList").show();
        $(".adminsNumber").css("background-color", "rgba(0,192,128,0.3)");
      }
      else {
        $(".adminsList").hide();
        $(".adminsNumber").css("background-color", "rgba(0,192,128,0)");
      }
    });

    $(".votingResultNegative").click(function(){
      if ($(".negativeMarks").is(':hidden')) {
        $(".negativeMarks").show();
        $(".votingResultNegative").css("background-color",  "rgba(255,0,0,0.3)");
        $(".positiveMarks").hide();
        $(".votingResultPositive").css("background-color", "rgba(0,255,0,0)");
      }
      else {
        $(".negativeMarks").hide();
        $(".votingResultNegative").css("background-color", "rgba(255,0,0,0)");
      }
    });

    $(".votingResultPositive").click(function(){
      if ($(".positiveMarks").is(':hidden')) {
        $(".positiveMarks").show();
        $(".votingResultPositive").css("background-color",  "rgba(0,192,128,0.3)");
        $(".negativeMarks").hide();
        $(".votingResultNegative").css("background-color", "rgba(255,0,0,0)");
      }
      else {
        $(".positiveMarks").hide();
        $(".votingResultPositive").css("background-color", "rgba(0,192,128,0)");
      }
    });