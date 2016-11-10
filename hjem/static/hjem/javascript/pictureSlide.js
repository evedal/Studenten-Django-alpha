/**
 * Created by Evdal on 03.09.2016.
 */
$(document).ready(function(){
	pictureslide();
	var width = $(".pictureCont").width();
	function pictureslide(){
		$('.picturelink').first().addClass('activepicture');
		$('.navbutton').first().addClass('activebutton');
		var position = 0;
		$('.navbutton').click(function(){
			var $this = $(this),
				$siblings = $this.parent().children();
			position = $siblings.index($this);

			$('.picturelink').removeClass('activepicture').eq(position).addClass('activepicture');
			$('.navbutton').removeClass('activebutton').eq(position).addClass('activebutton');
			$('.pictureslide').css('left', (position*-width)+'px');

		});
		$('.arrowrigth').click(function(){
			if (position == 3) {
				position = 0;
				$('.navbutton').removeClass('activebutton').first().addClass('activebutton');
				$('.pictureslide').css('left', '0px');
			}
			else{
				position += 1;
				$('.activebutton').removeClass('activebutton').next().addClass('activebutton');
				$('.pictureslide').css('left', (position*-width)+'px');
			}
		});
    	$('.arrowleft').click(function(){
			if (position == 0) {
				position = 3;
				$('.navbutton').removeClass('activebutton').last().addClass('activebutton');
				$('.pictureslide').css('left', '-'+width*3+'px');
			}
			else{
				position -= 1;
				$('.activebutton').removeClass('activebutton').prev().addClass('activebutton');
				$('.pictureslide').css('left', (position*-width)+'px');
			}
    	});
    	setInterval(function(){
			if (position == 3) {
				position = 0;
				$('.navbutton').removeClass('activebutton').first().addClass('activebutton');
				$('.pictureslide').css('left', '0px');
			}
			else{
				position += 1;
				$('.activebutton').removeClass('activebutton').next().addClass('activebutton');
				$('.pictureslide').css('left', (position*-width)+'px');
			}
    	}, 1000000000);
	};
});