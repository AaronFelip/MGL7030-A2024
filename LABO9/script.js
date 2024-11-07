//valider format de la date AAAA-MM-JJ

function validerDate() {
    let format= /[0-9]{4}-[0-1][0-9]-[0-3][0-9]/
    let date = document.getElementById('date').value;
    let estValide = format.test(date);
    return estValide;
}
// Tous les champs sont obligatoires
function champsRemplis() {
    let estRempli = true;
    const ids = ["nom", "prenom", "date", "code", "genre"];
    for (var i=0; i < ids.length; i++) {
        let champ = document.getElementById(ids[i]).value;
        if (champ == null || champ.lenght < 1){
            estRemplis = false;
        }
    }
    return estRemplis;
}

// Valider le genre F ou M
function validerGenre() {
    let genre = document.getElementById('genre').value.toUpperCase();
    return (genre == "M" || genre == "F" );
}

function validerCode () {
    let code = document.getElementById('code').value;

    // verifier le format général du code permanent entré
    let format = /[A-Z]{4}[0-9]{8}/;
    let codeValide = format.test(code);
    if(!codeValide) {
        return false;
    }
    // verifier les 3 premieres lettre du code permanent
    let nom = document.getElementById('nom').value.substr(0,3).toUpperCase();
    if (code.substr(0,3) !== nom) {
        return false;
    }

    //verifier la 4e lettre
    let prenom = document.getElementById('prenom').value.toUpperCase();
    if (code[3] !== prenom[0]) {
        return false;

    }

    let date = document.getElementById('date').value;

    // verifier que les 2 premiers chiffre correspondent au jour de naissance
    let jour = date.substr(8);
    if (code.substr(4,2) != jour) {
        return false;
    }


    // verifier que les 2 chiffres suivant correspondent au mois de naissance
    let mois = parseInt(date.substr(5,2));
    let genre = document.getElementById('genre').value.toUpperCase();
    let moisCode = parseInt(code.substr(6,2));
    if ((genre === "F" && moisCode !== (mois + 50)) || (genre === "M" && moisCode !== mois)){
        return false;
    }

    // verifier que les 2 chiffres suivant correspondent à l'année de naissance
    let annee = date.substr(2,2);
    if(code.substr(8,2) !== annee) {
        return false;
    }

    return true;
}

function valider(){

    let reussi = true;
    let errDate = document.getElementById('erreur-date');
    let errChamps = document.getElementById("erreur-champs-vides");
    let errGenre = document.getElementById("erreur-genre");
    let errCode = document.getElementById("erreur-code");

    if(!validerDate()){
        errDate.innerHTML = "La date est invalide!!!"
        reussi = false;
    } else {
        errDate.innerHTMl = "";
    }

    if(!champsRemplis){
        errChamps.innerHTML = "1 ou plusieurs champs sont vides!!!"
        reussi = false;
    } else {
        errChamps.innerHTML = "";
    }

    if(!validerGenre){
        errGenre.innerHTML = "Le genre est invalide!!!"
        reussi = false;
    } else {
        errGenre.innerHTML = "";
    }

    if(!validerCode()) {
        errCode.innerHTML = "Le code permanent est invalide!!!";
        reussi = false;
    }  else {
        errCode.innerHTML = ""
    }

    // si toutes les validations reussissent, on submit, sinon on reste sur la page
    if (reussi) {
        let form = document.getElementById("formulaire");
        form.submit();
    } else {
        let errGlobal = document.getElementById("erreur-global");
        errGlobal.innerHTML = "1 ou plusieurs champs sont invalides!!!";
    }
}