//код рабочий но из-за обновлений не сохраняется класс при переходах на другие страницы
document.addEventListener('DOMContentLoaded', function(){
    var buttons = document.querySelectorAll('.button_menu p');
    console.log(buttons);

    function no_class(){
        for(let i = 0; i < buttons.length; i++){
            var thisbutton = buttons[i];
            thisbutton.className = thisbutton.className.replace("active_now","");
        }
    }

    for(let i = 0; i < buttons.length; i++){
        var thisbutton = buttons[i];
        thisbutton.addEventListener('click', func);
        function func(event){
            no_class()
            this.className+= "active_now";
            console.log("hi"+i);
        }
    }
});


