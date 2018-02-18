const svg = d3.select("svg");
var width = +svg.attr("width");
var height = +svg.attr("height");

const body = d3.select("body");
const graphobj = {
    "nodes": JSON.parse(body.attr("nodes")),
    "links": JSON.parse(body.attr("edges")),
};

svg.call(d3.zoom().on('zoom', zoom));

var link = svg.append('g')
    .attr('class', 'line')
    .selectAll('line')
    .data(graphobj.links)
    .enter()
    .append('line')
    .attr('stroke', d => d.stroke);
    
var node = svg.append('g')
    .attr('class', 'nodes')
    .selectAll('nodes')
    .data(graphobj.nodes)
    .enter()
    .append('circle')
    .attr('r', d => d.r)
    .attr('fill', d => d.fill)
    .attr('id', d => d.id);

if(body.attr('edit')) {
    node.call(d3.drag().on('start', dragStart).on('drag', drag).on('end', dragEnd))
    .on('click', lClickNode)
    .on('contextmenu', rClickNode);
}

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

var sourceBox = d3.select('#source_name');
var targetBox = d3.select('#target_name');


var simulation = d3.forceSimulation(graphobj.nodes)
    .force('link', d3.forceLink(graphobj.links).id(d => d.id).strength(0))
    .on('tick', tick);


function zoom() {
    link.attr('transform', d3.event.transform);
    weight.attr('transform', d3.event.transform);
    node.attr('transform', d3.event.transform);
    text.attr('transform', d3.event.transform);
}

function tick() {
    link.attr('x1', d => d.source.x)
        .attr('x2', d => d.target.x)
        .attr('y1', d => d.source.y)
        .attr('y2', d => d.target.y);

    weight.attr('x', d => (d.source.x + d.target.x) / 2).attr('y', d => (d.source.y + d.target.y) / 2);

    node.attr('cx', d => d.x).attr('cy', d => d.y).attr('x', d => d.x).attr('y', d => d.y);
    text.attr('x', d => d.x).attr('y', d => d.y);
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

    fetch("/" + body.attr('map') + "/locations", { method: 'POST', body: json}).then(res => console.log(res));
}

function lClickNode(d) {
    sourceBox.attr('value', d.name);
}

function rClickNode(d) {
    targetBox.attr('value', d.name);
    d3.event.preventDefault();
}
