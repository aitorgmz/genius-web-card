$(document).ready(function(){
    //if($("#mainImage").is(":visible")) ?  $("#mainImage").css("visibility","hidden") : $("#mainImage").css("visibility","visible") ;
    const input = document.getElementById("id_song_image");
    console.log(input);

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
        console.log(base64);
        document.getElementById("id_song_image_base64").value = base64;
    };

    input.addEventListener("change", (e) => {
        uploadImage(e);
    });
});