$(document).ready(function(){
	$("#i").click(function(){
		// $(".visible").hide(2280);
		$(".visible").fadeOut(2280);
	});
	$("#i2").click(function(){
		$(".visible").fadeIn();
	});
	// alert("Астарожно, АМИН!");
	$("#i3").click(function(){
		$(".visible").toggle(228);
	});
	$(".ddd").mouseenter(function(){
		$(this).animate({
			left:"+=200",
			
			width:"228px",
		},2000).text("ДУДЕЦ");
	});

});