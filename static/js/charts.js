let chart = echarts.init(document.querySelector("#main"))


$(document).ready(() => {
    draw_movies()
});


window.onresize = function () {
    chart.resize();
}

function draw_movies() {
    chart.showLoading();
    $.ajax(
        {
            url: "/movie-json",
            type: "POST",
            dataType: "json",
            success: (data) => {
                chart.hideLoading();
                movies_expect(data["title"], data["expect"])
                console.log(data)

            },
            error: () => {
                chart.hideLoading();
                alert("讀取資料失敗")
            }
        }
    )
};



function movies_expect(xdata, ydata) {


    let option = {
        title: {
            text: 'yahoo電影'
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'left',
            top: 'center',
            feature: {
                magicType: { show: true, type: ['line', 'bar', 'tiled'] },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        tooltip: { trigger: 'axis' },
        legend: {},
        xAxis: {
            data: xdata
        },
        yAxis: {},
        series: [
            {
                itemStyle: {
                    color: '#172b85'
                },

                name: 'percent',
                type: 'bar',
                data: ydata
            }
        ]
    };
    chart.setOption(option);
}


