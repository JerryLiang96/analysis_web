// 指定图表的配置项和数据
var colorList = ['#ffe957', '#f29f3f', '#f2753f', '#e87e51', '#de8c68'];
var barOption = {

    title: {
        text: '评价情况数量统计',
        x: 'center'
    },
    tooltip: {
    },
    legend: {
        data: ['评价']
    },
    xAxis: {
        type: 'category',
        data: label_list
    },
    yAxis: {},
    series: [{
        name: '数量',
        type: 'bar',
        data: count_list,
        itemStyle: {
            color: function (params) {
                return colorList[params.dataIndex]
            }
        }
    }]
};

var pieOption = {
    title: {
        text: '评价情况比例统计',
        x: 'center'
    },
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: label_list
    },
    series: [
        {
            name: '占比',
            type: 'pie',
            radius: '55%',
            center: ['50%', '60%'],
            data: [
                { value: count_list[0], name: label_list[0] },
                { value: count_list[1], name: label_list[1] },
                { value: count_list[2], name: label_list[2] },
                { value: count_list[3], name: label_list[3] },
                { value: count_list[4], name: label_list[4] }
            ],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ],
};

pointOption = {
    tooltip: {
        position: 'top'
    },
    title: [{
        top: 0,
        text: '分类评论赞同数统计',
        x: 'center'
    }],
    singleAxis: [],
    series: [],
};

echarts.util.each(label_list, function (label, idx) {
    pointOption.title.push({
        textBaseline: 'middle',
        top: (idx + 0.5) * 100 / 5 + '%',
        text: label
    });
    pointOption.singleAxis.push({
        left: 150,
        top: (idx * 100 / 5 + 5) + '%',
        height: (100 / 5 - 10) + '%',
    });
    pointOption.series.push({
        singleAxisIndex: idx,
        coordinateSystem: 'singleAxis',
        type: 'scatter',
        data: [],
        symbolSize: function (dataItem) {
            return dataItem[0];
        }
    });
});

echarts.util.each(point_data, function (dataItem) {
    pointOption.series[dataItem[0]].data.push([dataItem[1]]);
});

bar.setOption(barOption);
pie.setOption(pieOption);
point.setOption(pointOption);