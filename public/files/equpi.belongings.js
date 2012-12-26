$(document).ready(function(){
	$(".equpi-belongingsElement-lovebox").hide();
	
	$(".equpi-belongingsElement").hover(function() {
		$(this).children(".equpi-belongingsElement-lovebox").height($(this).width() * 0.1);
		$(this).children(".equpi-belongingsElement-lovebox").css("font", 
			(""+($(this).children(".equpi-belongingsElement-lovebox").height() / 1.5)+" sans-serif"));
		$(this).children(".equpi-belongingsElement-lovebox").css("top", 
			(($(this).height() * 0.04) + 7));
  	$(this).addClass("equpi-belonging-hover");
		$(this).children(".equpi-belongingsElement-lovebox").show();
	}, function() {
  	$(this).removeClass("equpi-belonging-hover");
  	$(this).children(".equpi-belongingsElement-lovebox").hide();
	});	
});


