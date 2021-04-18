document.addEventListener('DOMContentLoaded', function(){
	var arrayImgSrc = [
		"static/main/img/slider/1.jpg","static/main/img/slider/2.jpg","static/main/img/slider/3.jpg",
		"static/main/img/slider/4.jpg","static/main/img/slider/5.jpg","static/main/img/slider/6.jpg",
		"static/main/img/slider/7.jpg","static/main/img/slider/8.jpg","static/main/img/slider/9.jpg",
	    "static/main/img/slider/10.jpg"
	];

    for(var i = 0; i < arrayImgSrc.length; i++){
        var dot = document.createElement("span");
        dot.className = "dot";
        var dot_container=document.querySelector('.dot-container');
        dot_container.append(dot);
    }


	var slideIndex =0;
	showSlides(slideIndex);
	
	function ButtonLeft(){
		slideIndex--;
		showSlides(slideIndex);
	};
	
	function ButtonRight(){
			slideIndex++;
			showSlides(slideIndex);
	};
	
	var BL = document.querySelector('.slideshow-container .ButtonSliderLeft');
	BL.onclick = ButtonLeft;
	
	var BR = document.querySelector('.slideshow-container .ButtonSliderRight');
	BR.onclick = ButtonRight;

	var timerId = setInterval(ButtonRight,4000);

    var alldots = document.querySelectorAll('.dot');

    for(let i = 0; i < alldots.length; i++){
        var thisdot = alldots[i];
        thisdot.addEventListener('click', func);
        function func(event){
            ///console.log("hi"+i);
            slideIndex=i;
			showSlides(slideIndex);
        }
    }

	function showSlides(n) {
        var dots = document.getElementsByClassName("dot");
		if (slideIndex < 0){
			slideIndex += arrayImgSrc.length;
		}
		if (slideIndex >= arrayImgSrc.length){
			slideIndex -= arrayImgSrc.length;
		}
		for(var i = 0; i < dots.length; i++){
			dots[i].className = dots[i].className.replace("active","");
		}

		dots[slideIndex].className+= " active";

		var url = arrayImgSrc[slideIndex];
		document.querySelector('.visible-image').setAttribute('src', url);
	}
});