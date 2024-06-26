import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import { AppRoutingModule } from '../app-routing.module';
import { NavbarComponent } from './navbar/navbar.component';
import { FormsModule } from '@angular/forms';
import { AreaPersonalComponent } from './area-personal/area-personal.component';


@NgModule({
  declarations: [
    FooterComponent,
    HeaderComponent,
    NavbarComponent,
    AreaPersonalComponent
  ],
  imports: [
    CommonModule,
    AppRoutingModule,
    FormsModule
  ],
  exports: [
    FooterComponent,
    HeaderComponent,
    NavbarComponent
  ]

})
export class LayautModule { }
