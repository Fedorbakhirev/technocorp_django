$(document).ready(function () {

    $('.menu a').each(function(){
        let location =window.location.protocol + '//' + window.location.host + window.location.pathname;
        console.log(location)
        let link = this.href;
        console.log(link)
        if(location == link){
            $(this).parent().addClass('bg-blue text-white');
        }
    });
});