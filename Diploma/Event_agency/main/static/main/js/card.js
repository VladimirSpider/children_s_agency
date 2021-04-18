document.addEventListener('DOMContentLoaded', function(){

    const cards = document.querySelectorAll('.card');

   for (let i = 0; i < cards.length; i++){
        const card = cards[i];
        card.addEventListener('mousemove', startrotate);
        card.addEventListener('mouseout', stoprotate);
   }

        function startrotate(event) {
            const body_img_gallery = this.querySelector('.body_img_gallery');

            const halfHeight = body_img_gallery.offsetHeight/2;
            const halfWidth = body_img_gallery.offsetWidth/2;

            body_img_gallery.style.transform = 'rotateX(' + -(event.offsetY - halfHeight)/10 + 'deg) rotateY(' + (event.offsetX - halfWidth)/10 + 'deg)';
        }

        function stoprotate(event) {
            const body_img_gallery = this.querySelector('.body_img_gallery');

            body_img_gallery.style.transform = 'rotate(0)';
        }
});