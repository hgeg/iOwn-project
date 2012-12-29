$(document).ready(function(){
	setelementheight = function() { 
		$('.equpi-friends-element').each(function(i) {
			var h = $(this).width() * 0.30;
			$(this).height(h);
			$(this).css('margin-top', '12px');
		});	
	}

	setelementheight();
	$('.equpi-friends-element').hide();
	$('.equpi-friends-element').each(function(i) {
		$(this).delay(i*500).fadeIn(500);
	});

	

	

	$(window).resize(setelementheight);
});