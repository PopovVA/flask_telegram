import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpModule} from '@angular/http'
import {FormsModule} from '@angular/forms'
import {HttpClientModule} from '@angular/common/http'

import { AppComponent } from './app.component';
import { MessagesComponent } from './messages/messages.component';

import { RouterModule, Routes } from '@angular/router';
import { MessageFormComponent } from './forms/message-form/message-form.component';

 const appRoutes: Routes = [
   { path: 'messages', component: MessagesComponent },
   { path: 'messages/:id', component: MessageFormComponent },
   { path: '', redirectTo: '/messages', pathMatch: 'full'},
   { path: '**', redirectTo: '/404'}
 ]

@NgModule({
  declarations: [
    AppComponent,
    MessagesComponent,
    MessageFormComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(
       appRoutes
     ),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
