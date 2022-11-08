console.log("while-løkker");

let teller = 10;
while (teller > 0) {
    console.log(teller);
    teller = teller - 1;
}

console.log("For -løkke:");
//   start     slutt     hopp
for (let i = 1; i <=10; i++) {
    console.log(i);
}

let arrayNavn = ["Jo", "Joo", "Jou"];
console.log(arrayNavn.length);
console.log(arrayNavn);
console.table(arrayNavn);
console.log(arrayNavn[1]);
arrayNavn[1] = "Navn"
console.table(arrayNavn);

for (let navn of arrayNavn) {
    console.log(navn);
}



//for (let i = 0; i < arrayNavn.length; i++){

//}


//let navn = "Jo Bjørnar";
//arrayNavn.push(navn);