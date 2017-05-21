var vm = new Vue({
    el: '#wechat',
    data: {},
    computed: {
        random1000: function() {
            var a = [];
            for (i = 0; i < 20; i++) {
                a[i] = Math.ceil(Math.random() * 1000);
            }
            return a;
        },
        random10000: function() {
            var a = [];
            for (i = 0; i < 20; i++) {
                a[i] = Math.ceil(Math.random() * 10000);
            }
            return a;
        },
        keyword: function() {
            var keyword = ['运动', '饮食', '糖尿病', '胰岛素', '睡眠', '易康伴侣', '迈豆', '医师助手', '志愿者', '施康培', '迈德', '中国医师协会', '世界糖尿病基金会', '诺迪维', '健康', '生活', '长寿', 'keyword1', 'keyword2', 'keyword3', 'keyword4', 'keyword5', 'keyword6']
            return keyword.map(function(word) {
                return {
                    name: word,
                    value: Math.ceil(Math.random() * 1000),
                }
            })
        },
        experts: function() {
            var experts = ['专家1', '专家2', '专家3', '专家4', '专家5', '专家6', '专家7', '专家8', '专家9', '专家10']
            var result = experts.map(function(expert) {
                return {
                    name: expert,
                    value: Math.ceil(Math.random() * 1000),
                    itemStyle: {
                        normal: {
                            color: color[Math.round(Math.random() * 10)]
                        }
                    }
                }
            });
            result.sort(function(a, b) {
                return b.value - a.value;
            });
            return result;
        },
    },
    methods: {
        refreash_pinned: function() {
            var a = function() {
                $(".pinned").pin({
                    containerSelector: '.min-height',
                    minWidth: 768
                });
            };
            setTimeout(a, 500);
        }
    }
});


var option_all_pie = {
    color: color,
    tooltip: {
        trigger: 'item',
        formatter: "{b}: {c} ({d}%)"
    },
    legend: [{
        // orient: 'vertical',
        x: 'center',
        y: 'top',
        data: ['医师助手文章数', '易康伴侣文章数', '医学志愿者文章数', '施康培文章数']
    }, {
        // orient: 'vertical',
        x: 'center',
        y: 'bottom',
        data: ['医师助手阅读量', '易康伴侣阅读量', '医学志愿者阅读量', '施康培阅读量']
    }, ],
    series: [{
        name: '微信公众号',
        type: 'pie',
        selectedMode: 'single',
        radius: [0, '30%'],
        center: ['50%', '50%'],
        label: {
            normal: {
                show: false,
                position: 'inner',
                formatter: '{d}%'
            }
        },
        labelLine: {
            normal: {
                show: false
            }
        },
        data: [
            { value: vm.random1000[1], name: '医师助手文章数' },
            { value: vm.random1000[2], name: '易康伴侣文章数' },
            { value: vm.random1000[3], name: '医学志愿者文章数' },
            { value: vm.random1000[4], name: '施康培文章数' }
        ]
    }, {
        name: '微信公众号',
        type: 'pie',
        radius: ['40%', '55%'],
        center: ['50%', '50%'],
        label: {
            normal: {
                show: false,
                formatter: '{d}%'
            }
        },
        data: [
            { value: vm.random10000[1], name: '医师助手阅读量' },
            { value: vm.random10000[2], name: '易康伴侣阅读量' },
            { value: vm.random10000[3], name: '医学志愿者阅读量' },
            { value: vm.random10000[4], name: '施康培阅读量' },
        ]
    }]
};

var chart_all_pie = echarts.init(document.getElementById('chart_all_pie'));
chart_all_pie.setOption(option_all_pie);


var option_all_wordcloud = {
    color: color,
    tooltip: {
        trigger: 'item',
        formatter: "{b}: {c}"
    },
    series: [{
        type: 'wordCloud',

        // The shape of the "cloud" to draw. Can be any polar equation represented as a
        // callback function, or a keyword present. Available presents are circle (default),
        // cardioid (apple or heart shape curve, the most known polar equation), diamond (
        // alias of square), triangle-forward, triangle, (alias of triangle-upright, pentagon, and star.

        // shape: 'circle',

        // Folllowing left/top/width/height/right/bottom are used for positioning the word cloud
        // Default to be put in the center and has 75% x 80% size.

        left: 'center',
        top: 'center',
        // width: '70%',
        // height: '80%',
        right: null,
        bottom: null,

        // Text size range which the value in data will be mapped to.
        // Default to have minimum 12px and maximum 60px size.

        sizeRange: [10, 60],

        // Text rotation range and step in degree. Text will be rotated randomly in range [-90, 90] by rotationStep 45

        rotationRange: [-90, 90],
        rotationStep: 45,

        // size of the grid in pixels for marking the availability of the canvas
        // the larger the grid size, the bigger the gap between words.

        gridSize: 8,

        // Global text style
        textStyle: {
            normal: {
                fontFamily: 'Microsoft YaHei',
                fontWeight: 'bold',
                // Color can be a callback function or a color string
                color: function() {
                    // Random color
                    return color[Math.round(Math.random() * 10)];
                }
            },
            emphasis: {
                shadowBlur: 10,
                shadowColor: '#333'
            }
        },

        // Data is an array. Each array item must have name and value property.
        data: vm.keyword,
    }]
};

var chart_all_wordcloud = echarts.init(document.getElementById('chart_all_wordcloud'));
chart_all_wordcloud.setOption(option_all_wordcloud);


var option_all_bar = {
    color: color,
    tooltip: {
        trigger: 'item',
        formatter: "{b}: {c}"
    },
    xAxis: [{
        type: 'value',
        position: 'top',
        axisTick: {
            show: false
        },

        nameTextStyle: {
            fontWeight: 'bold'
        }
    }],
    yAxis: [{
        type: 'category',
        data: vm.experts.map(function(a) {
            return a.name;
        }),
        inverse: true,
        axisTick: {
            show: false
        },
        axisLine: {
            show: false
        },
        nameTextStyle: {
            fontWeight: 'bold'
        }
    }],
    itemStyle: {
        normal: {
            barBorderRadius: [0, 1, 1, 0]
        },
    },
    series: [{
        name: '专家统计',
        type: 'bar',
        // label: {
        //     normal: {
        //         show: true,
        //         position: 'right',
        //         // formatter: '{d}%'
        //     }
        // },

        data: vm.experts,
    }]
};

var chart_all_bar = echarts.init(document.getElementById('chart_all_bar'));
chart_all_bar.setOption(option_all_bar);
