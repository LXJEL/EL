
var getKGname = "YAGO";
var knowledgegraph = {};

$.ajax({
    async:false,
    type: "POST",
    url: '/getKG/',
    data: {
        'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
        "KG_id": getKGname,
        "number": "2"
    }, success: function (data) {
        knowledgegraph = data;
        // console.log(data);
    }, error:function (data){
        console.log("访问失败！")
    }
});
var obj = eval('(' + knowledgegraph + ')');
// 初始化图表
const chart = echarts.init(document.getElementById('main'));

// 节点数据
const nodes = [];
for (const i in obj['nodes']) {
    nodes.push({id: obj['nodes'][i]['id'].toString(), name: obj['nodes'][i]['properties']['name'], symbolSize: 40, draggable: true})
}

// 边数据
const links = [];
for (const i in obj['links']) {
    links.push({source: obj['links'][i]['start_id'].toString(),
                target: obj['links'][i]['target_id'].toString(),
                rel: obj['links'][i]['relationship_type']})
}

// 构造数据
const graph = {
    nodes: nodes,
    links: links
};

// 配置项
const option = {
    
    tooltip: {
        trigger: 'item',
        formatter: '{b}'
    },
    series: [
        {
            type: 'graph',
            layout: 'force',
            data: graph.nodes,
            links: graph.links,
            roam: true,
            label: {
                normal: {
                    show: true
                }
            },
            lineStyle: {
                normal: {
                    color: '#4b565b',
                    width: 1,
                    type: 'solid'
                }
            },
            edgeSymbol: ['none', 'triangle'],
            edgeSymbolSize: [5, 8],
            edgeLabel: {
                normal: {
                  show: true,
                  formatter: function (x) {
                    return x.data.rel
                  },
                  textStyle: {
                    fontSize: 8,
                    color: '#4b565b'
                  }
                }
            },
            force: {
                repulsion: 1000,
                edgeLength: 150
            },
            draggable: true // 开启节点拖拽功能
        }
    ]
};



// 渲染图表
chart.setOption(option);

