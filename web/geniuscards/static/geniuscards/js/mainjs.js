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

    $("#searchGenius").click(function(){
        refreshData();
    });

    $("#generateImage").click(function(){
        getImageFromSongData();
    });

});

function initialize(){
    $("#spotifyCreation").css("display","none");
    $("#foundSongPanel").css("display","none");
    $("#generateImage").css("display","none");
    $("#searchGenius").text("SEARCH LYRICS");
    $("#geniusLyricsTextarea").css("visibility", "hidden");
    $("#geniusImage").css("visibility","hidden");
}

function initializeMainButtons(){
    $("#selectMode").click( function(){
        if ($("#spotifyCreation").css("display") == "none"){
            $("#spotifyCreation").css("display","flex");
            $("#localCreation").css("display","none");
            $("#selectMode").prop("value","Create manually");
        } else {
            $("#spotifyCreation").css("display", "none");
            $("#localCreation").css("display","flex");
            $("#selectMode").prop("value","Create using Spotify");
        }
    });
}

function refreshData(){
        let author = $("#id_genius_song_author").val();
        let song = $("#id_genius_song_song").val();
        $.ajax({
            url : 'http://127.0.0.1:8000/geniuscards/getSongData',
            type : 'POST',
            dataType:'json',
            data: {"author":author,"song":song},
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
                alert("Error recuperando resultados");
            }
        });
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