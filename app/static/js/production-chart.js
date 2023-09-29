$(function(){
    "use strict";
    
    // chart
    var chart = AmCharts.makeChart("production-chart", {
        "type": "serial",
        "theme": "light",
        
        "fontFamily": "Poppins",
        "marginTop":0,
        "marginRight": 30,
        "dataProvider": [ {
            "date": "2021-10-01",
            "value": 2000,
            "profit": 3000
          }, {
            "date": "2021-10-02",
            "value": 3500,
            "profit": 4000
          }, {
            "date": "2021-10-03",
            "value": 4000,
            "profit": 5000
          }, {
            "date": "2021-10-04",
            "value": 4500
          }, {
            "date": "2021-10-05",
            "value": 5000
          }, {
            "date": "2021-10-06",
            "value": 5500
          }, {
            "date": "2021-10-07",
            "value": 6000
          }, {
            "date": "2021-10-08",
            "value": 6500
          }, {
            "date": "2021-10-09",
            "value": 7000
          }, {
            "date": "2021-10-10",
            "value": 7500
          }, {
            "date": "2021-10-11",
            "value": 8000
          }, {
            "date": "2021-10-12",
            "value": 9000
          }, {
            "date": "2021-10-13",
            "value": 11000
          }, {
            "date": "2021-10-14",
            "value": 10000
          }, {
            "date": "2021-10-15",
            "value": 15000
          
          } ],

          
        "valueAxes": [{
            "position": "left",
              "title": "Amount"
        }],
        
        "graphs": [{
            "id":"g1",
            
            "bullet": "round",
            "bulletSize": 8,
            "lineColor": "#637bb6",
            
            "lineThickness": 2,
            "negativeLineColor": "#e74c3c",
            "type": "smoothedLine",
            "valueField": "value"
        }],
        
        
        "chartCursor": {
            "categoryBalloonDateFormat": "YYYY",
            "cursorAlpha": 0,
            "valueLineEnabled":true,
            "valueLineBalloonEnabled":true,
            "valueLineAlpha":0.5,
            "fullWidth":true
        },
        
        "dataDateFormat": "YYYY-MM-DD",
        "categoryField": "date",
        "categoryAxis": {
            "parseDates": true,
                      "dashLength": 1,
                      "minorGridEnabled": true
        },
        "export": {
            "enabled": true
        },
        "animation": {
          "enabled": true
      },
      "legend": {
        
        "showInLegend": "true",
        "periodValueText": "Cash",
        "cursor": "pointer",
        
        "itemclick": "toggleDataSeries"
    },
    

    });


    
    
});
