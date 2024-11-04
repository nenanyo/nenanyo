// You can reproduce this figure in plotly.js with the following code!

// Learn more about plotly.js here: https://plotly.com/javascript/getting-started

/* Here's an example minimal HTML template
 *
 * <!DOCTYPE html>
 *   <head>
 *     <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
 *   </head>
 *   <body>
 *   <!-- Plotly chart will be drawn inside this div -->
 *   <div id="plotly-div"></div>
 *     <script>
 *     // JAVASCRIPT CODE GOES HERE
 *     </script>
 *   </body>
 * </html>
 */

trace1 = {
  meta: {columnNames: {
      labels: 'data.0.labels', 
      values: 'data.0.values'
    }}, 
  type: 'pie', 
  domain: {
    x: [0, 0.45], 
    y: [0, 1]
  }, 
  textinfo: 'label+percent', 
  labelssrc: 'aroma1532:21:3e587a', 
  labels: ['여자', '남자'], 
  valuessrc: 'aroma1532:21:6a74b7', 
  values: [566398.8921161826, 994991.2045454546]
};
trace2 = {
  meta: {columnNames: {
      labels: 'data.1.labels', 
      values: 'data.1.values'
    }}, 
  type: 'pie', 
  domain: {
    x: [0.55, 1], 
    y: [0, 1]
  }, 
  textinfo: 'label+percent', 
  labelssrc: 'aroma1532:21:11c699', 
  labels: ['여자', '남자'], 
  valuessrc: 'aroma1532:21:007713', 
  values: [38.7344398340249, 31.075757575757574]
};
data = [trace1, trace2];
layout = {
  autosize: true, 
  colorway: ['#4c78a8', '#f58518', '#e45756', '#72b7b2', '#54a24b', '#eeca3b', '#b279a2', '#ff9da6', '#9d755d', '#bab0ac'], 
  template: {
    data: {
      bar: [
        {
          type: 'bar', 
          marker: {
            line: {
              color: '#E5ECF6', 
              width: 0.5
            }, 
            pattern: {
              size: 10, 
              fillmode: 'overlay', 
              solidity: 0.2
            }
          }, 
          error_x: {color: '#2a3f5f'}, 
          error_y: {color: '#2a3f5f'}
        }
      ], 
      pie: [
        {
          type: 'pie', 
          automargin: true
        }
      ], 
      table: [
        {
          type: 'table', 
          cells: {
            fill: {color: '#EBF0F8'}, 
            line: {color: 'white'}
          }, 
          header: {
            fill: {color: '#C8D4E3'}, 
            line: {color: 'white'}
          }
        }
      ], 
      carpet: [
        {
          type: 'carpet', 
          aaxis: {
            gridcolor: 'white', 
            linecolor: 'white', 
            endlinecolor: '#2a3f5f', 
            minorgridcolor: 'white', 
            startlinecolor: '#2a3f5f'
          }, 
          baxis: {
            gridcolor: 'white', 
            linecolor: 'white', 
            endlinecolor: '#2a3f5f', 
            minorgridcolor: 'white', 
            startlinecolor: '#2a3f5f'
          }
        }
      ], 
      mesh3d: [
        {
          type: 'mesh3d', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }
        }
      ], 
      contour: [
        {
          type: 'contour', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }, 
          colorscale: [['0', '#0d0887'], ['0.1111111111111111', '#46039f'], ['0.2222222222222222', '#7201a8'], ['0.3333333333333333', '#9c179e'], ['0.4444444444444444', '#bd3786'], ['0.5555555555555556', '#d8576b'], ['0.6666666666666666', '#ed7953'], ['0.7777777777777778', '#fb9f3a'], ['0.8888888888888888', '#fdca26'], ['1', '#f0f921']]
        }
      ], 
      heatmap: [
        {
          type: 'heatmap', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }, 
          colorscale: [['0', '#0d0887'], ['0.1111111111111111', '#46039f'], ['0.2222222222222222', '#7201a8'], ['0.3333333333333333', '#9c179e'], ['0.4444444444444444', '#bd3786'], ['0.5555555555555556', '#d8576b'], ['0.6666666666666666', '#ed7953'], ['0.7777777777777778', '#fb9f3a'], ['0.8888888888888888', '#fdca26'], ['1', '#f0f921']]
        }
      ], 
      scatter: [
        {
          type: 'scatter', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      surface: [
        {
          type: 'surface', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }, 
          colorscale: [['0', '#0d0887'], ['0.1111111111111111', '#46039f'], ['0.2222222222222222', '#7201a8'], ['0.3333333333333333', '#9c179e'], ['0.4444444444444444', '#bd3786'], ['0.5555555555555556', '#d8576b'], ['0.6666666666666666', '#ed7953'], ['0.7777777777777778', '#fb9f3a'], ['0.8888888888888888', '#fdca26'], ['1', '#f0f921']]
        }
      ], 
      barpolar: [
        {
          type: 'barpolar', 
          marker: {
            line: {
              color: '#E5ECF6', 
              width: 0.5
            }, 
            pattern: {
              size: 10, 
              fillmode: 'overlay', 
              solidity: 0.2
            }
          }
        }
      ], 
      heatmapgl: [
        {
          type: 'heatmapgl', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }, 
          colorscale: [['0', '#0d0887'], ['0.1111111111111111', '#46039f'], ['0.2222222222222222', '#7201a8'], ['0.3333333333333333', '#9c179e'], ['0.4444444444444444', '#bd3786'], ['0.5555555555555556', '#d8576b'], ['0.6666666666666666', '#ed7953'], ['0.7777777777777778', '#fb9f3a'], ['0.8888888888888888', '#fdca26'], ['1', '#f0f921']]
        }
      ], 
      histogram: [
        {
          type: 'histogram', 
          marker: {pattern: {
              size: 10, 
              fillmode: 'overlay', 
              solidity: 0.2
            }}
        }
      ], 
      parcoords: [
        {
          line: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}, 
          type: 'parcoords'
        }
      ], 
      scatter3d: [
        {
          line: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}, 
          type: 'scatter3d', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      scattergl: [
        {
          type: 'scattergl', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      choropleth: [
        {
          type: 'choropleth', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }
        }
      ], 
      scattergeo: [
        {
          type: 'scattergeo', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      histogram2d: [
        {
          type: 'histogram2d', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }, 
          colorscale: [['0', '#0d0887'], ['0.1111111111111111', '#46039f'], ['0.2222222222222222', '#7201a8'], ['0.3333333333333333', '#9c179e'], ['0.4444444444444444', '#bd3786'], ['0.5555555555555556', '#d8576b'], ['0.6666666666666666', '#ed7953'], ['0.7777777777777778', '#fb9f3a'], ['0.8888888888888888', '#fdca26'], ['1', '#f0f921']]
        }
      ], 
      scatterpolar: [
        {
          type: 'scatterpolar', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      contourcarpet: [
        {
          type: 'contourcarpet', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }
        }
      ], 
      scattercarpet: [
        {
          type: 'scattercarpet', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      scattermapbox: [
        {
          type: 'scattermapbox', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      scatterpolargl: [
        {
          type: 'scatterpolargl', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      scatterternary: [
        {
          type: 'scatterternary', 
          marker: {colorbar: {
              ticks: '', 
              outlinewidth: 0
            }}
        }
      ], 
      histogram2dcontour: [
        {
          type: 'histogram2dcontour', 
          colorbar: {
            ticks: '', 
            outlinewidth: 0
          }, 
          colorscale: [['0', '#0d0887'], ['0.1111111111111111', '#46039f'], ['0.2222222222222222', '#7201a8'], ['0.3333333333333333', '#9c179e'], ['0.4444444444444444', '#bd3786'], ['0.5555555555555556', '#d8576b'], ['0.6666666666666666', '#ed7953'], ['0.7777777777777778', '#fb9f3a'], ['0.8888888888888888', '#fdca26'], ['1', '#f0f921']]
        }
      ]
    }, 
    layout: {
      geo: {
        bgcolor: 'white', 
        showland: true, 
        lakecolor: 'white', 
        landcolor: '#E5ECF6', 
        showlakes: true, 
        subunitcolor: 'white'
      }, 
      font: {color: '#2a3f5f'}, 
      polar: {
        bgcolor: '#E5ECF6', 
        radialaxis: {
          ticks: '', 
          gridcolor: 'white', 
          linecolor: 'white'
        }, 
        angularaxis: {
          ticks: '', 
          gridcolor: 'white', 
          linecolor: 'white'
        }
      }, 
      scene: {
        xaxis: {
          ticks: '', 
          gridcolor: 'white', 
          gridwidth: 2, 
          linecolor: 'white', 
          zerolinecolor: 'white', 
          showbackground: true, 
          backgroundcolor: '#E5ECF6'
        }, 
        yaxis: {
          ticks: '', 
          gridcolor: 'white', 
          gridwidth: 2, 
          linecolor: 'white', 
          zerolinecolor: 'white', 
          showbackground: true, 
          backgroundcolor: '#E5ECF6'
        }, 
        zaxis: {
          ticks: '', 
          gridcolor: 'white', 
          gridwidth: 2, 
          linecolor: 'white', 
          zerolinecolor: 'white', 
          showbackground: true, 
          backgroundcolor: '#E5ECF6'
        }
      }, 
      title: {x: 0.05}, 
      xaxis: {
        ticks: '', 
        title: {standoff: 15}, 
        gridcolor: 'white', 
        linecolor: 'white', 
        automargin: true, 
        zerolinecolor: 'white', 
        zerolinewidth: 2
      }, 
      yaxis: {
        ticks: '', 
        title: {standoff: 15}, 
        gridcolor: 'white', 
        linecolor: 'white', 
        automargin: true, 
        zerolinecolor: 'white', 
        zerolinewidth: 2
      }, 
      mapbox: {style: 'light'}, 
      ternary: {
        aaxis: {
          ticks: '', 
          gridcolor: 'white', 
          linecolor: 'white'
        }, 
        baxis: {
          ticks: '', 
          gridcolor: 'white', 
          linecolor: 'white'
        }, 
        caxis: {
          ticks: '', 
          gridcolor: 'white', 
          linecolor: 'white'
        }, 
        bgcolor: '#E5ECF6'
      }, 
      colorway: ['#636efa', '#EF553B', '#00cc96', '#ab63fa', '#FFA15A', '#19d3f3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'], 
      coloraxis: {colorbar: {
          ticks: '', 
          outlinewidth: 0
        }}, 
      hovermode: 'closest', 
      colorscale: {
        diverging: [['0', '#8e0152'], ['0.1', '#c51b7d'], ['0.2', '#de77ae'], ['0.3', '#f1b6da'], ['0.4', '#fde0ef'], ['0.5', '#f7f7f7'], ['0.6', '#e6f5d0'], ['0.7', '#b8e186'], ['0.8', '#7fbc41'], ['0.9', '#4d9221'], ['1', '#276419']], 
        sequential: [['0', '#0d0887'], ['0.1111111111111111', '#46039f'], ['0.2222222222222222', '#7201a8'], ['0.3333333333333333', '#9c179e'], ['0.4444444444444444', '#bd3786'], ['0.5555555555555556', '#d8576b'], ['0.6666666666666666', '#ed7953'], ['0.7777777777777778', '#fb9f3a'], ['0.8888888888888888', '#fdca26'], ['1', '#f0f921']], 
        sequentialminus: [['0', '#0d0887'], ['0.1111111111111111', '#46039f'], ['0.2222222222222222', '#7201a8'], ['0.3333333333333333', '#9c179e'], ['0.4444444444444444', '#bd3786'], ['0.5555555555555556', '#d8576b'], ['0.6666666666666666', '#ed7953'], ['0.7777777777777778', '#fb9f3a'], ['0.8888888888888888', '#fdca26'], ['1', '#f0f921']]
      }, 
      hoverlabel: {align: 'left'}, 
      plot_bgcolor: '#E5ECF6', 
      paper_bgcolor: 'white', 
      shapedefaults: {line: {color: '#2a3f5f'}}, 
      autotypenumbers: 'strict', 
      annotationdefaults: {
        arrowhead: 0, 
        arrowcolor: '#2a3f5f', 
        arrowwidth: 1
      }
    }
  }, 
  annotations: [
    {
      x: 0.225, 
      y: 1, 
      font: {size: 16}, 
      text: '금액', 
      xref: 'paper', 
      yref: 'paper', 
      xanchor: 'center', 
      yanchor: 'bottom', 
      showarrow: false
    }, 
    {
      x: 0.775, 
      y: 1, 
      font: {size: 16}, 
      text: '건수', 
      xref: 'paper', 
      yref: 'paper', 
      xanchor: 'center', 
      yanchor: 'bottom', 
      showarrow: false
    }
  ]
};
Plotly.plot('plotly-div', {
  data: data,
  layout: layout
});