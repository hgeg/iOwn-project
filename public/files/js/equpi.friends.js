$(document).ready(function(){
	$(".equpi-friends-element").hover(function() {
		
		$(this).animate({
			left: '1%'
		}, 100);
		$(".equpi-friends-previewimage").stop(true, true);

		var hoveredFriend = $(this);
		var hoveredFriendPreview = hoveredFriend.children(".equpi-friends-details").children(".equpi-friends-preview");

		hoveredFriendPreview.children().each(function(i) {
			$(this).delay(1000*i).fadeIn(1000);
		});
	}, function() {
		$("*").stop();
		$(this).animate({
			left: '0%'
		}, 100);
		
		
		var hoveredFriend = $(this);
		var hoveredFriendPreview = hoveredFriend.children(".equpi-friends-details").children(".equpi-friends-preview");
		$(".equpi-friends-previewimage").not(hoveredFriendPreview.children()).stop(true, true).fadeOut();
		hoveredFriendPreview.children().stop(true, true).fadeOut();
	});
});