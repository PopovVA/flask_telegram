import { MessagesService } from './messages.service'
import { Message } from './message'
import { HttpClient } from '@angular/common/http'
import { Component, OnInit } from '@angular/core';

@Component ({
    selector: 'app-messages',
    templateUrl: './messages.component.html',
    providers: [MessagesService, ]
})

export class MessagesComponent implements OnInit {
    messages: Message[]

    constructor(private messageService: MessagesService, private http: HttpClient) { }

    ngOnInit () {
        this.getMessages()
    }

    getMessages (): void {
        this.messageService.getMessages().subscribe(messages => (this.messages = messages))
    }
}