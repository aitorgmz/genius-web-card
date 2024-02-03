$(document).ready(function(){
    initializeBtns();
});

function initializeBtns(){

    $("#contactBtn").click(function(){
        $("#contactTab").css("display","flex");
        $("#projectsTab").css("display","none");
        $("#aboutMeTab").css("display","none");
    });

    $("#aboutMeBtn").click(function(){
        $("#aboutMeTab").css("display","flex");
        $("#contactTab").css("display","none");
        $("#projectsTab").css("display","none");
    });

     $("#projectsBtn").click(function(){
        $("#contactTab").css("display","none");
        $("#projectsTab").css("display","flex");
        $("#aboutMeTab").css("display","none");
    });

    $("#linkedInBtn").click(function(){
        window.open("https://es.linkedin.com/in/aitor-g%C3%B3mez-taboada-821330217", "_blank");
    });

    $("#mailToBtn").click(function(){
        window.open("mailto:aitorgtaboada@gmail.com", "_blank");
    });
}

