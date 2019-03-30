import { Component, OnInit } from '@angular/core';
import { Message } from '../../messages/message';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { MessagesService } from '../../messages/messages.service'

@Component({
  selector: 'app-message-form',
  templateUrl: './message-form.component.html',
  styleUrls: ['./message-form.component.css'],
  providers: [MessagesService]
})
export class MessageFormComponent implements OnInit {
  public message: Message;

  constructor(
    private activatedRoute: ActivatedRoute,
    private messagesService: MessagesService, 
    private http: HttpClient
  ) { }

  ngOnInit() {
    this.getMessage()
  }

  onSubmit(){
    this.messagesService.sendMessage(this.message.telegram_id, this.message.reply)
  }

  getMessage (): void {
    let messageId = this.activatedRoute.snapshot.paramMap.get("id");
    this.messagesService.getMessage(+messageId).subscribe(message => (this.message = message))
}

}
