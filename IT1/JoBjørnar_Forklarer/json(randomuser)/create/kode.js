let overskrift = document.createElement("h1")
overskrift.innerText = "Dette er en overskrift.";
//overskrift.classList.add();
overskrift.setAttribute("class","bakgrunn");
document.body.appendChild(overskrift);

let bilde = document.createElement("img");
bilde.src = "https://akamai.vgc.no/dredition-images/771/266/77126690/77126690-mobile-top-e7ec2669903a7e9bac035b0664c83560.jpg?format=auto"
bilde.setAttribute("src", "https://akamai.vgc.no/dredition-images/771/266/77126690/77126690-mobile-top-e7ec2669903a7e9bac035b0664c83560.jpg?format=auto")
document.body.appendChild(bilde);

document.addEventListener("keydown", function(evt) {
    let tast = evt.key;
    if(tast ==="c") {
        let overskrift = document.createElement("h1")
         overskrift.innerText = "Dette er en overskrift.";
        //overskrift.classList.add();
        overskrift.setAttribute("class","bakgrunn");
        document.body.appendChild(overskrift);
    }
    if(tast ==="r") {
        document.body.removeChild(overskrift);
    }
    console.log(tast);
})



document.addEventListener("keyup", tastaturOpp);

function tastaturOpp(evt) {
    let tast = evt.key;
    console.log("Tast opp: " + tast);
}

fetch('https://randomuser.me/api/?results=5')
	.then(response => response.json())
	// .then(response => console.log(response))
    .then(response => behandleSvar(response))
	.catch(err => console.error(err));

function behandleSvar(svar) {

    for (let j = 0; j < svar.results.lenght; j++) {
    
        // Testing
        console.log(svar);
        console.log("Navn: " + svar.results[j].name.first);
        console.log("Epost: " + svar.results[j].email);
        console.log("Bilde: " + svar.results[j].picture.large);

        // HTML-visning
        let navn = document.createElement("p");
        navn.innerText = "Navn: " + svar.results[j].name.first;
        let epost = document.createElement("p");
        epost.innerText = "Epost: " + svar.results[j].email;
        let bilde = document.createElement("img");
        bilde.src = svar.results[j].picture.large;
        document.querySelector("#utskrift").appendChild(navn);
        document.querySelector("#utskrift").appendChild(epost);
        document.querySelector("#utskrift").appendChild(bilde);
    }
}