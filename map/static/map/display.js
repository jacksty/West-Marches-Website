const svg = d3.select("svg");
var width = +svg.attr("width");
var height = +svg.attr("height");

const body = d3.select("body");
const graphobj = {
    "nodes": JSON.parse(body.attr("nodes")),
    "links": JSON.parse(body.attr("edges")),
};


var node = svg.append('g')
    .attr('class', 'nodes')
    .selectAll('circle')
    .data(graphobj.nodes)
    .enter()
    .append('circle')
    .attr('r', d => d.r)
    .attr('fill', d => d.fill)
    .attr('id', d => d.id)
    .call(d3.drag().on('start', dragStart).on('drag', drag).on('end', dragEnd));

var link = svg.append('g')
    .attr('class', 'line')
    .selectAll('line')
    .data(graphobj.links)
    .enter()
    .append('line')
    .attr('stroke', 'black');

var text = svg.append('g')
    .attr('class', 'text')
    .selectAll('text')
    .data(graphobj.nodes)
    .enter().append('text')
    .attr('x', 8)
    .attr('y', '.31em')
    .text(d => d.name);

var weight = svg.append('g')
    .attr('class', 'weight')
    .selectAll('weight')
    .data(graphobj.links)
    .enter().append('text')
    .attr('x', 8)
    .attr('y', '.31em')
    .text(d => d.weight);

node.append('title').text(d => {
    let tagList = '';
    d.tags.forEach(value => tagList += value.text + '\n');
    return tagList;
});


var simulation = d3.forceSimulation(graphobj.nodes)
    .force('link', d3.forceLink(graphobj.links).id(d => d.id).strength(0))
    .on('tick', tick);



function transform(d) {
    return `translate(${d.x},${d.y})`;
}

function tick() {
    link.attr('x1', d => d.source.x)
        .attr('x2', d => d.target.x)
        .attr('y1', d => d.source.y)
        .attr('y2', d => d.target.y);

    weight.attr('transform', d => `translate(${(d.source.x + d.target.x) / 2},${(d.source.y + d.target.y) / 2})`);

    node.attr('transform', transform);
    text.attr('transform', transform);
}

function dragStart(d){
    if (!d3.event.active)
        simulation.alphaTarget(0.3).restart();
    d.fx = null;
    d.fy = null;
}

function drag(d){
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragEnd(d){
    if (!d3.event.active)
        simulation.alphaTarget(0);
    d.fx= null;
    d.fy = null;
}

function outputNodes(){
    let json = JSON.stringify(graphobj.nodes.map(value => {return {
        id: value.id, x: value.x, y: value.y
    }}));
    console.log(json);
    fetch("/" + body.attr('map') + "/locations", { method: 'POST', body: json}).then(res => console.log(res));
}
