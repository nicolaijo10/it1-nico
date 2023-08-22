let nedtellig = setInterval(tikk,1000);

let utskrift = document.getElementById("utskrift");

let antallSekunder = prompt("Hvor mange sekunder?");

let musikkFerdig = new Audio("lyd/happy-day-113985.mp3");

let musikkUnderveis = new Audio("lyd/Saul goodman 3d (320 kbps).mp3")

function tikk() {
    antallSekunder = antallSekunder - 1; // Trekk fra 1 på antall sekunder//
    console.log(antallSekunder); //Skriv ut antall gjenværende sekund//
    document.getElementById("utskrift").innerText = antallSekunder;
    
    if (antallSekunder <= 3) {
        utskrift.style.color = "#FF0000";
    }

    if (antallSekunder <= 0) {
        document.getElementById("utskrift").innerText = "AUUGHHHHH"
        musikkFerdig.play();
        musikkUnderveis.pause();
        clearInterval(nedtellig);
        utskrift.style.color = "green";

    }

}

document.body.addEventListener("click", spillMusikk);

function spillMusikk() {
    musikkUnderveis.play();

}