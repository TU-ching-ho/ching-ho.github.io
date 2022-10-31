const timeEl = document.querySelector("#date");
function getTime() {
    let date = new Date();
    timeEl.innerText = `${date.getFullYear()}-${date.getMonth() + 1}\
    -${date.getDate()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;

    setTimeout(getTime, 1000);
}

// $(document).ready(() => {
//     getmybike()
// });
//台南自行車資訊
let looking = document.querySelector("#check");

looking.addEventListener("click", () => {
    let sta = document.querySelector("#station").value;
    if (sta == "") {
        alert("請選擇站名!");
        return;
    }
    getmybike()
})


function getmybike() {
    const sta = document.querySelector("#station").value;
    let look_station = document.querySelector("#station_forlook");
    let look_address = document.querySelector("#address");
    let look_capacity = document.querySelector("#capacity");
    let look_bikecount = document.querySelector("#bikecount");
    let look_spacecount = document.querySelector("#spacecount");
    let look_time = document.querySelector("#time");
    //console.log(sta);

    $.ajax(
        {
            url: "/bike-json",
            type: "POST",
            datatype: "json",
            success: (data) => {
                //console.log(data);
                var json = eval("(" + data + ")");
                //console.log(json);
                //console.log(json.title.length);
                //console.log(json['title'][0][0]);
                //console.log(json['title'])
                for (let index = 0; index < json.title.length; index++) {
                    //車站訊息json['title'][index][x]
                    //console.log(json['title'][index][0]);//車站

                    if (sta == json['title'][index][0]) {
                        //console.log(json['title'][index][0])
                        look_station.innerText = json['title'][index][0]
                        look_address.innerText = json['title'][index][1]
                        look_capacity.innerText = json['title'][index][2]
                        look_bikecount.innerText = json['title'][index][3]
                        look_spacecount.innerText = json['title'][index][4]
                        look_time.innerText = json['title'][index][5]
                    }

                }
            }
        }

    )
}

//台北自行車資訊
let taipei_looking = document.querySelector("#taipei_check");

taipei_looking.addEventListener("click", () => {
    const taipeista = document.querySelector("#taipeistation").value;
    console.log(taipeista);
    if (taipeista == "") {
        alert("請選擇站名!");
        return;
    }
    get_my_taipeibike()

})

function get_my_taipeibike() {
    const taipeista = document.querySelector("#taipeistation").value;
    let look_station = document.querySelector("#taipeistation_forlook");
    let look_address = document.querySelector("#taipeiaddress");
    let look_capacity = document.querySelector("#taipeicapacity");
    let look_bikecount = document.querySelector("#taipeibikecount");
    let look_spacecount = document.querySelector("#taipeispacecount");
    let look_time = document.querySelector("#taipeitime");
    console.log(taipeista);

    $.ajax(
        {
            url: "/taipeibike-json",
            type: "POST",
            datatype: "json",
            success: (data) => {
                //console.log(data);
                var json = eval("(" + data + ")");
                //console.log(json);


                for (let index = 0; index < json.datas.length; index++) {


                    if (taipeista == json['datas'][index][0]) {
                        //console.log(json['title'][index][0])
                        look_station.innerText = json['datas'][index][0]
                        look_address.innerText = json['datas'][index][1]
                        look_capacity.innerText = json['datas'][index][2]
                        look_bikecount.innerText = json['datas'][index][3]
                        look_spacecount.innerText = json['datas'][index][4]
                        look_time.innerText = json['datas'][index][5]
                    }

                }
            }
        }

    )
}