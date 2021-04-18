document.addEventListener('DOMContentLoaded', function(){

	var modal = document.getElementById("myModal");
	var img = document.querySelectorAll(".myImg");
	var modalImg = document.getElementById("img01");
	//var captionText = document.getElementById("caption");

	for(let i = 0; i < img.length; i++){
		var our_img = img[i];
		our_img.addEventListener('click', clickImg);
	}

	function clickImg(event){
		modal.style.display = "block";
		modalImg.src = this.src;
		//captionText.innerHTML = this.alt;
	}

	var span = document.querySelector(".close");
	span.onclick = function(){
		modal.style.display = "none";
	}

});