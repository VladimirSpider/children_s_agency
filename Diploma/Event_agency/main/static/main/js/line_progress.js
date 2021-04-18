document.addEventListener('DOMContentLoaded', function(){

    //const progress = document.querySelector('.progress');
    //window.addEventListener('scroll', progressBar);

    //function progressBar(event){
    //    let windowScroll = document.body.scrollTop || document.documentElement.scrollTop;
    //    let windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    //    let percent = windowScroll / windowHeight * 100;
   // console.log(windowScroll);
   // console.log(windowHeight);
   // console.log(percent);
   //     progress.style.width = percent + '%';


    //}

    /*var window_content = document.querySelectorAll('.block_scroll');
    var progress_all = document.querySelectorAll('.progress');
    for (let i = 0; i < window_content.length; i++){
        var window = window_content[i];

        window.addEventListener('scroll', progressBar);
        var s = window_content.indexOf(window);
        console.log(s);
        console.log(1);
        }

        function progressBar(event){
            var windowScroll = window.scrollTop;
            var windowHeight = window.scrollHeight - window.clientHeight;
            var percent = windowScroll / windowHeight * 100;

            progress_all[0].style.width = percent + '%';
        }*/

    const progress = document.querySelector('.progress');
    var  window_content = document.querySelector('.block_scroll');
    window_content.addEventListener('scroll', progressBar);

    function progressBar(event){
        let windowScroll = window_content.scrollTop;
        let windowHeight = window_content.scrollHeight - window_content.clientHeight;
        let percent = windowScroll / windowHeight * 100;
   // console.log(windowScroll);
   // console.log(windowHeight);
   // console.log(percent);
        progress.style.width = percent + '%';
    }

});
