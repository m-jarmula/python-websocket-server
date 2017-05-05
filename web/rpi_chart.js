function RpiChart(opts){
  var selector = opts.type + "-chart"
  var options = {
    type: "line",
    showInLegend: true,
    lineThickness: 2,
    name: opts.type,
    color: opts.color || "#F08080",
    dataPoints: opts.dataPoints || []
  }
  var chart = new CanvasJS.Chart(selector.toLowerCase(), {
    title: {
      text: opts.type,
      fontSize: 30
    },
    animationEnabled: false,
    axisX: {
      gridColor: "Silver",
      tickColor: "silver",
      valueFormatString: "DD/MMM"
    },
    toolTip: {
      shared: true
    },
    theme: "theme2",
    axisY: {
      gridColor: "Silver",
      tickColor: "silver"
    },
    legend: {
      verticalAlign: "bottom",
      horizontalAlign: "center"
    },
    data: [options],
  });
  this.render = function(){
    chart.render();
    return this;
  }
  this.addPoint = function(value){
    options.dataPoints.push({x: new Date(), y: value });
    return this;
  }
}
