let toLike = false;
let antallForsok = 0; 


while(!toLike) {  
  antallForsok++;


let terning1 = terning();
let terning2 = terning();
let terning3 = terning();

console.log("Fikk " + terning1 + ", " + terning2 + ", " + terning3);

if (terning1 === terning2 && terning2 === terning3) {
    toLike = true;
    console.log("Fikk tre like på " + antallForsok + " forsøk");
  }
}

function terning() {
    return Math.floor(Math.random() * 3) + 1;
}

function yatzy(antallTerninger) {
  let tekst = "balls";
  for (let i = 0; i < antallTerninger; i++) {
    let resultat = terning();
    tekst += resultat + "balls ";
  }
  console.log(tekst);
 }