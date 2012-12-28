$(document).ready(function(){
	var selectedElement = null;
	$(".equpi-belongingsElement-detailsbox").hide(0);
	$(".equpi-belongingsElement-controlCol").hide(0);
	
	$(".equpi-belongingsElement").click(function() {
		if (selectedElement == null || $(this).get(0) != selectedElement.get(0)) {
			selectedElement = $(this);
			var selectedElementControlCol = $(this).children(".equpi-belongingsElement-controlCol");
			var selectedElementMainCol = $(this).children(".equpi-belongingsElement-mainCol");
			var selectedCategory = $(this).parent();
			var otherElementsInSelectedCategory = $(this).siblings();

			var otherCategories = $(".equpi-belongingsCategory").not(selectedCategory);
			var otherElementsInOtherCategories = otherCategories.children();

			//Shrink all other Categories
			otherCategories.animate({
				width: '14%'
			}, 200);
			//Grow the selected Category 
			selectedCategory.animate({
				width: '20%'
			}, 200);
			//Shrink and Grow Elements
			selectedElement.animate({
				width: '96%'
			}, 200);
			otherElementsInSelectedCategory.animate({
				width: '72%'
			}, 200);
			otherElementsInOtherCategories.animate({
				width: '96%'
			}, 200);

			//Shrink and Grow MainCol
			selectedElementMainCol.animate({
				width: '75%'
			}, 200);
			$(".equpi-belongingsElement-mainCol").not(selectedElementMainCol).animate({
				width: '100%'
			}, 200);

			//Hide and Show ControlCol
			selectedElementControlCol.show(200);
			$(".equpi-belongingsElement-controlCol").not(selectedElementControlCol).hide(200);

			
			selectedElement.addClass("equpi-belonging-hover");
			otherElementsInSelectedCategory.removeClass("equpi-belonging-hover");
			otherElementsInOtherCategories.removeClass("equpi-belonging-hover");




			selectedElementMainCol.children(".equpi-belongingsElement-detailsbox").show(200);
			otherElementsInSelectedCategory.children(".equpi-belongingsElement-mainCol").children(".equpi-belongingsElement-detailsbox").hide(200);
			otherElementsInOtherCategories.children(".equpi-belongingsElement-mainCol").children(".equpi-belongingsElement-detailsbox").hide(200);
		}
	});
});


