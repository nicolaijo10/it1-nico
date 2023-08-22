function tilfeldigHilsen() {
    let tilfeldig = Math.floor(Math.random() * 3);
    if (tilfeldig === 0) {
    console.log("Hei");
    } else if (tilfeldig === 1) {
    console.log("Hallo");
    } else if (tilfeldig === 2) {
    console.log("God dag");
    }

}

// oppgave 11
function arealTrekant(grunnlinje, hoyde) {
    let areal = (grunnlinje * hoyde) / 2;
    return areal;
}

//oppgave 12

function arealRektangel(lengde, bredde) {
    if ((lengde <= 0) || (bredde <= 0)) {
    return "Du må oppgi positive tall for lengde og bredde.";
}
    if ((typeof(lengde) === "string") || (typeof(bredde) === "string")) {
    return "Du må oppgi tall (ikke tekst).";
}
    let areal = lengde * bredde;
    return areal;
}





