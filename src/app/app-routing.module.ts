

import {NgModule}  from '@angular/core';
import {Routes ,RouterModule} from '@angular/router';

import {InicioComponent} from './pages/inicio/inicio.component';
import {ContactComponent} from './pages/contact/contact.component';
import { GaleriaComponent } from './pages/galeria/galeria.component';
import { ColaboradoresComponent } from './pages/colaboradores/colaboradores.component';
import { LoginComponent } from './pages/login/login.component';
import { SignupComponent } from './pages/signup/signup.component';
import {EstadisticaComponent} from './pages/estadistica/estadistica.component';


const app_routes: Routes = [

	{ path: 'home', component: InicioComponent},
	{ path: 'contact', component:ContactComponent},
	{path:'galeria',component:GaleriaComponent},
	{path:'about',component:ColaboradoresComponent},
	{path: 'login',component:LoginComponent},
	{path:'signup',component:SignupComponent},
	{path: 'estadistica', component:EstadisticaComponent},
	{ path: '**', pathMatch: 'full', redirectTo: 'home' }


];


@NgModule({
	imports : [
		RouterModule.forRoot( app_routes)
	],
	exports : [
		RouterModule
	]
	
})

export class AppRoutingModule { }