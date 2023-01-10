let arrBrukere = [];

const skjema = document.getElementById("skjemaRegistrering")

skjema.addEventListener("submit", registerBruker);

function registerBruker(evt) {
    evt.preventDefault();
    let nyEpost = document.getElementById("inpEpost").value;
    let nyttPassord = document.getElementById("inpPassord").value;
    
    // Oppretter et objekt fra input
    let objBruker = {
        epost : nyEpost,
        passord : nyttPassord
    };
    arrBrukere.push(objBruker);
    console.log(arrBrukere); //sjekker om obj ble lagt til

    //utskrift til HTML
    let ut = "<li>" + nyEpost + ", " + nyttPassord + "</li>";
    document.getElementById("utskrift").innerHTML += ut;
}