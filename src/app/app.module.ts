import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { GraficaService } from "./services/grafica.service";

import {AppRoutingModule} from './app-routing.module';

import { AppComponent } from './app.component';
import { HeaderComponent } from './shared/header/header.component';
import { FooterComponent } from './shared/footer/footer.component';
import { InicioComponent } from './pages/inicio/inicio.component';
import { CarouselComponent } from './pages/carousel/carousel.component';
import { ContactComponent } from './pages/contact/contact.component';
import { TestimoniosComponent } from './pages/testimonios/testimonios.component';
import { ServiciosComponent } from './pages/servicios/servicios.component';
import { HorarioComponent } from './pages/horario/horario.component';
import { GaleriaComponent } from './pages/galeria/galeria.component';
import { ColaboradoresComponent } from './pages/colaboradores/colaboradores.component';
import { LoginComponent } from './pages/login/login.component';
import { SignupComponent } from './pages/signup/signup.component';
import { EstadisticaComponent } from './pages/estadistica/estadistica.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    InicioComponent,
    CarouselComponent,
    ContactComponent,
    TestimoniosComponent,
    ServiciosComponent,
    HorarioComponent,
    GaleriaComponent,
    ColaboradoresComponent,
    LoginComponent,
    SignupComponent,
    EstadisticaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [GraficaService],
  bootstrap: [AppComponent]
})
export class AppModule { }
