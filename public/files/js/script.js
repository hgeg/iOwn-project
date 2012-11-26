
$(document).ready(function(){


		<!--ImageGrid Script-->
		
		$(function() {
			
				$( '#ri-grid' ).gridrotator( {
					rows		: 3,
					columns		: 15,
					animType	: 'fadeInOut',
					animSpeed	: 1000,
					interval	: 600,
					step		: 1,
					w320		: {
						rows	: 3,
						columns	: 4
					},
					w240		: {
						rows	: 3,
						columns	: 4
					}
				} );
			
			});
			
			
		<!--Form Script-->	

	$('#subscribe').submit(function() {
	$.ajax({
		url: 'inc/newsletter.php',
		data: 'ajax=true&email=' + escape($('#email').val()),
		success: function(data) {
			var data = jQuery.parseJSON(data);
			if (data.success == 1) {
				alertMessage(data.message, 'success');
				$('#subscribe-submit').addClass('btn-green').val($('#subscribe-submit').data('done'));
			}
			else {
				alertMessage(data.message, 'error');
			}
		}
	});
	return false;
});

function alertMessage(message, type) {
	$bar = $('#alertbar');
	if ($bar.length) {
		$bar.animate({
			top: '-45px'
		}, 150, 'easeOutQuad', function() {
			$bar.removeAttr('class').addClass(type).find('.message').html(message);
			$bar.animate({
				top: 0
			}, 500, 'easeOutBounce')
		});
	}
	else {
		$('body').prepend('<div id="alertbar" class="' + type + '"><span class="message">' + message + '</span><span class="close">&times;</span></div>');
		$('#alertbar').show().animate({
			top: 0
		}, 500, 'easeOutBounce');
	}
}

$('body').on('click', '.close', function() {
	$(this).closest('#alertbar').animate({
		top: '-45px'
	}, 500, 'easeOutExpo', function() {
		$(this).remove();
	});
});
