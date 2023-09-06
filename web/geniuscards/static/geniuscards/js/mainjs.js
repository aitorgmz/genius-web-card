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
});

function initialize(){
    $("#spotifyCreation").css("display","none");
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