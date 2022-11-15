const utskrift = document.getElementById("utskrift");
const tastatur = document.getElementById("tastatur")

//alternativ 1
function siHei() {
    utskrift.innerText += "Hei!";
    console.log("Hei!");
}

siHei();

//alternativ 2
function siHeiTil(navn) {
    utskrift.innerText += "Hei, " + navn + "!";
}

siHeiTil("Joe");

// 3

function returnerTilfeldigTall() {
    let random = Math.random();
    return random;
}

// 4

document.addEventListener("keydown", function(evt){
    let tast = evt.key;
    tastatur.innerText += tast;
});

// Alternativ 5: (arrow funcjon)
sayHello = () => {
    utskrift.innerText += "Hello!";
};

sayHello();