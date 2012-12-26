$(document).ready(function(){
	$(".equpi-belongingsElement-detailsbox").animate({
		height: 'toggle'
	}, 0);
	
	$(".equpi-belongingsElement").hover(function() {
		$(this).addClass("equpi-belonging-hover");
		$(this).children(".equpi-belongingsElement-detailsbox").animate({
			height: 'toggle'
		}, 100);
	}, function() {
		$(this).removeClass("equpi-belonging-hover");
		$(this).children(".equpi-belongingsElement-detailsbox").animate({
			height: 'toggle'
		}, 100);
		
	});
});


