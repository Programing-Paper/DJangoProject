const config = {
    type: 'bar',
    data: {
        labels: {{ labels_activos|safe }}
        datasets:[{
            data:{{ labels_stock|safe }},
            backgroundColor: ['rgba(255, 99, 132, 0.2)','rgba(255, 159, 64, 0.2)','rgba(255, 205, 86, 0.2)','rgba(75, 192, 192, 0.2)','rgba(54, 162, 235, 0.2)'],
            borderColor: ['rgb(255, 99, 132)','rgb(255, 159, 64)','rgb(255, 205, 86)','rgb(75, 192, 192)','rgb(54, 162, 235)'],
            label:'Activos',
            borderWidth:1
        }],
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }],
        },
        responsive: true,
    },
  };
  var stockChart= new Chart($('#indicador-activos'),config)


    const ctx = document.getElementById('indicador-activos').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: {{ labels_activos|safe }},
            datasets: [{
                label: 'Numero de registros',
                data: {{ labels_stock|safe }},
                backgroundColor: [
                    'rgba(37, 85, 175, 1)',
                    'rgba(0, 109, 255, 0.58)',
                    'rgba(140, 140, 140, 1)',
                    'rgba(232, 19, 19, 0.68)',
                    
                ],
                borderColor: [
                    'rgba(37, 85, 175, 1)',
                    'rgba(0, 109, 255, 0.58)',
                    'rgba(140, 140, 140, 1)',
                    'rgba(232, 19, 19, 0.68)',          
                ],
                borderWidth: 1
            }]
        },
        respontive: 'true',
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });