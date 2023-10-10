var loadingGif = "data:image/gif;base64,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";
var infoIcon ="data:image/png;base64,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"

$(document).ready(function(){
    initialize();
    initializeMainButtons();
    const imageInput = document.getElementById("id_song_image");

    const convertBase64 = (file) => {
        return new Promise((resolve, reject) => {
            const fileReader = new FileReader();
            fileReader.readAsDataURL(file);

            fileReader.onload = () => {
                resolve(fileReader.result);
            };

            fileReader.onerror = (error) => {
                reject(error);
            };
        });
    };

    const uploadImage = async (event) => {
        const file = event.target.files[0];
        const base64 = await convertBase64(file);
        document.getElementById("id_song_image_base64").value = base64;
    };

    imageInput.addEventListener("change", (e) => {
        uploadImage(e);
    });

    $("#submitButtonManually").click(function(e){
        e.preventDefault();
        getImageFromLocalData();
    });

    $("#searchGenius").click(function(e){
        e.preventDefault();
        refreshData();
    });

    $("#generateImage").click(function(){
        getImageFromSongData();
    });

});

function initialize(){
    $("#spotifyCreation").css("display","flex");
    $("#generateImage").css("display","flex");
    $("#searchGenius").text("SEARCH LYRICS");
    $("#geniusLyricsTextarea").css("visibility", "visible");
    $("#geniusImage").css("visibility","visible");
    $("#localCreation").css("display","none");
    $("#selectMode").prop("value","Create manually");
    $("#foundSongPanel").css("display","none");
    $("#infoButton").attr("src", infoIcon);
    $("#tooltip").css("display", "none");
    $("#geniusErrorDiv").css("display","none");
    $("#manualErrorDiv").css("display","none");
    $("#infoButton").hover(function(){
        $("#tooltip").css("display", "flex");
    }, function(){
        $("#tooltip").css("display", "none");
    });
}

function initializeMainButtons(){
          $("#selectorDivSpotify").click(function(){
          if($("#spotifyCreation").css("display") == "none"){
                $("#localCreation").animate({width: 'toggle'});
                $("#spotifyCreation").animate({width: 'toggle'});
                $("#selectorDivSpotify").animate({backgroundColor: 'black', color: 'white'})
                $("#selectorDivManual").animate({backgroundColor: 'white', color: 'black'})
            }
          });
          $("#selectorDivManual").click(function(){
            if($("#localCreation").css("display") == "none"){
                $("#spotifyCreation").animate({width: 'toggle'});
                $("#localCreation").animate({width: 'toggle'});
                $("#selectorDivManual").animate({backgroundColor: 'black', color: 'white'})
                $("#selectorDivSpotify").animate({backgroundColor: 'white', color: 'black'})
            }
          });
}

function getImageFromLocalData(){
    let song_title = $("#id_song_title").val();
    let song_author = $("#id_song_author").val();
    let song_lyrics = $("#id_song_lyrics").val();
    let song_image_base64 = $("#id_song_image_base64").val();
    if(song_title.trim() != "" && song_author.trim() != "" && song_lyrics != "" && song_image_base64 != ""){
        if($("#manualErrorDiv").is(":visible")){
           $("#manualErrorDiv").toggle(250);
        }
        $.ajax({
            url : 'http://127.0.0.1:8000/geniuscards/getImageFromLocalData',
            type : 'POST',
            dataType:'json',
            data: {"song_title":song_title,"song_author":song_author, "song_lyrics":song_lyrics, "song_image_base64":song_image_base64},
            success : function(data) {
                $("#mainImage").prop("src",Object.entries(data)[0][1]);
            },
            error : function(request,error) {
                $("#manualErrorMessage").text("There was an error processing your image.");
                $("#manualErrorDiv").toggle(250);
            }
        });
    } else {
        $("#manualErrorMessage").text("You need to complete all the fields to create an image.");
        if(!$("#manualErrorDiv").is(":visible")){
            $("#manualErrorDiv").toggle(250);
        }
    }
}


function refreshData(){
        let author = $("#id_genius_song_author").val();
        let song = $("#id_genius_song_song").val();
        if(song.trim().length != 0 && author.trim().length != 0){
            if($("#geniusErrorDiv").is(":visible")){
                $("#geniusErrorDiv").toggle(250);
            }
            $.ajax({
                url : 'http://127.0.0.1:8000/geniuscards/getSongData',
                type : 'POST',
                dataType:'json',
                data: {"author":author,"song":song},
                beforeSend: function(){
                    $("#foundSongCover").attr("src",loadingGif);
                    $("#foundSongPanel").css("display","flex");
                },
                success : function(data) {
                    let geniusSong = Object.entries(data)[0][1];
                    let geniusArtist = Object.entries(data)[1][1];
                    let geniusLyrics = String(Object.entries(data)[2][1]);
                    let geniusCoverUrl = Object.entries(data)[3][1];
                    geniusLyrics  = geniusLyrics.substring(geniusLyrics.indexOf("Lyrics")+6);
                    $("#geniusLyricsTextarea").val(geniusLyrics);
                    $("#foundSongName").text(geniusSong+" ");
                    $("#foundSongArtist").text(" by "+geniusArtist);
                    $("#foundSongCover").attr("src",geniusCoverUrl);
                    $("#geniusLyricsTextarea").css("visibility", "visible");
                    $("#geniusImage").css("visibility","visible");
                    $("#foundSongPanel").css("display","flex");
                    $("#generateImage").css("display","flex");
                    $("#searchGenius").attr("value","SEARCH AGAIN");
                },
                error : function(request,error)
                {
                    $("#foundSongPanel").css("display","none");
                    $("#geniusErrorMessage").text("We can´t find your song. Try again.");
                    $("#geniusErrorDiv").toggle(250);
                }
            });
        } else {
            if(!$("#geniusErrorDiv").is(":visible")){
              $("#geniusErrorDiv").toggle(250);
            }
            else if ($("#geniusErrorDiv").is(":visible") && $("#geniusErrorMessage").text() == "We can´t find your song. Try again."){
                $("#geniusErrorMessage").text("You must complete both fields.");
            }
        }
}


function getImageFromSongData(){
        let song = $("#foundSongName").text();
        let author = $("#foundSongArtist").text();
        author = author.replace(" by","");
        let lyricsStart = $("#geniusLyricsTextarea")[0].selectionStart;
        let lyricsEnd = $("#geniusLyricsTextarea")[0].selectionEnd;
        let lyrics = $("#geniusLyricsTextarea").val().substring(lyricsStart, lyricsEnd);
        let image = "";
        convertToBase64($('#foundSongCover').prop('src'), function(base64Image) {
            base64Image = base64Image.replace("data:image/","");
            base64Image = base64Image.replace("png;","");
            base64Image = base64Image.replace("jpeg;","");
            base64Image = base64Image.replace("base64,","");
            console.log(base64Image);
            $.ajax({
                url : 'http://127.0.0.1:8000/geniuscards/getImageFromSongData',
                type : 'POST',
                dataType:'json',
                data: {"song":song,"author":author,"lyrics":lyrics,"image":base64Image},
                success : function(data) {

                    $("#geniusImage").attr("src","data:image/png;base64,"+Object.entries(data)[0][1]);
                },
                error : function(request,error)
                {
                    alert("Error recuperando resultados");
                }
            });
        });
}

function convertToBase64(url, callback) {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var reader = new FileReader();
    reader.onloadend = function() {
      callback(reader.result);
    };
    reader.readAsDataURL(xhr.response);
  };
  xhr.open('GET', url);
  xhr.responseType = 'blob';
  xhr.send();
}