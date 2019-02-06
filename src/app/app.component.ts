


import { Component } from '@angular/core';
import { GraficaService } from './services/grafica.service'
import { Chart } from 'chart.js';
import { Observable } from 'rxjs';
import 'rxjs/add/operator/map';
//import { map, take } from 'rxjs/operators';

import { map} from 'rxjs/operators'



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'yoga';
  chart = [];
  LineChart=[];
  BarChart=[];
  PieChart=[];

  constructor( private _grafica: GraficaService){}

  ngOnInit(){
    this._grafica.graficoEstadistico()
    .subscribe(res => {
      
      //console.log(res)

      let temp_max = res['weather'].map(res => res.main.temp_max)
      let temp_min = res['weather'].map(res => res.main.temp_min)
      let alldates = res['weather'].map(res => res.dt)

      let weatherDates = []
      
      console.log(alldates);


      alldates.forEach((res) => {
        let jsdate = new Date(res * 1000)
        weatherDates.push(jsdate.toLocaleTimeString('en'), {year: 'numeric', month:'short',day:'numeric'})         
      });
      
      console.log(weatherDates);


      this.chart = new Chart('canvas',{
        type: 'line',
        data: {
          labels: weatherDates,
          datasets: [
            {
              data: temp_max,
              borderColor: '#3cba9f',
              fill:false

            },
            {
              data: temp_min,
              borderColor: '#ffcc00',
              fill:false

            },
          ]
        },

        options: {
          legend:{
            display:true
          },
          scales:{
            xAxes:[{
              display: true
            }],
            yAxes:[{
              display: true
            }]
          }
        }
      })

    })
    

    /*
        // Line chart:
    this.LineChart = new Chart('lineChart', {
      type: 'line',
    data: {
    labels: ["Jan", "Feb", "March", "April", "May", "June","July","Aug","Sep","Oct","Nov","Dec"],
    datasets: [{
        label: 'Number of Items Sold in Months',
        data: [9,7 , 3, 5, 2, 10,15,16,19,3,1,9],
        fill:false,
        lineTension:0.2,
        borderColor:"red",
        borderWidth: 1
    }]
    }, 
    options: {
    title:{
        text:"Line Chart",
        display:true
    },
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            }
        }]
    }
    }
    });

    // Bar chart:
    this.BarChart = new Chart('barChart', {
      type: 'bar',
    data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [{
        label: '# of Votes',
        data: [9,7 , 3, 5, 2, 10],
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
            'rgba(255,99,132,1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
    }]
    }, 
    options: {
    title:{
        text:"Bar Chart",
        display:true
    },
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            }
        }]
    }
    }
    });

    // pie chart:
    this.PieChart = new Chart('pieChart', {
      type: 'pie',
    data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [{
        label: '# of Votes',
        data: [9,7 , 3, 5, 2, 10],
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
            'rgba(255,99,132,1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
    }]
    }, 
    options: {
    title:{
        text:"Bar Chart",
        display:true
    },
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            }
        }]
    }
    }
    });
    


  
    
*/
  }


}
