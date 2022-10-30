const timeEl = document.querySelector("#date");
function getTime() {
    let date = new Date();
    timeEl.innerText = `${date.getFullYear()}-${date.getMonth() + 1}\
    -${date.getDate()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;

    setTimeout(getTime, 1000);
}


$(document).ready(() => {
    changecolor()
});


function changecolor() {
    let table = document.getElementById("mybank")
    let tds = table.getElementsByTagName("td")
    for (i = 0; i < tds.length; i++) {
        //console.log(tds[i].innerText);
        if (tds[i].innerText == "-") {
            tds[i].style.backgroundColor = "black"
            console.log(tds[i]);
        }
        //console.log(tds[i]);
    }
}

//console.log(tds[i].innerText); td訊息