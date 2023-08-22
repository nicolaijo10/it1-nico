//15
function terningTreSider() {
    return Math.floor(Math.random() * 3) + 1;
}
  
function treLike() {
    let treLike = false;
  
    while(treLike) {
      let terning1 = terningTreSider();
      let terning2 = terningTreSider();
      let terning3 = terningTreSider();
  
      let sum = terning1 + terning2 + terning3;
  
      console.log("Summen av de tre terningene ble: " + sum);
  
      if (terning1 === terning2 && terning1 === terning3) {
        treLike = true;
        console.log("Fikk tre like!");
        }
    }
}
