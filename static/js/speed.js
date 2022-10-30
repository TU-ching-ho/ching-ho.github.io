const getspeed = (distance, second, point = 2) => ((distance / second) * 60 / 100).toFixed(point);


const cal = document.querySelector("#calc");
let distance = document.querySelector("#distance");
let second = document.querySelector("#second");
const res = document.querySelector("#reset")


cal.addEventListener("click", () => {
    let speeD = document.querySelector("#comment .speed");

    let distance = document.querySelector("#distance").value;
    let second = document.querySelector("#second").value;
    if (distance == "" || second == "") {
        alert("輸入不能為空");
        return;
    }

    let speeDans = getspeed(distance, second);
    if (isNaN(speeDans)) {
        alert("請輸入數值");
        return;
    }

    speeD.innerHTML = speeDans;

});

res.addEventListener("click", () => {
    let speeD = document.querySelector("#comment .speed");
    if (speeD !== "") {
        speeD.innerHTML = ""
    }

})