const timeEl = document.querySelector("#date");
function getTime() {
    let date = new Date();
    timeEl.innerText = `${date.getFullYear()}-${date.getMonth() + 1}\
    -${date.getDate()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;

    setTimeout(getTime, 1000);
}