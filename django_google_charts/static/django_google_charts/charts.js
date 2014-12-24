$(document).ready(function() {

  function drawCharts() {
    var elements = document.querySelectorAll('[data-chart-url]');
    for (var i = 0; i < elements.length; i++) {
      drawChart(elements[i]);
    }
  }

  function drawChart(chartElement) {
    var options = chartElement.getAttribute('data-chart-options');
    var url = chartElement.getAttribute('data-chart-url');

    $.getJSON(url, function(data) {
      var dataTable = new google.visualization.DataTable();

      var types = [];

      for (var i = 0; i < data.cols.length; i++) {
        var col = data.cols[i];
        types.push(col[0]);
        dataTable.addColumn(col[0], col[1]);
      }

      for (var i = 0; i < data.rows.length; i++) {
        var row = data.rows[i];
        var formattedRow = [];
        for (var j = 0; j < row.length; j++) {
          switch (types[j]) {
            case 'datetime':
              formattedRow.push(new Date(row[j]));
              break;
            default:
              formattedRow.push(row[j]);
          }
        }

        dataTable.addRow(formattedRow);
      }

      var chart = new google.visualization.LineChart(chartElement);
      chart.draw(dataTable, JSON.parse(options));
    });
  }

  google.setOnLoadCallback(drawCharts);

});