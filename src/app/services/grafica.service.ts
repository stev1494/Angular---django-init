


import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from 'rxjs';
import 'rxjs/add/operator/map';
import { map, take } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class GraficaService {

  constructor(private _http: HttpClient) { }

  graficoEstadistico(){
    return this._http.get('http://api.openweathermap.org/data/2.5/weather?q=Guayaquil,ec&APPID=14429bce4def3c909d027e17fee39071')
     .map( res => res);

  }
}
